"""Extrakce citelneho textu ze stazenych zdroju.

POZOR na nazvy modulu: soubory se jmenuji html_extractor.py / pdf_extractor.py
zamerne. Modul pojmenovany html.py by stinil stdlib modul `html`, na kterem
zavisi beautifulsoup4 (`from html.entities import ...`), a bs4 by pak spadlo
na ImportError kdykoli by byl tento adresar na sys.path.

Kazdy extraktor vraci ExtractResult s normalizovanym textem a seznamem varovani.
Varovani NENI chyba - typicky znamena, ze se zmenila struktura stranky a musel
se pouzit fallback na plny text. Takovy zdroj vyprodukuje velky diff, ktery je
nutne posoudit rucne, ne automaticky promitnout do dat.
"""
from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ExtractResult:
    text: str
    warnings: list[str] = field(default_factory=list)


def normalize(text: str) -> str:
    """Sjednoti bily znak, aby diff nereagoval na reformatovani HTML.

    Radky se zachovavaji (nesou strukturu), ale mezery uvnitr radku se srazi
    a prazdne radky se zahodi. Bez toho by kazda zmena odsazeni v sablone
    vypadala jako zmena obsahu.
    """
    lines = (" ".join(line.split()) for line in text.splitlines())
    return "\n".join(line for line in lines if line)


def extract(raw: bytes, source_type: str, *, selector: str | None = None) -> ExtractResult:
    """Dispatch podle typu zdroje z config/sources.yaml."""
    if source_type == "html":
        from . import html_extractor

        return html_extractor.extract(raw, selector=selector)
    if source_type == "pdf":
        from . import pdf_extractor

        return pdf_extractor.extract(raw)
    raise ValueError(f"neznamy typ zdroje: {source_type!r} (podporovane: html, pdf)")
