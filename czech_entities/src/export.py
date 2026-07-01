"""Finální join všech vrstev -> jeden dataset (parquet + xlsx).

Jeden řádek na IČO. Sloupce dle SPEC. U každého odvozeného příznaku je
dohledatelný zdroj a datum (přes source_id / *_zdroj / *_rok).

GDPR: dle rozhodnutí uživatele je univerzum včetně OSVČ; filtrování/omezení
polí u fyzických osob se řeší zde (parametr fo_minimal).
"""
from __future__ import annotations

import logging
from pathlib import Path

import duckdb

log = logging.getLogger("czech_entities.export")

# Finální pořadí a názvy sloupců dle SPEC.
FINAL_COLUMNS = [
    "ico", "nazev", "pravni_forma", "sidlo_kraj", "sidlo_okres", "nace",
    "datum_vzniku", "stav",
    "insolvence_flag", "insolvence_stav",
    "ma_zaverku_flag", "posledni_rok_zaverky",
    "uver_flag", "uver_castka", "uver_rok", "uver_zdroj", "uver_confidence",
]

FINAL_VIEW_SQL = """
CREATE OR REPLACE VIEW final_dataset AS
WITH ins AS (
    -- nejnovější insolvenční záznam na IČO
    SELECT ico, insolvence_flag, insolvence_stav,
           ROW_NUMBER() OVER (PARTITION BY ico
                              ORDER BY posledni_udalost_at DESC NULLS LAST) rn
    FROM insolvence
), zav AS (
    -- má-li subjekt uloženou závěrku + poslední rok
    SELECT ico,
           BOOL_OR(dostupne_pdf OR TRUE) AS ma_zaverku_flag,
           MAX(rok) AS posledni_rok_zaverky
    FROM zaverka_meta
    GROUP BY ico
), uv AS (
    -- nejnovější extrahovaná úvěrová indicie na IČO
    SELECT ico, uver_flag, uver_castka, rok AS uver_rok,
           zdroj_url AS uver_zdroj, confidence AS uver_confidence,
           ROW_NUMBER() OVER (PARTITION BY ico ORDER BY rok DESC NULLS LAST) rn
    FROM uver
)
SELECT
    s.ico,
    s.nazev,
    COALESCE(s.pravni_forma_txt, s.pravni_forma)      AS pravni_forma,
    s.sidlo_kraj,
    s.sidlo_okres,
    s.nace,
    s.datum_vzniku,
    s.stav,
    COALESCE(ins.insolvence_flag, FALSE)              AS insolvence_flag,
    ins.insolvence_stav,
    COALESCE(zav.ma_zaverku_flag, FALSE)              AS ma_zaverku_flag,
    zav.posledni_rok_zaverky,
    uv.uver_flag,
    uv.uver_castka,
    uv.uver_rok,
    uv.uver_zdroj,
    uv.uver_confidence
FROM subjekt s
LEFT JOIN ins ON ins.ico = s.ico AND ins.rn = 1
LEFT JOIN zav ON zav.ico = s.ico
LEFT JOIN uv  ON uv.ico  = s.ico AND uv.rn = 1
"""


def build_final_view(con: duckdb.DuckDBPyConnection) -> None:
    con.execute(FINAL_VIEW_SQL)


def export(con: duckdb.DuckDBPyConnection, out_dir: str | Path) -> dict:
    """Vytvoří final_dataset a zapíše parquet + xlsx. Vrací počty."""
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)
    build_final_view(con)

    parquet_path = out / "ekonomicke_subjekty_cr.parquet"
    con.execute(
        f"COPY (SELECT * FROM final_dataset) TO '{parquet_path}' (FORMAT PARQUET)"
    )

    # xlsx přes pandas (celý dataset může být obří -> pro xlsx dáváme jen souhrn
    # + prvních N řádků; plný výstup je v parquetu). Dohodnutý limit řádků xlsx.
    n_total = con.execute("SELECT COUNT(*) FROM final_dataset").fetchone()[0]
    xlsx_path = out / "ekonomicke_subjekty_cr.xlsx"
    _write_xlsx(con, xlsx_path, n_total)

    log.info("export hotov: %s (%d řádků), %s", parquet_path.name, n_total, xlsx_path.name)
    return {"parquet": str(parquet_path), "xlsx": str(xlsx_path), "radku": n_total}


def _write_xlsx(con, xlsx_path: Path, n_total: int, max_rows: int = 200_000) -> None:
    import pandas as pd

    with pd.ExcelWriter(xlsx_path, engine="openpyxl") as xw:
        # List 1: souhrn / metadata
        summary = con.execute(
            """
            SELECT 'subjektů celkem' AS metrika, COUNT(*)::BIGINT AS hodnota FROM final_dataset
            UNION ALL SELECT 'z toho insolvence', COUNT(*) FILTER (WHERE insolvence_flag) FROM final_dataset
            UNION ALL SELECT 'má závěrku', COUNT(*) FILTER (WHERE ma_zaverku_flag) FROM final_dataset
            UNION ALL SELECT 'úvěr flag=true', COUNT(*) FILTER (WHERE uver_flag) FROM final_dataset
            UNION ALL SELECT 'úvěr nelze určit', COUNT(*) FILTER (WHERE ma_zaverku_flag AND uver_flag IS NULL) FROM final_dataset
            """
        ).df()
        summary.to_excel(xw, sheet_name="souhrn", index=False)

        # List 2: data (omezeno kvůli limitu xlsx ~1M řádků; plný výstup = parquet)
        limit = min(n_total, max_rows)
        df = con.execute(f"SELECT * FROM final_dataset LIMIT {limit}").df()
        df.to_excel(xw, sheet_name="data", index=False)

        if n_total > max_rows:
            note = pd.DataFrame(
                {"pozn.": [
                    f"xlsx obsahuje prvních {max_rows} řádků z {n_total}. "
                    "Kompletní dataset je v parquet souboru."
                ]}
            )
            note.to_excel(xw, sheet_name="pozn", index=False)
