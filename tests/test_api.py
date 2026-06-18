"""Testy API endpointů nad testovací DB (FastAPI TestClient)."""
import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def client(built_db, monkeypatch):
    # nasměruj app na testovací DB; q() čte DATABASE_URL z env při každém dotazu
    monkeypatch.setenv("DATABASE_URL", built_db["url"])
    from api.app import app
    return TestClient(app)


def test_banks(client):
    r = client.get("/api/banks")
    assert r.status_code == 200
    codes = {b["code"] for b in r.json()}
    assert {"cs", "kb"} <= codes


def test_dashboard_cs(client):
    r = client.get("/api/dashboard/cs")
    assert r.status_code == 200
    d = r.json()
    assert d["bank"]["code"] == "cs"
    assert d["period"]["year"] == 2026 and d["period"]["quarter"] == 1
    assert len(d["kpis"]) > 0
    assert len(d["categories"]) == 6
    np = [k for k in d["kpis"] if k["code"] == "net_profit"]
    assert np and abs(np[0]["value"] - 7086.0) < 1.0


def test_dashboard_kb_empty(client):
    """KB nemá reported data -> prázdný dashboard (UI ukáže empty-state)."""
    r = client.get("/api/dashboard/kb")
    assert r.status_code == 200
    d = r.json()
    assert d["kpis"] == [] and d["categories"] == []


def test_compare(client):
    r = client.get("/api/compare", params={"banks": "cs,kb", "basis": "adjusted"})
    assert r.status_code == 200
    d = r.json()
    assert [b["code"] for b in d["banks"]] == ["cs", "kb"]
    assert len(d["groups"]) == 4
    pairs = {m["code"]: m for g in d["groups"] for m in g["metrics"]}
    assert "net_profit" in pairs
    assert pairs["net_profit"]["cs"]["v"] is not None


def test_facts_endpoint(client):
    r = client.get("/api/facts", params={"bank": "cs", "code": "net_profit", "period_type": "Q"})
    assert r.status_code == 200
    rows = r.json()
    assert len(rows) > 0
    assert {"fiscal_year", "quarter", "value"} <= set(rows[0])


def test_root_serves_spa(client):
    r = client.get("/")
    assert r.status_code == 200
    assert "BankPulse" in r.text
