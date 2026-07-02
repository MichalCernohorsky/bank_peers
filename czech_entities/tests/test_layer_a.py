"""Offline test vrstvy A: syntetický VREO tar.gz -> tabulka subjekt.

Downloader vezme předpřipravený soubor z cache jako cache-hit (bez sítě),
takže projedeme reálnou cestu ingest() end-to-end bez přístupu na ares.gov.cz.
"""
import io
import sys
import tarfile
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import db, layer_a_res  # noqa: E402

# Dva syntetické záznamy VREO (namespaced i bez ns), třetí s neplatným IČO.
REC_OK = """<?xml version="1.0"?>
<Zaznam>
  <ico>45244782</ico>
  <obchodniJmeno>ČEZ, a. s.</obchodniJmeno>
  <pravniForma>121</pravniForma>
  <sidlo><nazevKraje>Hlavní město Praha</nazevKraje><nazevObce>Praha</nazevObce></sidlo>
  <czNace>3511</czNace>
  <datumVzniku>1992-05-06</datumVzniku>
  <pravniStav>aktivní</pravniStav>
</Zaznam>"""

REC_FO = """<?xml version="1.0"?>
<Zaznam xmlns="urn:cz:isvs:ares">
  <ico>00006947</ico>
  <obchodniJmeno>Testovací OSVČ</obchodniJmeno>
  <pravniForma>101</pravniForma>
  <nazevOkresu>Brno-město</nazevOkresu>
  <datumVzniku>10.01.2001</datumVzniku>
  <pravniStav>aktivní</pravniStav>
</Zaznam>"""

REC_BAD = """<?xml version="1.0"?>
<Zaznam><ico>99999999</ico><obchodniJmeno>Neplatné IČO</obchodniJmeno></Zaznam>"""


def _make_archive(path: Path):
    with tarfile.open(path, "w:gz") as tar:
        for name, content in [("a.xml", REC_OK), ("b.xml", REC_FO), ("c.xml", REC_BAD)]:
            data = content.encode("utf-8")
            info = tarfile.TarInfo(name)
            info.size = len(data)
            tar.addfile(info, io.BytesIO(data))


CONFIG = """
rate_limit: {ares_max_per_min: 300}
ares:
  vreo_all_url: "https://ares.gov.cz/otevrena-data/ares_vreo_all.tar.gz"
  vreo_field_map:
    ico: [ico]
    nazev: [obchodniJmeno]
    pravni_forma: [pravniForma]
    sidlo_text: [sidlo]
    sidlo_kraj: [nazevKraje]
    sidlo_okres: [nazevOkresu]
    sidlo_obec: [nazevObce]
    nace: [czNace]
    datum_vzniku: [datumVzniku]
    datum_zaniku: [datumZaniku]
    stav: [pravniStav]
    datova_schranka: [datovaSchranka]
  fo_pravni_forma_prefix: ["10", "11"]
"""


def test_ingest_end_to_end():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        cache = tmp / "cache"; cache.mkdir()
        # předpřiprav archiv do cache pod očekávaným jménem -> cache hit
        _make_archive(cache / "ares_vreo_all.tar.gz")
        cfg = tmp / "sources.yaml"; cfg.write_text(CONFIG, encoding="utf-8")

        con = db.connect(":memory:")
        db.init_schema(con)
        layer_a_res.ingest(con, str(cfg), str(cache))

        rows = con.execute(
            "SELECT ico, nazev, je_fo, sidlo_kraj, nace, datum_vzniku, ico_valid "
            "FROM subjekt ORDER BY ico").fetchall()
        # neplatné IČO (99999999) se uloží, ale ico_valid=False; validní 2 mají True
        icos = [r[0] for r in rows]
        assert "45244782" in icos and "00006947" in icos
        cez = [r for r in rows if r[0] == "45244782"][0]
        assert cez[1] == "ČEZ, a. s."
        assert cez[2] is False            # a.s. není FO
        assert cez[3] == "Hlavní město Praha"
        assert cez[4] == "3511"
        assert str(cez[5]) == "1992-05-06"
        assert cez[6] is True

        osvc = [r for r in rows if r[0] == "00006947"][0]
        assert osvc[2] is True            # pravní forma 101 -> FO
        assert str(osvc[5]) == "2001-01-10"   # parsování d.m.Y

        bad = [r for r in rows if r[0] == "99999999"][0]
        assert bad[6] is False            # kontrolní číslice nesedí
        print("OK  vrstva A end-to-end:", icos)


def test_idempotence():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        cache = tmp / "cache"; cache.mkdir()
        _make_archive(cache / "ares_vreo_all.tar.gz")
        cfg = tmp / "sources.yaml"; cfg.write_text(CONFIG, encoding="utf-8")
        con = db.connect(":memory:"); db.init_schema(con)
        layer_a_res.ingest(con, str(cfg), str(cache))
        layer_a_res.ingest(con, str(cfg), str(cache))   # 2. běh nesmí duplikovat
        n = con.execute("SELECT COUNT(*) FROM subjekt").fetchone()[0]
        assert n == 3, n
        print("OK  idempotence: 3 řádky i po 2 bězích")


if __name__ == "__main__":
    test_ingest_end_to_end()
    test_idempotence()
    print("\nvšechny testy vrstvy A prošly")
