"""
offers_browser.py — headless-browser fetch (Playwright) pro sběr sazeb v PRODUKCI.

Proč: weby bank blokují prosté HTTP (WAF, 403), ale reálný prohlížeč projde. Tento
modul načte stránku headless Chromiem a vrátí text pro extrakci. Zapíná se přes
`OFFERS_BROWSER=1` (viz pipeline.offers._fetch).

Pozn.: vyžaduje prostředí s OTEVŘENÝM outboundem k doménám bank. V tomto sandboxu je
síť k bankám blokovaná (proxy allowlist), takže tu fetch neproběhne — kód je připraven
pro produkci / samostatný fetch-worker. Chromium bývá předinstalovaný
(PLAYWRIGHT_BROWSERS_PATH); jinak: `pip install playwright && playwright install chromium`.
Respektuj robots.txt / ToS webů a nestahuj agresivně.
"""
import os
from pathlib import Path

DESKTOP_UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
              "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")


def _chrome_path():
    base = os.environ.get("PLAYWRIGHT_BROWSERS_PATH", "/opt/pw-browsers")
    for c in sorted(Path(base).glob("chromium-*/chrome-linux/chrome")):
        return str(c)
    return None   # necháme Playwright najít vlastní stažený build


def fetch_text(url, timeout=45000, proxy=None, wait_until="domcontentloaded"):
    """Načte URL headless prohlížečem a vrátí text <body>. Vyhazuje při chybě."""
    from playwright.sync_api import sync_playwright

    proxy = proxy or os.environ.get("HTTPS_PROXY")
    launch = {"headless": True, "args": ["--no-sandbox", "--disable-dev-shm-usage"]}
    cp = _chrome_path()
    if cp:
        launch["executable_path"] = cp
    if proxy:
        launch["proxy"] = {"server": proxy}

    with sync_playwright() as p:
        browser = p.chromium.launch(**launch)
        try:
            page = browser.new_page(user_agent=DESKTOP_UA, locale="cs-CZ")
            page.goto(url, wait_until=wait_until, timeout=timeout)
            return page.inner_text("body")
        finally:
            browser.close()
