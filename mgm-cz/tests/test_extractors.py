"""Smoke testy parsovani pro kazdy typ zdroje - vse offline nad fixtures."""
from pathlib import Path

import pytest

from extractors import extract, normalize

FIXTURES = Path(__file__).resolve().parent / "fixtures"


def read(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()


# --------------------------------------------------------------------------- HTML

def test_html_selector_vytahne_hlavni_obsah():
    result = extract(read("stranka-v1.html"), "html", selector="main")
    assert "500 Kč" in result.text
    assert "Doporučte nás příteli" in result.text
    assert not result.warnings


def test_html_selector_orizne_navigaci_a_paticku():
    result = extract(read("stranka-v1.html"), "html", selector="main")
    assert "Menu" not in result.text
    assert "© Banka" not in result.text


def test_html_zahodi_script_a_style():
    result = extract(read("stranka-v1.html"), "html", selector=None)
    assert "tracking pixel" not in result.text
    assert "color:red" not in result.text


def test_html_fallback_pri_zmene_struktury_varuje():
    """Redesign odstranil <main> - musi se pouzit plny text A ohlasit varovani."""
    result = extract(read("stranka-redesign.html"), "html", selector="main")
    assert "1 000 Kč" in result.text
    assert result.warnings, "zmena struktury musi vyprodukovat varovani"
    assert "fallback" in result.warnings[0]


def test_reformatovane_html_nevyrobi_zmenu():
    """Prehazene odsazeni a zdvojene mezery nesmi vypadat jako zmena obsahu."""
    original = extract(read("stranka-v1.html"), "html", selector="main").text
    reformatted = extract(read("stranka-v1-reformatovana.html"), "html", selector="main").text
    assert original == reformatted


# ---------------------------------------------------------------------------- PDF

def test_pdf_vytahne_text():
    result = extract(read("pravidla-v1.pdf"), "pdf")
    assert "500 Kc" in result.text
    assert "Maximalne 10 doporucenych rocne." in result.text
    assert not result.warnings


def test_pdf_zachyti_zmenu_castky():
    v1 = extract(read("pravidla-v1.pdf"), "pdf").text
    v2 = extract(read("pravidla-v2.pdf"), "pdf").text
    assert v1 != v2
    assert "750 Kc" in v2 and "750 Kc" not in v1


def test_pdf_bez_textove_vrstvy_varuje():
    result = extract(read("sken-bez-textu.pdf"), "pdf")
    assert result.text == ""
    assert result.warnings and "sken" in result.warnings[0].lower()


# --------------------------------------------------------------------- normalizace

def test_normalize_srazi_mezery_a_zahodi_prazdne_radky():
    assert normalize("a  \n\n  b   c \n\n") == "a\nb c"


def test_neznamy_typ_zdroje_spadne_srozumitelne():
    with pytest.raises(ValueError, match="neznamy typ zdroje"):
        extract(b"x", "docx")
