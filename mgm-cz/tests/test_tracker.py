"""Testy trackeru - bez site, vse nad fixtures a falesnym fetcherem."""
from pathlib import Path

import pytest

import run as tracker

FIXTURES = Path(__file__).resolve().parent / "fixtures"

SUBJECT = {"record_id": "testovaci-banka__program", "subject": "Testovací banka"}


def fake_fetch(fixture: str):
    """Fetcher, ktery misto site vraci obsah fixture."""
    payload = (FIXTURES / fixture).read_bytes()

    def _fetch(url: str) -> tracker.FetchResult:
        return tracker.FetchResult(True, payload, status=200)

    return _fetch


def failing_fetch(error: str):
    def _fetch(url: str) -> tracker.FetchResult:
        return tracker.FetchResult(False, error=error)

    return _fetch


def run_source(fixture, today, snapshots, *, selector="main", stype="html",
               anchors=None, fetch=None):
    source = {
        "url": "https://example.test/doporucte-nas",
        "type": stype,
        "selector": selector,
        "anchors": anchors or [],
    }
    return tracker.process_source(
        SUBJECT, source, fetch or fake_fetch(fixture), today, snapshots, write=True
    )


# ------------------------------------------------------------------ zakladni behy

def test_prvni_beh_zalozi_snapshot(tmp_path):
    outcome = run_source("stranka-v1.html", "2026-01-01", tmp_path)
    assert outcome.status == "first_snapshot"
    assert outcome.needs_review is False
    saved = list(tmp_path.rglob("*.txt"))
    assert len(saved) == 1
    assert "500 Kč" in saved[0].read_text(encoding="utf-8")


def test_snapshot_uklada_i_surovy_soubor(tmp_path):
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    assert list(tmp_path.rglob("*.html")), "surovy HTML snapshot musi zustat vedle .txt"


def test_pdf_snapshot_ma_priponu_pdf(tmp_path):
    run_source("pravidla-v1.pdf", "2026-01-01", tmp_path, selector=None, stype="pdf")
    assert list(tmp_path.rglob("*.pdf"))


# ------------------------------------------------- DEFINITION OF DONE: zadne falesne zmeny

def test_druhy_beh_na_nezmenenych_datech_nehlasi_zmenu(tmp_path):
    """DoD ze zadani: opakovany beh nad stejnym obsahem nesmi hlasit zmenu."""
    first = run_source("stranka-v1.html", "2026-01-01", tmp_path)
    assert first.status == "first_snapshot"

    second = run_source("stranka-v1.html", "2026-01-02", tmp_path)
    assert second.status == "unchanged"
    assert second.diff == ""
    assert second.needs_review is False


def test_opakovany_beh_tyz_den_nehlasi_zmenu(tmp_path):
    """Dvoji spusteni ve stejny den se porovnava proti stejnemu baseline."""
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    run_source("stranka-v1.html", "2026-01-02", tmp_path)
    again = run_source("stranka-v1.html", "2026-01-02", tmp_path)
    assert again.status == "unchanged"


def test_zmena_tyz_den_se_neztrati(tmp_path):
    """Regrese: zmena mezi dvema behy tehoz dne se MUSI zachytit.

    Driv se porovnavalo jen proti starsim dnum, takze druhy beh prepsal dnesni
    snapshot novym obsahem a rozdil zmizel - navzdy, protoze zitrejsi beh uz
    videl jen novou verzi.
    """
    first = run_source("jedna-castka-v1.html", "2026-01-01", tmp_path)
    assert first.status == "first_snapshot"

    same_day = run_source("jedna-castka-v2.html", "2026-01-01", tmp_path)
    assert same_day.status == "changed", "zmena tyz den se nesmi ztratit"
    assert same_day.proposed["amounts_added"] == ["750 CZK"]


def test_druhy_beh_tyz_den_je_unchanged_ne_first_snapshot(tmp_path):
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    second = run_source("stranka-v1.html", "2026-01-01", tmp_path)
    assert second.status == "unchanged"


def test_reformatovane_html_neni_zmena(tmp_path):
    """Zmena odsazeni v sablone nesmi vypadat jako zmena podminek."""
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    outcome = run_source("stranka-v1-reformatovana.html", "2026-01-02", tmp_path)
    assert outcome.status == "unchanged"


def test_tri_behy_bez_zmeny_nevyrobi_ani_jednu_udalost(tmp_path):
    statuses = [
        run_source("stranka-v1.html", day, tmp_path).status
        for day in ("2026-01-01", "2026-01-02", "2026-01-03")
    ]
    assert statuses == ["first_snapshot", "unchanged", "unchanged"]


# ------------------------------------------------------------------ detekce zmen

def test_zmena_castky_je_detekovana(tmp_path):
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    outcome = run_source("stranka-v2.html", "2026-01-02", tmp_path)
    assert outcome.status == "changed"
    assert "750 CZK" in outcome.proposed["amounts_added"]


def test_castecna_zmena_shodnych_castek_vyzaduje_review(tmp_path):
    """Stranka nese 500 Kc dvakrat (doporucujici i doporuceny); zmeni se jen jedna.

    Mnozinovy diff nema pozici, takze "500 CZK" ze stranky nezmizi a nejde
    rozhodnout, ktere ze dvou cisel se zmenilo. Takova zmena MUSI jit na cloveka.
    """
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    outcome = run_source("stranka-v2.html", "2026-01-02", tmp_path)
    assert outcome.proposed["amounts_removed"] == [], "500 Kc zustava na strance"
    assert outcome.needs_review is True


def test_cista_vymena_jedine_castky_nevyzaduje_review(tmp_path):
    """Jedina castka na strance se zmeni 500 -> 750: jednoznacne, bez review."""
    run_source("jedna-castka-v1.html", "2026-01-01", tmp_path)
    outcome = run_source("jedna-castka-v2.html", "2026-01-02", tmp_path)
    assert outcome.status == "changed"
    assert outcome.proposed["amounts_added"] == ["750 CZK"]
    assert outcome.proposed["amounts_removed"] == ["500 CZK"]
    assert outcome.needs_review is False


def test_redesign_stranky_vyzaduje_review(tmp_path):
    """Rozpadly selektor + mnoho zmen = heuristice se neveri."""
    run_source("stranka-v1.html", "2026-01-01", tmp_path)
    outcome = run_source("stranka-redesign.html", "2026-01-02", tmp_path)
    assert outcome.status == "changed"
    assert outcome.needs_review is True
    assert any("fallback" in w for w in outcome.warnings)


def test_zmena_v_pdf_je_detekovana(tmp_path):
    run_source("pravidla-v1.pdf", "2026-01-01", tmp_path, selector=None, stype="pdf")
    outcome = run_source("pravidla-v2.pdf", "2026-01-02", tmp_path, selector=None, stype="pdf")
    assert outcome.status == "changed"
    assert "750 CZK" in outcome.proposed["amounts_added"]


# ---------------------------------------------------------------------- odolnost

def test_chybejici_kotva_varuje(tmp_path):
    outcome = run_source("stranka-v1.html", "2026-01-01", tmp_path,
                         anchors=["hypotéka"])
    assert any("kotv" in w for w in outcome.warnings)


def test_pritomna_kotva_nevaruje(tmp_path):
    outcome = run_source("stranka-v1.html", "2026-01-01", tmp_path,
                         anchors=["doporučen", "Kč"])
    assert not outcome.warnings


def test_chyba_stahovani_neshodi_beh(tmp_path):
    outcome = run_source("stranka-v1.html", "2026-01-01", tmp_path,
                         fetch=failing_fetch("HTTP 503"))
    assert outcome.status == "error"
    assert "503" in outcome.detail
    assert not list(tmp_path.rglob("*.txt")), "pri chybe se nesmi ulozit snapshot"


def test_robots_zakaz_se_respektuje(tmp_path):
    fetcher = tracker.Fetcher({"respect_robots": True})
    fetcher._robots["https://example.test"] = _DenyAll()
    result = fetcher.fetch("https://example.test/cokoliv")
    assert result.ok is False
    assert "robots" in result.error


class _DenyAll:
    def can_fetch(self, ua, url):
        return False


# ------------------------------------------------------------------ pomocne funkce

def test_slug_je_stabilni_a_ruzny_pro_ruzne_url():
    a = tracker.slug_for("https://example.test/doporucte-nas")
    assert a == tracker.slug_for("https://example.test/doporucte-nas")
    assert a != tracker.slug_for("https://example.test/jina-stranka")


def test_slug_rozlisi_stejny_nazev_na_ruznych_domenach():
    """Dve banky mivaji stranku se stejnym nazvem - nesmi si prepsat snapshot."""
    a = tracker.slug_for("https://banka-a.test/doporuceni")
    b = tracker.slug_for("https://banka-b.test/doporuceni")
    assert a != b


@pytest.mark.parametrize("text,expected", [
    ("odměna 500 Kč", {"500 CZK"}),
    ("500 Kc bez diakritiky z PDF", {"500 CZK"}),
    ("1 500 Kč a 2000 CZK", {"1500 CZK", "2000 CZK"}),
    ("sazba 4,06 % p.a.", {"4,06 %"}),
    ("bonus 75 GBP", {"75 GBP"}),
    ("žádná částka", set()),
])
def test_rozpoznani_castek(text, expected):
    assert tracker._tokens(text, tracker.AMOUNT_RE) == expected


def test_rozpoznani_dat():
    found = tracker._tokens("platí do 31. 12. 2026 a od 2026-01-30", tracker.DATE_RE)
    assert found == {"31.12.2026", "2026-01-30"}


def test_analyse_bez_zmeny_castek_vyzaduje_review():
    diff, proposed, needs_review = tracker.analyse(
        "podmínka A\nodměna 500 Kč", "podmínka B\nodměna 500 Kč", []
    )
    assert proposed["amounts_added"] == []
    assert needs_review is True, "textova zmena bez zmeny castky patri cloveku"
