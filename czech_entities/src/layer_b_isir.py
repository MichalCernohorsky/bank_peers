"""Vrstva B — insolvenční rejstřík (ISIR) přes SOAP webovou službu.

ISIR nemá prostý CSV bulk; kompletní data se stahují inkrementálně metodou
getIsirPub0012 (vrací akce s id > poslední_id, max 1000 na volání). Stav
(poslední zpracované id) se drží v DuckDB → resumovatelné, idempotentní.

Z každé akce nás zajímá dlužník: IČO (u PO), spisová značka a stav řízení.
Do tabulky `insolvence` ukládáme příznak + poslední známý stav na IČO.

V TOMTO prostředí je isir.justice.cz blokován → reálný běh na stroji bez
blokace. Parser odpovědi je offline testovaný na vzorku XML.
"""
from __future__ import annotations

import datetime as dt
import logging
from pathlib import Path
from xml.etree import ElementTree as ET

import yaml

from src import db
from src.http_client import Downloader
from src.ico import normalize_ico

log = logging.getLogger("czech_entities.layer_b")

SOAP_TEMPLATE = (
    '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" '
    'xmlns:typ="http://isirws.cca.cz/types/">'
    "<soapenv:Body>"
    "<typ:getIsirPub0012Request>"
    "<typ:idPodnetu>{last_id}</typ:idPodnetu>"
    "</typ:getIsirPub0012Request>"
    "</soapenv:Body></soapenv:Envelope>"
)


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def parse_isir_response(xml_bytes: bytes) -> tuple[list[dict], int | None]:
    """Z SOAP odpovědi vytáhne seznam akcí a nejvyšší id.

    Vrací (zaznamy, max_id). Každý záznam: {ico, spisova_znacka, stav, id, datum}.
    Namespace-agnostické (localname), robustní vůči variantám schématu.
    """
    root = ET.fromstring(xml_bytes)
    zaznamy: list[dict] = []
    max_id: int | None = None

    # každá "udalost"/"data" položka je jeden záznam řízení
    for el in root.iter():
        if _local(el.tag) not in ("data", "udalost", "stav"):
            continue
        flat: dict[str, str] = {}
        for ch in el.iter():
            ln = _local(ch.tag)
            if ch.text and ch.text.strip() and ln not in flat:
                flat[ln] = ch.text.strip()
        ico = normalize_ico(flat.get("ic") or flat.get("ico"))
        rid = flat.get("id") or flat.get("idpodnetu")
        rid_int = int(rid) if rid and rid.isdigit() else None
        if rid_int is not None:
            max_id = rid_int if max_id is None else max(max_id, rid_int)
        if not ico and not flat.get("spisznacka") and not flat.get("spisovaznacka"):
            continue
        zaznamy.append({
            "ico": ico,
            "spisova_znacka": flat.get("spisznacka") or flat.get("spisovaznacka"),
            "stav": flat.get("druhstavurizeni") or flat.get("stav") or flat.get("typudalosti"),
            "id": rid_int,
            "datum": flat.get("datumzalozeniudalosti") or flat.get("datum"),
        })
    return zaznamy, max_id


def _get_last_id(con) -> int:
    row = con.execute(
        "SELECT poznamka FROM ingestion_run WHERE vrstva='B_risk' "
        "AND stav='ok' ORDER BY run_id DESC LIMIT 1"
    ).fetchone()
    if row and row[0] and row[0].startswith("last_id="):
        return int(row[0].split("=", 1)[1])
    return 0


def _upsert(con, zaznamy: list[dict], source_id: int) -> int:
    n = 0
    now = dt.datetime.now()
    for z in zaznamy:
        if not z["ico"]:
            continue
        d = None
        if z.get("datum"):
            try:
                d = dt.date.fromisoformat(z["datum"][:10])
            except ValueError:
                d = None
        con.execute("DELETE FROM insolvence WHERE ico=?", [z["ico"]])
        con.execute(
            "INSERT INTO insolvence VALUES (?,?,?,?,?,?,?)",
            [z["ico"], True, z["stav"], z["spisova_znacka"], d, source_id, now],
        )
        n += 1
    return n


def ingest(con, config_path: str, cache_dir: str, force: bool = False,
           max_calls: int = 100000):
    cfg = yaml.safe_load(Path(config_path).read_text(encoding="utf-8"))
    isir = cfg["isir"]
    endpoint = isir["endpoint"]

    sid = db.register_source(con, "ISIR", endpoint, None, "ISIR SOAP getIsirPub0012")
    rid = db.start_run(con, "B_risk")
    last_id = 0 if force else _get_last_id(con)
    total, calls = 0, 0

    with Downloader(cache_dir) as dl:
        while calls < max_calls:
            body = SOAP_TEMPLATE.format(last_id=last_id)
            try:
                dl.rate.wait()
                resp = dl._client.post(
                    endpoint, content=body.encode("utf-8"),
                    headers={"Content-Type": "text/xml; charset=utf-8", "SOAPAction": ""},
                )
                resp.raise_for_status()
            except Exception as e:
                log.error("ISIR volání selhalo (last_id=%d): %s", last_id, e)
                db.finish_run(con, rid, total, 1, "failed", f"last_id={last_id}")
                raise
            zaznamy, max_id = parse_isir_response(resp.content)
            if not zaznamy or max_id is None or max_id <= last_id:
                break
            total += _upsert(con, zaznamy, sid)
            last_id = max_id
            calls += 1
            if calls % 50 == 0:
                log.info("ISIR: %d volání, %d insolvenčních záznamů, last_id=%d",
                         calls, total, last_id)

    db.finish_run(con, rid, total, 0, "ok", f"last_id={last_id}")
    log.info("vrstva B hotová: %d insolvenčních subjektů (last_id=%d)", total, last_id)
