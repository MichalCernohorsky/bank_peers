#!/usr/bin/env python3
"""
watch.py — ingestion automatika.

Pro každou banku z config/calendar.yaml:
  1. je-li zveřejnění "due" (publish_date <= dnes), získej dokument
     (kind: local soubor / http URL vzor; manual = není co stahovat),
  2. spočítej sha256 -> idempotence: známý accepted checksum přeskoč,
  3. postav STAGING databázi nad dokumentem a projdi validací (run_build),
  4. brána: validace musí projít A headline metrika existovat pro nejnovější období,
     jinak NEpromotuj a pošli alert,
  5. projde-li brána, promotuj do produkce (build do cílové DATABASE_URL),
  6. provenance: zapiš do registru (data/ingest_registry.json) sha + retrieved_at + vintage
     (restatement téhož období = nový vintage), každý fakt má source (z run_build).

CLI:
  python -m pipeline.watch --once [--today 2026-06-19] [--target sqlite:///data/cs_financials.db]
                           [--source cs=path/k/souboru.xlsx] [--force]
Exit kód 1, pokud byla nějaká "due" dávka odmítnuta validační bránou (pro CI/scheduler alert).
"""
import argparse
import datetime as dt
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.build_db import run_build  # noqa: E402
from pipeline.db import Conn  # noqa: E402
from pipeline.notify import notify as default_notify  # noqa: E402
from pipeline.settings import get_settings  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CALENDAR = ROOT / "config" / "calendar.yaml"
DEFAULT_REGISTRY = ROOT / "data" / "ingest_registry.json"
DEFAULT_INCOMING = ROOT / "data" / "incoming"
DEFAULT_MANUAL_DROP = ROOT / "data" / "manual_drop"   # sem se nahrává ručně, když auto-zdroj selže

# Záchranná povinná sada (když ji kalendář nespecifikuje v gate.required_metrics):
DEFAULT_REQUIRED = ["net_profit", "operating_result", "operating_income",
                    "net_interest_income", "total_assets", "net_customer_loans", "customer_deposits"]
DEFAULT_MIN_COVERAGE = 0.8


def parse_period(s: str):
    m = re.fullmatch(r"(\d{4})Q([1-4])", str(s).strip())
    if not m:
        raise ValueError(f"špatný formát období: {s!r} (čekám 'YYYYQn')")
    return int(m.group(1)), int(m.group(2))


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def load_calendar(path) -> dict:
    return yaml.safe_load(Path(path).read_text())


def load_registry(path) -> dict:
    p = Path(path)
    if p.exists():
        return json.loads(p.read_text())
    return {"documents": []}


def save_registry(path, reg) -> None:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(reg, ensure_ascii=False, indent=2))


def due_releases(cal: dict, today: dt.date):
    """Vrátí [(bank, period_str, publish_date, doc_cfg, gate_cfg)] pro zveřejnění <= dnes."""
    defaults_gate = (cal.get("defaults") or {}).get("gate") or {}
    out = []
    for bank, bcfg in (cal.get("banks") or {}).items():
        doc = bcfg.get("document") or {}
        gate = {**defaults_gate, **(bcfg.get("gate") or {})}
        for rel in bcfg.get("releases") or []:
            pub = rel["publish_date"]
            pub = pub if isinstance(pub, dt.date) else dt.date.fromisoformat(str(pub))
            if pub <= today:
                out.append((bank, str(rel["period"]), pub, doc, gate))
    return out


def fetch_document(doc: dict, period, source_override: str | None):
    """Vrátí (bytes, filename) nebo None. Podporuje kind: local / http."""
    kind = doc.get("kind")
    if kind == "local":
        p = Path(source_override or doc.get("path", ""))
        if not p.exists():
            return None
        return p.read_bytes(), p.name
    if kind == "http":
        if source_override:
            p = Path(source_override)
            return (p.read_bytes(), p.name) if p.exists() else None
        import urllib.request
        y, q = period
        url = doc["url_pattern"].format(year=y, quarter=q, q=q, yyyy=y)
        with urllib.request.urlopen(url, timeout=30) as r:  # noqa: S310 (produkční IR URL)
            return r.read(), url.rsplit("/", 1)[-1]
    return None  # manual / none -> není co stahovat


def _bank_source_map(config_dir: Path, bank: str) -> str:
    banks = yaml.safe_load((config_dir / "banks.yaml").read_text())["banks"]
    for b in banks:
        if b["code"] == bank:
            return (b.get("source") or {}).get("map", bank)
    return bank


def expected_reported_codes(config_dir: Path, bank: str) -> set:
    """Metriky, které má banka podle své source-mapy reálně dodávat (mimo GAP/PARTIAL/derive),
    protnuté s katalogem metrics.yaml. = 'co od téhle banky čekáme'."""
    map_name = _bank_source_map(config_dir, bank)
    smap_path = config_dir / "sources" / f"{map_name}.yaml"
    if not smap_path.exists():
        return set()
    catalog = {m["code"] for m in yaml.safe_load((config_dir / "metrics.yaml").read_text())["metrics"]}
    smap = yaml.safe_load(smap_path.read_text())
    exp = set()
    for e in smap.get("mapping", []):
        if e.get("status") in ("GAP", "PARTIAL"):
            continue
        if "derive" in (e.get("primary") or {}):
            continue
        if e["code"] in catalog:
            exp.add(e["code"])
    return exp


def completeness(url: str, bank: str, config_dir: Path, required: list, min_coverage: float) -> dict:
    """Ověř, že data REÁLNĚ máme: povinné metriky pro nejnovější období + pokrytí očekávané sady."""
    con = Conn(url)
    try:
        latest = con.query_one(
            """SELECT p.fiscal_year AS y, p.quarter AS q FROM fact f
               JOIN bank b ON b.id=f.bank_id AND b.code=?
               JOIN period p ON p.id=f.period_id
               WHERE p.period_type='Q' AND f.basis='reported'
               ORDER BY p.fiscal_year DESC, p.quarter DESC LIMIT 1""", (bank,))
        present = {r["c"] for r in con.query(
            """SELECT DISTINCT f.code AS c FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
               WHERE f.basis='reported' AND f.value IS NOT NULL""", (bank,))}

        def at_latest(code):
            if not latest:
                return False
            r = con.query_one(
                """SELECT f.value AS v FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
                   JOIN period p ON p.id=f.period_id
                   WHERE f.code=? AND p.fiscal_year=? AND p.quarter=? AND f.basis='reported'""",
                (bank, code, latest["y"], latest["q"]))
            return bool(r) and r["v"] is not None

        required_missing = [m for m in required if not at_latest(m)]
    finally:
        con.close()

    expected = expected_reported_codes(config_dir, bank)
    coverage = (len(expected & present) / len(expected)) if expected else 1.0
    coverage_missing = sorted(expected - present)
    ok = (not required_missing) and (coverage >= min_coverage)
    return {
        "latest": (f"{latest['y']}Q{latest['q']}" if latest else None),
        "required_missing": required_missing,
        "coverage": round(coverage, 3),
        "coverage_missing": coverage_missing,
        "complete_ok": ok,
    }


def _headline_present(url: str, bank: str, metric: str) -> bool:
    con = Conn(url)
    try:
        row = con.query_one(
            """SELECT f.value AS v FROM fact f
               JOIN bank b ON b.id=f.bank_id AND b.code=?
               JOIN period p ON p.id=f.period_id
               WHERE f.code=? AND p.period_type='Q' AND f.basis='reported'
               ORDER BY p.fiscal_year DESC, p.quarter DESC LIMIT 1""",
            (bank, metric))
    finally:
        con.close()
    return bool(row) and row["v"] is not None


def resolve_document(doc: dict, bank: str, period, source_override, manual_dir: Path):
    """Zdroj dokumentu: override -> kalendář (local/http) -> ruční drop-folder.
    Vrací (bytes, filename, mode) nebo None. mode: 'auto' | 'manual'."""
    got = fetch_document(doc, period, source_override)
    if got:
        return got[0], got[1], "auto"
    drop = Path(manual_dir) / bank
    if drop.exists():
        files = [p for p in drop.iterdir() if p.suffix.lower() in (".xlsx", ".xls")]
        if files:
            newest = max(files, key=lambda p: p.stat().st_mtime)
            return newest.read_bytes(), newest.name, "manual"
    return None


def run_once(*, config_dir=None, calendar_path=DEFAULT_CALENDAR, registry_path=DEFAULT_REGISTRY,
             incoming_dir=DEFAULT_INCOMING, manual_dir=DEFAULT_MANUAL_DROP, target_url=None,
             today=None, source_overrides=None, force=False, notify=default_notify) -> dict:
    config_dir = Path(config_dir or (ROOT / "config"))
    today = today or dt.date.today()
    target_url = target_url or get_settings().database_url
    source_overrides = source_overrides or {}

    cal = load_calendar(calendar_path)
    reg = load_registry(registry_path)
    accepted_sha = {d["sha256"] for d in reg["documents"] if d["status"] == "accepted"}

    results = []
    for bank, period_str, pub, doc, gate in due_releases(cal, today):
        period = parse_period(period_str)
        kind = doc.get("kind")
        if kind in (None, "manual", "none"):
            results.append({"bank": bank, "period": period_str, "action": "skip-manual"})
            continue

        fetched = resolve_document(doc, bank, period, source_overrides.get(bank), manual_dir)
        if not fetched:
            notify(f"Ingest {bank} {period_str}: dokument nedostupný — NAHRAJ RUČNĚ",
                   f"Automatický zdroj (kind={kind}) selhal a v drop-folderu nic není. "
                   f"Nahraj soubor do {Path(manual_dir) / bank}/ a spusť `python -m pipeline.watch --once`.",
                   level="alert")
            results.append({"bank": bank, "period": period_str, "action": "missing-document"})
            continue

        raw, name, src_mode = fetched
        sha = sha256_bytes(raw)
        if sha in accepted_sha and not force:
            results.append({"bank": bank, "period": period_str, "action": "skip-idempotent", "sha256": sha})
            continue

        # ulož příchozí dokument (provenance/audit)
        Path(incoming_dir).mkdir(parents=True, exist_ok=True)
        suffix = Path(name).suffix or ".bin"
        incoming = Path(incoming_dir) / f"{bank}_{period_str}_{sha[:8]}{suffix}"
        incoming.write_bytes(raw)

        # staging build + validační brána (nikdy nepromotuj nevalidní data)
        retrieved_at = dt.datetime.now().isoformat(timespec="seconds")
        prior_accepted = sum(1 for d in reg["documents"]
                             if d["bank"] == bank and d["period"] == period_str and d["status"] == "accepted")
        vintage = prior_accepted + 1
        entry = {"bank": bank, "period": period_str, "file": name, "sha256": sha,
                 "retrieved_at": retrieved_at, "vintage": vintage, "publish_date": str(pub),
                 "source_mode": src_mode}

        required = gate.get("required_metrics", DEFAULT_REQUIRED)
        min_cov = gate.get("min_coverage", DEFAULT_MIN_COVERAGE)
        headline_metric = gate.get("headline_metric", "net_profit")

        staging = Path(tempfile.mkdtemp(prefix="ingest_stg_")) / "staging.db"
        staging_url = f"sqlite:///{staging}"
        comp = {"complete_ok": False, "required_missing": required, "coverage": 0.0, "coverage_missing": []}
        try:
            r = run_build(config_dir, incoming, staging_url)
            checks_ok = bool(r["all_ok"])
            headline_ok = _headline_present(staging_url, bank, headline_metric) if checks_ok else False
            comp = completeness(staging_url, bank, config_dir, required, min_cov)
            valid_ok = checks_ok or not gate.get("require_validation", True)
            gate_ok = valid_ok and headline_ok and comp["complete_ok"]
        except Exception as e:  # poškozený soubor / parse error = brána neprošla
            checks_ok = headline_ok = gate_ok = False
            r = {"checks": [], "n_facts": 0, "error": str(e)}

        entry.update({"checks_ok": checks_ok, "headline_ok": headline_ok, "n_facts": r.get("n_facts", 0),
                      "coverage": comp["coverage"], "required_missing": comp["required_missing"],
                      "coverage_missing": comp["coverage_missing"]})

        if gate_ok:
            run_build(config_dir, incoming, target_url)   # promote do produkce
            entry["status"] = "accepted"
            accepted_sha.add(sha)
            notify(f"Ingest {bank} {period_str}: OK (vintage {vintage}, zdroj {src_mode})",
                   f"{entry['n_facts']} faktů, validace prošla, pokrytí {comp['coverage']:.0%}, "
                   f"všechny povinné metriky přítomny — promotováno do produkce.", level="info")
            results.append({"bank": bank, "period": period_str, "action": "promoted",
                            "vintage": vintage, "sha256": sha, "source_mode": src_mode})
        else:
            entry["status"] = "rejected"
            # důvod + výzva k ručnímu nahrání kompletního souboru
            if not checks_ok:
                reason = "rekonciliace/parsování selhalo"
            elif not headline_ok:
                reason = f"chybí headline metrika ({headline_metric})"
            else:
                reason = (f"NEKOMPLETNÍ data — chybí povinné: {comp['required_missing']}; "
                          f"pokrytí {comp['coverage']:.0%} (chybí {len(comp['coverage_missing'])}: "
                          f"{comp['coverage_missing'][:8]})")
            notify(f"Ingest {bank} {period_str}: ZAMÍTNUTO bránou — NAHRAJ RUČNĚ",
                   f"{reason}. Produkce NEZMĚNĚNA. Nahraj kompletní soubor do "
                   f"{Path(manual_dir) / bank}/ a spusť `python -m pipeline.watch --once`.", level="alert")
            results.append({"bank": bank, "period": period_str, "action": "rejected",
                            "sha256": sha, "reason": reason})

        reg["documents"].append(entry)
        save_registry(registry_path, reg)

    save_registry(registry_path, reg)
    return {"today": str(today), "results": results, "registry_path": str(registry_path)}


def main():
    ap = argparse.ArgumentParser(description="Ingestion automatika (watcher).")
    ap.add_argument("--once", action="store_true", help="jeden průchod (jinak stejné chování)")
    ap.add_argument("--today", help="datum YYYY-MM-DD (default dnes)")
    ap.add_argument("--calendar", default=str(DEFAULT_CALENDAR))
    ap.add_argument("--registry", default=str(DEFAULT_REGISTRY))
    ap.add_argument("--target", help="cílová DATABASE_URL (default z env/.env)")
    ap.add_argument("--source", action="append", default=[], metavar="bank=path",
                    help="přebij zdrojový dokument banky lokální cestou (lze opakovat)")
    ap.add_argument("--force", action="store_true", help="ignoruj idempotenci (přestav i známý checksum)")
    args = ap.parse_args()

    overrides = {}
    for s in args.source:
        bank, _, path = s.partition("=")
        overrides[bank] = path
    today = dt.date.fromisoformat(args.today) if args.today else None

    out = run_once(calendar_path=args.calendar, registry_path=args.registry, target_url=args.target,
                   today=today, source_overrides=overrides, force=args.force)

    for r in out["results"]:
        print(f"  {r['bank']:6} {r['period']:8} -> {r['action']}")
    if not out["results"]:
        print("  (žádné due zveřejnění)")
    rejected = [r for r in out["results"] if r["action"] in ("rejected", "missing-document")]
    sys.exit(1 if rejected else 0)


if __name__ == "__main__":
    main()
