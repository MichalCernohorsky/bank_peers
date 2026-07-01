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

BATCH = 5000


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


def ingest(con, config_path: str, cache_dir: str, force: bool = False, sample: int = 0):
    cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    ares = cfg["ares"]
    rate = cfg.get("rate_limit", {}).get("ares_max_per_min", 300)

    with Downloader(cache_dir, max_per_min=rate) as dl:
        archive = dl.fetch_file(ares["vreo_all_url"], "ares_vreo_all.tar.gz", force=force)

    if sample:
        dump_sample_structure(archive, n=sample)
        return

    sid = db.register_source(con, "ARES", ares["vreo_all_url"], str(archive),
                             "VREO kompletní bulk (XML/IČO v tar.gz)")
    rid = db.start_run(con, "A_master")

    fmap = ares["vreo_field_map"]
    fo_prefixes = ares.get("fo_pravni_forma_prefix", [])
    inserted, errors, batch = 0, 0, []
    con.execute("BEGIN TRANSACTION")
    try:
        for root in iter_vreo_records(archive):
            try:
                row = _record_to_row(root, fmap, fo_prefixes, sid)
            except Exception as e:  # robustnost: jeden špatný záznam neshodí běh
                errors += 1
                log.debug("chyba záznamu: %s", e)
                continue
            if row is None:
                errors += 1
                continue
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
        db.finish_run(con, rid, inserted, errors, "failed")
        raise

    db.finish_run(con, rid, inserted, errors, "ok")
    log.info("vrstva A hotová: %d subjektů, %d chyb", inserted, errors)


def _flush(con, batch: list[list]) -> None:
    # INSERT OR REPLACE dle IČO (idempotence při opakovaném běhu)
    con.execute("DELETE FROM subjekt WHERE ico IN (SELECT ico FROM (VALUES "
                + ",".join("(?)" for _ in batch) + ") AS t(ico))",
                [r[0] for r in batch])
    con.executemany(
        "INSERT INTO subjekt VALUES (" + ",".join("?" * 16) + ")", batch
    )
