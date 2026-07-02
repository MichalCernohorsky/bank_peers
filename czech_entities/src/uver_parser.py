"""Jádro vrstvy C: extrakce bankovního úvěru z textu rozvahy.

Oddělené od stahování/PDF, aby šlo čistě jednotkově testovat.
Vstupem je text (z pdfplumber nebo OCR), výstupem strukturovaná indicie.

Hledané položky pasiv (dle konfigurace), typicky:
  - "Bankovní úvěry a výpomoci"  (starší členění rozvahy)
  - "Závazky k úvěrovým institucím" (IFRS/nové členění)

Pozor (dle SPEC): u mikro/malých jednotek ve zkráceném rozsahu se bankovní
úvěry samostatně nevyčleňují → výsledek „nelze určit". To je limit dat.
"""
from __future__ import annotations

import re
import unicodedata
from dataclasses import dataclass


@dataclass
class UverIndicie:
    uver_flag: bool | None      # True/False = nalezeno/nenalezeno; None = nelze určit
    uver_castka: float | None   # v jednotkách výkazu (obv. tis. Kč); None = nelze určit
    polozka_text: str | None
    confidence: str             # 'pdf_text' | 'ocr' | 'neurcito'


def _strip_diacritics(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c))


def _norm(s: str) -> str:
    """Na porovnávání: bez diakritiky, malá písmena, zhuštěné mezery."""
    return re.sub(r"\s+", " ", _strip_diacritics(s).lower()).strip()


# Číslo v českém výkazu: "1 234 567", "1.234.567", "12 345,00", "(5 000)" = záporné.
# Bereme celočíselnou/desetinnou hodnotu, oddělovače tisíců mezera/tečka/nbsp.
_NUM_RE = re.compile(
    r"\(?-?\s*\d{1,3}(?:[  . ]\d{3})*(?:,\d+)?\)?"
)


def _parse_number(token: str) -> float | None:
    t = token.strip()
    neg = t.startswith("(") and t.endswith(")")
    t = t.strip("()").replace(" ", " ").replace(" ", " ")
    t = t.replace(" ", "").replace(".", "")   # odstraň oddělovače tisíců
    t = t.replace(",", ".")                    # desetinná čárka -> tečka
    if not re.fullmatch(r"-?\d+(\.\d+)?", t):
        return None
    val = float(t)
    return -val if neg else val


def _numbers_in(line: str) -> list[float]:
    out = []
    for m in _NUM_RE.finditer(line):
        v = _parse_number(m.group(0))
        if v is not None:
            out.append(v)
    return out


def parse_uver_from_text(
    text: str,
    polozky: list[str],
    confidence: str = "pdf_text",
) -> UverIndicie:
    """Najde v textu rozvahy řádek s bankovním úvěrem a jeho částku.

    Logika:
      - normalizuje položky i řádky (bez diakritiky).
      - projde řádky; první, který obsahuje některou z položek, vezme.
      - z řádku (nebo následujícího, když na řádku číslo není) vytáhne
        první rozumné číslo jako "běžné období" (levý sloupec Netto).
      - když položka není nalezena vůbec → nelze určit (None flag).
      - když je nalezena, ale bez čísla → flag=True, castka=None
        (úvěr existuje jako řádek, ale hodnotu nešlo přečíst).
    """
    if not text or not text.strip():
        return UverIndicie(None, None, None, "neurcito")

    norm_polozky = [(_norm(p), p) for p in polozky]
    lines = text.splitlines()
    norm_lines = [_norm(l) for l in lines]

    for i, nline in enumerate(norm_lines):
        for np, orig in norm_polozky:
            if np and np in nline:
                nums = _numbers_in(lines[i])
                # číslo na dalším řádku (rozvaha někdy zalomí popis a hodnotu)
                if not nums and i + 1 < len(lines):
                    nxt = _norm(lines[i + 1])
                    # jen pokud další řádek není jiná pojmenovaná položka
                    if not any(p2 in nxt for p2, _ in norm_polozky):
                        nums = _numbers_in(lines[i + 1])
                if nums:
                    castka = nums[0]
                    return UverIndicie(
                        uver_flag=(castka != 0),
                        uver_castka=castka,
                        polozka_text=lines[i].strip(),
                        confidence=confidence,
                    )
                return UverIndicie(
                    uver_flag=True,
                    uver_castka=None,
                    polozka_text=lines[i].strip(),
                    confidence=confidence,
                )

    # položka nebyla v textu vůbec → nelze určit (typicky zkrácený rozsah)
    return UverIndicie(None, None, None, "neurcito")
