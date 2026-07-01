"""ARES REST v3 — doplnění atributů k SEZNAMU IČO (detaily, ne celý registr).

Dle SPEC: API se používá jen na dohledání detailů/delt, NIKDY na celé univerzum
(hrozí blok nad ~500 dotazů/min). Rate-limit řeší Downloader.

Vstup: seznam IČO (soubor, jeden IČO na řádek) NEBO IČO v tabulce subjekt bez
atributů. Výstup: řádky do tabulky subjekt (upsert).

JSON detail (v3) mapujeme flexibilně — klíče se mohou lišit verzí; navigace
zkouší více variant. Mapování dat je offline testované na vzorku odpovědi.
"""
from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path

import yaml

from src import db
from src.http_client import Downloader
from src.ico import is_valid_ico, normalize_ico

log = logging.getLogger("czech_entities.ares_rest")


def _first(d: dict, *keys):
    for k in keys:
        v = d.get(k)
        if v not in (None, "", []):
            return v
    return None


def _nace(subjekt: dict):
    v = _first(subjekt, "czNace", "cinnosti", "nace")
    if isinstance(v, list) and v:
        return str(v[0])
    return str(v) if v else None


def map_detail(js: dict, fo_prefixes: list[str], source_id: int) -> list | None:
    """Zmapuje JSON detail ARES ekonomického subjektu na řádek tabulky subjekt."""
    ico = normalize_ico(_first(js, "ico"))
    if ico is None:
        return None
    sidlo = js.get("sidlo") or {}
    if not isinstance(sidlo, dict):
        sidlo = {}
    pf = _first(js, "pravniForma", "kodPravniFormy")
    pf = str(pf) if pf is not None else None
    datum_vzniku = _first(js, "datumVzniku")
    stav = "zaniklý" if _first(js, "datumZaniku") else "aktivní"
    d = None
    if datum_vzniku:
        try:
            d = dt.date.fromisoformat(str(datum_vzniku)[:10])
        except ValueError:
            d = None
    return [
        ico, is_valid_ico(ico),
        _first(js, "obchodniJmeno", "nazev"),
        pf, None,
        bool(pf and any(pf.startswith(p) for p in fo_prefixes)),
        _first(sidlo, "nazevKraje", "kraj"),
        _first(sidlo, "nazevOkresu", "okres"),
        _first(sidlo, "nazevObce", "obec"),
        _first(sidlo, "textovaAdresa", "textova_adresa"),
        _nace(js), d, stav,
        _first(js, "datovaSchranka", "idDatoveSchranky"),
        source_id, dt.datetime.now(),
    ]


def _read_ico_list(path: str) -> list[str]:
    out = []
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        ico = normalize_ico(line.strip().split(";")[0])
        if ico:
            out.append(ico)
    return out


def enrich(con, config_path: str, cache_dir: str, ico_file: str | None = None,
           limit: int | None = None) -> dict:
    cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    ares = cfg["ares"]
    rate = cfg.get("rate_limit", {}).get("ares_max_per_min", 300)
    fo_prefixes = ares.get("fo_pravni_forma_prefix", [])
    detail_tmpl = ares["rest_detail"]

    if ico_file:
        icos = _read_ico_list(ico_file)
    else:
        # IČO v tabulce subjekt bez názvu (nedoplněné)
        q = "SELECT ico FROM subjekt WHERE nazev IS NULL"
        if limit:
            q += f" LIMIT {int(limit)}"
        icos = [r[0] for r in con.execute(q).fetchall()]
    if limit:
        icos = icos[:limit]
    if not icos:
        log.info("enrich: žádná IČO ke zpracování")
        return {"zpracovano": 0}

    sid = db.register_source(con, "ARES-REST", detail_tmpl, None,
                             "detail per IČO (v3)")
    rid = db.start_run(con, "A_master")
    ok, err = 0, 0
    with Downloader(cache_dir, max_per_min=rate) as dl:
        for i, ico in enumerate(icos):
            try:
                js = dl.get_json(detail_tmpl.format(ico=ico))
                row = map_detail(js, fo_prefixes, sid)
                if row is None:
                    err += 1
                    continue
                con.execute("DELETE FROM subjekt WHERE ico=?", [row[0]])
                con.execute("INSERT INTO subjekt VALUES (" + ",".join("?" * 16) + ")", row)
                ok += 1
            except Exception as e:
                err += 1
                log.warning("enrich IČO %s selhalo: %s", ico, e)
            if (i + 1) % 100 == 0:
                log.info("enrich: %d/%d (ok=%d, chyb=%d)", i + 1, len(icos), ok, err)
    db.finish_run(con, rid, ok, err, "ok")
    log.info("enrich hotov: doplněno %d IČO, %d chyb", ok, err)
    return {"zpracovano": ok, "chyb": err}
