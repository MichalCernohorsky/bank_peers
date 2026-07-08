"""Thin client for the official MLB Stats API (free, no API key).

All network access of the pipeline goes through this module, so retry
behaviour and rate limiting live in exactly one place.
"""
from __future__ import annotations

import logging
import time

import requests

BASE_URL = "https://statsapi.mlb.com/api/v1"
BASE_URL_V11 = "https://statsapi.mlb.com/api/v1.1"

log = logging.getLogger(__name__)


class MlbApiError(RuntimeError):
    """Raised when the MLB Stats API stays unreachable after retries."""


class MlbApi:
    def __init__(self, pause_s: float = 0.15, max_retries: int = 4, timeout_s: int = 30):
        self.session = requests.Session()
        self.session.headers["User-Agent"] = "mlb-data-pipeline/1.0"
        self.pause_s = pause_s
        self.max_retries = max_retries
        self.timeout_s = timeout_s

    def _get(self, url: str, params: dict | None = None) -> dict:
        last_err: Exception | None = None
        for attempt in range(self.max_retries + 1):
            try:
                resp = self.session.get(url, params=params, timeout=self.timeout_s)
                resp.raise_for_status()
                time.sleep(self.pause_s)  # be polite to the free API
                return resp.json()
            except (requests.RequestException, ValueError) as err:
                last_err = err
                wait = 2 ** attempt
                log.warning("Požadavek %s selhal (%s), pokus %d/%d, čekám %ds",
                            url, err, attempt + 1, self.max_retries + 1, wait)
                time.sleep(wait)
        raise MlbApiError(
            f"MLB Stats API je nedostupné ({url}): {last_err}. "
            "Zkontroluj připojení k internetu a spusť skript znovu."
        )

    # ------------------------------------------------------------------
    # endpoints
    # ------------------------------------------------------------------

    def schedule(self, *, season: int | None = None, date: str | None = None,
                 game_types: str | None = None, hydrate: str | None = None) -> list[dict]:
        """Return a flat list of games from /schedule (sportId=1 = MLB)."""
        params: dict = {"sportId": 1}
        if season:
            params["season"] = season
        if date:
            params["date"] = date
        if game_types:
            params["gameTypes"] = game_types
        if hydrate:
            params["hydrate"] = hydrate
        data = self._get(f"{BASE_URL}/schedule", params)
        games = []
        for day in data.get("dates", []):
            games.extend(day.get("games", []))
        return games

    def game_feed_live(self, game_pk: int) -> dict:
        """Full game feed: gameData (weather, players, venue) + liveData (boxscore)."""
        return self._get(f"{BASE_URL_V11}/game/{game_pk}/feed/live")

    def teams(self, season: int) -> list[dict]:
        data = self._get(f"{BASE_URL}/teams", {"sportId": 1, "season": season})
        return data.get("teams", [])

    def venues(self, venue_ids: list[int]) -> list[dict]:
        if not venue_ids:
            return []
        params = {"venueIds": ",".join(str(v) for v in venue_ids),
                  "hydrate": "location,fieldInfo"}
        data = self._get(f"{BASE_URL}/venues", params)
        return data.get("venues", [])

    def people(self, person_ids: list[int]) -> list[dict]:
        if not person_ids:
            return []
        out: list[dict] = []
        # the API caps the personIds list, request in chunks of 100
        for i in range(0, len(person_ids), 100):
            chunk = person_ids[i:i + 100]
            params = {"personIds": ",".join(str(p) for p in chunk)}
            data = self._get(f"{BASE_URL}/people", params)
            out.extend(data.get("people", []))
        return out
