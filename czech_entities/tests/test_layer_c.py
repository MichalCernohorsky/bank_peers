"""Offline test orchestrace vrstvy C (coverage + extract) přes fake klienta.

Fake klient vrací pro některá IČO reálné vygenerované PDF s rozvahou, pro jiná
nic (simulace OSVČ/firem bez závěrky). Ověřuje se počítání coverage i zápis do
uver a finální join v exportu.
"""
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from src import db, layer_c_coverage, layer_c_extract, export  # noqa: E402
from src.justice_sbirka import SbirkaClient, Listina  # noqa: E402

ROZVAHA = [
    "ROZVAHA v plnem rozsahu ke dni 31.12.2024 (v tis. Kc)",
    "PASIVA CELKEM                                 125 430",
    "A. Vlastni kapital                             45 230",
    "B.+C. Cizi zdroje                              80 200",
    "   C.II. Kratkodobe zavazky                    39 000",
    "B.IV. Bankovni uvery a vypomoci                35 000",
    "   1. Dlouhodobe bankovni uvery                20 000",
    "Casove rozliseni pasiv                            800",
]


def _make_pdf(path: Path):
    from fpdf import FPDF
    from fpdf.enums import XPos, YPos
    pdf = FPDF(); pdf.add_page(); pdf.set_font("Courier", size=10)
    for line in ROZVAHA:
        pdf.cell(0, 6, line, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.output(str(path))


class FakeClient(SbirkaClient):
    """IČO končící lichou číslicí -> má závěrku s úvěrem; jinak nic."""
    def __init__(self, pdf_path: Path):
        self.pdf_path = pdf_path

    def resolve_subjekt_id(self, ico: str):
        return "S" + ico if int(ico[-1]) % 2 == 1 else None

    def list_listiny(self, subjekt_id: str):
        return [Listina("DOK1", "účetní závěrka", 2024,
                        f"https://or.justice.cz/detail?dokument=DOK1")]

    def download_pdf(self, listina, dest_dir):
        return str(self.pdf_path)


CONFIG = """
rate_limit: {justice_max_per_min: 120}
justice:
  or_search: x
  or_sbirka_firma: x
  or_sbirka_detail: x
  typy_listin: ["účetní závěrka"]
uver_extrakce:
  roky_zpet: 1
  ocr_jazyk: ces
  polozky_uver: ["Bankovní úvěry a výpomoci", "Závazky k úvěrovým institucím"]
"""


def _seed_subjekty(con, icos):
    import datetime as dt
    for ico in icos:
        con.execute("INSERT INTO subjekt VALUES (" + ",".join(["?"] * 16) + ")",
                    [ico, True, f"Firma {ico}", "112", None, False,
                     "Praha", None, None, None, "4711", None, "aktivní",
                     None, 1, dt.datetime.now()])


def test_coverage_and_extract():
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        pdf = tmp / "z.pdf"; _make_pdf(pdf)
        cfg = tmp / "sources.yaml"; cfg.write_text(CONFIG, encoding="utf-8")
        con = db.connect(":memory:"); db.init_schema(con)
        # 4 firmy: 2 s lichou koncovkou (mají úvěr), 2 se sudou (bez závěrky)
        icos = ["27074351", "45244783", "45244782", "00006948"]
        _seed_subjekty(con, icos)
        fake = FakeClient(pdf)

        stat = layer_c_coverage.measure(con, str(cfg), str(tmp), n=10, client=fake)
        assert stat["vzorek"] == 4
        assert stat["ma_zaverku"] == 2, stat        # jen liché
        assert stat["uver_ok"] == 2, stat
        assert stat["citelne"] == 2, stat

        res = layer_c_extract.run(con, str(cfg), str(tmp), client=fake)
        assert res["zpracovano"] == 4
        assert res["s_uverem"] == 2, res
        rows = con.execute(
            "SELECT ico, uver_flag, uver_castka FROM uver ORDER BY ico").fetchall()
        for r in rows:
            assert r[1] is True and r[2] == 35000, r

        # finální export view
        export.build_final_view(con)
        final = con.execute(
            "SELECT ico, uver_flag, uver_castka, ma_zaverku_flag "
            "FROM final_dataset ORDER BY ico").fetchall()
        assert len(final) == 4
        s_uver = [f for f in final if f[1]]
        assert len(s_uver) == 2
        print("OK  vrstva C coverage+extract+export, s úvěrem:", len(s_uver))


if __name__ == "__main__":
    test_coverage_and_extract()
    print("\ntest vrstvy C prošel")
