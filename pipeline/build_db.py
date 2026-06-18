#!/usr/bin/env python3
"""
build_db.py — postaví celou databázi z konfigurace a zdrojového xlsx.
Cílí SQLite i PostgreSQL (dle DATABASE_URL / 3. argumentu) přes pipeline.db.Conn.

Kroky:
  1. schéma (schema/001_init.sql nebo 001_init_postgres.sql dle dialektu)
  2. seed bank + metric (z metrics.yaml)
  3. load faktů (pipeline.ingest)  -> kvartální (Q) řádky, flow jako samostatné čtvrtletí
  4. roční (FY) řádky  -> flow = Q4 YTD, stock = Q4 stav, ratio = Q4 hodnota
  5. derivace odvozených metrik (total_liabilities, loan_to_deposit_ratio)
  6. validace (rekonciliační kontroly) + zápis ingestion_run

Použití:
  python -m pipeline.build_db [config_dir] [xlsx] [out_db|DATABASE_URL]
Bez argumentů bere hodnoty z env/.env (viz pipeline.settings).
"""
import datetime as dt
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.db import Conn, dialect_of, normalize_url, sqlite_path  # noqa: E402
from pipeline.ingest import ingest  # noqa: E402
from pipeline.settings import get_settings  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]


def period_id(con, bank_id, year, ptype, quarter):
    """Vrátí id období; pokud neexistuje, vloží ho. NULL-safe na quarter (FY)."""
    end = {1: f"{year}-03-31", 2: f"{year}-06-30", 3: f"{year}-09-30", 4: f"{year}-12-31"}
    pe = f"{year}-12-31" if ptype == "FY" else end[quarter]
    row = con.query_one(
        f"SELECT id FROM period WHERE bank_id=? AND fiscal_year=? AND period_type=? AND quarter {con.null_eq} ?",
        (bank_id, year, ptype, quarter))
    if row:
        return row["id"]
    return con.insert(
        "INSERT INTO period(bank_id,fiscal_year,period_type,quarter,period_end) VALUES(?,?,?,?,?)",
        (bank_id, year, ptype, quarter, pe))


def _schema_sql(dialect):
    name = "001_init_postgres.sql" if dialect == "postgres" else "001_init.sql"
    return (ROOT / "schema" / name).read_text()


def run_build(cfg, xlsx, database_url):
    """Postaví databázi a vrátí dict s výsledky (vč. validačních checků)."""
    import csv as _csv

    import yaml as _yaml

    cfg, xlsx = Path(cfg), Path(xlsx)
    url = normalize_url(database_url)
    dialect = dialect_of(url)

    t0 = dt.datetime.now()
    facts, metrics, todo, src_used = ingest(cfg, xlsx)

    # u sqlite zahoď starý soubor; u pg řeší re-build DROP ... CASCADE ve schématu
    if dialect == "sqlite":
        p = Path(sqlite_path(url))
        if p.exists():
            p.unlink()
        p.parent.mkdir(parents=True, exist_ok=True)

    con = Conn(url)
    con.executescript(_schema_sql(dialect))

    # --- 2: seed banks (z banks.yaml) + metric ---
    banks_cfg = _yaml.safe_load((cfg / "banks.yaml").read_text())["banks"]
    bankid = {}
    for i, b in enumerate(banks_cfg, start=1):
        con.execute("INSERT INTO bank(id,code,name,parent_group) VALUES(?,?,?,?)",
                    (i, b["code"], b["name"], b.get("parent_group")))
        bankid[b["code"]] = i
    BANK = bankid["cs"]
    for code, m in metrics.items():
        con.execute("""INSERT INTO metric(code,label_cs,label_en,category,unit,type,interim_basis,
                       quarter_calc,annual_calc,annualize,formula,headline)
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (code, m.get("label_cs"), m.get("label_en"), m.get("category"), m.get("unit"),
                     m.get("type"), m.get("interim_basis"), m.get("quarter_calc"), m.get("annual_calc"),
                     int(bool(m.get("annualize"))), m.get("formula"), int(bool(m.get("headline")))))

    # --- source rows ---
    src_id = {}
    for key, meta in src_used.items():
        src_id[key] = con.insert(
            "INSERT INTO source(bank_id,doc_type,file,sheet,retrieved_at) VALUES(?,?,?,?,?)",
            (BANK, f"xlsx_{key}", meta["file"], meta["sheet"], t0))
    src_id["derived"] = con.insert(
        "INSERT INTO source(bank_id,doc_type,file,sheet,retrieved_at) VALUES(?,?,?,?,?)",
        (BANK, "derived", None, None, t0))

    # --- 3+4: Q a FY řádky ---
    n = 0
    for code, per in facts.items():
        if code not in metrics:   # katalog metrik je zdroj pravdy (jako u manuálních dat)
            continue
        typ = metrics.get(code, {}).get("type", "stock")
        years = {}
        for (y, q), (v, src) in sorted(per.items()):
            years.setdefault(y, {})[q] = (v, src)
            pid = period_id(con, BANK, y, "Q", q)
            if typ == "flow":
                prev = per.get((y, q - 1))
                vq = v if q == 1 else (v - prev[0] if prev else None)
                con.execute("INSERT INTO fact(bank_id,code,period_id,basis,value,value_ytd,source_id) VALUES(?,?,?,?,?,?,?)",
                            (BANK, code, pid, "reported", vq, v, src_id[src]))
            else:
                con.execute("INSERT INTO fact(bank_id,code,period_id,basis,value,source_id) VALUES(?,?,?,?,?,?)",
                            (BANK, code, pid, "reported", v, src_id[src]))
            n += 1
        for y, qs in years.items():
            if 4 not in qs:
                continue
            v4, src4 = qs[4]
            pid = period_id(con, BANK, y, "FY", None)
            con.execute("INSERT INTO fact(bank_id,code,period_id,basis,value,source_id) VALUES(?,?,?,?,?,?)",
                        (BANK, code, pid, "reported", v4, src_id[src4]))
            n += 1

    # --- 4b: manuální data (všechny CSV v config/manual/, libovolná banka + báze) ---
    n_man = 0
    man_dir = cfg / "manual"
    if man_dir.exists():
        for csv_file in sorted(man_dir.glob("*.csv")):
            man_src = con.insert(
                "INSERT INTO source(bank_id,doc_type,file,sheet,retrieved_at) VALUES(?,?,?,?,?)",
                (None, csv_file.stem, "C_S_Peer_Group_Q1_2026_Final.pdf", None, t0))
            for row in _csv.DictReader(csv_file.open()):
                code = row["code"]
                bank = row.get("bank", "cs")
                if code not in metrics or bank not in bankid:
                    continue
                y, q = int(row["fiscal_year"]), int(row["quarter"])
                pid = period_id(con, bankid[bank], y, "Q", q)
                con.execute("""INSERT OR IGNORE INTO fact(bank_id,code,period_id,basis,value,source_id)
                               VALUES(?,?,?,?,?,?)""",
                            (bankid[bank], code, pid, row.get("basis", "reported"), float(row["value"]), man_src))
                n_man += 1

    # --- 5: derivace odvozených metrik (jen reported báze) ---
    def derive_ratio(new_code, num, den, scale=100.0):
        rows = con.query("""
            SELECT fa.bank_id AS bank_id, fa.period_id AS period_id, fa.value AS vn, fb.value AS vd
            FROM fact fa
            JOIN fact fb ON fa.period_id=fb.period_id AND fb.code=? AND fb.basis='reported'
            WHERE fa.code=? AND fa.basis='reported'""", (den, num))
        cnt = 0
        for r in rows:
            if r["vn"] is not None and r["vd"] not in (None, 0):
                con.execute("""INSERT OR IGNORE INTO fact(bank_id,code,period_id,basis,value,source_id,derived)
                               VALUES(?,?,?,?,?,?,1)""",
                            (r["bank_id"], new_code, r["period_id"], "reported", r["vn"] / r["vd"] * scale, src_id["derived"]))
                cnt += 1
        return cnt

    d1 = 0
    for r in con.query("""
            SELECT fa.bank_id AS bank_id, fa.period_id AS period_id, fa.value AS ta, fb.value AS te
            FROM fact fa
            JOIN fact fb ON fa.period_id=fb.period_id AND fb.code='total_equity' AND fb.basis='reported'
            WHERE fa.code='total_assets' AND fa.basis='reported'"""):
        if r["ta"] is not None and r["te"] is not None:
            con.execute("""INSERT OR IGNORE INTO fact(bank_id,code,period_id,basis,value,source_id,derived)
                           VALUES(?,?,?,?,?,?,1)""",
                        (r["bank_id"], "total_liabilities", r["period_id"], "reported", r["ta"] - r["te"], src_id["derived"]))
            d1 += 1
    d2 = derive_ratio("loan_to_deposit_ratio", "net_customer_loans", "customer_deposits")
    con.commit()

    # --- 6: validace ---
    checks = []

    def near(a, b, tol):
        return a is not None and b is not None and abs(a - b) <= tol

    # (a) operating_result_Q ≈ operating_income_Q - operating_expenses_Q
    rows = con.query("""
        SELECT p.fiscal_year AS y, p.quarter AS q, oi.value AS inc, oe.value AS exp, orr.value AS res
        FROM period p
        JOIN fact oi  ON oi.period_id=p.id  AND oi.code='operating_income'  AND oi.basis='reported'
        JOIN fact oe  ON oe.period_id=p.id  AND oe.code='operating_expenses' AND oe.basis='reported'
        JOIN fact orr ON orr.period_id=p.id AND orr.code='operating_result'  AND orr.basis='reported'
        WHERE p.period_type='Q'""")
    bad = [(r["y"], r["q"]) for r in rows if not near(r["res"], r["inc"] - r["exp"], 2.0)]
    checks.append(("operating_result = income - expenses (Q)", len(rows) - len(bad), len(rows), bad[:5]))

    # (b) sum(net_profit Q1..Q4) == net_profit FY
    bad = []
    fy = {r["y"]: r["v"] for r in con.query(
        """SELECT p.fiscal_year AS y, f.value AS v FROM fact f JOIN period p ON p.id=f.period_id
           WHERE f.code='net_profit' AND p.period_type='FY' AND f.basis='reported'""")}
    qsum = {}
    for r in con.query("""SELECT p.fiscal_year AS y, f.value AS v FROM fact f JOIN period p ON p.id=f.period_id
                          WHERE f.code='net_profit' AND p.period_type='Q' AND f.basis='reported'"""):
        qsum.setdefault(r["y"], []).append(r["v"])
    n_ok = tested = 0
    for y, fv in fy.items():
        if y in qsum and len(qsum[y]) == 4 and all(v is not None for v in qsum[y]):
            tested += 1
            if near(sum(qsum[y]), fv, 2.0):
                n_ok += 1
            else:
                bad.append(y)
    checks.append(("Sum(net_profit Q1..Q4) = net_profit FY", n_ok, tested, bad[:5]))

    # (c) total_assets == total_equity + total_liabilities
    rows = con.query("""
        SELECT ta.value AS a, te.value AS e, tl.value AS l FROM fact ta
        JOIN fact te ON te.period_id=ta.period_id AND te.code='total_equity'      AND te.basis='reported'
        JOIN fact tl ON tl.period_id=ta.period_id AND tl.code='total_liabilities' AND tl.basis='reported'
        WHERE ta.code='total_assets' AND ta.basis='reported'""")
    nbad = sum(1 for r in rows if not near(r["a"], r["e"] + r["l"], 1.0))
    checks.append(("total_assets = equity + liabilities", len(rows) - nbad, len(rows), []))

    # (d) kotva: net_profit 2026 Q1 == 7086
    v = con.query_one("""SELECT f.value AS v FROM fact f JOIN period p ON p.id=f.period_id
                         WHERE f.code='net_profit' AND p.fiscal_year=2026 AND p.quarter=1 AND f.basis='reported'""")
    anchor_ok = near(v["v"] if v else None, 7086.0, 1.0)
    checks.append(("kotva: net_profit 2026Q1 = 7086", int(anchor_ok), 1, []))

    all_ok = all(ok == tot for _, ok, tot, _ in checks)
    t1 = dt.datetime.now()
    con.execute("INSERT INTO ingestion_run(started_at,finished_at,status,rows_loaded,log) VALUES(?,?,?,?,?)",
                (t0, t1, "ok" if all_ok else "validation_warnings", n, str(checks)))
    con.commit()

    have = {r["code"] for r in con.query("SELECT DISTINCT code FROM fact")}
    remaining = sorted(set(t[0] for t in todo) - have)
    con.close()

    return {
        "url": url, "dialect": dialect, "n_facts": n, "n_manual": n_man,
        "n_metrics": len(facts), "derived": {"total_liabilities": d1, "loan_to_deposit_ratio": d2},
        "remaining_gap": remaining, "checks": checks, "all_ok": all_ok,
    }


def main():
    s = get_settings()
    cfg = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "config"
    xlsx = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(s.xlsx_path)
    target = sys.argv[3] if len(sys.argv) > 3 else s.database_url

    r = run_build(cfg, xlsx, target)

    print(f"DB: {r['url']}  ({r['dialect']})")
    print(f"Načteno: {r['n_metrics']} ingestovaných metrik, {r['n_facts']} faktů (Q+FY)")
    print(f"Doplněno z PDF (potvrzené): {r['n_manual']} faktů")
    print(f"Odvozeno: total_liabilities ({r['derived']['total_liabilities']}), "
          f"loan_to_deposit_ratio ({r['derived']['loan_to_deposit_ratio']})")
    print(f"GAP zbývá (bez dat): {len(r['remaining_gap'])} -> {r['remaining_gap']}")
    print("\nVALIDACE:")
    for name, ok, tot, ex in r["checks"]:
        flag = "OK " if ok == tot else "!! "
        extra = f"  selhalo: {ex}" if ex else ""
        print(f"  [{flag}] {name}: {ok}/{tot}{extra}")
    print("\nStav běhu:", "OK" if r["all_ok"] else "VAROVÁNÍ")

    # validace je brána: na neúspěšné rekonciliaci skonči nenulovým kódem
    if not r["all_ok"]:
        sys.exit(1)


if __name__ == "__main__":
    main()
