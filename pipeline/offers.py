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
ACCENTS = {"cs": "#C8102E", "kb": "#A6192E", "csob": "#0098D4", "moneta": "#6A2C70"}
UA = "Mozilla/5.0 (compatible; BankPulseBot/1.0; +https://example.com/bot)"


def _load_products(config_dir):
    return yaml.safe_load((Path(config_dir) / "products.yaml").read_text())["products"]


def _fetch(url, timeout=20):
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


def _bank_offer(code, cfg, live=True, notify=default_notify):
    fb = cfg.get("fallback", {})
    offer = {
        "code": code, "name": cfg.get("name", code.upper()),
        "short": cfg.get("short", code.upper()[:4]),
        "accent": cfg.get("accent", ACCENTS.get(code, "#334155")),
        "url": cfg.get("url"),
        "rate": fb.get("rate"), "rate_label": fb.get("rate_label", "—"),
        "conditions": fb.get("conditions", ""), "promo": fb.get("promo", ""),
        "as_of": fb.get("as_of"), "news": [], "status": "fallback",
    }
    if live and cfg.get("url"):
        try:
            html = _fetch(cfg["url"])
            got = _extract_rate(html, cfg.get("rate_regex", r"(\d+[,.]\d+)\s*%"))
            if got:
                offer["rate"], offer["rate_label"] = got[0], "až " + got[1]
                offer["status"] = "live"
                offer["as_of"] = dt.date.today().isoformat()
        except Exception as e:
            notify(f"Sazby {code}: web nedostupný — použit fallback",
                   f"{cfg.get('url')} ({e.__class__.__name__})", level="info")
    offer["news"] = _fetch_news(cfg.get("news_rss")) if live else []
    return offer


def _matrix_offer(code, cfg):
    """Nabídka pro produkt s více lhůtami (termínovaný vklad): sazba per délka."""
    fb = cfg.get("fallback", {})
    rates = {str(k): v for k, v in (fb.get("rates") or {}).items()}
    return {
        "code": code, "name": cfg.get("name", code.upper()),
        "short": cfg.get("short", code.upper()[:4]),
        "accent": cfg.get("accent", ACCENTS.get(code, "#334155")),
        "url": cfg.get("url"), "rates": rates,
        "conditions": fb.get("conditions", ""), "promo": fb.get("promo", ""),
        "as_of": fb.get("as_of"), "news": [], "status": "fallback",
    }


def snapshot(product, config_dir=None, live=False, notify=default_notify):
    """Sestaví snapshot nabídek. live=False -> jen z configu (bez sítě).
    Produkt s klíčem `terms` = maticový (banka × délka), jinak tabulka (jedna sazba)."""
    config_dir = Path(config_dir or (ROOT / "config"))
    products = _load_products(config_dir)
    if product not in products:
        raise ValueError(f"neznámý produkt: {product}")
    p = products[product]
    base = {
        "product": product, "label": p.get("label_cs", product), "unit": p.get("unit", "percent"),
        "note": p.get("note", ""), "updated_at": dt.datetime.now().isoformat(timespec="seconds"),
    }
    if p.get("terms"):   # maticový produkt (termínovaný vklad)
        banks = [_matrix_offer(code, bcfg) for code, bcfg in p["banks"].items()]
        banks.sort(key=lambda b: -max([v for v in b["rates"].values() if v is not None], default=0))
        return {**base, "kind": "matrix", "terms": p["terms"],
                "term_labels": p.get("term_labels", [f"{t}M" for t in p["terms"]]), "banks": banks}
    banks = [_bank_offer(code, bcfg, live=live, notify=notify) for code, bcfg in p["banks"].items()]
    banks.sort(key=lambda b: (b["rate"] is None, -(b["rate"] or 0)))   # nejvyšší sazba nahoře
    return {**base, "kind": "table", "banks": banks}


def refresh(product, config_dir=None, out=DEFAULT_OUT, notify=default_notify):
    snap = snapshot(product, config_dir=config_dir, live=True, notify=notify)
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    Path(out).write_text(json.dumps(snap, ensure_ascii=False, indent=2))
    live = sum(1 for b in snap["banks"] if b["status"] == "live")
    print(f"Sazby {product}: {len(snap['banks'])} bank ({live} live, {len(snap['banks']) - live} fallback) -> {out}")
    return snap


def main():
    ap = argparse.ArgumentParser(description="Sběr produktových nabídek (sazby/promo/news).")
    ap.add_argument("--product", default="savings_account")
    ap.add_argument("--out", default=str(DEFAULT_OUT))
    args = ap.parse_args()
    refresh(args.product, out=args.out)


if __name__ == "__main__":
    main()
