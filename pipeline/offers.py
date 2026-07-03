#!/usr/bin/env python3
"""
offers.py — sběr produktových nabídek (sazby / promo / news) pro sekci „Sazby".

Config-driven scraping s bezpečnostní sítí: pro každou banku zkus stáhnout produktovou
stránku a vytáhnout sazbu (regex). Když fetch selže (WAF/timeout) nebo se sazba nedá
spolehlivě přečíst, použij `fallback` z config/products.yaml a fakt označ statusem:
  live      = staženo a přečteno z webu
  fallback  = použita ověřená hodnota z configu (web nedostupný/neparsovatelný)
News: volitelně z RSS (news_rss).

Brána (návrh → potvrzení člověkem): refresh() živě sebere data a porovná se
schváleným snapshotem. Velký skok (> REVIEW_DELTA) nebo validační flag se zadrží
do staging + pending a NEPUBLIKUJE; publikuje se až po `--approve`. Publikovaný
stav je per-produkt v data/offers_<product>.json (čte ho /api/offers).

  python -m pipeline.offers --product savings_account            # živý sběr + brána
  python -m pipeline.offers --product savings_account --review   # co čeká ke schválení
  python -m pipeline.offers --product savings_account --approve  # staging -> published
  python -m pipeline.offers --product savings_account --reject   # zahodí návrh

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
DATA_DIR = ROOT / "data"          # adresář se stavem (lze přebít v testech)
ACCENTS = {"cs": "#1A3A5C", "kb": "#A6192E", "csob": "#0098D4", "moneta": "#6A2C70"}  # shodné s peer comparison
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
        "highlight": bool(cfg.get("highlight")),
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
        "highlight": bool(cfg.get("highlight")),
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


# --- úložiště stavu (per-produkt): published / staging / pending / changelog ---
def published_path(product):
    """Publikovaný snapshot, který čte /api/offers. Nic neověřeného sem nesmí."""
    return DATA_DIR / f"offers_{product}.json"


def _staging_path(product):
    """Návrh čekající na schválení (živě stažený, ale zadržený bránou)."""
    return DATA_DIR / f"offers_{product}.staging.json"


def _pending_path(product):
    """Souhrn důvodů zadržení (co přesně je ke schválení)."""
    return DATA_DIR / f"offers_{product}.pending.json"


def _changelog_path():
    return DATA_DIR / "offers_changelog.json"


def _append_changelog(entry):
    p = _changelog_path()
    log = json.loads(p.read_text()) if p.exists() else []
    log.append(entry)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(log, ensure_ascii=False, indent=2))


def _publish(product, snap, changes=None, reason="auto"):
    """Zapíše snapshot do published + zaznamená do changelogu."""
    p = published_path(product)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(snap, ensure_ascii=False, indent=2))
    _append_changelog({
        "at": dt.datetime.now().isoformat(timespec="seconds"),
        "product": product, "action": "publish", "reason": reason,
        "changes": changes or [],
    })


def _hold(product, snap, changes, big, flagged_data):
    """Zadrží návrh do staging + zapíše pending (důvody). Nepublikuje."""
    for b in snap["banks"]:
        if b["code"] in {c["bank"] for c in big} or b.get("flags"):
            b["needs_review"] = True
    sp, pp = _staging_path(product), _pending_path(product)
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text(json.dumps(snap, ensure_ascii=False, indent=2))
    pending = {
        "at": dt.datetime.now().isoformat(timespec="seconds"), "product": product,
        "big_changes": big, "flagged": flagged_data, "changes": changes,
    }
    pp.write_text(json.dumps(pending, ensure_ascii=False, indent=2))
    return pending


def refresh(product, config_dir=None, live=True, notify=default_notify):
    """Živý sběr + důvěryhodnostní brána (návrh → potvrzení člověkem).

    - první běh (bootstrap): publikuje rovnou (není s čím porovnat);
    - malá/žádná změna a bez validačních flagů: auto-publikuje;
    - velký skok (> REVIEW_DELTA) NEBO validační flag: zadrží do staging + pending,
      pošle alert a NEPUBLIKUJE — čeká na `approve()`.
    """
    pub = published_path(product)
    prev = json.loads(pub.read_text()) if pub.exists() else None
    snap = snapshot(product, config_dir=config_dir, live=live, notify=notify)

    changes = diff_snapshot(prev, snap)
    big = [c for c in changes if c.get("old") is not None and c.get("new") is not None
           and abs(c["new"] - c["old"]) > REVIEW_DELTA]
    flagged_data = [b["code"] for b in snap["banks"] if b.get("flags")]

    if prev is None:                                   # bootstrap: první publikace
        _publish(product, snap, changes, reason="bootstrap")
        action = "publikováno (bootstrap)"
    elif not big and not flagged_data:                 # důvěryhodná změna -> auto-publish
        _publish(product, snap, changes, reason="auto")
        action = "publikováno (auto)"
    else:                                              # zadržet ke schválení
        _hold(product, snap, changes, big, flagged_data)
        detail = "; ".join(f"{c['bank']} {c.get('term','')} {c['old']}→{c['new']}" for c in big[:6])
        notify(f"Sazby {product}: {len(big)} velkých změn / flagy {flagged_data} ke schválení",
               f"{detail}  —  schval: python -m pipeline.offers --product {product} --approve",
               level="alert")
        action = "ZADRŽENO ke schválení (needs_review)"

    live_n = sum(1 for b in snap["banks"] if b.get("method") in ("http", "browser"))
    print(f"Sazby {product}: {len(snap['banks'])} subjektů ({live_n} live, "
          f"{len(snap['banks']) - live_n} fallback), {len(changes)} změn, "
          f"{len(big)} velkých, flagy {flagged_data} -> {action}")
    return snap


def pending(product):
    """Vrátí čekající návrh (staging snapshot + důvody), nebo None když nic nečeká."""
    pp, sp = _pending_path(product), _staging_path(product)
    if not pp.exists() or not sp.exists():
        return None
    return {"reasons": json.loads(pp.read_text()), "snapshot": json.loads(sp.read_text())}


def approve(product, notify=default_notify):
    """Potvrdí čekající návrh: staging -> published, zapíše audit, uklidí pending."""
    sp, pp = _staging_path(product), _pending_path(product)
    if not sp.exists():
        print(f"Sazby {product}: nic ke schválení.")
        return None
    snap = json.loads(sp.read_text())
    for b in snap["banks"]:
        b.pop("needs_review", None)
    reasons = json.loads(pp.read_text()) if pp.exists() else {}
    _publish(product, snap, reasons.get("changes", []), reason="approved")
    sp.unlink(missing_ok=True)
    pp.unlink(missing_ok=True)
    notify(f"Sazby {product}: schváleno a publikováno", "", level="info")
    print(f"Sazby {product}: schváleno -> {published_path(product)}")
    return snap


def reject(product):
    """Zahodí čekající návrh (staging + pending); published zůstává beze změny."""
    _staging_path(product).unlink(missing_ok=True)
    _pending_path(product).unlink(missing_ok=True)
    _append_changelog({"at": dt.datetime.now().isoformat(timespec="seconds"),
                       "product": product, "action": "reject"})
    print(f"Sazby {product}: návrh zamítnut, publikovaná data beze změny.")


def main():
    ap = argparse.ArgumentParser(description="Sběr produktových nabídek (sazby/promo/news) + brána schválení.")
    ap.add_argument("--product", default="savings_account")
    ap.add_argument("--review", action="store_true", help="vypíše, co čeká na schválení")
    ap.add_argument("--approve", action="store_true", help="potvrdí čekající návrh (staging -> published)")
    ap.add_argument("--reject", action="store_true", help="zahodí čekající návrh")
    ap.add_argument("--no-live", action="store_true", help="jen z configu, bez sítě")
    args = ap.parse_args()

    if args.review:
        pend = pending(args.product)
        if not pend:
            print(f"Sazby {args.product}: nic nečeká na schválení.")
        else:
            r = pend["reasons"]
            print(f"Sazby {args.product} — ke schválení (z {r.get('at')}):")
            for c in r.get("big_changes", []):
                print(f"  velký skok: {c['bank']} {c.get('term','')} {c['old']}→{c['new']}")
            if r.get("flagged"):
                print(f"  validační flagy: {r['flagged']}")
            print(f"  schval: python -m pipeline.offers --product {args.product} --approve")
    elif args.approve:
        approve(args.product)
    elif args.reject:
        reject(args.product)
    else:
        refresh(args.product, live=not args.no_live)


if __name__ == "__main__":
    main()
