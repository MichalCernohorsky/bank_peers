"""Testy validátoru IČO. Spuštění: python -m pytest czech_entities/tests -q
(nebo bez pytestu: python czech_entities/tests/test_ico.py)
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.ico import is_valid_ico, normalize_ico, ico_check_digit  # noqa: E402

# Reálná platná IČO (kontrolní číslice sedí).
VALID = ["45244782", "00006947", "27074358", "60193336", "25596641"]
# Neplatná (špatná kontrolní číslice nebo tvar).
INVALID = ["12345678", "1234567", "abcd", "", "123456789", "00000000"]


def test_valid():
    for ico in VALID:
        assert is_valid_ico(ico), ico


def test_invalid():
    for ico in INVALID:
        assert not is_valid_ico(ico), ico


def test_normalize():
    assert normalize_ico(6947) == "00006947"
    assert normalize_ico("  45244782 ") == "45244782"
    assert normalize_ico("1x") is None
    assert normalize_ico(123456789) is None  # >8


def test_check_digit_matches():
    # poslední číslice reálných IČO musí odpovídat výpočtu
    for ico in VALID:
        assert ico_check_digit(ico[:7]) == int(ico[7]), ico


if __name__ == "__main__":
    test_valid(); test_invalid(); test_normalize(); test_check_digit_matches()
    print("všechny testy IČO prošly")
