"""Vrstva C — plná extrakce úvěrové indicie z účetních závěrek.

Cílený batch (NE slepé OCR všeho): jen PO se sbírkou listin. Idempotentní a
resumovatelné přes tabulky zaverka_meta / pdf_job / uver — přerušený běh
pokračuje, ne od nuly.

Pouštět AŽ po milníku coverage (layer_c_coverage) a po rozhodnutí uživatele
o rozsahu (plošně vs. omezeně). Parametr limit umožňuje omezený běh.
"""
from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path

import yaml

from src import db
from src.http_client import Downloader
from src.justice_sbirka import HttpSbirkaClient, SbirkaClient, pick_latest_zaverka
from src import pdf_extract
from src.uver_parser import parse_uver_from_text

log = logging.getLogger("czech_entities.layer_c")


def _todo_icos(con, limit: int | None) -> list[str]:
    """PO, které ještě nemají záznam v uver (resume). Jen právnické osoby."""
    q = ("SELECT s.ico FROM subjekt s "
         "LEFT JOIN uver u ON u.ico = s.ico "
         "WHERE COALESCE(s.je_fo, FALSE)=FALSE AND u.ico IS NULL")
    if limit:
        q += f" LIMIT {int(limit)}"
    return [r[0] for r in con.execute(q).fetchall()]


def run(con, config_path: str, cache_dir: str, limit: int | None = None,
        client: SbirkaClient | None = None) -> dict:
    cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    polozky = cfg["uver_extrakce"]["polozky_uver"]
    roky_zpet = cfg["uver_extrakce"].get("roky_zpet", 1)
    ocr_jazyk = cfg["uver_extrakce"]["ocr_jazyk"]

    icos = _todo_icos(con, limit)
    if not icos:
        log.info("vrstva C: nic ke zpracování (vše hotové nebo prázdná vrstva A)")
        return {"zpracovano": 0}

    dl = Downloader(cache_dir, max_per_min=cfg["rate_limit"]["justice_max_per_min"])
    if client is None:
        client = HttpSbirkaClient(cfg["justice"], dl, cfg["justice"]["typy_listin"])

    sid = db.register_source(con, "SBIRKA_LISTIN", cfg["justice"]["or_sbirka_firma"],
                             None, "účetní závěrky ze sbírky listin")
    rid = db.start_run(con, "C_extract")
    pdf_dir = Path(cache_dir) / "zaverky_pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    zpracovano, s_uverem, chyb = 0, 0, 0
    now = dt.datetime.now()
    for i, ico in enumerate(icos):
        try:
            subjekt_id = client.resolve_subjekt_id(ico)
            listiny = client.list_listiny(subjekt_id) if subjekt_id else []
            for l in listiny:
                con.execute("INSERT INTO zaverka_meta VALUES (?,?,?,?,?,?,?)",
                            [ico, l.rok, l.typ, l.pdf_url, bool(l.pdf_url), sid, now])
            zav = pick_latest_zaverka(listiny, roky_zpet) if listiny else []
            if not zav:
                zpracovano += 1
                continue
            l = zav[0]
            pdf_path = client.download_pdf(l, pdf_dir)
            stav = "downloaded" if pdf_path else "failed"
            text, conf, je_sken = ("", "neurcito", None)
            if pdf_path:
                text, conf, je_sken = pdf_extract.extract(pdf_path, ocr_jazyk)
                stav = "parsed" if conf == "pdf_text" else ("ocr" if conf == "ocr" else "failed")
            con.execute("INSERT INTO pdf_job VALUES (?,?,?,?,?,?,?,?)",
                        [ico, l.rok, l.pdf_url, pdf_path, stav, je_sken, None, now])
            r = parse_uver_from_text(text, polozky, conf)
            con.execute("INSERT INTO uver VALUES (?,?,?,?,?,?,?,?,?)",
                        [ico, l.rok, r.uver_flag, r.uver_castka, r.polozka_text,
                         r.confidence, l.pdf_url, sid, now])
            if r.uver_flag:
                s_uverem += 1
            zpracovano += 1
        except Exception as e:
            chyb += 1
            log.debug("vrstva C %s: %s", ico, e)
        if (i + 1) % 100 == 0:
            log.info("vrstva C: %d/%d, s úvěrem=%d, chyb=%d",
                     i + 1, len(icos), s_uverem, chyb)

    dl.close()
    db.finish_run(con, rid, zpracovano, chyb, "ok")
    log.info("vrstva C hotová: zpracováno=%d, s úvěrem=%d, chyb=%d",
             zpracovano, s_uverem, chyb)
    return {"zpracovano": zpracovano, "s_uverem": s_uverem, "chyb": chyb}
