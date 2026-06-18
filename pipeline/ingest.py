"""
ingest.py — parsování ČS xlsx podle config/sources/cs.yaml.

Vrací:
  facts   {code: {(year, quarter): (value, src_key)}}   (znaménkově normalizováno, YTD pro flow)
  metrics {code: metric_def}
  todo    [(code, status, hint)]                         (GAP / derive — doplnit jinde)
  src_used {src_key: {file, sheet}}
"""
import datetime as dt
from pathlib import Path
import openpyxl, yaml

SRC_PRIORITY = {"ifrs9": 3, "ias39": 2, "kpi": 1}
SHEET_OF = {"ifrs9": "Fin_Statements_IFRS9", "kpi": "Key_figures", "ias39": "Fin_statements "}


def qkey(d):
    if isinstance(d, dt.datetime) and d.month in (3, 6, 9, 12):
        return d.year, d.month // 3
    return None


def _header_row(rows):
    best = max(range(len(rows)), key=lambda i: sum(1 for c in rows[i] if qkey(c)))
    if sum(1 for c in rows[best] if qkey(c)) < 4:
        raise ValueError("date header not found")
    return best


def _label_col(header):
    first_dt = min((j for j, c in enumerate(header) if qkey(c)), default=1)
    cand = [j for j in range(first_dt) if isinstance(header[j], str)]
    return cand[-1] if cand else 0


def _load_sheet(wb, sheet):
    rows = list(wb[sheet].iter_rows(values_only=True))
    h = _header_row(rows)
    cols = {j: qkey(c) for j, c in enumerate(rows[h]) if qkey(c)}
    return rows, cols, _label_col(rows[h])


def _read_rows(rows, cols, lcol, labels):
    res = {lbl: {} for lbl in labels}
    want = set(labels)
    for r in rows:
        lbl = r[lcol] if lcol < len(r) else None
        if isinstance(lbl, str) and lbl in want:
            for j, yq in cols.items():
                if j < len(r) and isinstance(r[j], (int, float)):
                    res[lbl][yq] = float(r[j])
    return res


def _series(entry_src, sheets, sign):
    src = entry_src.get("src")
    if src not in sheets:
        return {}
    rows, cols, lcol = sheets[src]
    labels = entry_src.get("rows") or ([entry_src["row"]] if "row" in entry_src else [])
    if not labels:
        return {}
    data = _read_rows(rows, cols, lcol, labels)
    merged = {}
    for lbl in labels:
        for yq, v in data[lbl].items():
            merged[yq] = merged.get(yq, 0.0) + v
    if sign == "flip_to_pos":
        merged = {yq: -v for yq, v in merged.items()}
    return {yq: (v, src) for yq, v in merged.items()}


def ingest(config_dir, xlsx_path):
    config_dir, xlsx_path = Path(config_dir), Path(xlsx_path)
    metrics = {m["code"]: m for m in yaml.safe_load((config_dir / "metrics.yaml").read_text())["metrics"]}
    smap = yaml.safe_load((config_dir / "sources" / "cs.yaml").read_text())

    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    sheets, src_used = {}, {}
    for key, sheet in SHEET_OF.items():
        try:
            sheets[key] = _load_sheet(wb, sheet)
            src_used[key] = {"file": xlsx_path.name, "sheet": sheet}
        except Exception as e:
            print(f"[warn] list {sheet!r} přeskočen: {e}")

    facts, todo = {}, []
    for entry in smap["mapping"]:
        code = entry["code"]
        if entry.get("status") in ("GAP", "PARTIAL") or "derive" in (entry.get("primary") or {}):
            hint = entry.get("source_hint") or entry.get("primary") or {}
            todo.append((code, entry.get("status", "derive"), hint))
            continue
        sign = entry.get("sign", "as_is")
        per = {}
        for key in ("primary", "history", "long_kpi"):
            es = entry.get(key)
            if es and "src" in es:
                for yq, (v, src) in _series(es, sheets, sign).items():
                    if yq not in per or SRC_PRIORITY[src] > SRC_PRIORITY[per[yq][1]]:
                        per[yq] = (v, src)
        if per:
            facts[code] = per
    return facts, metrics, todo, src_used
