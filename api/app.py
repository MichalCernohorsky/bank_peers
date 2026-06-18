"""
api/app.py — backend nad fact tabulkou.

Spuštění:
  pip install fastapi uvicorn
  uvicorn api.app:app --reload
Endpointy:
  GET /api/banks
  GET /api/metrics
  GET /api/facts?bank=cs&code=net_profit&period_type=Q&basis=reported
  GET /api/dashboard/{bank}     -> headline KPI + série pro frontend
"""
import sqlite3
from pathlib import Path
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "data" / "cs_financials.db"
WEB = ROOT / "web"
app = FastAPI(title="Bank Results API")
# CORS zůstává pro dev (např. otevření samostatného HTML), ale frontend se
# servíruje ze stejného originu jako API (viz StaticFiles níže) -> fetch bez CORS.
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])


def q(sql, args=()):
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    rows = [dict(r) for r in con.execute(sql, args).fetchall()]
    con.close()
    return rows


@app.get("/api/banks")
def banks():
    return q("SELECT code,name,parent_group FROM bank ORDER BY name")


@app.get("/api/metrics")
def metrics():
    return q("SELECT code,label_cs,label_en,category,unit,type,headline FROM metric ORDER BY category,code")


@app.get("/api/facts")
def facts(bank: str = "cs", code: str = Query(...), period_type: str = "Q", basis: str = "reported"):
    return q("""
        SELECT p.fiscal_year, p.quarter, p.period_end, f.value, f.value_ytd, f.derived, s.doc_type AS source
        FROM fact f
        JOIN bank b   ON b.id=f.bank_id AND b.code=?
        JOIN period p ON p.id=f.period_id AND p.period_type=?
        LEFT JOIN source s ON s.id=f.source_id
        WHERE f.code=? AND f.basis=?
        ORDER BY p.fiscal_year, p.quarter
    """, (bank, period_type, code, basis))


@app.get("/api/dashboard/{bank}")
def dashboard(bank: str = "cs"):
    """Plný přehled: headline KPI, série pro grafy, a všechny metriky po kategoriích."""
    yr = q("""SELECT MAX(p.fiscal_year) y FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
              JOIN period p ON p.id=f.period_id WHERE p.period_type='Q' AND f.basis='reported'""", (bank,))[0]["y"]
    qt = q("""SELECT MAX(p.quarter) q FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
              JOIN period p ON p.id=f.period_id WHERE p.period_type='Q' AND p.fiscal_year=? AND f.basis='reported'""", (bank, yr))[0]["q"]

    def val(code, y, qq):
        r = q("""SELECT f.value v FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
                 JOIN period p ON p.id=f.period_id
                 WHERE f.code=? AND p.period_type='Q' AND p.fiscal_year=? AND p.quarter=? AND f.basis='reported'""",
              (bank, code, y, qq))
        return r[0]["v"] if r else None

    def qseries(code, n=None):
        rows = q("""SELECT p.fiscal_year y, p.quarter q, f.value v FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
                    JOIN period p ON p.id=f.period_id WHERE f.code=? AND p.period_type='Q' AND f.basis='reported'
                    ORDER BY p.fiscal_year, p.quarter""", (bank, code))
        return rows[-n:] if n else rows

    def yoy(code, typ, v, y, qq):
        pv = val(code, y - 1, qq)
        if v is None or pv in (None, 0):
            return None
        return (v - pv) * 100 if typ == "ratio" else (v / pv - 1) * 100

    mets = q("SELECT code,label_cs,unit,type,category,headline FROM metric")
    kpis = []
    for m in [x for x in mets if x["headline"]]:
        v = val(m["code"], yr, qt)
        if v is None:
            continue
        kpis.append({"code": m["code"], "label_cs": m["label_cs"], "unit": m["unit"], "type": m["type"],
                     "value": v, "yoy": yoy(m["code"], m["type"], v, yr, qt)})

    CATS = [("income_statement", "Výsledovka"), ("balance_sheet", "Rozvaha"), ("capital", "Kapitál"),
            ("asset_quality", "Kvalita portfolia"), ("ratios", "Poměrové ukazatele"), ("business_volume", "Objemy a provoz")]
    categories = []
    for ckey, ctitle in CATS:
        rows = []
        for m in [x for x in mets if x["category"] == ckey]:
            ser = qseries(m["code"])
            if not ser:
                continue
            last = ser[-1]
            rows.append({"code": m["code"], "label": m["label_cs"], "unit": m["unit"], "type": m["type"],
                         "headline": m["headline"], "latest": last["v"], "ly": last["y"], "lq": last["q"],
                         "yoy": yoy(m["code"], m["type"], last["v"], last["y"], last["q"]),
                         "spark": ser[-13:]})
        if rows:
            categories.append({"key": ckey, "title": ctitle, "metrics": rows})

    return JSONResponse({
        "bank": q("SELECT code,name,parent_group FROM bank WHERE code=?", (bank,))[0],
        "period": {"year": yr, "quarter": qt},
        "kpis": kpis,
        "categories": categories,
        "quarterly": {c: qseries(c, 9) for c in ["net_profit", "operating_result", "operating_income", "net_interest_income"]},
        "annual": qseries_fy(bank),
    })


def qseries_fy(bank):
    return q("""SELECT p.fiscal_year y, f.value v FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
                JOIN period p ON p.id=f.period_id WHERE f.code='net_profit' AND p.period_type='FY' AND f.basis='reported'
                ORDER BY p.fiscal_year""", (bank,))


@app.get("/api/compare")
def compare(banks: str = "cs,kb", basis: str = "adjusted", year: int = 2026, quarter: int = 1):
    codes = [c.strip() for c in banks.split(",")]
    accents = {"cs": "#1A3A5C", "kb": "#A6192E", "csob": "#0098D4", "moneta": "#6A2C70"}
    meta = {m["code"]: m for m in q("SELECT code,label_cs,unit,type FROM metric")}

    def val(bank, code, y, qq):
        r = q("""SELECT f.value v FROM fact f JOIN bank b ON b.id=f.bank_id AND b.code=?
                 JOIN period p ON p.id=f.period_id
                 WHERE f.code=? AND p.period_type='Q' AND p.fiscal_year=? AND p.quarter=? AND f.basis=?""",
              (bank, code, y, qq, basis))
        return r[0]["v"] if r else None

    def pair(code):
        out = {"code": code, "label": meta[code]["label_cs"], "unit": meta[code]["unit"]}
        for bk in codes:
            v, pv = val(bk, code, year, quarter), val(bk, code, year - 1, quarter)
            yoy = None
            if v is not None and pv not in (None, 0):
                yoy = (v - pv) * 100 if meta[code]["type"] == "ratio" else (v / pv - 1) * 100
            out[bk] = {"v": v, "prev": pv, "yoy": yoy}
        return out

    layout = [
        ("Profitabilita", "bn", ["net_profit", "operating_result", "operating_income", "net_interest_income", "net_fee_commission_income"]),
        ("Efektivita a návratnost", "pct", ["cost_income_ratio", "roe"]),
        ("Velikost rozvahy", "bn", ["total_assets", "gross_customer_loans", "customer_deposits"]),
        ("Kvalita portfolia", "pct", ["npl_ratio"]),
    ]
    groups = [{"title": t, "unit": u, "metrics": [pair(c) for c in cs]} for t, u, cs in layout]
    slope = {"label": "ROE", "unit": "pct",
             "banks": {bk: [{"t": "Q1 2025", "v": val(bk, "roe", year - 1, quarter)},
                            {"t": "Q1 2026", "v": val(bk, "roe", year, quarter)}] for bk in codes}}
    return {
        "period": {"year": year, "quarter": quarter},
        "banks": [{**q("SELECT code,name FROM bank WHERE code=?", (c,))[0], "accent": accents.get(c, "#333")} for c in codes],
        "groups": groups, "slope": slope,
    }


# --- frontend (stejný origin jako API) ---
# Root "/" vrací sloučenou SPA; ostatní statické soubory (app.html, snapshoty,
# starší samostatné HTML) servíruje StaticFiles. API routy výše mají přednost,
# protože jsou registrované dřív než mount na "/".
@app.get("/", include_in_schema=False)
def index():
    return FileResponse(WEB / "app.html")


app.mount("/", StaticFiles(directory=WEB), name="web")
