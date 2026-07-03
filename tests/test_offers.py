"""Testy produktových nabídek (pipeline.offers) — snapshot z configu, bez sítě."""
import datetime as dt
import json

import pytest

from pipeline import offers as O
from pipeline.offers import diff_snapshot, is_stale, snapshot, validate_rate


def test_provenance_fields():
    s = snapshot("savings_account")
    assert s["disclaimer"] and s["fresh_days"]
    for b in s["banks"]:
        assert b["method"] == "fallback" and b["checked_at"]
        assert "stale" in b and "flags" in b


def test_validate_rate_range():
    assert validate_rate(0.038) and validate_rate(None)
    assert not validate_rate(0.09) and not validate_rate(-0.01)   # mimo rozsah


def test_staleness():
    today = dt.date(2026, 7, 3)
    assert is_stale("2026-01", 45, today=today) is True    # staré -> ověřit
    assert is_stale("2026-06", 45, today=today) is False   # čerstvé
    assert is_stale(None, 45, today=today) is True         # chybí datum -> ber jako staré


def test_change_detection_diff():
    prev = {"kind": "table", "banks": [{"code": "cs", "rate": 0.038}]}
    new = {"kind": "table", "banks": [{"code": "cs", "rate": 0.030}]}
    d = diff_snapshot(prev, new)
    assert d == [{"bank": "cs", "old": 0.038, "new": 0.030}]


def test_term_deposit_matrix():
    s = snapshot("term_deposit")
    assert s["kind"] == "matrix" and s["terms"] and s["term_labels"]
    for b in s["banks"]:
        assert isinstance(b["rates"], dict) and b["short"] and b["name"]

    def maxr(b):
        vals = [v for v in b["rates"].values() if v is not None]
        return max(vals) if vals else 0
    ms = [maxr(b) for b in s["banks"]]
    assert ms == sorted(ms, reverse=True)   # nejvyšší sazba nahoře


def test_snapshot_from_config():
    s = snapshot("savings_account")   # live=False -> jen config, žádná síť
    assert s["product"] == "savings_account" and s["label"] and s["kind"] == "table"
    codes = {b["code"] for b in s["banks"]}
    # celý retailový trh, ne jen 4 IR banky
    assert {"cs", "kb", "csob", "moneta"} <= codes
    assert {"airbank", "raiffeisenbank", "mbank"} <= codes
    assert len(codes) >= 12
    for b in s["banks"]:
        assert b["status"] == "fallback"          # bez sítě = ověřený fallback
        assert b["rate"] is not None and b["rate_label"]
        assert b["accent"].startswith("#") and b["short"] and b["name"]


def test_snapshot_sorted_by_rate_desc():
    s = snapshot("savings_account")
    rates = [b["rate"] for b in s["banks"]]
    assert rates == sorted(rates, reverse=True)   # nejvyšší sazba nahoře


def test_unknown_product_raises():
    with pytest.raises(ValueError):
        snapshot("neexistuje")


# --- brána schválení (návrh → potvrzení člověkem): stav v izolovaném DATA_DIR ---
@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    monkeypatch.setattr(O, "DATA_DIR", tmp_path)   # stav mimo repo
    return tmp_path


def test_bootstrap_publishes(data_dir):
    """První běh nemá s čím porovnat -> publikuje rovnou, nic nezadrží."""
    O.refresh("savings_account", live=False)
    pub = O.published_path("savings_account")
    assert pub.exists()                       # publikováno
    assert not O._staging_path("savings_account").exists()
    assert O.pending("savings_account") is None
    assert json.loads(pub.read_text())["product"] == "savings_account"


def test_small_change_auto_publishes(data_dir):
    """Malá/žádná změna proti publikovanému -> auto-publish (bez zadržení)."""
    O.refresh("savings_account", live=False)
    before = json.loads(O.published_path("savings_account").read_text())
    O.refresh("savings_account", live=False)   # stejná data z configu
    after = json.loads(O.published_path("savings_account").read_text())
    assert before["banks"][0]["code"] == after["banks"][0]["code"]
    assert O.pending("savings_account") is None


def test_big_jump_is_held_not_published(data_dir):
    """Velký skok (> REVIEW_DELTA) se zadrží do staging a NEPUBLIKUJE."""
    O.refresh("savings_account", live=False)   # bootstrap publish
    pub = O.published_path("savings_account")
    published = json.loads(pub.read_text())

    # podvrhni publikovanou sazbu tak, aby nový snapshot vypadal jako velký skok dolů
    doctored = published["banks"][0]["rate"] + 0.02   # +2 p.b. rozdíl
    published["banks"][0]["rate"] = doctored
    pub.write_text(json.dumps(published, ensure_ascii=False))

    alerts = []
    O.refresh("savings_account", live=False,
              notify=lambda *a, **k: alerts.append((a, k)))

    # published zůstal na podvrhu (nepublikovalo se), návrh čeká ke schválení
    assert json.loads(pub.read_text())["banks"][0]["rate"] == doctored
    pend = O.pending("savings_account")
    assert pend and pend["reasons"]["big_changes"]
    assert any(k.get("level") == "alert" for _, k in alerts)


def test_approve_promotes_staging(data_dir):
    """approve() přenese staging -> published a uklidí pending."""
    O.refresh("savings_account", live=False)
    pub = O.published_path("savings_account")
    published = json.loads(pub.read_text())
    published["banks"][0]["rate"] = published["banks"][0]["rate"] + 0.02
    pub.write_text(json.dumps(published, ensure_ascii=False))
    O.refresh("savings_account", live=False, notify=lambda *a, **k: None)

    staged = json.loads(O._staging_path("savings_account").read_text())
    O.approve("savings_account", notify=lambda *a, **k: None)

    now_pub = json.loads(pub.read_text())
    assert now_pub["banks"][0]["rate"] == staged["banks"][0]["rate"]   # promotováno
    assert all("needs_review" not in b for b in now_pub["banks"])      # vyčištěno
    assert O.pending("savings_account") is None                       # pending uklizen


def test_reject_keeps_published(data_dir):
    """reject() zahodí návrh; publikovaná data zůstanou beze změny."""
    O.refresh("savings_account", live=False)
    pub = O.published_path("savings_account")
    published = json.loads(pub.read_text())
    published["banks"][0]["rate"] = published["banks"][0]["rate"] + 0.02
    pub.write_text(json.dumps(published, ensure_ascii=False))
    before = pub.read_text()
    O.refresh("savings_account", live=False, notify=lambda *a, **k: None)

    O.reject("savings_account")
    assert pub.read_text() == before               # published beze změny
    assert O.pending("savings_account") is None    # návrh zahozen
