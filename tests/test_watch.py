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
        "calendar": cal,
        "cal_path": cal_path,
        "registry": tmp_path / "registry.json",
        "incoming": tmp_path / "incoming",
        "manual": tmp_path / "manual_drop",
        "target": f"sqlite:///{tmp_path / 'prod.db'}",
        "target_path": tmp_path / "prod.db",
        "alerts": alerts,
        "notify": fake_notify,
    }


def _run(env, **kw):
    return watch.run_once(
        calendar_path=env["cal"], registry_path=env["registry"], incoming_dir=env["incoming"],
        manual_dir=env["manual"], target_url=env["target"], today=TODAY, notify=env["notify"], **kw)


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


def test_completeness_blocks_when_required_metric_missing(env):
    # vynuť povinnou metriku, kterou ČS xlsx nemá (rwa je GAP) -> nekompletní -> ruční nahrání
    cal = env["calendar"]
    cal["defaults"]["gate"]["required_metrics"] = ["net_profit", "rwa"]
    env["cal_path"].write_text(json.dumps(cal))
    out = _run(env)
    assert any(r["action"] == "rejected" for r in out["results"] if r["bank"] == "cs")
    assert not env["target_path"].exists()                     # produkce nezměněna
    alert = [a for a in env["alerts"] if a["level"] == "alert"][0]
    assert "NAHRAJ RUČNĚ" in alert["subject"]
    assert "rwa" in alert["body"]                              # řekne přesně co chybí
    cs = [d for d in json.loads(env["registry"].read_text())["documents"] if d["bank"] == "cs"][0]
    assert cs["status"] == "rejected" and "rwa" in cs["required_missing"]


def test_complete_data_passes_coverage(env):
    _run(env)                                                 # výchozí required = vše, co ČS má
    cs = [d for d in json.loads(env["registry"].read_text())["documents"] if d["bank"] == "cs"][0]
    assert cs["status"] == "accepted"
    assert cs["coverage"] >= 0.8 and cs["required_missing"] == []


def test_manual_drop_fallback(env):
    # auto-zdroj selže (neexistující cesta), ale ruční drop-folder má kompletní soubor
    drop = env["manual"] / "cs"
    drop.mkdir(parents=True)
    (drop / "key_figures.xlsx").write_bytes(FIXTURE.read_bytes())
    out = _run(env, source_overrides={"cs": "/does/not/exist.xlsx"})
    cs = [r for r in out["results"] if r["bank"] == "cs"][0]
    assert cs["action"] == "promoted" and cs["source_mode"] == "manual"
    assert env["target_path"].exists()


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


def test_peer_bank_ingest_keeps_other_sources(env, monkeypatch):
    """Regrese: stažený dokument peer banky se NESMÍ použít jako globální (ČS) zdroj.

    Watcher dřív předával stažený soubor jako globální xlsx — u release peer banky
    tím přepsal zdroj ČS, validační kotva spadla a brána zamítla i korektní data.
    """
    calls = []
    real_build = watch.run_build

    def spy_build(cfg, xlsx, url, bank_sources=None):
        calls.append({"xlsx": Path(xlsx), "bank_sources": dict(bank_sources or {})})
        return real_build(cfg, xlsx, url, bank_sources=bank_sources)

    monkeypatch.setattr(watch, "run_build", spy_build)
    # KB potřebuje VLASTNÍ kopii souboru — shodný checksum by spustil idempotentní skip
    kb_doc = env["cal_path"].parent / "kb_source.xlsx"
    kb_doc.write_bytes(FIXTURE.read_bytes() + b"\0")   # jiný sha256, stejný obsah listů
    env["calendar"]["banks"]["kb"] = {
        "document": {"kind": "local", "path": str(kb_doc)},
        "releases": [{"period": "2026Q1", "publish_date": "2026-05-07"}],
    }
    env["cal_path"].write_text(json.dumps(env["calendar"]))
    _run(env)

    incoming_files = {p.resolve() for p in env["incoming"].glob("*")}
    assert incoming_files, "žádný dokument nebyl stažen"
    assert any("kb" in c["bank_sources"] for c in calls), "build pro KB se nespustil"
    for c in calls:
        # ŽÁDNÝ build (staging ani promote) nesmí dostat stažený dokument jako globální
        # xlsx — ten patří výhradně do bank_sources dané banky.
        assert c["xlsx"].resolve() not in incoming_files, (
            f"stažený dokument {c['xlsx'].name} použit jako globální zdroj (přepsal by ČS)")
        assert set(c["bank_sources"]) <= {"cs", "kb"} and c["bank_sources"]
