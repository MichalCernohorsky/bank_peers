"""Validace zaznamu MGM programu proti schema/mgm-program.schema.json.

Bez zavislosti (stdlib only) - zamerne. Pokryva podmnozinu JSON Schema, kterou
schema skutecne pouziva, plus SEMANTICKE kontroly vynucujici pravidla kvality
ze zadani (kazde cislo ma zdroj; confidence 'high' vyzaduje T&C; ...).

Pouziti:
    python3 tracker/validate.py data/mgm-programs.json
"""
from __future__ import annotations

import json
import re
import sys
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCHEMA_PATH = ROOT / "schema" / "mgm-program.schema.json"

_TYPES = {
    "string": str,
    "number": (int, float),
    "integer": int,
    "boolean": bool,
    "array": list,
    "object": dict,
}


def _type_ok(value, spec) -> bool:
    types = spec if isinstance(spec, list) else [spec]
    for t in types:
        if t == "null":
            if value is None:
                return True
        elif t == "boolean":
            if isinstance(value, bool):
                return True
        elif t == "number":
            if isinstance(value, (int, float)) and not isinstance(value, bool):
                return True
        elif t in _TYPES and isinstance(value, _TYPES[t]):
            # bool je podtrida int - nesmi projit jako number/integer
            if t in ("integer",) and isinstance(value, bool):
                continue
            return True
    return False


def _check_format(value, fmt, path, errors) -> None:
    if value is None or not isinstance(value, str):
        return
    if fmt == "date":
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError:
            errors.append(f"{path}: '{value}' neni datum ve formatu YYYY-MM-DD")
    elif fmt == "uri":
        if not re.match(r"^https?://\S+$", value):
            errors.append(f"{path}: '{value}' neni http(s) URL")


def _validate_against(value, spec: dict, path: str, errors: list[str]) -> None:
    """Rekurzivni validace jedne hodnoty proti (pod)schematu."""
    if "enum" in spec:
        if value not in spec["enum"]:
            allowed = ", ".join(repr(v) for v in spec["enum"])
            errors.append(f"{path}: {value!r} neni v povolenych hodnotach ({allowed})")
        return

    if "type" in spec and not _type_ok(value, spec["type"]):
        errors.append(f"{path}: ocekavan typ {spec['type']}, prislo {type(value).__name__}")
        return

    if isinstance(value, str):
        if "pattern" in spec and not re.match(spec["pattern"], value):
            errors.append(f"{path}: '{value}' neodpovida vzoru {spec['pattern']}")
        if "format" in spec:
            _check_format(value, spec["format"], path, errors)

    if isinstance(value, dict) and "properties" in spec:
        for req in spec.get("required", []):
            if req not in value:
                errors.append(f"{path}: chybi povinne pole '{req}'")
        if spec.get("additionalProperties") is False:
            for key in value:
                if key not in spec["properties"]:
                    errors.append(f"{path}: nezname pole '{key}'")
        for key, sub in spec["properties"].items():
            if key in value:
                _validate_against(value[key], sub, f"{path}.{key}", errors)

    if isinstance(value, dict) and isinstance(spec.get("additionalProperties"), dict):
        for key, val in value.items():
            _validate_against(val, spec["additionalProperties"], f"{path}.{key}", errors)

    if isinstance(value, list) and "items" in spec:
        for i, item in enumerate(value):
            _validate_against(item, spec["items"], f"{path}[{i}]", errors)


def _semantic_checks(rec: dict, path: str, errors: list[str]) -> None:
    """Pravidla kvality ze zadani, ktera cisty JSON Schema nevyjadri."""
    status = rec.get("status")
    sources = rec.get("sources") or []

    # "nenalezeno" je platna informace - ale pak nesmi nest odmeny.
    if status == "none":
        for field in ("reward_referrer", "reward_referee", "reward_type",
                      "reward_referrer_value", "reward_referee_value"):
            if rec.get(field) not in (None, "", []):
                errors.append(f"{path}: status='none', ale {field} je vyplnene ({rec[field]!r})")
    elif status == "active":
        # Jen u 'active' je absence odmeny rozpor. U 'unknown'/'ended' je legitimni,
        # ze program existuje (nebo existoval), ale vysi odmeny se nepodarilo overit.
        if not rec.get("reward_referrer") and not rec.get("reward_referee"):
            errors.append(f"{path}: status='active' bez jakekoli odmeny - pouzij 'unknown' nebo doplň odmenu")

    # confidence 'high' == oficialni T&C, ne marketing.
    if rec.get("confidence") == "high":
        if not any(s.get("type") == "tc" for s in sources):
            errors.append(f"{path}: confidence='high' vyzaduje aspoň jeden zdroj type='tc'")

    # Kazde cislo musi mit zdroj.
    has_number = any(rec.get(f) is not None for f in ("reward_referrer_value", "reward_referee_value"))
    if has_number and not rec.get("source_url") and not sources:
        errors.append(f"{path}: ciselna odmena bez source_url i bez sources")

    # Ciselna hodnota vyzaduje menu.
    for side in ("referrer", "referee"):
        val = rec.get(f"reward_{side}_value")
        cur = rec.get(f"reward_{side}_currency")
        if val is not None and not cur:
            errors.append(f"{path}: reward_{side}_value={val} bez reward_{side}_currency")

    # Datum overeni nesmi byt v budoucnosti.
    for field in ("source_date", "last_checked"):
        raw = rec.get(field)
        if isinstance(raw, str):
            try:
                if datetime.strptime(raw, "%Y-%m-%d").date() > date.today():
                    errors.append(f"{path}: {field}='{raw}' je v budoucnosti")
            except ValueError:
                pass  # format uz reportoval _check_format

    # Kampan: od <= do
    period = rec.get("campaign_period") or {}
    frm, to = period.get("from"), period.get("to")
    if isinstance(frm, str) and isinstance(to, str):
        try:
            if datetime.strptime(frm, "%Y-%m-%d") > datetime.strptime(to, "%Y-%m-%d"):
                errors.append(f"{path}: campaign_period.from ({frm}) je po .to ({to})")
        except ValueError:
            pass


def validate_records(records: list[dict], schema: dict | None = None) -> list[str]:
    """Vrati seznam chyb; prazdny seznam = vse v poradku."""
    schema = schema or json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    errors: list[str] = []
    seen: dict[str, int] = {}

    for i, rec in enumerate(records):
        rid = rec.get("record_id", f"<bez record_id #{i}>")
        path = f"[{i}] {rid}"
        if not isinstance(rec, dict):
            errors.append(f"{path}: zaznam neni objekt")
            continue
        _validate_against(rec, schema, path, errors)
        _semantic_checks(rec, path, errors)
        if isinstance(rid, str):
            if rid in seen:
                errors.append(f"{path}: duplicitni record_id (uz na indexu {seen[rid]})")
            else:
                seen[rid] = i

    return errors


def main(argv: list[str]) -> int:
    target = Path(argv[1]) if len(argv) > 1 else ROOT / "data" / "mgm-programs.json"
    if not target.exists():
        print(f"CHYBA: soubor neexistuje: {target}", file=sys.stderr)
        return 2

    payload = json.loads(target.read_text(encoding="utf-8"))
    records = payload["records"] if isinstance(payload, dict) else payload

    errors = validate_records(records)
    if errors:
        print(f"NEVALIDNI: {len(errors)} chyb v {target}", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    print(f"OK: {len(records)} zaznamu validnich ({target})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
