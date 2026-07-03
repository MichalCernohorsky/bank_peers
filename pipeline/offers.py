#!/usr/bin/env python3
"""
offers.py — sběr produktových nabídek (sazby / promo / news) pro sekci „Sazby".

Config-driven scraping s bezpečnostní sítí: pro každou banku zkus stáhnout produktovou
stránku a vytáhnout sazbu (regex). Když fetch selže (WAF/timeout) nebo se sazba nedá
spolehlivě přečíst, použij `fallback` z config/products.yaml a fakt označ statusem:
  live      = staženo a přečteno z webu
  fallback  = použita ověřená hodnota z configu (web nedostupný/neparsovatelný)
News: automaticky z Google News RSS (dotaz per produkt + per banka v `news:` sekci configu)
a z oficiálních RSS bank (`news_rss`, kde existuje). Jen titulek+odkaz+zdroj+datum, filtr
klíčových slov, čerstvost, dedupe — nedostupný feed se přeskočí potichu.

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
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime
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


def validate_rate(v, rate_max=RATE_MAX):
    """Věrohodná sazba: kladná a v očekávaném rozsahu produktu (vklady ≤ 6 %,
    úvěry/karty víc — strop per produkt v config `rate_max`)."""
    return v is None or (0 < v <= rate_max)


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


def _load_cfg(config_dir):
    return yaml.safe_load((Path(config_dir) / "products.yaml").read_text())


def _load_products(config_dir):
    return _load_cfg(config_dir)["products"]


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


# --- novinky: Google News RSS (páteř) + oficiální RSS bank (kde existuje) ---
GNEWS_URL = "https://news.google.com/rss/search?q={q}&hl=cs&gl=CZ&ceid=CZ:cs"


def _news_key(title):
    """Normalizovaný klíč titulku pro dedupe (napříč zdroji)."""
    return re.sub(r"\W+", "", title.lower())[:80]


def _parse_rss_news(xml_text, limit=6, max_age_days=60, exclude=(), today=None):
    """RSS (Google News i klasický feed) -> [{title, url, source, published}].
    Trust vrstva: jen titulek+odkaz (žádný obsah), filtr klíčových slov,
    čerstvost max_age_days, dedupe titulků."""
    out, seen = [], set()
    for it in ET.fromstring(xml_text).findall(".//item"):
        title = (it.findtext("title") or "").strip()
        link = (it.findtext("link") or "").strip()
        src = (it.findtext("source") or "").strip()
        if src and title.endswith(" - " + src):     # Google News: "Titulek - Médium"
            title = title[: -len(" - " + src)].rstrip()
        if not title or not link:
            continue
        published = ""
        pd = it.findtext("pubDate")
        if pd:
            try:
                d = parsedate_to_datetime(pd).date()
                if max_age_days and ((today or dt.date.today()) - d).days > max_age_days:
                    continue                          # příliš staré -> pryč
                published = d.isoformat()
            except Exception:
                pass
        low = title.lower()
        if any(x.lower() in low for x in exclude or ()):
            continue                                  # nerelevantní (inzerce, soutěže…)
        key = _news_key(title)
        if key in seen:
            continue
        seen.add(key)
        out.append({"title": title, "url": link, "source": src, "published": published})
        if len(out) >= limit:
            break
    return out


def _fetch_news(rss_url=None, query=None, limit=6, max_age_days=60, exclude=(), today=None):
    """Novinky z oficiálního RSS banky (přednost) a/nebo Google News dotazu.
    Best-effort: nedostupný feed -> přeskočí se potichu (news nejsou brána)."""
    urls = [u for u in (rss_url, GNEWS_URL.format(q=urllib.parse.quote(query)) if query else None) if u]
    items = []
    for url in urls:
        try:
            items += _parse_rss_news(_fetch(url), limit=limit, max_age_days=max_age_days,
                                     exclude=exclude, today=today)
        except Exception:
            pass
    seen, out = set(), []
    for n in items:                                   # dedupe napříč zdroji
        k = _news_key(n["title"])
        if k in seen:
            continue
        seen.add(k)
        out.append(n)
    return out[:limit]


def _provenance(offer, fresh_days, rate_max=RATE_MAX):
    """Doplní důvěryhodnostní metadata: flags (validace), stale (čerstvost), checked_at."""
    flags = []
    if not validate_rate(offer.get("rate"), rate_max):
        flags.append("sazba mimo očekávaný rozsah")
    if not offer.get("conditions"):
        flags.append("chybí podmínky")
    if not offer.get("as_of"):
        flags.append("chybí datum platnosti")
    offer["flags"] = flags
    offer["stale"] = is_stale(offer.get("as_of"), fresh_days)
    offer["checked_at"] = dt.date.today().isoformat()
    return offer


def _bank_offer(code, cfg, live=True, fresh_days=FRESH_DAYS, notify=default_notify, rate_max=RATE_MAX,
                news=None):
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
            if got and validate_rate(got[0], rate_max):     # publikuj jen věrohodnou hodnotu
                offer["rate"], offer["rate_label"] = got[0], "až " + got[1]
                offer["status"], offer["method"] = "live", "http"
                offer["as_of"] = dt.date.today().isoformat()
        except Exception as e:
            notify(f"Sazby {code}: web nedostupný — použit fallback",
                   f"{cfg.get('url')} ({e.__class__.__name__})", level="info")
    n = news or {}
    offer["news"] = _fetch_news(cfg.get("news_rss"), query=n.get("query"), limit=n.get("limit", 6),
                                max_age_days=n.get("max_age_days", 60),
                                exclude=n.get("exclude") or ()) if live else []
    return _provenance(offer, fresh_days, rate_max)


def _matrix_offer(code, cfg, fresh_days=FRESH_DAYS, rate_max=RATE_MAX):
    """Nabídka pro produkt s více lhůtami (termín. vklad / fixace hypotéky): sazba per klíč."""
    fb = cfg.get("fallback", {})
    rates = {str(k): v for k, v in (fb.get("rates") or {}).items()}
    flags = [] if all(validate_rate(v, rate_max) for v in rates.values()) else ["sazba mimo očekávaný rozsah"]
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
    cfg = _load_cfg(config_dir)
    products = cfg["products"]
    if product not in products:
        raise ValueError(f"neznámý produkt: {product}")
    p = products[product]
    fresh_days = p.get("fresh_days", FRESH_DAYS)
    rate_max = p.get("rate_max", RATE_MAX)
    better = p.get("better", "high")   # high=vyšší lepší (vklady), low=nižší lepší (úvěry)
    ncfg = cfg.get("news") or {}       # zdroje novinek (Google News dotazy, limity)
    n_opts = {"limit": ncfg.get("limit", 6), "max_age_days": ncfg.get("max_age_days", 60),
              "exclude": p.get("news_exclude")}
    base = {
        "product": product, "label": p.get("label_cs", product), "unit": p.get("unit", "percent"),
        "group": p.get("group", ""), "better": better,
        "note": p.get("note", ""), "updated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "fresh_days": fresh_days, "disclaimer": "Sazby jsou orientační; před uzavřením ověřte u banky.",
        # novinky k produktu (trh) — plní se jen při živém sběru
        "news": _fetch_news(query=p.get("news_query"), **n_opts) if live else [],
    }
    if p.get("terms"):   # maticový produkt (termínovaný vklad / hypotéka dle fixace)
        banks = [_matrix_offer(code, bcfg, fresh_days, rate_max) for code, bcfg in p["banks"].items()]

        def mkey(b):   # nejlepší nabídka nahoře: nejnižší (better=low) / nejvyšší (high)
            vals = [v for v in b["rates"].values() if v is not None]
            if not vals:
                return (1, 0)   # bez sazby -> na konec
            return (0, min(vals)) if better == "low" else (0, -max(vals))
        banks.sort(key=mkey)
        return {**base, "kind": "matrix", "terms": p["terms"],
                "term_labels": p.get("term_labels", [f"{t}M" for t in p["terms"]]), "banks": banks}
    bank_queries = ncfg.get("banks") or {}   # per banka dotaz (jen vybrané, např. domácí 4)
    banks = [_bank_offer(code, bcfg, live=live, fresh_days=fresh_days, notify=notify, rate_max=rate_max,
                         news={**n_opts, "query": bank_queries.get(code)})
             for code, bcfg in p["banks"].items()]
    if better == "low":
        banks.sort(key=lambda b: (b["rate"] is None, b["rate"] or float("inf")))   # nejnižší sazba nahoře
    else:
        banks.sort(key=lambda b: (b["rate"] is None, -(b["rate"] or 0)))            # nejvyšší sazba nahoře
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
