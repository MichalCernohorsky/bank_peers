"""Validace a normalizace IČO (identifikační číslo osoby).

IČO je 8místné číslo s kontrolní číslicí na poslední pozici (modulo 11).
Ve zdrojích bývá bez vedoucích nul (např. int 12345 = "00012345").

Algoritmus kontrolní číslice:
  - vezmi prvních 7 číslic a1..a7
  - váhy 8,7,6,5,4,3,2
  - suma = sum(a_i * w_i);  zbytek = suma % 11
  - kontrolní číslice c:
        zbytek == 0 -> c = 1
        zbytek == 1 -> c = 0
        jinak       -> c = 11 - zbytek
  - platí, pokud c == a8
"""
from __future__ import annotations


def normalize_ico(value) -> str | None:
    """Doplní na 8 číslic vedoucími nulami. Vrátí None pro nesmysl.

    Přijímá int i str (i s mezerami). Nekontroluje kontrolní číslici —
    jen tvar. Pro validaci použij is_valid_ico().
    """
    if value is None:
        return None
    s = str(value).strip().replace(" ", "")
    if not s:
        return None
    if not s.isdigit():
        return None
    if len(s) > 8:
        return None
    return s.zfill(8)


def ico_check_digit(first7: str) -> int:
    """Vrátí očekávanou kontrolní číslici pro prvních 7 číslic."""
    weights = (8, 7, 6, 5, 4, 3, 2)
    s = sum(int(first7[i]) * weights[i] for i in range(7))
    rem = s % 11
    if rem == 0:
        return 1
    if rem == 1:
        return 0
    return 11 - rem


def is_valid_ico(value) -> bool:
    """True, pokud je IČO 8místné a sedí kontrolní číslice (modulo 11)."""
    ico = normalize_ico(value)
    if ico is None or len(ico) != 8:
        return False
    return ico_check_digit(ico[:7]) == int(ico[7])


if __name__ == "__main__":
    # rychlá manuální kontrola na známých IČO
    samples = {
        "45244782": True,   # ČEZ
        "00006947": True,   # Ministerstvo financí
        "27074358": True,   # Alza
        "12345678": False,  # náhoda
        "1234567": False,   # krátké
        "abcd": False,
    }
    for ico, expected in samples.items():
        got = is_valid_ico(ico)
        flag = "OK" if got == expected else "FAIL"
        print(f"{flag}  {ico!r:>12}  valid={got}  (čekáno {expected})")
