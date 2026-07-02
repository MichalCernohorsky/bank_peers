"""Testy jádra extrakce úvěru z rozvahy (offline, syntetické výkazy)."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.uver_parser import parse_uver_from_text, _parse_number, _norm  # noqa: E402

POLOZKY = [
    "Bankovní úvěry a výpomoci",
    "Závazky k úvěrovým institucím",
    "Krátkodobé bankovní úvěry",
]

# Reálně vypadající úsek pasiv rozvahy (plný rozsah).
ROZVAHA_PLNA = """
PASIVA CELKEM                                        125 430
B. Cizí zdroje                                        80 200
   B.II. Dlouhodobé závazky                            5 000
   B.III. Krátkodobé závazky                          40 200
   B.IV. Bankovní úvěry a výpomoci                     35 000
        1. Dlouhodobé bankovní úvěry                   20 000
        2. Krátkodobé bankovní úvěry                   15 000
"""

# IFRS členění.
ROZVAHA_IFRS = """
Závazky
  Závazky k úvěrovým institucím                     1 234 567
  Závazky k klientům                                9 000 000
"""

# Zkrácený rozsah mikro jednotky — bankovní úvěry NEjsou vyčleněny.
ROZVAHA_ZKRACENA = """
PASIVA CELKEM                                          850
A. Vlastní kapitál                                     300
B.+C. Cizí zdroje                                       550
"""

# Řádek s položkou, ale bez čitelné hodnoty (např. rozbité OCR).
ROZVAHA_BEZ_CISLA = """
B.IV. Bankovní úvěry a výpomoci
"""

# Záporná hodnota v závorce.
ROZVAHA_ZAPORNA = """
Bankovní úvěry a výpomoci                            (5 000)
"""


def test_parse_number():
    assert _parse_number("35 000") == 35000
    assert _parse_number("1 234 567") == 1234567
    assert _parse_number("1.234.567") == 1234567
    assert _parse_number("12 345,50") == 12345.5
    assert _parse_number("(5 000)") == -5000
    assert _parse_number("abc") is None


def test_plna_rozvaha():
    r = parse_uver_from_text(ROZVAHA_PLNA, POLOZKY)
    assert r.uver_flag is True
    assert r.uver_castka == 35000, r.uver_castka
    assert "Bankovní úvěry a výpomoci" in r.polozka_text
    assert r.confidence == "pdf_text"


def test_ifrs():
    r = parse_uver_from_text(ROZVAHA_IFRS, POLOZKY)
    assert r.uver_flag is True
    assert r.uver_castka == 1234567


def test_zkracena_nelze_urcit():
    r = parse_uver_from_text(ROZVAHA_ZKRACENA, POLOZKY)
    assert r.uver_flag is None       # nelze určit
    assert r.uver_castka is None
    assert r.confidence == "neurcito"


def test_polozka_bez_cisla():
    r = parse_uver_from_text(ROZVAHA_BEZ_CISLA, POLOZKY)
    assert r.uver_flag is True       # řádek existuje
    assert r.uver_castka is None     # hodnotu nešlo přečíst


def test_zaporna():
    r = parse_uver_from_text(ROZVAHA_ZAPORNA, POLOZKY)
    assert r.uver_castka == -5000


def test_prazdny_vstup():
    r = parse_uver_from_text("", POLOZKY)
    assert r.uver_flag is None and r.confidence == "neurcito"


def test_norm():
    assert _norm("Bankovní  ÚVĚRY") == "bankovni uvery"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"OK  {fn.__name__}")
    print(f"\nvšech {len(fns)} testů úvěr-parseru prošlo")
