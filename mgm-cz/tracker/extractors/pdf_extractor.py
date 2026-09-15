"""Extrakce textu z PDF."""
from __future__ import annotations

import io

from . import ExtractResult, normalize


def extract(raw: bytes) -> ExtractResult:
    try:
        from pypdf import PdfReader
    except ImportError as exc:  # pragma: no cover
        raise RuntimeError("chybi pypdf - spust `pip install -r requirements.txt`") from exc

    warnings: list[str] = []
    reader = PdfReader(io.BytesIO(raw))

    if getattr(reader, "is_encrypted", False):
        try:
            reader.decrypt("")  # bezne u PDF chranenych jen proti editaci
        except Exception:
            warnings.append("PDF je sifrovane a nepodarilo se ho otevrit")
            return ExtractResult("", warnings)

    pages: list[str] = []
    for i, page in enumerate(reader.pages):
        try:
            pages.append(page.extract_text() or "")
        except Exception as exc:
            warnings.append(f"strana {i + 1}: extrakce selhala ({exc})")

    text = normalize("\n".join(pages))
    if not text:
        # Nejcastejsi pricina: naskenovany dokument bez textove vrstvy.
        warnings.append(
            "z PDF se nepodarilo vytahnout zadny text - pravdepodobne sken bez OCR; "
            "sleduje se jen hash souboru"
        )
    return ExtractResult(text, warnings)
