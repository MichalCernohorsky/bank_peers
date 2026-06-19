"""Testy ingestion automatiky (pipeline.watch) — offline, proti fixture xlsx."""
import datetime as dt
import json
from pathlib import Path

import pytest

from pipeline import watch
from pipeline.db import Conn

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "tests" / "fixtures" / "key_figures_sample.xlsx"
TODAY = dt.date(2026, 6, 19)


@pytest.fixture
def env(tmp_path):
    """Izolovaný kalendář/registr/incoming + cílová DB + zachytávač alertů."""
    cal = {
        "defaults": {"gate": {"require_validation": True, "headline_metric": "net_profit"}},
        "banks": {
            "cs": {"document": {"kind": "local", "path": str(FIXTURE)},
                   "releases": [{"period": "2026Q1", "publish_date": "2026-05-06"}]},
            "kb": {"document": {"kind": "manual"},
                   "releases": [{"period": "2026Q1", "publish_date": "2026-05-07"}]},
        },
    }
    cal_path = tmp_path / "calendar.yaml"
    cal_path.write_text(json.dumps(cal))   # JSON je validní YAML
    alerts = []

    def fake_notify(subject, body="", level="info"):
        alerts.append({"subject": subject, "body": body, "level": level})
        return subject

    return {
        "cal": str(cal_path),
        "registry": tmp_path / "registry.json",
        "incoming": tmp_path / "incoming",
        "target": f"sqlite:///{tmp_path / 'prod.db'}",
        "target_path": tmp_path / "prod.db",
        "alerts": alerts,
        "notify": fake_notify,
    }


def _run(env, **kw):
    return watch.run_once(
        calendar_path=env["cal"], registry_path=env["registry"], incoming_dir=env["incoming"],
        target_url=env["target"], today=TODAY, notify=env["notify"], **kw)


def test_due_releases_filter():
    cal = {"banks": {"cs": {"document": {"kind": "local"}, "releases": [
        {"period": "2026Q1", "publish_date": "2026-05-06"},   # due
        {"period": "2026Q2", "publish_date": "2026-08-05"},   # budoucí
    ]}}}
    due = watch.due_releases(cal, TODAY)
    periods = {p for _, p, *_ in due}
    assert periods == {"2026Q1"}


def test_first_ingest_accepted_and_provenance(env):
    out = _run(env)
    actions = {(r["bank"], r["action"]) for r in out["results"]}
    assert ("cs", "promoted") in actions
    assert ("kb", "skip-manual") in actions
    # produkce postavena + headline sedí
    assert env["target_path"].exists()
    con = Conn(env["target"])
    row = con.query_one("""SELECT f.value v FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code='cs'
                           JOIN period p ON p.id=f.period_id
                           WHERE f.code='net_profit' AND p.fiscal_year=2026 AND p.quarter=1 AND f.basis='reported'""")
    con.close()
    assert row and abs(row["v"] - 7086.0) < 1.0
    # provenance v registru
    reg = json.loads(env["registry"].read_text())
    cs = [d for d in reg["documents"] if d["bank"] == "cs"][0]
    assert cs["status"] == "accepted" and cs["vintage"] == 1
    assert len(cs["sha256"]) == 64 and cs["retrieved_at"] and cs["n_facts"] > 2000
    # alert o úspěchu (level info, ne alert)
    assert any(a["level"] == "info" and "OK" in a["subject"] for a in env["alerts"])


def test_idempotent_skip(env):
    _run(env)
    env["alerts"].clear()
    out2 = _run(env)
    assert any(r["action"] == "skip-idempotent" for r in out2["results"] if r["bank"] == "cs")
    reg = json.loads(env["registry"].read_text())
    assert sum(1 for d in reg["documents"] if d["bank"] == "cs") == 1   # žádný nový zápis


def test_validation_gate_blocks_and_alerts(env, monkeypatch):
    # simuluj neúspěšnou rekonciliaci -> nesmí promotovat, musí přijít alert
    monkeypatch.setattr(watch, "run_build",
                        lambda cfg, xlsx, url: {"all_ok": False, "checks": [], "n_facts": 0})
    out = _run(env)
    assert any(r["action"] == "rejected" for r in out["results"] if r["bank"] == "cs")
    assert not env["target_path"].exists()   # produkce nezměněna
    assert any(a["level"] == "alert" and "ZAMÍTNUTO" in a["subject"] for a in env["alerts"])
    reg = json.loads(env["registry"].read_text())
    assert [d for d in reg["documents"] if d["bank"] == "cs"][0]["status"] == "rejected"


def test_missing_document_alerts(env):
    # přebij zdroj na neexistující cestu
    out = _run(env, source_overrides={"cs": "/does/not/exist.xlsx"})
    assert any(r["action"] == "missing-document" for r in out["results"] if r["bank"] == "cs")
    assert any(a["level"] == "alert" for a in env["alerts"])
    assert not env["target_path"].exists()


def test_restatement_creates_new_vintage(env):
    # předvyplň registr přijatým záznamem pro stejné období s jiným checksumem
    watch.save_registry(env["registry"], {"documents": [
        {"bank": "cs", "period": "2026Q1", "file": "old.xlsx", "sha256": "0" * 64,
         "retrieved_at": "2026-05-06T08:00:00", "vintage": 1, "status": "accepted"}
    ]})
    out = _run(env)
    assert any(r["action"] == "promoted" and r["vintage"] == 2 for r in out["results"] if r["bank"] == "cs")
    reg = json.loads(env["registry"].read_text())
    cs = [d for d in reg["documents"] if d["bank"] == "cs"]
    assert {d["vintage"] for d in cs} == {1, 2}   # restatement = nový vintage, historie zachována
