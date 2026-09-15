"""Generuje report/mgm-cz-report.md a data/mgm-programs.csv z data/mgm-programs.json.

Datove casti reportu (prehledova tabulka, karty subjektu, priloha zdroju,
statistiky) se generuji VZDY z JSON, takze se nemusi udrzovat rucne.
Analyticke sekce jsou autorske a ziji v report/sections/*.md; generator je
jen vklada na sve misto.

Pouziti:
    python3 tracker/report.py
"""
from __future__ import annotations

import csv
import json
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "mgm-programs.json"
CSV_OUT = ROOT / "data" / "mgm-programs.csv"
REPORT_OUT = ROOT / "report" / "mgm-cz-report.md"
SECTIONS = ROOT / "report" / "sections"

# record_id + 18 poli ze zadani, v poradi ze zadani.
CSV_FIELDS = [
    "record_id", "subject", "subject_type", "program_name", "status",
    "product_scope", "reward_referrer", "reward_referee", "reward_type",
    "conditions", "channel", "limits", "timing", "campaign_period",
    "eligibility", "source_url", "source_date", "confidence", "notes",
]

STATUS_LABEL = {
    "active": "aktivní",
    "paused": "pozastaven",
    "ended": "ukončen",
    "unknown": "neověřeno",
    "none": "nemá MGM",
}

CONFIDENCE_LABEL = {"high": "vysoká", "medium": "střední", "low": "nízká"}

SOURCE_TYPE_LABEL = {
    "tc": "T&C",
    "marketing": "oficiální marketing",
    "press": "tisková zpráva",
    "secondary": "sekundární",
    "archive": "archiv",
}


def _sort_key(rec: dict) -> tuple:
    """Razeni: nejdriv banky, pak podle nazvu bez ohledu na diakritiku a velikost pismen."""
    name = unicodedata.normalize("NFKD", rec["subject"])
    name = "".join(c for c in name if not unicodedata.combining(c))
    return (rec["subject_type"] != "bank", name.casefold())


def load_records() -> tuple[list[dict], dict]:
    payload = json.loads(DATA.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        return payload, {}
    return payload["records"], payload


def _flat(value) -> str:
    """Zplosti hodnotu pro CSV / tabulku."""
    if value is None:
        return ""
    if isinstance(value, bool):
        return "ano" if value else "ne"
    if isinstance(value, list):
        return "; ".join(str(v) for v in value)
    if isinstance(value, dict):  # campaign_period
        frm, to = value.get("from") or "?", value.get("to") or "?"
        note = value.get("note")
        base = f"{frm} – {to}"
        return f"{base} ({note})" if note else base
    return str(value)


def write_csv(records: list[dict]) -> None:
    CSV_OUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUT.open("w", encoding="utf-8", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=CSV_FIELDS, extrasaction="ignore")
        writer.writeheader()
        for rec in records:
            writer.writerow({k: _flat(rec.get(k)) for k in CSV_FIELDS})


def _md_cell(text: str, limit: int = 120) -> str:
    """Bezpecna bunka markdown tabulky."""
    if not text:
        return "—"
    text = " ".join(str(text).split()).replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "…"


def build_overview(records: list[dict]) -> str:
    rows = [
        "| Subjekt | Typ | Status | Odměna doporučující | Odměna doporučený | Klíčová podmínka | Limit | Conf. | Zdroj |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for r in sorted(records, key=_sort_key):
        url = r.get("source_url")
        src = f"[odkaz]({url})" if url else "—"
        rows.append(
            f"| **{r['subject']}** "
            f"| {'banka' if r['subject_type'] == 'bank' else 'neobanka'} "
            f"| {STATUS_LABEL.get(r['status'], r['status'])} "
            f"| {_md_cell(r.get('reward_referrer'), 80)} "
            f"| {_md_cell(r.get('reward_referee'), 80)} "
            f"| {_md_cell(r.get('conditions'), 100)} "
            f"| {_md_cell(r.get('limits'), 60)} "
            f"| {CONFIDENCE_LABEL.get(r.get('confidence'), '?')} "
            f"| {src} |"
        )
    return "\n".join(rows)


def build_cards(records: list[dict]) -> str:
    out: list[str] = []
    for group, label in (("bank", "Banky"), ("neobank", "Neobanky a fintechy")):
        group_recs = sorted(
            (r for r in records if r["subject_type"] == group), key=_sort_key
        )
        out.append(f"### {label}\n")
        for r in group_recs:
            flag = "" if r.get("in_original_scope", True) else " *(doplněno)*"
            out.append(f"#### {r['subject']}{flag}\n")
            prog = r.get("program_name") or "—"
            rows = [
                ("Program", prog),
                ("Status", STATUS_LABEL.get(r["status"], r["status"])),
                ("Produkty", _flat(r.get("product_scope"))),
                ("Odměna doporučující", r.get("reward_referrer")),
                ("Odměna doporučený", r.get("reward_referee")),
                ("Typ odměny", r.get("reward_type")),
                ("Podmínky", r.get("conditions")),
                ("Kanál", _flat(r.get("channel"))),
                ("Limity", r.get("limits")),
                ("Lhůty", r.get("timing")),
                ("Platnost kampaně", _flat(r.get("campaign_period"))),
                ("Kdo se může účastnit", r.get("eligibility")),
                ("Confidence", CONFIDENCE_LABEL.get(r.get("confidence"), "?")),
                ("Ověřeno dne", r.get("source_date")),
            ]
            out.append("| Pole | Hodnota |")
            out.append("|---|---|")
            for key, val in rows:
                out.append(f"| {key} | {_md_cell(val, 400)} |")
            out.append("")
            fc = r.get("field_confidence") or {}
            if fc:
                detail = ", ".join(f"`{k}`: {CONFIDENCE_LABEL.get(v, v)}" for k, v in fc.items())
                out.append(f"*Nižší jistota u jednotlivých polí:* {detail}\n")
            if r.get("notes"):
                out.append(f"**Poznámky.** {r['notes']}\n")
    return "\n".join(out)


def build_appendix(records: list[dict]) -> str:
    out = []
    for r in sorted(records, key=_sort_key):
        sources = r.get("sources") or []
        if not sources:
            continue
        out.append(f"**{r['subject']}**\n")
        for s in sources:
            stype = SOURCE_TYPE_LABEL.get(s.get("type"), s.get("type"))
            title = s.get("title") or s["url"]
            conf = CONFIDENCE_LABEL.get(s.get("confidence"), "?")
            out.append(f"- [{title}]({s['url']}) — {stype}, jistota {conf}, ověřeno {s.get('date')}")
        out.append("")
    return "\n".join(out)


def build_stats(records: list[dict]) -> str:
    by_status: dict[str, int] = {}
    by_conf: dict[str, int] = {}
    for r in records:
        by_status[r["status"]] = by_status.get(r["status"], 0) + 1
        by_conf[r["confidence"]] = by_conf.get(r["confidence"], 0) + 1

    banks = sum(1 for r in records if r["subject_type"] == "bank")
    neo = len(records) - banks
    status_txt = ", ".join(
        f"{STATUS_LABEL.get(k, k)}: {v}" for k, v in sorted(by_status.items(), key=lambda kv: -kv[1])
    )
    conf_txt = ", ".join(
        f"{CONFIDENCE_LABEL.get(k, k)}: {v}" for k, v in sorted(by_conf.items(), key=lambda kv: -kv[1])
    )
    return (
        f"- **Subjektů celkem:** {len(records)} ({banks} bank, {neo} neobank/fintechů)\n"
        f"- **Podle statusu:** {status_txt}\n"
        f"- **Podle jistoty zdroje:** {conf_txt}\n"
    )


def _section(name: str) -> str:
    path = SECTIONS / name
    if not path.exists():
        return f"> *(Sekce `{name}` zatím není napsaná.)*\n"
    return path.read_text(encoding="utf-8").strip() + "\n"


def build_report(records: list[dict], meta: dict) -> str:
    generated = meta.get("generated_at", "?")
    parts = [
        "# Member-Get-Member programy na českém bankovním trhu\n",
        f"*Datová základna ověřena k {generated}. "
        "Report je generovaný z `data/mgm-programs.json` skriptem `tracker/report.py` — "
        "needitovat ručně; analytické sekce se upravují v `report/sections/`.*\n",
        "---\n",
        "## 1. Executive summary\n",
        _section("01-executive-summary.md"),
        "\n### Souhrnná čísla\n",
        build_stats(records),
        "\n---\n",
        "## 2. Přehledová tabulka\n",
        build_overview(records),
        "\n\n---\n",
        "## 3. Detailní karty subjektů\n",
        build_cards(records),
        "\n---\n",
        "## 4. Historie a trendy\n",
        _section("04-historie.md"),
        "\n---\n",
        "## 5. Srovnání: banky vs. neobanky\n",
        _section("05-srovnani.md"),
        "\n---\n",
        "## 6. Metodika a limity\n",
        _section("06-metodika.md"),
        "\n---\n",
        "## 7. Příloha — kompletní seznam zdrojů\n",
        build_appendix(records),
    ]
    return "\n".join(parts)


def main() -> int:
    if not DATA.exists():
        print(f"CHYBA: chybi {DATA}", file=sys.stderr)
        return 2
    records, meta = load_records()
    write_csv(records)
    REPORT_OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT_OUT.write_text(build_report(records, meta), encoding="utf-8")
    print(f"OK: {CSV_OUT.relative_to(ROOT)} ({len(records)} radku)")
    print(f"OK: {REPORT_OUT.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
