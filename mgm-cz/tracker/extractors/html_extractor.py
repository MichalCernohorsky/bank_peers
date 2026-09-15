"""Extrakce textu z HTML."""
from __future__ import annotations

from . import ExtractResult, normalize

# Bloky, ktere nikdy nenesou podminky programu a jen by delaly sum v diffu.
_DROP_TAGS = ("script", "style", "noscript", "svg", "iframe", "template")


def extract(raw: bytes, *, selector: str | None = None) -> ExtractResult:
    try:
        from bs4 import BeautifulSoup
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("chybi beautifulsoup4 - spust `pip install -r requirements.txt`") from exc

    warnings: list[str] = []
    soup = BeautifulSoup(raw, "html.parser")

    for tag in soup(_DROP_TAGS):
        tag.decompose()

    root = soup
    if selector:
        matched = soup.select(selector)
        if matched:
            # Vic shod slucujeme, aby se stranka rozdelena do sekci neorezala.
            text = "\n".join(node.get_text("\n") for node in matched)
            return ExtractResult(normalize(text), warnings)
        # FALLBACK: selektor nesedi -> zmenila se struktura stranky.
        warnings.append(
            f"selektor {selector!r} nic nenasel - fallback na plny text stranky; "
            "zkontroluj, jestli se nezmenila struktura a neaktualizuj data automaticky"
        )
        root = soup

    body = root.body if getattr(root, "body", None) else root
    return ExtractResult(normalize(body.get_text("\n")), warnings)
