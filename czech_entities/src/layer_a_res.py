"""Vrstva A — master data z ARES/RES bulk (VREO tar.gz, jeden XML na IČO).

Univerzum = řádky tabulky `subjekt`. Import je streamovaný (archiv má jednotky
GB), namespace-agnostický a řízený mapováním z config/sources.yaml (konvence:
mapování v konfiguraci, ne v kódu).

POZN.: Přesné XML tagy VREO je nutné potvrdit proti reálnému vzorku — použij
`--sample`, který vypíše strom tagů prvních N záznamů, aby šlo `vreo_field_map`
doladit bez zásahu do kódu.

V TOMTO prostředí je ares.gov.cz blokován egress-politikou → stažení proběhne
až na stroji bez blokace. Kód je ale plně funkční a offline testovaný na
syntetickém archivu.
"""
from __future__ import annotations

import datetime as dt
import io
import logging
import tarfile
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml

from src import db
from src.http_client import Downloader
from src.ico import is_valid_ico, normalize_ico

log = logging.getLogger("czech_entities.layer_a")

BATCH = 100000


def _localname(tag: str) -> str:
    """Odstraní XML namespace: '{uri}obchodniJmeno' -> 'obchodnijmeno'."""
    return tag.rsplit("}", 1)[-1].lower()


def _index_by_localname(root: ET.Element) -> dict[str, str]:
    """Zploští strom na {localname: text} (první výskyt vyhrává)."""
    out: dict[str, str] = {}
    for el in root.iter():
        ln = _localname(el.tag)
        if ln not in out and el.text and el.text.strip():
            out[ln] = el.text.strip()
    return out


def _pick(flat: dict[str, str], candidates: list[str]) -> str | None:
    for c in candidates:
        v = flat.get(c.lower())
        if v:
            return v
    return None


def _parse_date(s: str | None):
    if not s:
        return None
    s = s.strip()[:10]
    for fmt in ("%Y-%m-%d", "%d.%m.%Y"):
        try:
            return dt.datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return None


def _is_fo(pravni_forma: str | None, prefixes: list[str]) -> bool:
    if not pravni_forma:
        return False
    pf = pravni_forma.strip()
    return any(pf.startswith(p) for p in prefixes)


def iter_vreo_records(archive_path: Path):
    """Streamovaně vydává (ET.Element) záznamů z tar.gz (jeden XML na člen)."""
    with tarfile.open(archive_path, "r:*") as tar:
        for member in tar:
            if not member.isfile():
                continue
            if not member.name.lower().endswith(".xml"):
                continue
            f = tar.extractfile(member)
            if f is None:
                continue
            data = f.read()
            try:
                root = ET.parse(io.BytesIO(data)).getroot()
            except ET.ParseError as e:
                log.warning("nevalidní XML %s: %s", member.name, e)
                continue
            yield root


def _record_to_row(root: ET.Element, fmap: dict, fo_prefixes: list[str], source_id: int):
    flat = _index_by_localname(root)
    raw_ico = _pick(flat, fmap["ico"])
    ico = normalize_ico(raw_ico)
    if ico is None:
        return None
    pf = _pick(flat, fmap["pravni_forma"])
    return [
        ico,
        is_valid_ico(ico),
        _pick(flat, fmap["nazev"]),
        pf,
        None,  # pravni_forma_txt (číselník se joinuje zvlášť, je-li)
        _is_fo(pf, fo_prefixes),
        _pick(flat, fmap["sidlo_kraj"]),
        _pick(flat, fmap["sidlo_okres"]),
        _pick(flat, fmap["sidlo_obec"]),
        _pick(flat, fmap["sidlo_text"]),
        _pick(flat, fmap["nace"]),
        _parse_date(_pick(flat, fmap["datum_vzniku"])),
        _pick(flat, fmap["stav"]),
        _pick(flat, fmap["datova_schranka"]),
        source_id,
        dt.datetime.now(),
    ]


def dump_sample_structure(archive_path: Path, n: int = 5) -> None:
    """Vypíše localname->hodnota prvních n záznamů — pro doladění mapování."""
    for i, root in enumerate(iter_vreo_records(archive_path)):
        if i >= n:
            break
        print(f"--- záznam {i} (root <{_localname(root.tag)}>) ---")
        for k, v in _index_by_localname(root).items():
            print(f"    {k:28} = {v[:60]}")


# --- CSV cesta (RES/ARES CSV open data) --------------------------------------
def _open_text(path: Path):
    """Otevře .csv, .csv.gz nebo první .csv v .zip jako textový stream (utf-8)."""
    import gzip
    import io
    import zipfile

    name = path.name.lower()
    if name.endswith(".gz"):
        return io.TextIOWrapper(gzip.open(path, "rb"), encoding="utf-8", errors="replace")
    if name.endswith(".zip"):
        zf = zipfile.ZipFile(path)
        inner = next((n for n in zf.namelist() if n.lower().endswith(".csv")), None)
        if inner is None:
            raise ValueError(f"v {path.name} není žádný .csv")
        return io.TextIOWrapper(zf.open(inner), encoding="utf-8", errors="replace")
    return open(path, "r", encoding="utf-8", errors="replace")


def _resolve_csv_cols(header: list[str], col_map: dict) -> dict:
    """Namapuje kandidátní názvy sloupců na skutečné indexy (case-insensitive)."""
    idx = {h.strip().lower(): i for i, h in enumerate(header)}
    resolved = {}
    for field, candidates in col_map.items():
        for c in candidates:
            if c.lower() in idx:
                resolved[field] = idx[c.lower()]
                break
    return resolved


def _csv_row_to_row(rec: list[str], cols: dict, fo_prefixes: list[str],
                    source_id: int, kraj_ciselnik: dict | None = None):
    def g(field):
        i = cols.get(field)
        if i is None or i >= len(rec):
            return None
        v = rec[i].strip()
        return v or None

    ico = normalize_ico(g("ico"))
    if ico is None:
        return None
    pf = g("pravni_forma")
    okres = g("sidlo_okres")

    # stav: explicitní, jinak odvození z data zániku (RES kraj/stav nemá)
    stav = g("stav") or ("zaniklý" if g("datum_zaniku") else "aktivní")
    # kraj: explicitní, jinak odvození z LAU kódu okresu (NUTS3 = OKRESLAU[:5])
    kraj = g("sidlo_kraj")
    if kraj is None and okres and kraj_ciselnik:
        kraj = kraj_ciselnik.get(okres[:5])

    return [
        ico, is_valid_ico(ico), g("nazev"), pf, None, _is_fo(pf, fo_prefixes),
        kraj, okres, g("sidlo_obec"), g("sidlo_text"),
        g("nace"), _parse_date(g("datum_vzniku")), stav,
        g("datova_schranka"), source_id, dt.datetime.now(),
    ]


def iter_csv_rows(path: Path, col_map: dict, fo_prefixes: list[str], source_id: int,
                  kraj_ciselnik: dict | None = None):
    import csv as _csv

    with _open_text(path) as fh:
        # autodetekce oddělovače (ČSÚ RES je ',', jiné exporty bývají ';')
        sample = fh.read(4096)
        fh.seek(0)
        try:
            dialect = _csv.Sniffer().sniff(sample, delimiters=",;\t")
        except _csv.Error:
            class dialect:  # noqa: N801
                delimiter = ","
        reader = _csv.reader(fh, dialect)
        header = next(reader, None)
        if not header:
            return
        cols = _resolve_csv_cols(header, col_map)
        if "ico" not in cols:
            raise ValueError(
                "CSV: nenalezen sloupec IČO. Uprav ares.csv_col_map v configu. "
                f"Hlavička: {header[:12]}")
        for rec in reader:
            row = _csv_row_to_row(rec, cols, fo_prefixes, source_id, kraj_ciselnik)
            if row is not None:
                yield row


# --- společný zapisovací cyklus ----------------------------------------------
def _consume_rows(con, rid: int, row_iter, source_desc: str) -> None:
    inserted, batch = 0, []
    con.execute("BEGIN TRANSACTION")
    try:
        for row in row_iter:
            batch.append(row)
            if len(batch) >= BATCH:
                _flush(con, batch)
                inserted += len(batch)
                batch = []
                if inserted % 100000 == 0:
                    log.info("vrstva A: %d subjektů…", inserted)
        if batch:
            _flush(con, batch)
            inserted += len(batch)
        con.execute("COMMIT")
    except Exception:
        con.execute("ROLLBACK")
        db.finish_run(con, rid, inserted, 0, "failed")
        raise
    db.finish_run(con, rid, inserted, 0, "ok")
    log.info("vrstva A hotová (%s): %d subjektů", source_desc, inserted)


def _detect_format(path: Path) -> str:
    n = path.name.lower()
    if n.endswith((".tar.gz", ".tgz", ".tar")):
        return "vreo"
    if ".csv" in n or n.endswith((".zip", ".gz")):
        return "csv"
    return "vreo"


def ingest(con, config_path: str, cache_dir: str, force: bool = False,
           sample: int = 0, file: str | None = None, source: str = "auto"):
    """Vrstva A. Zdroj lze zvolit:

      - `file`: lokální bulk soubor (BEZ egressu) — doporučeno v prostředí s blokem.
                Stáhni bulk jednou jinde, sem nahraj a ukaž na něj.
      - jinak stáhne dle configu (VREO tar.gz nebo CSV url).

    source: 'auto' | 'vreo' | 'csv'. Při 'auto' se hádá dle přípony.
    """
    cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    ares = cfg["ares"]
    rate = cfg.get("rate_limit", {}).get("ares_max_per_min", 300)
    fo_prefixes = ares.get("fo_pravni_forma_prefix", [])

    # 1) získání zdrojového souboru: lokální (bez sítě) nebo stažení
    if file:
        src_path = Path(file)
        if not src_path.exists():
            raise FileNotFoundError(f"zdrojový soubor neexistuje: {src_path}")
        src_url = f"file://{src_path}"
    else:
        fmt0 = source if source != "auto" else "vreo"
        url = ares["csv_url"] if fmt0 == "csv" else ares["vreo_all_url"]
        fname = "res_data.csv.zip" if fmt0 == "csv" else "ares_vreo_all.tar.gz"
        with Downloader(cache_dir, max_per_min=rate) as dl:
            src_path = dl.fetch_file(url, fname, force=force)
        src_url = url

    fmt = source if source != "auto" else _detect_format(src_path)

    if sample:
        if fmt == "vreo":
            dump_sample_structure(src_path, n=sample)
        else:
            _dump_csv_header(src_path)
        return

    sid = db.register_source(con, "ARES/RES", src_url, str(src_path),
                             f"vrstva A bulk ({fmt})")
    rid = db.start_run(con, "A_master")

    if fmt == "csv":
        col_map = ares["csv_col_map"]
        kraj_ciselnik = ares.get("kraj_ciselnik")
        rows = iter_csv_rows(src_path, col_map, fo_prefixes, sid, kraj_ciselnik)
        _consume_rows(con, rid, rows, "CSV")
    else:
        fmap = ares["vreo_field_map"]
        rows = _vreo_row_iter(src_path, fmap, fo_prefixes, sid)
        _consume_rows(con, rid, rows, "VREO")


def _vreo_row_iter(archive_path: Path, fmap, fo_prefixes, sid):
    for root in iter_vreo_records(archive_path):
        try:
            row = _record_to_row(root, fmap, fo_prefixes, sid)
        except Exception as e:  # jeden špatný záznam neshodí běh
            log.debug("chyba záznamu: %s", e)
            continue
        if row is not None:
            yield row


def _dump_csv_header(path: Path) -> None:
    import csv as _csv
    with _open_text(path) as fh:
        sample = fh.read(4096)
        fh.seek(0)
        try:
            dialect = _csv.Sniffer().sniff(sample, delimiters=",;\t")
        except _csv.Error:
            class dialect:  # noqa: N801
                delimiter = ","
        header = next(_csv.reader(fh, dialect), [])
    print("--- hlavička CSV (uprav ares.csv_col_map dle těchto názvů) ---")
    for i, col in enumerate(header):
        print(f"    [{i:2}] {col.replace(chr(0xFEFF), '')}")


_SUBJEKT_COLS = [
    "ico", "ico_valid", "nazev", "pravni_forma", "pravni_forma_txt", "je_fo",
    "sidlo_kraj", "sidlo_okres", "sidlo_obec", "sidlo_text", "nace",
    "datum_vzniku", "stav", "datova_schranka", "source_id", "ingest_at",
]


def _flush(con, batch: list[list]) -> None:
    """Bulk upsert dávky přes registrovaný DataFrame (řádově rychlejší než
    executemany). DELETE dle IČO drží idempotenci při opakovaném běhu.
    """
    import pandas as pd

    df = pd.DataFrame(batch, columns=_SUBJEKT_COLS)
    con.register("_batch_df", df)
    try:
        con.execute("DELETE FROM subjekt WHERE ico IN (SELECT ico FROM _batch_df)")
        con.execute("INSERT INTO subjekt SELECT * FROM _batch_df")
    finally:
        con.unregister("_batch_df")
