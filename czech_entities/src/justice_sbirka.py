"""Klient sbírky listin na or.justice.cz (vrstva C, metadata + PDF).

or.justice.cz je HTML aplikace (IAS UI), NE strojové API. Postup:
  1. IČO -> subjektId (vyhledání)
  2. subjektId -> seznam listin (vypis-sl-firma), filtr na účetní závěrky + roky
  3. dokumentId -> URL PDF (vypis-sl-detail)

DŮLEŽITÉ: přesné HTML/parametry se v tomto prostředí nedaly ověřit (host
blokován egress-politikou). Regexy níže odpovídají zavedené struktuře IAS UI a
je NUTNÉ je při reálném běhu potvrdit proti živému HTML. Proto je klient
oddělený a orchestrace vrstvy C ho bere jako závislost (lze podstrčit fake).
"""
from __future__ import annotations

import logging
import re
from dataclasses import dataclass

from src.http_client import Downloader

log = logging.getLogger("czech_entities.justice")


@dataclass
class Listina:
    dokument_id: str
    typ: str
    rok: int | None
    pdf_url: str | None


class SbirkaClient:
    """Rozhraní: implementace přes reálné HTTP nebo fake v testech."""

    def resolve_subjekt_id(self, ico: str) -> str | None:
        raise NotImplementedError

    def list_listiny(self, subjekt_id: str) -> list[Listina]:
        raise NotImplementedError

    def download_pdf(self, listina: Listina, dest_dir) -> "str | None":
        raise NotImplementedError


# Regexy pro parsování IAS UI HTML (nutno potvrdit proti živému HTML).
_RE_SUBJEKT_ID = re.compile(r"subjektId=(\d+)")
_RE_DOKUMENT = re.compile(r"dokument=([A-Za-z0-9]+)")
_RE_ROK = re.compile(r"(19|20)\d{2}")
_TYPY_DEFAULT = ["účetní závěrka", "výroční zpráva"]


class HttpSbirkaClient(SbirkaClient):
    def __init__(self, cfg: dict, downloader: Downloader,
                 typy_listin: list[str] | None = None):
        self.cfg = cfg
        self.dl = downloader
        self.typy = [t.lower() for t in (typy_listin or _TYPY_DEFAULT)]

    def resolve_subjekt_id(self, ico: str) -> str | None:
        url = self.cfg["or_search"]
        try:
            self.dl.rate.wait()
            r = self.dl._client.get(url, params={"ico": ico})
            r.raise_for_status()
        except Exception as e:
            log.warning("resolve subjektId(%s) selhalo: %s", ico, e)
            return None
        m = _RE_SUBJEKT_ID.search(r.text)
        return m.group(1) if m else None

    def list_listiny(self, subjekt_id: str) -> list[Listina]:
        url = self.cfg["or_sbirka_firma"].format(subjektId=subjekt_id)
        try:
            self.dl.rate.wait()
            r = self.dl._client.get(url)
            r.raise_for_status()
        except Exception as e:
            log.warning("list_listiny(%s) selhalo: %s", subjekt_id, e)
            return []
        return self._parse_listiny(r.text, subjekt_id)

    def _parse_listiny(self, html: str, subjekt_id: str) -> list[Listina]:
        out: list[Listina] = []
        # velmi hrubý parser: řádky s odkazem na dokument + typ v okolí.
        # Reálně nutno nahradit robustním HTML parserem (lxml) proti živé stránce.
        for m in _RE_DOKUMENT.finditer(html):
            dok = m.group(1)
            window = html[max(0, m.start() - 300): m.end() + 300].lower()
            if not any(t in window for t in self.typy):
                continue
            rok_m = _RE_ROK.search(window)
            rok = int(rok_m.group(0)) if rok_m else None
            typ = next((t for t in self.typy if t in window), "listina")
            pdf_url = self.cfg["or_sbirka_detail"].format(
                dokument=dok, subjektId=subjekt_id)
            out.append(Listina(dok, typ, rok, pdf_url))
        return out

    def download_pdf(self, listina: Listina, dest_dir) -> str | None:
        if not listina.pdf_url:
            return None
        try:
            path = self.dl.fetch_file(
                listina.pdf_url, f"sl_{listina.dokument_id}.pdf")
            return str(path)
        except Exception as e:
            log.warning("stažení PDF %s selhalo: %s", listina.dokument_id, e)
            return None


def pick_latest_zaverka(listiny: list[Listina], roky_zpet: int = 1) -> list[Listina]:
    """Vybere poslední N let účetních závěrek (default: poslední dostupný rok)."""
    zav = [l for l in listiny if "závěrka" in l.typ.lower() or "zaverka" in l.typ.lower()]
    if not zav:
        zav = listiny  # fallback: cokoli s rozvahou (např. výroční zpráva)
    zav.sort(key=lambda l: (l.rok or 0), reverse=True)
    return zav[:max(1, roky_zpet)]
