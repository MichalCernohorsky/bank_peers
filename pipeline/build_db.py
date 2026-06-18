#!/usr/bin/env python3
"""
build_db.py — postaví celou databázi z konfigurace a zdrojového xlsx.

Kroky:
  1. schéma (schema/001_init.sql)
  2. seed bank + metric (z metrics.yaml)
  3. load faktů (pipeline.ingest)  -> kvartální (Q) řádky, flow jako samostatné čtvrtletí
  4. roční (FY) řádky  -> flow = Q4 YTD, stock = Q4 stav, ratio = Q4 hodnota
  5. derivace odvozených metrik (total_liabilities, loan_to_deposit_ratio)
  6. validace (rekonciliační kontroly) + zápis ingestion_run

Použití:
  python -m pipeline.build_db [config_dir] [xlsx] [out_db]
"""
import sys, sqlite3, datetime as dt
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.ingest import ingest

ROOT = Path(__file__).resolve().parents[1]


def period_id(cur, bank_id, year, ptype, quarter):
    end = {1: f"{year}-03-31", 2: f"{year}-06-30", 3: f"{year}-09-30", 4: f"{year}-12-31"}
    pe = f"{year}-12-31" if ptype == "FY" else end[quarter]
    cur.execute("INSERT OR IGNORE INTO period(bank_id,fiscal_year,period_type,quarter,period_end) VALUES(?,?,?,?,?)",
                (bank_id, year, ptype, quarter, pe))
    cur.execute("SELECT id FROM period WHERE bank_id=? AND fiscal_year=? AND period_type=? AND quarter IS ?",
                (bank_id, year, ptype, quarter))
    return cur.fetchone()[0]


def main():
    cfg = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "config"
    xlsx = Path(sys.argv[2]) if len(sys.argv) > 2 else Path("/mnt/user-data/uploads/key_figures_q1_2026.xlsx")
    db = Path(sys.argv[3]) if len(sys.argv) > 3 else ROOT / "data" / "cs_financials.db"

    t0 = dt.datetime.now().isoformat(timespec="seconds")
    facts, metrics, todo, src_used = ingest(cfg, xlsx)

    if db.exists():
        db.unlink()
    con = sqlite3.connect(db)
    cur = con.cursor()
    cur.executescript((ROOT / "schema" / "001_init.sql").read_text())

    # --- seed banks (z banks.yaml) + metric ---
    import yaml as _yaml
    banks_cfg = _yaml.safe_load((cfg / "banks.yaml").read_text())["banks"]
    bankid = {}
    for i, b in enumerate(banks_cfg, start=1):
        cur.execute("INSERT INTO bank(id,code,name,parent_group) VALUES(?,?,?,?)",
                    (i, b["code"], b["name"], b.get("parent_group")))
        bankid[b["code"]] = i
    BANK = bankid["cs"]   # ČS xlsx ingest
    for code, m in metrics.items():
        cur.execute("""INSERT INTO metric(code,label_cs,label_en,category,unit,type,interim_basis,
                       quarter_calc,annual_calc,annualize,formula,headline)
                       VALUES(?,?,?,?,?,?,?,?,?,?,?,?)""",
                    (code, m.get("label_cs"), m.get("label_en"), m.get("category"), m.get("unit"),
                     m.get("type"), m.get("interim_basis"), m.get("quarter_calc"), m.get("annual_calc"),
                     int(bool(m.get("annualize"))), m.get("formula"), int(bool(m.get("headline")))))

    # --- source rows ---
    src_id = {}
    for key, meta in src_used.items():
        cur.execute("INSERT INTO source(bank_id,doc_type,file,sheet,retrieved_at) VALUES(?,?,?,?,?)",
                    (BANK, f"xlsx_{key}", meta["file"], meta["sheet"], t0))
        src_id[key] = cur.lastrowid
    cur.execute("INSERT INTO source(bank_id,doc_type,file,sheet,retrieved_at) VALUES(?,?,?,?,?)",
                (BANK, "derived", None, None, t0))
    src_id["derived"] = cur.lastrowid

    # --- 3+4: Q a FY řádky ---
    n = 0
    for code, per in facts.items():
        typ = metrics.get(code, {}).get("type", "stock")
        years = {}
        for (y, q), (v, src) in sorted(per.items()):
            years.setdefault(y, {})[q] = (v, src)
            pid = period_id(cur, BANK, y, "Q", q)
            if typ == "flow":
                prev = per.get((y, q - 1))
                vq = v if q == 1 else (v - prev[0] if prev else None)
                cur.execute("INSERT INTO fact(bank_id,code,period_id,basis,value,value_ytd,source_id) VALUES(?,?,?,?,?,?,?)",
                            (BANK, code, pid, "reported", vq, v, src_id[src]))
            else:
                cur.execute("INSERT INTO fact(bank_id,code,period_id,basis,value,source_id) VALUES(?,?,?,?,?,?)",
                            (BANK, code, pid, "reported", v, src_id[src]))
            n += 1
        # FY řádky (jen kompletní roky se Q4)
        for y, qs in years.items():
            if 4 not in qs:
                continue
            v4, src4 = qs[4]
            pid = period_id(cur, BANK, y, "FY", None)
            cur.execute("INSERT INTO fact(bank_id,code,period_id,basis,value,source_id) VALUES(?,?,?,?,?,?)",
                        (BANK, code, pid, "reported", v4, src_id[src4]))
            n += 1

    # --- 4b: manuální data (všechny CSV v config/manual/, libovolná banka + báze) ---
    import csv as _csv
    n_man = 0
    man_dir = cfg / "manual"
    if man_dir.exists():
        for csv_file in sorted(man_dir.glob("*.csv")):
            cur.execute("INSERT INTO source(bank_id,doc_type,file,sheet,retrieved_at) VALUES(?,?,?,?,?)",
                        (None, csv_file.stem, "C_S_Peer_Group_Q1_2026_Final.pdf", None, t0))
            man_src = cur.lastrowid
            for row in _csv.DictReader(csv_file.open()):
                code = row["code"]
                bank = row.get("bank", "cs")
                if code not in metrics or bank not in bankid:
                    continue
                y, q = int(row["fiscal_year"]), int(row["quarter"])
                pid = period_id(cur, bankid[bank], y, "Q", q)
                cur.execute("""INSERT OR IGNORE INTO fact(bank_id,code,period_id,basis,value,source_id)
                               VALUES(?,?,?,?,?,?)""",
                            (bankid[bank], code, pid, row.get("basis", "reported"), float(row["value"]), man_src))
                n_man += 1

    # --- 5: derivace odvozených metrik (jen reported báze) ---
    def derive_ratio(new_code, num, den, scale=100.0):
        rows = cur.execute("""
            SELECT fa.bank_id,fa.period_id,fa.value,fb.value FROM fact fa
            JOIN fact fb ON fa.period_id=fb.period_id AND fb.code=? AND fb.basis='reported'
            WHERE fa.code=? AND fa.basis='reported'""", (den, num)).fetchall()
        cnt = 0
        for bank_id, pid, vn, vd in rows:
            if vn is not None and vd not in (None, 0):
                cur.execute("""INSERT OR IGNORE INTO fact(bank_id,code,period_id,basis,value,source_id,derived)
                               VALUES(?,?,?,?,?,?,1)""", (bank_id, new_code, pid, "reported", vn / vd * scale, src_id["derived"]))
                cnt += 1
        return cnt

    # total_liabilities = total_assets - total_equity
    d1 = 0
    for bank_id, pid, ta, te in cur.execute("""
            SELECT fa.bank_id,fa.period_id,fa.value,fb.value FROM fact fa
            JOIN fact fb ON fa.period_id=fb.period_id AND fb.code='total_equity' AND fb.basis='reported'
            WHERE fa.code='total_assets' AND fa.basis='reported'""").fetchall():
        if ta is not None and te is not None:
            cur.execute("""INSERT OR IGNORE INTO fact(bank_id,code,period_id,basis,value,source_id,derived)
                           VALUES(?,?,?,?,?,?,1)""", (bank_id, "total_liabilities", pid, "reported", ta - te, src_id["derived"]))
            d1 += 1
    d2 = derive_ratio("loan_to_deposit_ratio", "net_customer_loans", "customer_deposits")
    con.commit()

    # --- 6: validace ---
    checks = []

    def near(a, b, tol):
        return a is not None and b is not None and abs(a - b) <= tol

    # (a) operating_result_Q ≈ operating_income_Q - operating_expenses_Q
    rows = cur.execute("""
        SELECT p.fiscal_year,p.quarter,
               oi.value AS inc, oe.value AS exp, orr.value AS res
        FROM period p
        JOIN fact oi  ON oi.period_id=p.id  AND oi.code='operating_income'  AND oi.basis='reported'
        JOIN fact oe  ON oe.period_id=p.id  AND oe.code='operating_expenses' AND oe.basis='reported'
        JOIN fact orr ON orr.period_id=p.id AND orr.code='operating_result'  AND orr.basis='reported'
        WHERE p.period_type='Q'""").fetchall()
    bad = [(y, q) for y, q, inc, exp, res in rows if not near(res, inc - exp, 2.0)]
    checks.append(("operating_result = income − expenses (Q)", len(rows) - len(bad), len(rows), bad[:5]))

    # (b) sum(net_profit Q1..Q4) == net_profit FY
    bad = []
    fy = dict(cur.execute("""SELECT p.fiscal_year,f.value FROM fact f JOIN period p ON p.id=f.period_id
                             WHERE f.code='net_profit' AND p.period_type='FY' AND f.basis='reported'""").fetchall())
    qsum = {}
    for y, val in cur.execute("""SELECT p.fiscal_year,f.value FROM fact f JOIN period p ON p.id=f.period_id
                                 WHERE f.code='net_profit' AND p.period_type='Q' AND f.basis='reported'"""):
        qsum.setdefault(y, []).append(val)
    n_ok = 0
    tested = 0
    for y, fv in fy.items():
        if y in qsum and len(qsum[y]) == 4 and all(v is not None for v in qsum[y]):
            tested += 1
            if near(sum(qsum[y]), fv, 2.0):
                n_ok += 1
            else:
                bad.append(y)
    checks.append(("Σ(net_profit Q1..Q4) = net_profit FY", n_ok, tested, bad[:5]))

    # (c) total_assets == total_equity + total_liabilities
    rows = cur.execute("""
        SELECT ta.value, te.value, tl.value FROM fact ta
        JOIN fact te ON te.period_id=ta.period_id AND te.code='total_equity'      AND te.basis='reported'
        JOIN fact tl ON tl.period_id=ta.period_id AND tl.code='total_liabilities' AND tl.basis='reported'
        WHERE ta.code='total_assets' AND ta.basis='reported'""").fetchall()
    nbad = sum(1 for a, e, l in rows if not near(a, e + l, 1.0))
    checks.append(("total_assets = equity + liabilities", len(rows) - nbad, len(rows), []))

    # (d) kotva: net_profit 2026 Q1 == 7086
    v = cur.execute("""SELECT f.value FROM fact f JOIN period p ON p.id=f.period_id
                       WHERE f.code='net_profit' AND p.fiscal_year=2026 AND p.quarter=1 AND f.basis='reported'""").fetchone()
    anchor_ok = near(v[0] if v else None, 7086.0, 1.0)
    checks.append(("kotva: net_profit 2026Q1 = 7086", int(anchor_ok), 1, []))

    all_ok = all(ok == tot for _, ok, tot, _ in checks)
    t1 = dt.datetime.now().isoformat(timespec="seconds")
    cur.execute("INSERT INTO ingestion_run(started_at,finished_at,status,rows_loaded,log) VALUES(?,?,?,?,?)",
                (t0, t1, "ok" if all_ok else "validation_warnings", n, str(checks)))
    con.commit()

    # --- report ---
    print(f"DB: {db}")
    print(f"Načteno: {len(facts)} ingestovaných metrik, {n} faktů (Q+FY)")
    print(f"Doplněno z PDF (potvrzené): {n_man} faktů")
    print(f"Odvozeno: total_liabilities ({d1}), loan_to_deposit_ratio ({d2})")
    have = {r[0] for r in cur.execute("SELECT DISTINCT code FROM fact").fetchall()}
    remaining = sorted(set(t[0] for t in todo) - have)
    print(f"GAP zbývá (bez dat): {len(remaining)} -> {remaining}")
    print("\nVALIDACE:")
    for name, ok, tot, ex in checks:
        flag = "OK " if ok == tot else "!! "
        extra = f"  selhalo: {ex}" if ex else ""
        print(f"  [{flag}] {name}: {ok}/{tot}{extra}")
    print("\nStav běhu:", "OK" if all_ok else "VAROVÁNÍ")
    con.close()


if __name__ == "__main__":
    main()
