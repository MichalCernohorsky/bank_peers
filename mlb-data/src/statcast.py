"""Statcast enrichment (pitch-level data -> per-start metrics).

Downloads straight from the Baseball Savant CSV endpoint day by day - only
days that actually have final games in our DB - with retries and response
validation (Savant occasionally returns an HTML error page instead of CSV,
which is also why we don't go through pybaseball here). Raw daily extracts
are cached in data/statcast_cache/, so re-runs never re-download.

Metric definitions (documented approximations):
- avg_velocity_fastball: mean release_speed of four-seamers (FF); if a pitcher
  threw fewer than 5 FF, sinkers (SI) are included as fallback.
- whiff_rate: swinging strikes / swings.
- csw_rate: (called strikes + swinging strikes) / all pitches.
- xba_against / xslg_against: mean expected BA/SLG on batted balls
  (estimated_*_using_speedangle) - batted-ball quality, strikeouts excluded.
- barrel_rate_against: barrels (launch_speed_angle == 6) / batted balls.
"""
from __future__ import annotations

import datetime
import io
import logging
import time
from pathlib import Path

import pandas as pd
import requests
from sqlalchemy import select, text
from sqlalchemy.orm import Session

from .schema import PitcherStart, PitcherStartStatcast, get_engine, upsert

log = logging.getLogger("statcast")

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "statcast_cache"
SAVANT_CSV_URL = "https://baseballsavant.mlb.com/statcast_search/csv"
PAUSE_BETWEEN_DAYS_S = 2
MAX_RETRIES = 5

SWING_DESCRIPTIONS = {
    "swinging_strike", "swinging_strike_blocked", "foul", "foul_tip",
    "hit_into_play", "foul_bunt", "missed_bunt", "bunt_foul_tip",
}
WHIFF_DESCRIPTIONS = {"swinging_strike", "swinging_strike_blocked", "missed_bunt"}
CSW_DESCRIPTIONS = {"called_strike", "swinging_strike", "swinging_strike_blocked"}


# ---------------------------------------------------------------------------
# aggregation (pure pandas -> unit-testable without network)
# ---------------------------------------------------------------------------

def aggregate_pitcher_games(pitches: pd.DataFrame) -> pd.DataFrame:
    """Aggregate pitch-level Statcast rows to one row per (game_pk, pitcher)."""
    required = {"game_pk", "pitcher", "description"}
    missing = required - set(pitches.columns)
    if missing:
        raise ValueError(f"Statcast extrakt postrádá sloupce: {sorted(missing)}")

    df = pitches.copy()
    df["is_swing"] = df["description"].isin(SWING_DESCRIPTIONS)
    df["is_whiff"] = df["description"].isin(WHIFF_DESCRIPTIONS)
    df["is_csw"] = df["description"].isin(CSW_DESCRIPTIONS)
    df["is_bip"] = df["description"].eq("hit_into_play")
    if "launch_speed_angle" in df.columns:
        df["is_barrel"] = df["launch_speed_angle"].eq(6) & df["is_bip"]
    else:
        df["is_barrel"] = False

    rows = []
    for (game_pk, pitcher_id), grp in df.groupby(["game_pk", "pitcher"]):
        n_pitches = len(grp)
        n_swings = int(grp["is_swing"].sum())
        n_bip = int(grp["is_bip"].sum())

        ff = grp[grp.get("pitch_type", pd.Series(dtype=object)).eq("FF")]["release_speed"].dropna() \
            if "pitch_type" in grp.columns else pd.Series(dtype=float)
        if len(ff) < 5 and "pitch_type" in grp.columns:
            ff = grp[grp["pitch_type"].isin(["FF", "SI"])]["release_speed"].dropna()
        avg_velo = round(float(ff.mean()), 2) if len(ff) else None

        bip = grp[grp["is_bip"]]
        xba = bip["estimated_ba_using_speedangle"].dropna() \
            if "estimated_ba_using_speedangle" in grp.columns else pd.Series(dtype=float)
        xslg = bip["estimated_slg_using_speedangle"].dropna() \
            if "estimated_slg_using_speedangle" in grp.columns else pd.Series(dtype=float)

        rows.append({
            "game_pk": int(game_pk),
            "pitcher_id": int(pitcher_id),
            "avg_velocity_fastball": avg_velo,
            "whiff_rate": round(grp["is_whiff"].sum() / n_swings, 4) if n_swings else None,
            "csw_rate": round(grp["is_csw"].sum() / n_pitches, 4) if n_pitches else None,
            "xba_against": round(float(xba.mean()), 4) if len(xba) else None,
            "xslg_against": round(float(xslg.mean()), 4) if len(xslg) else None,
            "barrel_rate_against": round(grp["is_barrel"].sum() / n_bip, 4) if n_bip else None,
            "pitch_count": n_pitches,
        })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# download with cache
# ---------------------------------------------------------------------------

def _fetch_day(date: datetime.date) -> pd.DataFrame:
    """Download all pitches of one date from Baseball Savant, cached on disk.

    A single day is ~4-5k rows, safely under Savant's per-query row cap.
    Retries with backoff and rejects non-CSV (HTML error page) responses.
    """
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"statcast_{date:%Y-%m-%d}.csv.gz"
    if cache_file.exists():
        return pd.read_csv(cache_file, compression="gzip", low_memory=False)

    params = {
        "all": "true", "type": "details", "player_type": "pitcher",
        "game_date_gt": str(date), "game_date_lt": str(date),
    }
    last_err: Exception | None = None
    for attempt in range(MAX_RETRIES):
        try:
            resp = requests.get(SAVANT_CSV_URL, params=params, timeout=180,
                                headers={"User-Agent": "mlb-data-pipeline/1.0"})
            resp.raise_for_status()
            header = resp.text.partition("\n")[0]
            if "game_pk" not in header and "pitch_type" not in header:
                raise ValueError(f"odpověď není CSV (začíná: {resp.text[:80]!r})")
            df = pd.read_csv(io.StringIO(resp.text), low_memory=False)
            df.to_csv(cache_file, index=False, compression="gzip")
            return df
        except Exception as err:  # noqa: BLE001 - retry any fetch/parse hiccup
            last_err = err
            wait = 5 * 2 ** attempt
            log.warning("Statcast %s selhal (%s), pokus %d/%d, čekám %ds",
                        date, err, attempt + 1, MAX_RETRIES, wait)
            time.sleep(wait)
    raise RuntimeError(f"Statcast pro {date} se nepodařilo stáhnout: {last_err}")


def _season_game_dates(session: Session, season: int) -> list[datetime.date]:
    """Only days that actually have final games -> no wasted off-day requests."""
    rows = session.execute(text(
        "SELECT DISTINCT game_date FROM games "
        "WHERE season = :s AND status = 'final' ORDER BY game_date"),
        {"s": season}).scalars().all()
    return [datetime.date.fromisoformat(str(d)[:10]) for d in rows]


def _store_aggregates(session: Session, agg: pd.DataFrame) -> int:
    """Keep only rows belonging to known starts, upsert them."""
    if agg.empty:
        return 0
    start_keys = set(session.execute(
        select(PitcherStart.game_pk, PitcherStart.pitcher_id)
    ).all())
    rows = [r for r in agg.to_dict("records")
            if (r["game_pk"], r["pitcher_id"]) in start_keys]
    n = upsert(session, PitcherStartStatcast, rows, ["game_pk", "pitcher_id"])
    session.commit()
    return n


def backfill_statcast(db_path, seasons: list[int]) -> None:
    engine = get_engine(db_path)
    with Session(engine) as session:
        for season in seasons:
            dates = _season_game_dates(session, season)
            total = 0
            for i, date in enumerate(dates, start=1):
                was_cached = (CACHE_DIR / f"statcast_{date:%Y-%m-%d}.csv.gz").exists()
                df = _fetch_day(date)
                if not df.empty:
                    total += _store_aggregates(session, aggregate_pitcher_games(df))
                if i % 20 == 0 or i == len(dates):
                    log.info("Statcast sezóna %d: %d/%d dnů, %d řádků startérů",
                             season, i, len(dates), total)
                if not was_cached:
                    time.sleep(PAUSE_BETWEEN_DAYS_S)
            log.info("Statcast sezóna %d hotová: uloženo %d řádků pro startéry.",
                     season, total)


def update_statcast_for_date(db_path, date: datetime.date) -> int:
    """Daily refresh: yesterday's pitches -> pitcher_starts_statcast."""
    engine = get_engine(db_path)
    df = _fetch_day(date)
    if df.empty:
        log.info("Statcast %s: žádná data.", date)
        return 0
    with Session(engine) as session:
        n = _store_aggregates(session, aggregate_pitcher_games(df))
    log.info("Statcast %s: uloženo %d řádků.", date, n)
    return n


if __name__ == "__main__":
    import argparse

    from .log_setup import setup_logging
    from .schema import DEFAULT_DB_PATH

    parser = argparse.ArgumentParser(description="Statcast backfill.")
    parser.add_argument("--seasons", default="2019-2025")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    args = parser.parse_args()
    setup_logging("statcast.log")
    from .backfill import parse_seasons
    backfill_statcast(args.db, parse_seasons(args.seasons))
