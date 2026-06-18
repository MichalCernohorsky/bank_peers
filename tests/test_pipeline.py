"""Testy build/ingest pipeline proti reálnému xlsx vzorku (tests/fixtures)."""
from pipeline.db import Conn


def test_validation_all_pass(built_db):
    """Všechny 4 rekonciliační kontroly musí projít (validace = brána)."""
    r = built_db["result"]
    assert r["all_ok"] is True
    for name, ok, tot, bad in r["checks"]:
        assert ok == tot, f"check selhal: {name} ({ok}/{tot}) {bad}"


def test_counts_nonzero(built_db):
    r = built_db["result"]
    assert r["n_metrics"] == 30
    assert r["n_facts"] > 2000
    assert r["derived"]["total_liabilities"] > 0
    assert r["derived"]["loan_to_deposit_ratio"] > 0


def test_anchor_net_profit(built_db):
    """Kotva: net_profit 2026 Q1 = 7086 (headline z reportu)."""
    con = Conn(built_db["url"])
    row = con.query_one("""SELECT f.value AS v FROM fact f JOIN period p ON p.id=f.period_id
                           WHERE f.code='net_profit' AND p.fiscal_year=2026 AND p.quarter=1
                           AND f.basis='reported'""")
    con.close()
    assert row is not None and abs(row["v"] - 7086.0) < 1.0


def test_ytd_diff_quarter_derivation(built_db):
    """Flow metrika: samostatné čtvrtletí value = YTD_n - YTD_(n-1); Q1 value = YTD_1."""
    con = Conn(built_db["url"])
    rows = con.query("""SELECT p.quarter AS q, f.value AS v, f.value_ytd AS ytd
                        FROM fact f JOIN period p ON p.id=f.period_id
                        WHERE f.code='net_profit' AND p.period_type='Q' AND p.fiscal_year=2025
                        AND f.basis='reported' ORDER BY p.quarter""")
    con.close()
    by = {r["q"]: r for r in rows}
    assert set(by) == {1, 2, 3, 4}
    # Q1: samostatné čtvrtletí = YTD
    assert abs(by[1]["v"] - by[1]["ytd"]) < 1e-6
    # Q2..Q4: value = YTD_n - YTD_(n-1)
    for q in (2, 3, 4):
        assert abs(by[q]["v"] - (by[q]["ytd"] - by[q - 1]["ytd"])) < 1e-6


def test_fy_rollup_equals_q4_ytd(built_db):
    """FY flow = Q4 YTD pro kompletní rok."""
    con = Conn(built_db["url"])
    fy = con.query_one("""SELECT f.value AS v FROM fact f JOIN period p ON p.id=f.period_id
                          WHERE f.code='net_profit' AND p.period_type='FY' AND p.fiscal_year=2025
                          AND f.basis='reported'""")
    q4 = con.query_one("""SELECT f.value_ytd AS ytd FROM fact f JOIN period p ON p.id=f.period_id
                          WHERE f.code='net_profit' AND p.period_type='Q' AND p.fiscal_year=2025
                          AND p.quarter=4 AND f.basis='reported'""")
    con.close()
    assert fy is not None and q4 is not None
    assert abs(fy["v"] - q4["ytd"]) < 1e-6


def test_derivation_total_liabilities(built_db):
    """Odvozeno: total_liabilities = total_assets - total_equity (stejné období)."""
    con = Conn(built_db["url"])
    rows = con.query("""SELECT ta.value AS a, te.value AS e, tl.value AS l, tl.derived AS d
                        FROM fact ta
                        JOIN fact te ON te.period_id=ta.period_id AND te.code='total_equity' AND te.basis='reported'
                        JOIN fact tl ON tl.period_id=ta.period_id AND tl.code='total_liabilities' AND tl.basis='reported'
                        WHERE ta.code='total_assets' AND ta.basis='reported'""")
    con.close()
    assert rows
    for r in rows:
        assert r["d"] == 1   # označeno jako dopočítané
        assert abs(r["l"] - (r["a"] - r["e"])) < 1.0
