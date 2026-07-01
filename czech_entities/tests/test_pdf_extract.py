"""Test PDF -> text -> úvěr na REÁLNÉM vygenerovaném PDF (strojově čitelném).

Ověřuje celý řetězec vrstvy C kromě stahování/OCR (síť + tesseract se v tomto
prostředí neověřují). fpdf2 je jen testovací závislost pro generování vzorku.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import pdf_extract  # noqa: E402
from src.uver_parser import parse_uver_from_text  # noqa: E402

POLOZKY = ["Bankovní úvěry a výpomoci", "Závazky k úvěrovým institucím"]

# Text rozvahy bez diakritiky (fpdf2 core font Helvetica zvládne latin-1;
# uver_parser stejně diakritiku odstraňuje, takže se to reálného chování týká).
ROZVAHA_LINES = [
    "ROZVAHA v plnem rozsahu ke dni 31.12.2024 (v tisicich Kc)",
    "Nazev ucetni jednotky: Testovaci Firma s.r.o.   IC: 27074358",
    "PASIVA                                         Bezne  Minule",
    "PASIVA CELKEM                                 125 430  118 000",
    "A. Vlastni kapital                             45 230   42 000",
    "B.+C. Cizi zdroje                              80 200   76 000",
    "   B. Rezervy                                   1 200    1 000",
    "   C.I. Dlouhodobe zavazky                      5 000    6 000",
    "   C.II. Kratkodobe zavazky                    39 000   35 000",
    "B.IV. Bankovni uvery a vypomoci                35 000   34 000",
    "   1. Dlouhodobe bankovni uvery                20 000   22 000",
    "   2. Kratkodobe bankovni uvery                15 000   12 000",
    "Casove rozliseni pasiv                            800      700",
]


def _make_pdf(path: Path):
    from fpdf import FPDF
    from fpdf.enums import XPos, YPos
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Courier", size=10)
    for line in ROZVAHA_LINES:
        pdf.cell(0, 6, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.output(str(path))


def test_pdf_to_uver():
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "zaverka.pdf"
        _make_pdf(p)
        text, conf, je_sken = pdf_extract.extract(p)
        assert conf == "pdf_text", (conf, je_sken)
        assert je_sken is False
        assert "PASIVA" in text.upper()

        # parser hledá i "Bankovní úvěry a výpomoci" (s diakritikou) -> match přes _norm
        r = parse_uver_from_text(text, POLOZKY, confidence=conf)
        assert r.uver_flag is True, r
        assert r.uver_castka == 35000, r.uver_castka
        print("OK  PDF->text->úvěr:", r.uver_castka, r.confidence)


if __name__ == "__main__":
    test_pdf_to_uver()
    print("\ntest PDF extrakce prošel")
