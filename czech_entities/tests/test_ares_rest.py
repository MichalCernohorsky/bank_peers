"""Offline test mapování ARES REST v3 detailu na řádek tabulky subjekt."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src.ares_rest import map_detail, _read_ico_list  # noqa: E402

# Zjednodušený, strukturně realistický JSON detailu v3.
DETAIL = {
    "ico": "45244782",
    "obchodniJmeno": "ČEZ, a. s.",
    "pravniForma": "121",
    "datumVzniku": "1992-05-06",
    "sidlo": {
        "nazevKraje": "Hlavní město Praha",
        "nazevOkresu": "Praha 4",
        "nazevObce": "Praha",
        "textovaAdresa": "Duhová 1444/2, Michle, 14000 Praha 4",
    },
    "czNace": ["3511", "3514"],
    "datovaSchranka": "abc123",
}

DETAIL_FO = {
    "ico": "10100101",
    "obchodniJmeno": "Jan Novák",
    "pravniForma": "101",
    "datumVzniku": "2010-03-01",
    "datumZaniku": "2020-01-01",
    "sidlo": {"nazevKraje": "Jihomoravský", "nazevObce": "Brno"},
    "czNace": "4711",
}


def test_map_po():
    row = map_detail(DETAIL, fo_prefixes=["10", "11"], source_id=1)
    assert row[0] == "45244782" and row[1] is True
    assert row[2] == "ČEZ, a. s."
    assert row[3] == "121" and row[5] is False          # není FO
    assert row[6] == "Hlavní město Praha"
    assert row[7] == "Praha 4"
    assert row[10] == "3511"                             # první NACE ze seznamu
    assert str(row[11]) == "1992-05-06"
    assert row[12] == "aktivní"
    assert row[13] == "abc123"
    print("OK  map PO:", row[2], row[6], row[10])


def test_map_fo_zanikly():
    row = map_detail(DETAIL_FO, fo_prefixes=["10", "11"], source_id=1)
    assert row[5] is True                                 # PF 101 -> FO
    assert row[12] == "zaniklý"                           # má datumZaniku
    assert row[10] == "4711"                              # NACE jako string
    print("OK  map FO zaniklý")


def test_read_ico_list(tmp_path=None):
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "icos.txt"
        p.write_text("45244782\n6947\n neplatne \n27074358;pozn\n", encoding="utf-8")
        icos = _read_ico_list(str(p))
        assert "45244782" in icos and "00006947" in icos and "27074358" in icos
        print("OK  read_ico_list:", icos)


if __name__ == "__main__":
    test_map_po(); test_map_fo_zanikly(); test_read_ico_list()
    print("\nvšechny testy ARES REST mapování prošly")
