"""Offline test CSV cesty vrstvy A (RES/ARES CSV) přes lokální soubor.

Ověřuje: mapování sloupců dle configu, ';' oddělovač, .gz vstup, odvození
je_fo, validaci IČO a idempotenci. Bez jakéhokoli přístupu k síti.
"""
import gzip
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import db, layer_a_res  # noqa: E402

CSV = (
    "ICO;OBCHODNI_JMENO;PRAVNI_FORMA;NAZ_KRAJ;NAZ_OKRES;NACE;DATUM_VZNIKU;STAV\n"
    "45244782;ČEZ, a. s.;121;Hlavní město Praha;Praha;3511;1992-05-06;aktivní\n"
    "00006947;Ministerstvo financí;325;Hlavní město Praha;Praha;8411;1969-01-01;aktivní\n"
    "27074358;Alza.cz a.s.;121;Hlavní město Praha;Praha;4791;1994-05-26;aktivní\n"
    "10100101;Jan Novák OSVČ;101;Jihomoravský;Brno-město;4711;2010-03-01;aktivní\n"
    ";Chybí IČO;121;;;;;\n"
)

CONFIG = """
rate_limit: {ares_max_per_min: 300}
ares:
  vreo_all_url: x
  csv_url: x
  fo_pravni_forma_prefix: ["10", "11"]
  csv_col_map:
    ico: [ICO]
    nazev: [OBCHODNI_JMENO]
    pravni_forma: [PRAVNI_FORMA]
    sidlo_text: [ADRESA]
    sidlo_kraj: [NAZ_KRAJ]
    sidlo_okres: [NAZ_OKRES]
    sidlo_obec: [NAZ_OBEC]
    nace: [NACE]
    datum_vzniku: [DATUM_VZNIKU]
    stav: [STAV]
    datova_schranka: [ID_DS]
"""


def _run(csv_path: Path, cfg_path: Path):
    con = db.connect(":memory:"); db.init_schema(con)
    layer_a_res.ingest(con, str(cfg_path), cache_dir=str(csv_path.parent),
                       file=str(csv_path), source="csv")
    return con


def test_csv_plain():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        csv_p = tmp / "res.csv"; csv_p.write_text(CSV, encoding="utf-8")
        cfg = tmp / "sources.yaml"; cfg.write_text(CONFIG, encoding="utf-8")
        con = _run(csv_p, cfg)
        rows = con.execute(
            "SELECT ico, nazev, je_fo, sidlo_kraj, nace, datum_vzniku, ico_valid "
            "FROM subjekt ORDER BY ico").fetchall()
        icos = [r[0] for r in rows]
        # 4 platné řádky (řádek bez IČO se zahodí)
        assert icos == ["00006947", "10100101", "27074358", "45244782"], icos
        cez = [r for r in rows if r[0] == "45244782"][0]
        assert cez[1] == "ČEZ, a. s." and cez[3] == "Hlavní město Praha"
        assert cez[4] == "3511" and str(cez[5]) == "1992-05-06" and cez[6] is True
        osvc = [r for r in rows if r[0] == "10100101"][0]
        assert osvc[2] is True     # PF 101 -> FO
        assert [r for r in rows if r[0] == "45244782"][0][2] is False
        print("OK  CSV plain:", icos)


def test_csv_gz_and_idempotence():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        gz_p = tmp / "res.csv.gz"
        with gzip.open(gz_p, "wt", encoding="utf-8") as fh:
            fh.write(CSV)
        cfg = tmp / "sources.yaml"; cfg.write_text(CONFIG, encoding="utf-8")
        con = db.connect(":memory:"); db.init_schema(con)
        layer_a_res.ingest(con, str(cfg), str(tmp), file=str(gz_p), source="csv")
        layer_a_res.ingest(con, str(cfg), str(tmp), file=str(gz_p), source="csv")
        n = con.execute("SELECT COUNT(*) FROM subjekt").fetchone()[0]
        assert n == 4, n     # bez duplikace
        print("OK  CSV gz + idempotence: 4 řádky")


if __name__ == "__main__":
    test_csv_plain(); test_csv_gz_and_idempotence()
    print("\nvšechny testy CSV cesty vrstvy A prošly")
