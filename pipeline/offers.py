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


def _bank_names(config_dir):
    banks = yaml.safe_load((Path(config_dir) / "banks.yaml").read_text())["banks"]
    return {b["code"]: b["name"] for b in banks}


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


def _bank_offer(code, name, cfg, live=True, notify=default_notify):
    fb = cfg.get("fallback", {})
    offer = {
        "code": code, "name": name, "accent": ACCENTS.get(code, "#333"),
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


def snapshot(product, config_dir=None, live=False, notify=default_notify):
    """Sestaví snapshot nabídek. live=False -> jen z configu (bez sítě)."""
    config_dir = Path(config_dir or (ROOT / "config"))
    products = _load_products(config_dir)
    if product not in products:
        raise ValueError(f"neznámý produkt: {product}")
    p = products[product]
    names = _bank_names(config_dir)
    banks = [_bank_offer(code, names.get(code, code.upper()), bcfg, live=live, notify=notify)
             for code, bcfg in p["banks"].items()]
    banks.sort(key=lambda b: (b["rate"] is None, -(b["rate"] or 0)))   # nejvyšší sazba nahoře
    return {
        "product": product, "label": p.get("label_cs", product), "unit": p.get("unit", "percent"),
        "note": p.get("note", ""), "updated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "banks": banks,
    }


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
