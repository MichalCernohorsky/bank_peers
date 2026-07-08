"""Statcast enrichment via pybaseball (pitch-level data -> per-start metrics).

Downloads month by month with pauses (Baseball Savant rate limits) and caches
raw monthly extracts in data/statcast_cache/, so re-runs do not re-download.

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
import logging
import time
from pathlib import Path

import pandas as pd
from sqlalchemy import select
from sqlalchemy.orm import Session

from .schema import PitcherStart, PitcherStartStatcast, get_engine, upsert

log = logging.getLogger("statcast")

CACHE_DIR = Path(__file__).resolve().parent.parent / "data" / "statcast_cache"
PAUSE_BETWEEN_MONTHS_S = 20

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

def _fetch_range(start: datetime.date, end: datetime.date) -> pd.DataFrame:
    """Download one date range from Baseball Savant, cached on disk."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file = CACHE_DIR / f"statcast_{start:%Y-%m-%d}_{end:%Y-%m-%d}.csv.gz"
    if cache_file.exists():
        log.info("Cache hit: %s", cache_file.name)
        return pd.read_csv(cache_file, compression="gzip", low_memory=False)

    from pybaseball import statcast  # lazy import - heavy dependency

    log.info("Stahuji Statcast %s až %s ...", start, end)
    df = statcast(start_dt=str(start), end_dt=str(end), verbose=False)
    if df is None:
        df = pd.DataFrame()
    df.to_csv(cache_file, index=False, compression="gzip")
    log.info("Staženo %d nadhozů, uloženo do %s", len(df), cache_file.name)
    return df


def _season_months(season: int) -> list[tuple[datetime.date, datetime.date]]:
    """Month windows covering the season (2020 started in July)."""
    first_month = 7 if season == 2020 else 3
    ranges = []
    for month in range(first_month, 12):
        start = datetime.date(season, month, 1)
        end = (datetime.date(season, month + 1, 1) - datetime.timedelta(days=1)
               if month < 12 else datetime.date(season, 12, 31))
        ranges.append((start, end))
    return ranges


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
            total = 0
            for start, end in _season_months(season):
                df = _fetch_range(start, end)
                if df.empty:
                    continue
                total += _store_aggregates(session, aggregate_pitcher_games(df))
                time.sleep(PAUSE_BETWEEN_MONTHS_S)
            log.info("Statcast sezóna %d: uloženo %d řádků pro startéry.", season, total)


def update_statcast_for_date(db_path, date: datetime.date) -> int:
    """Daily refresh: yesterday's pitches -> pitcher_starts_statcast."""
    engine = get_engine(db_path)
    df = _fetch_range(date, date)
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
