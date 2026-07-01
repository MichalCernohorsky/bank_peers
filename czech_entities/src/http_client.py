"""Rate-limited HTTP klient pro bulk stahování z veřejných registrů.

Principy dané SPEC:
  - explicitní rate-limiter (ARES blokuje nad ~500 req/min → default konzervativně)
  - retry s exponenciálním backoffem na síťové/5xx chyby
  - stahování velkých souborů streamem na disk (bulk dumpy mají desítky–stovky MB)
  - cache: pokud soubor už na disku je a není vynucené obnovení, nestahuj znovu
    (idempotence + resumovatelnost dle SPEC)
"""
from __future__ import annotations

import logging
import time
from pathlib import Path

import httpx
from tenacity import (
    retry,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential,
)

log = logging.getLogger("czech_entities.http")

# proxy prostředí používá vlastní CA bundle; httpx ho vezme z env (SSL_CERT_FILE),
# jinak spoléháme na systémový trust store.
DEFAULT_TIMEOUT = httpx.Timeout(60.0, connect=30.0)
DEFAULT_HEADERS = {
    "User-Agent": "czech-entities-adhoc-analysis/1.0 (open-data bulk; contact via repo)",
    "Accept-Encoding": "gzip, deflate",
}


class RateLimiter:
    """Jednoduchý blokující rate-limiter: min. rozestup mezi požadavky.

    max_per_min=300 → rozestup 0.2 s. Konzervativní vůči ARES limitu 500/min.
    """

    def __init__(self, max_per_min: int = 300):
        self.min_interval = 60.0 / max(1, max_per_min)
        self._last = 0.0

    def wait(self) -> None:
        now = time.monotonic()
        delta = now - self._last
        if delta < self.min_interval:
            time.sleep(self.min_interval - delta)
        self._last = time.monotonic()


class Downloader:
    """Klient pro stahování s cache na disku a rate-limitem."""

    def __init__(
        self,
        cache_dir: str | Path,
        max_per_min: int = 300,
        client: httpx.Client | None = None,
    ):
        self.cache_dir = Path(cache_dir)
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        self.rate = RateLimiter(max_per_min)
        self._client = client or httpx.Client(
            timeout=DEFAULT_TIMEOUT,
            headers=DEFAULT_HEADERS,
            follow_redirects=True,
        )

    def close(self) -> None:
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        self.close()

    @retry(
        retry=retry_if_exception_type(
            (httpx.TransportError, httpx.HTTPStatusError)
        ),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=2, max=60),
        reraise=True,
    )
    def _stream_to(self, url: str, dest: Path) -> None:
        self.rate.wait()
        tmp = dest.with_suffix(dest.suffix + ".part")
        with self._client.stream("GET", url) as resp:
            # 5xx a 429 chceme retryovat, 4xx (kromě 429) je trvalá chyba
            if resp.status_code == 429 or resp.status_code >= 500:
                resp.raise_for_status()
            resp.raise_for_status()
            total = 0
            with open(tmp, "wb") as fh:
                for chunk in resp.iter_bytes(chunk_size=1 << 20):
                    fh.write(chunk)
                    total += len(chunk)
        tmp.replace(dest)
        log.info("staženo %s (%.1f MB) -> %s", url, total / 1e6, dest.name)

    def fetch_file(
        self, url: str, filename: str | None = None, force: bool = False
    ) -> Path:
        """Stáhne URL do cache. Vrací cestu. Když už soubor je a not force, přeskočí."""
        name = filename or url.rstrip("/").split("/")[-1] or "download"
        dest = self.cache_dir / name
        if dest.exists() and not force and dest.stat().st_size > 0:
            log.info("cache hit: %s (přeskočeno stažení)", dest.name)
            return dest
        self._stream_to(url, dest)
        return dest

    @retry(
        retry=retry_if_exception_type(
            (httpx.TransportError, httpx.HTTPStatusError)
        ),
        stop=stop_after_attempt(5),
        wait=wait_exponential(multiplier=2, min=2, max=60),
        reraise=True,
    )
    def get_json(self, url: str, params: dict | None = None) -> dict:
        """ARES REST — jen na detaily/delty, NE na celý registr (viz SPEC)."""
        self.rate.wait()
        resp = self._client.get(url, params=params)
        if resp.status_code == 429 or resp.status_code >= 500:
            resp.raise_for_status()
        resp.raise_for_status()
        return resp.json()
