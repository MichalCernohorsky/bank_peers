"""
ingest.py — parsování strukturovaného xlsx zdroje banky podle config/sources/<bank>.yaml.

Multi-source / multi-format: banka + cesta jsou parametry. Listy, priorita a interim
báze (ytd_cumulative vs qtd) se berou z hlavičky `sources:` v source-mapě.

Mapování řádku na metriku má dvě varianty:
  - label-based:  primary/history/long_kpi: { src, row|rows }   (ČS — match textu popisku)
  - row-based:    at: { src, row: <číslo Excel řádku> }          (peers — robustní na popisky)

Období v hlavičce umí být datetime i text: "1Q 2026", "Q1 2026", "31 Mar 2026", "2026-03".

Vrací:
  facts       {code: {(year, quarter): (value, src_key)}}   (znaménkově normalizováno)
  todo        [(code, status, hint)]
  src_used    {src_key: {file, sheet}}
  src_interim {src_key: 'ytd_cumulative' | 'qtd' | ...}
"""
import datetime as dt
import re
from pathlib import Path

import openpyxl
import yaml

_MONTHS = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
           "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12}


def period_of(c):
    """Z buňky hlavičky vrať (year, quarter) pro čtvrtletní konce, jinak None."""
    if isinstance(c, dt.datetime):
        return (c.year, c.month // 3) if c.month in (3, 6, 9, 12) else None
    if isinstance(c, str):
        s = c.strip()
        m = re.search(r"([1-4])\s*Q\s*([12]\d{3})", s)          # 1Q 2026
        if m:
            return int(m.group(2)), int(m.group(1))
        m = re.search(r"Q\s*([1-4])[ \-/]*([12]\d{3})", s)      # Q1 2026
        if m:
            return int(m.group(2)), int(m.group(1))
        m = re.search(r"\b(\d{1,2})\s+([A-Za-z]{3})[a-z]*\s+([12]\d{3})", s)   # 31 Mar 2026
        if m:
            mon = _MONTHS.get(m.group(2).lower()[:3])
            if mon in (3, 6, 9, 12):
                return int(m.group(3)), mon // 3
        m = re.search(r"([12]\d{3})[-/](\d{2})", s)             # 2026-03
        if m and int(m.group(2)) in (3, 6, 9, 12):
            return int(m.group(1)), int(m.group(2)) // 3
    return None


def _header_row(rows):
    best = max(range(len(rows)), key=lambda i: sum(1 for c in rows[i] if period_of(c)))
    if sum(1 for c in rows[best] if period_of(c)) < 4:
        raise ValueError("date header not found")
    return best


def _label_col(header):
    first_dt = min((j for j, c in enumerate(header) if period_of(c)), default=1)
    cand = [j for j in range(first_dt) if isinstance(header[j], str)]
    return cand[-1] if cand else 0


def _load_sheet(wb, sheet):
    rows = list(wb[sheet].iter_rows(values_only=True))
    h = _header_row(rows)
    cols = {j: period_of(c) for j, c in enumerate(rows[h]) if period_of(c)}
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


def _apply_sign(v, sign):
    return -v if sign == "flip_to_pos" else v


def _series(entry_src, sheets, sign):
    """label-based série (ČS)."""
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
    return {yq: (_apply_sign(v, sign), src) for yq, v in merged.items()}


def _row_series(rows, cols, rownum, sign):
    """row-based série (peers) — čte konkrétní Excel řádek napříč obdobími."""
    if not (1 <= rownum <= len(rows)):
        return {}
    r = rows[rownum - 1]
    out = {}
    for j, yq in cols.items():
        if j < len(r) and isinstance(r[j], (int, float)):
            out[yq] = (_apply_sign(float(r[j]), sign), None)
    return out


def _source_layout(smap):
    """Z hlavičky `sources:` vytáhne listy, priority a interim báze pro xlsx-zdroje."""
    sources_cfg = smap.get("sources", {})
    sheet_of, priority, interim = {}, {}, {}
    for i, (key, meta) in enumerate(sources_cfg.items(), start=1):
        sheet = meta.get("sheet")
        if not sheet:
            continue
        sheet_of[key] = sheet
        priority[key] = meta.get("priority", i)
        interim[key] = meta.get("interim_pl", "ytd_cumulative")
    return sheet_of, priority, interim


def ingest(config_dir, bank_code, xlsx_path):
    config_dir, xlsx_path = Path(config_dir), Path(xlsx_path)
    smap = yaml.safe_load((config_dir / "sources" / f"{bank_code}.yaml").read_text())
    sheet_of, priority, interim = _source_layout(smap)

    wb = openpyxl.load_workbook(xlsx_path, data_only=True)
    sheets, src_used, src_interim = {}, {}, {}
    for key, sheet in sheet_of.items():
        try:
            sheets[key] = _load_sheet(wb, sheet)
            src_used[key] = {"file": xlsx_path.name, "sheet": sheet}
            src_interim[key] = interim[key]
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

        at = entry.get("at")
        if at:   # row-based (peers)
            src = at["src"]
            if src not in sheets:
                continue
            rows, cols, _ = sheets[src]
            per = {yq: (v, src) for yq, (v, _) in _row_series(rows, cols, at["row"], sign).items()}
            if per:
                facts[code] = per
            continue

        # label-based (ČS): primary/history/long_kpi s prioritou zdroje
        per = {}
        for key in ("primary", "history", "long_kpi"):
            es = entry.get(key)
            if es and "src" in es:
                for yq, (v, src) in _series(es, sheets, sign).items():
                    if yq not in per or priority[src] > priority[per[yq][1]]:
                        per[yq] = (v, src)
        if per:
            facts[code] = per
    return facts, todo, src_used, src_interim
