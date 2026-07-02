"""Offline test parseru ISIR SOAP odpovědi + upsert do insolvence."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import db, layer_b_isir  # noqa: E402

# Zjednodušená, ale strukturně realistická SOAP odpověď getIsirPub0012.
SAMPLE = """<?xml version="1.0"?>
<S:Envelope xmlns:S="http://schemas.xmlsoap.org/soap/envelope/">
 <S:Body>
  <ns:getIsirPub0012Response xmlns:ns="http://isirws.cca.cz/types/">
    <data>
      <id>1001</id>
      <ic>27074358</ic>
      <spisZnacka>INS 1234/2024</spisZnacka>
      <druhStavuRizeni>Konkurs</druhStavuRizeni>
      <datumZalozeniUdalosti>2024-05-01</datumZalozeniUdalosti>
    </data>
    <data>
      <id>1002</id>
      <ic>45244782</ic>
      <spisZnacka>INS 9999/2023</spisZnacka>
      <druhStavuRizeni>Vyhlášen úpadek</druhStavuRizeni>
      <datumZalozeniUdalosti>2023-11-20</datumZalozeniUdalosti>
    </data>
  </ns:getIsirPub0012Response>
 </S:Body>
</S:Envelope>""".encode("utf-8")


def test_parse():
    zaznamy, max_id = layer_b_isir.parse_isir_response(SAMPLE)
    assert max_id == 1002, max_id
    icos = {z["ico"] for z in zaznamy}
    assert "27074358" in icos and "45244782" in icos, icos
    z0 = [z for z in zaznamy if z["ico"] == "27074358"][0]
    assert z0["stav"] == "Konkurs"
    assert z0["spisova_znacka"] == "INS 1234/2024"
    print("OK  ISIR parse: max_id=", max_id, "icos=", icos)


def test_upsert():
    con = db.connect(":memory:"); db.init_schema(con)
    zaznamy, _ = layer_b_isir.parse_isir_response(SAMPLE)
    sid = db.register_source(con, "ISIR", "x")
    n = layer_b_isir._upsert(con, zaznamy, sid)
    assert n == 2
    row = con.execute(
        "SELECT insolvence_flag, insolvence_stav FROM insolvence WHERE ico='27074358'"
    ).fetchone()
    assert row[0] is True and row[1] == "Konkurs"
    # opakovaný upsert nesmí duplikovat
    layer_b_isir._upsert(con, zaznamy, sid)
    assert con.execute("SELECT COUNT(*) FROM insolvence").fetchone()[0] == 2
    print("OK  ISIR upsert idempotentní")


if __name__ == "__main__":
    test_parse(); test_upsert()
    print("\nvšechny testy vrstvy B prošly")
