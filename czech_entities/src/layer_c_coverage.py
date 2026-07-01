"""POVINNÝ MILNÍK před plnou vrstvou C — měření coverage na vzorku.

Vezme náhodný vzorek ~500 právnických osob (je_fo=FALSE) a změří:
  - kolik má vůbec dohledatelnou účetní závěrku,
  - kolik PDF je strojově čitelných vs. skenů (nutné OCR),
  - úspěšnost extrakce položky bankovního úvěru.

Výstup: tabulka coverage % (do konzole + tabulka coverage_sample v DuckDB).
Teprve podle ní uživatel rozhodne, zda vrstvu C jet plošně.

NEPOUŠTĚJ plné stahování/OCR bez tohoto měření (dle SPEC).
"""
from __future__ import annotations

import logging
from pathlib import Path

import yaml

from src.http_client import Downloader
from src.justice_sbirka import (
    HttpSbirkaClient,
    SbirkaClient,
    pick_latest_zaverka,
)
from src import pdf_extract
from src.uver_parser import parse_uver_from_text

log = logging.getLogger("czech_entities.coverage")


def sample_po(con, n: int) -> list[str]:
    """Náhodný vzorek n IČO právnických osob (ne OSVČ)."""
    rows = con.execute(
        "SELECT ico FROM subjekt WHERE COALESCE(je_fo, FALSE)=FALSE "
        f"USING SAMPLE reservoir({int(n)} ROWS)"
    ).fetchall()
    return [r[0] for r in rows]


def measure(con, config_path: str, cache_dir: str, n: int = 500,
            client: SbirkaClient | None = None) -> dict:
    cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    polozky = cfg["uver_extrakce"]["polozky_uver"]
    roky_zpet = cfg["uver_extrakce"].get("roky_zpet", 1)

    icos = sample_po(con, n)
    if not icos:
        log.warning("žádné PO v tabulce subjekt — nejdřív spusť vrstvu A")
        return {}

    dl = Downloader(cache_dir, max_per_min=cfg["rate_limit"]["justice_max_per_min"])
    if client is None:
        client = HttpSbirkaClient(cfg["justice"], dl,
                                  typy_listin=cfg["justice"]["typy_listin"])

    con.execute("DELETE FROM coverage_sample")
    stat = {"vzorek": len(icos), "ma_zaverku": 0, "pdf": 0,
            "citelne": 0, "sken": 0, "uver_ok": 0, "nelze_urcit": 0}

    pdf_dir = Path(cache_dir) / "coverage_pdf"
    pdf_dir.mkdir(parents=True, exist_ok=True)

    for i, ico in enumerate(icos):
        ma_zav = pdf_ok = citelne = uver_ok = False
        pozn = ""
        try:
            sid = client.resolve_subjekt_id(ico)
            listiny = client.list_listiny(sid) if sid else []
            zav = pick_latest_zaverka(listiny, roky_zpet) if listiny else []
            ma_zav = bool(zav)
            if ma_zav:
                stat["ma_zaverku"] += 1
                pdf_path = client.download_pdf(zav[0], pdf_dir)
                if pdf_path:
                    pdf_ok = True
                    stat["pdf"] += 1
                    text, conf, je_sken = pdf_extract.extract(
                        pdf_path, cfg["uver_extrakce"]["ocr_jazyk"])
                    citelne = (conf == "pdf_text")
                    stat["citelne"] += int(citelne)
                    stat["sken"] += int(je_sken)
                    r = parse_uver_from_text(text, polozky, conf)
                    if r.uver_flag is not None:
                        uver_ok = True
                        stat["uver_ok"] += 1
                    else:
                        stat["nelze_urcit"] += 1
                    pozn = f"conf={conf} flag={r.uver_flag} castka={r.uver_castka}"
        except Exception as e:
            pozn = f"chyba: {e}"
            log.debug("coverage %s: %s", ico, e)

        con.execute("INSERT INTO coverage_sample VALUES (?,?,?,?,?,?)",
                    [ico, ma_zav, pdf_ok, citelne, uver_ok, pozn])
        if (i + 1) % 50 == 0:
            log.info("coverage: %d/%d zpracováno", i + 1, len(icos))

    dl.close()
    _print_report(stat)
    return stat


def _print_report(stat: dict) -> None:
    v = max(1, stat["vzorek"])
    mz = max(1, stat["ma_zaverku"])
    pdf = max(1, stat["pdf"])
    print("\n===== COVERAGE VRSTVY C (vzorek PO) =====")
    print(f"  vzorek PO:                    {stat['vzorek']}")
    print(f"  má dohledatelnou závěrku:     {stat['ma_zaverku']}  ({100*stat['ma_zaverku']/v:.1f} %)")
    print(f"  PDF staženo:                  {stat['pdf']}  ({100*stat['pdf']/mz:.1f} % z těch se závěrkou)")
    print(f"  strojově čitelné:             {stat['citelne']}  ({100*stat['citelne']/pdf:.1f} % z PDF)")
    print(f"  skeny (nutné OCR):            {stat['sken']}  ({100*stat['sken']/pdf:.1f} % z PDF)")
    print(f"  úvěr úspěšně vyhodnocen:      {stat['uver_ok']}  ({100*stat['uver_ok']/pdf:.1f} % z PDF)")
    print(f"  položka nenalezena (nelze):   {stat['nelze_urcit']}")
    print("=========================================")
    print("Podle těchto čísel rozhodni, zda pustit plnou vrstvu C plošně,")
    print("nebo jen 'kde to šlo'. (viz SPEC — milník před plnou vrstvou C)\n")
