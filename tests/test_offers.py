"""Testy produktových nabídek (pipeline.offers) — snapshot z configu, bez sítě."""
import datetime as dt

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
    import pytest
    with pytest.raises(ValueError):
        snapshot("neexistuje")
