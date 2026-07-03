#!/usr/bin/env python3
"""
offers.py — sběr produktových nabídek (sazby / promo / news) pro sekci „Sazby".

Config-driven scraping s bezpečnostní sítí: pro každou banku zkus stáhnout produktovou
stránku a vytáhnout sazbu (regex). Když fetch selže (WAF/timeout) nebo se sazba nedá
spolehlivě přečíst, použij `fallback` z config/products.yaml a fakt označ statusem:
  live      = staženo a přečteno z webu
  fallback  = použita ověřená hodnota z configu (web nedostupný/neparsovatelný)
News: volitelně z RSS (news_rss). Výstup: data/offers.json (čte ho /api/offers).

  python -m pipeline.offers --product savings_account [--out data/offers.json]

Pozn.: respektuj ToS webů; scraping je best-effort a v prostředí za WAF spadne na fallback.
"""
import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.notify import notify as default_notify  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_OUT = ROOT / "data" / "offers.json"
CHANGELOG = ROOT / "data" / "offers_changelog.json"
ACCENTS = {"cs": "#C8102E", "kb": "#A6192E", "csob": "#0098D4", "moneta": "#6A2C70"}
UA = "Mozilla/5.0 (compatible; BankPulseBot/1.0; +https://example.com/bot)"

# --- důvěryhodnostní vrstva: rozsah, čerstvost, změny ---
RATE_MAX = 0.06            # sazba nad 6 % je podezřelá -> flag
FRESH_DAYS = 45           # starší -> „ověřit"
REVIEW_DELTA = 0.01       # skok > 1 p.b. proti minulé hodnotě -> ke schválení + alert


def _parse_asof(s):
    if not s:
        return None
    try:
        return dt.date(int(s[:4]), int(s[5:7]), 15) if len(s) == 7 else dt.date.fromisoformat(s)
    except Exception:
        return None


def is_stale(as_of, fresh_days=FRESH_DAYS, today=None):
    d = _parse_asof(as_of)
    if not d:
        return True
    return ((today or dt.date.today()) - d).days > fresh_days


def validate_rate(v):
    return v is None or (0 < v <= RATE_MAX)


def diff_snapshot(prev, new):
    """Rozdíl sazeb proti minulému snapshotu (pro audit + zadržení velkých skoků)."""
    changes = []
    pj = {b["code"]: b for b in (prev or {}).get("banks", [])}
    for b in new["banks"]:
        old = pj.get(b["code"], {})
        if new.get("kind") == "matrix":
            for t, v in (b.get("rates") or {}).items():
                ov = (old.get("rates") or {}).get(t)
                if ov != v:
                    changes.append({"bank": b["code"], "term": t, "old": ov, "new": v})
        else:
            if old.get("rate") != b.get("rate"):
                changes.append({"bank": b["code"], "old": old.get("rate"), "new": b.get("rate")})
    return changes


def _load_products(config_dir):
    return yaml.safe_load((Path(config_dir) / "products.yaml").read_text())["products"]


def _fetch(url, timeout=20):
    # OFFERS_BROWSER=1 -> headless Chromium (projde WAF); jinak prosté HTTP.
    if os.environ.get("OFFERS_BROWSER"):
        from pipeline.offers_browser import fetch_text
        return fetch_text(url, timeout=timeout * 1000)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:  # noqa: S310 (veřejná produktová URL)
        return r.read().decode("utf-8", "ignore")


def _extract_rate(html, rate_regex):
    """Best-effort: první procentní hodnota odpovídající vzoru. Vrátí (fraction, label) nebo None."""
    m = re.search(rate_regex, html)
    if not m:
        return None
    num = float(m.group(1).replace(",", "."))
    return num / 100.0, f"{m.group(1)} %"


def _fetch_news(rss_url, limit=3):
    if not rss_url:
        return []
    try:
        xml = _fetch(rss_url)
        root = ET.fromstring(xml)
        items = root.findall(".//item")[:limit]
        out = []
        for it in items:
            title = (it.findtext("title") or "").strip()
            link = (it.findtext("link") or "").strip()
            if title:
                out.append({"title": title, "url": link})
        return out
    except Exception:
        return []


def _provenance(offer, fresh_days):
    """Doplní důvěryhodnostní metadata: flags (validace), stale (čerstvost), checked_at."""
    flags = []
    if not validate_rate(offer.get("rate")):
        flags.append("sazba mimo očekávaný rozsah")
    if not offer.get("conditions"):
        flags.append("chybí podmínky")
    if not offer.get("as_of"):
        flags.append("chybí datum platnosti")
    offer["flags"] = flags
    offer["stale"] = is_stale(offer.get("as_of"), fresh_days)
    offer["checked_at"] = dt.date.today().isoformat()
    return offer


def _bank_offer(code, cfg, live=True, fresh_days=FRESH_DAYS, notify=default_notify):
    fb = cfg.get("fallback", {})
    offer = {
        "code": code, "name": cfg.get("name", code.upper()),
        "short": cfg.get("short", code.upper()[:4]),
        "accent": cfg.get("accent", ACCENTS.get(code, "#334155")),
        "url": cfg.get("url"),
        "rate": fb.get("rate"), "rate_label": fb.get("rate_label", "—"),
        "conditions": fb.get("conditions", ""), "promo": fb.get("promo", ""),
        "as_of": fb.get("as_of"), "news": [], "status": "fallback", "method": "fallback",
    }
    if live and cfg.get("url"):
        try:
            html = _fetch(cfg["url"])
            got = _extract_rate(html, cfg.get("rate_regex", r"(\d+[,.]\d+)\s*%"))
            if got and validate_rate(got[0]):     # publikuj jen věrohodnou hodnotu
                offer["rate"], offer["rate_label"] = got[0], "až " + got[1]
                offer["status"], offer["method"] = "live", "http"
                offer["as_of"] = dt.date.today().isoformat()
        except Exception as e:
            notify(f"Sazby {code}: web nedostupný — použit fallback",
                   f"{cfg.get('url')} ({e.__class__.__name__})", level="info")
    offer["news"] = _fetch_news(cfg.get("news_rss")) if live else []
    return _provenance(offer, fresh_days)


def _matrix_offer(code, cfg, fresh_days=FRESH_DAYS):
    """Nabídka pro produkt s více lhůtami (termínovaný vklad): sazba per délka."""
    fb = cfg.get("fallback", {})
    rates = {str(k): v for k, v in (fb.get("rates") or {}).items()}
    flags = [] if all(validate_rate(v) for v in rates.values()) else ["sazba mimo očekávaný rozsah"]
    if not fb.get("as_of"):
        flags.append("chybí datum platnosti")
    return {
        "code": code, "name": cfg.get("name", code.upper()),
        "short": cfg.get("short", code.upper()[:4]),
        "accent": cfg.get("accent", ACCENTS.get(code, "#334155")),
        "url": cfg.get("url"), "rates": rates,
        "conditions": fb.get("conditions", ""), "promo": fb.get("promo", ""),
        "as_of": fb.get("as_of"), "news": [], "status": "fallback", "method": "fallback",
        "flags": flags, "stale": is_stale(fb.get("as_of"), fresh_days),
        "checked_at": dt.date.today().isoformat(),
    }


def snapshot(product, config_dir=None, live=False, notify=default_notify):
    """Sestaví snapshot nabídek. live=False -> jen z configu (bez sítě).
    Produkt s klíčem `terms` = maticový (banka × délka), jinak tabulka (jedna sazba)."""
    config_dir = Path(config_dir or (ROOT / "config"))
    products = _load_products(config_dir)
    if product not in products:
        raise ValueError(f"neznámý produkt: {product}")
    p = products[product]
    fresh_days = p.get("fresh_days", FRESH_DAYS)
    base = {
        "product": product, "label": p.get("label_cs", product), "unit": p.get("unit", "percent"),
        "note": p.get("note", ""), "updated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "fresh_days": fresh_days, "disclaimer": "Sazby jsou orientační; před uzavřením ověřte u banky.",
    }
    if p.get("terms"):   # maticový produkt (termínovaný vklad)
        banks = [_matrix_offer(code, bcfg, fresh_days) for code, bcfg in p["banks"].items()]
        banks.sort(key=lambda b: -max([v for v in b["rates"].values() if v is not None], default=0))
        return {**base, "kind": "matrix", "terms": p["terms"],
                "term_labels": p.get("term_labels", [f"{t}M" for t in p["terms"]]), "banks": banks}
    banks = [_bank_offer(code, bcfg, live=live, fresh_days=fresh_days, notify=notify)
             for code, bcfg in p["banks"].items()]
    banks.sort(key=lambda b: (b["rate"] is None, -(b["rate"] or 0)))   # nejvyšší sazba nahoře
    return {**base, "kind": "table", "banks": banks}


def refresh(product, config_dir=None, out=DEFAULT_OUT, notify=default_notify):
    """Živý sběr + důvěryhodnostní brána: velké skoky sazeb označí k ručnímu schválení
    (needs_review) a pošle alert; audit se zapíše do offers_changelog.json."""
    out = Path(out)
    prev = json.loads(out.read_text()) if out.exists() else None
    snap = snapshot(product, config_dir=config_dir, live=True, notify=notify)

    changes = diff_snapshot(prev, snap)
    big = [c for c in changes if c.get("old") is not None and c.get("new") is not None
           and abs(c["new"] - c["old"]) > REVIEW_DELTA]
    if big:
        flagged = {c["bank"] for c in big}
        for b in snap["banks"]:
            if b["code"] in flagged:
                b["needs_review"] = True
        notify(f"Sazby {product}: {len(big)} velkých změn ke schválení",
               "; ".join(f"{c['bank']} {c.get('term','') } {c['old']}→{c['new']}" for c in big[:6]),
               level="alert")

    flagged_data = [b["code"] for b in snap["banks"] if b.get("flags")]
    if flagged_data:
        notify(f"Sazby {product}: validační flagy u {flagged_data}",
               "zkontroluj rozsah/podmínky/datum", level="alert")

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(snap, ensure_ascii=False, indent=2))
    if changes:
        log = json.loads(CHANGELOG.read_text()) if CHANGELOG.exists() else []
        log.append({"at": dt.datetime.now().isoformat(timespec="seconds"), "product": product, "changes": changes})
        CHANGELOG.write_text(json.dumps(log, ensure_ascii=False, indent=2))

    live = sum(1 for b in snap["banks"] if b.get("method") in ("http", "browser"))
    print(f"Sazby {product}: {len(snap['banks'])} subjektů ({live} live, {len(snap['banks']) - live} fallback), "
          f"{len(changes)} změn, {len(big)} ke schválení -> {out}")
    return snap


def main():
    ap = argparse.ArgumentParser(description="Sběr produktových nabídek (sazby/promo/news).")
    ap.add_argument("--product", default="savings_account")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    refresh(args.product, out=args.out)


if __name__ == "__main__":
    main()
