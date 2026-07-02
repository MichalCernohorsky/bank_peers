"""Extrakce textu z PDF účetní závěrky + detekce skenu + OCR fallback.

Vrací (text, confidence):
  - 'pdf_text' = text šel přečíst přímo (strojově čitelné PDF)
  - 'ocr'      = PDF byl sken, proběhl OCR (ocrmypdf/tesseract, jazyk ces)
  - 'neurcito' = nešlo přečíst ani OCR

Importy PDF/OCR jsou lazy, aby modul šel načíst i tam, kde knihovny/binárky
nejsou (a šla testovat orchestrace).
"""
from __future__ import annotations

import logging
import shutil
import subprocess
import tempfile
from pathlib import Path

log = logging.getLogger("czech_entities.pdf")

# Minimální množství textu, pod kterým považujeme PDF za sken (jen šum/hlavičky).
MIN_TEXT_CHARS = 200


def extract_text_direct(pdf_path: str | Path) -> str:
    """Přímá extrakce textu přes pdfplumber. Prázdný string = žádná text. vrstva."""
    import pdfplumber

    parts: list[str] = []
    with pdfplumber.open(str(pdf_path)) as pdf:
        for page in pdf.pages:
            t = page.extract_text() or ""
            if t:
                parts.append(t)
    return "\n".join(parts)


def _has_ocr_tools() -> bool:
    return shutil.which("ocrmypdf") is not None


def run_ocr(pdf_path: str | Path, jazyk: str = "ces") -> str:
    """Spustí ocrmypdf (přidá textovou vrstvu) a vrátí extrahovaný text.

    Vyžaduje systémové ocrmypdf + tesseract-ocr-ces. Když chybí, vrací "".
    """
    if not _has_ocr_tools():
        log.warning("ocrmypdf není nainstalováno — sken nelze OCR-ovat")
        return ""
    with tempfile.TemporaryDirectory() as tmp:
        out_pdf = Path(tmp) / "ocr.pdf"
        try:
            subprocess.run(
                ["ocrmypdf", "-l", jazyk, "--force-ocr", "--quiet",
                 str(pdf_path), str(out_pdf)],
                check=True, timeout=600,
            )
        except (subprocess.CalledProcessError, subprocess.TimeoutExpired) as e:
            log.warning("OCR selhalo pro %s: %s", pdf_path, e)
            return ""
        return extract_text_direct(out_pdf)


def extract(pdf_path: str | Path, jazyk: str = "ces") -> tuple[str, str, bool]:
    """Vrátí (text, confidence, je_sken).

    Strategie: nejdřív přímá extrakce; když je textu málo → sken → OCR.
    """
    try:
        text = extract_text_direct(pdf_path)
    except Exception as e:
        log.warning("čtení PDF selhalo %s: %s", pdf_path, e)
        text = ""

    if len(text.strip()) >= MIN_TEXT_CHARS:
        return text, "pdf_text", False

    # málo textu -> pravděpodobně sken -> OCR
    ocr_text = run_ocr(pdf_path, jazyk)
    if len(ocr_text.strip()) >= MIN_TEXT_CHARS:
        return ocr_text, "ocr", True
    # ani jedno nepomohlo; vrať co máme
    best = text if len(text) >= len(ocr_text) else ocr_text
    return best, "neurcito", True
