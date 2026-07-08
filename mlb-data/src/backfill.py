"""One-off historical backfill 2019-2025.

Usage:
    python -m src.backfill                     # all seasons 2019-2025
    python -m src.backfill --seasons 2024      # single season
    python -m src.backfill --limit 50          # quick test run
    python -m src.backfill --skip-statcast     # MLB Stats API only
    python -m src.backfill --only-reference    # refresh teams/venues/park factors

The script is resumable: games whose boxscore is already stored are skipped,
so after an interruption simply run it again and it continues where it left
off. Progress is logged as "sezóna 2023: 1450/2430 zápasů".
"""
from __future__ import annotations

import argparse
import logging
from collections import Counter

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from . import park_factors
from .log_setup import setup_logging
from .mlb_api import MlbApi
from .parsers import (
    parse_game_feed,
    parse_person,
    parse_schedule_game,
    parse_team,
    parse_venue,
)
from .schema import (
    DEFAULT_DB_PATH,
    BullpenAppearance,
    Game,
    Pitcher,
    PitcherStart,
    Team,
    TeamGameBatting,
    Venue,
    create_all,
    get_engine,
    upsert,
)

log = logging.getLogger("backfill")

SEASONS = list(range(2019, 2026))
# R = regular season, F/D/L/W = playoff rounds (stored but flagged via game_type)
GAME_TYPES = "R,F,D,L,W"
COMMIT_EVERY = 20  # games per transaction -> resumable without half-written games


# ---------------------------------------------------------------------------
# reference data: teams, venues, park factors
# ---------------------------------------------------------------------------

def ingest_reference_data(session: Session, api: MlbApi, seasons: list[int]) -> None:
    log.info("Stahuji referenční data (týmy, stadiony, park factors)...")
    teams_by_id: dict[int, dict] = {}
    for season in seasons:
        for t in api.teams(season):
            teams_by_id[t["id"]] = parse_team(t)
    venue_ids = sorted({t["venue_id"] for t in teams_by_id.values() if t["venue_id"]})
    venues = [parse_venue(v) for v in api.venues(venue_ids)]
    for v in venues:
        v["park_factor_runs"], v["park_factor_hr"] = park_factors.lookup(v["name"])

    upsert(session, Venue, venues, ["venue_id"])
    upsert(session, Team, list(teams_by_id.values()), ["team_id"])
    session.commit()
    log.info("Uloženo %d týmů a %d stadionů.", len(teams_by_id), len(venues))


def ensure_venue_stub(session: Session, venue_id: int | None, name: str = "") -> None:
    """Games occasionally take place at venues outside team home parks
    (London, Mexico City, Field of Dreams...) - store a stub row so FK holds."""
    if venue_id is None:
        return
    if session.get(Venue, venue_id) is None:
        pf_runs, pf_hr = park_factors.lookup(name or None)
        upsert(session, Venue, [{
            "venue_id": venue_id, "name": name or f"venue {venue_id}",
            "park_factor_runs": pf_runs, "park_factor_hr": pf_hr,
        }], ["venue_id"])


# ---------------------------------------------------------------------------
# per-game ingest
# ---------------------------------------------------------------------------

def ingest_game_feed(session: Session, api: MlbApi, game_pk: int) -> str:
    """Fetch feed/live for one game and upsert all derived rows.

    Returns the parsed game status.
    """
    feed = api.game_feed_live(game_pk)
    parsed = parse_game_feed(feed)
    game_row = parsed["game"]
    ensure_venue_stub(session, game_row["venue_id"],
                      (feed["gameData"].get("venue") or {}).get("name", ""))
    upsert(session, Pitcher, parsed["pitchers"], ["pitcher_id"])
    upsert(session, Game, [game_row], ["game_pk"])
    upsert(session, PitcherStart, parsed["pitcher_starts"], ["game_pk", "pitcher_id"])
    upsert(session, TeamGameBatting, parsed["team_game_batting"], ["game_pk", "team_id"])
    upsert(session, BullpenAppearance, parsed["bullpen_appearances"], ["game_pk", "pitcher_id"])
    return game_row["status"]


def ingest_schedule_row(session: Session, api: MlbApi, sched_game: dict) -> None:
    """Store a game that has no boxscore (postponed/cancelled/scheduled)."""
    row = parse_schedule_game(sched_game)
    ensure_venue_stub(session, row["venue_id"], (sched_game.get("venue") or {}).get("name", ""))
    probable_ids = [pid for pid in (row["home_starter_id"], row["away_starter_id"]) if pid]
    missing = [pid for pid in probable_ids if session.get(Pitcher, pid) is None]
    if missing:
        upsert(session, Pitcher, [parse_person(p) for p in api.people(missing)], ["pitcher_id"])
    upsert(session, Game, [row], ["game_pk"])


# ---------------------------------------------------------------------------
# season loop
# ---------------------------------------------------------------------------

def backfill_season(session: Session, api: MlbApi, season: int,
                    limit: int | None = None) -> Counter:
    schedule = api.schedule(season=season, game_types=GAME_TYPES)
    # deduplicate: a postponed game appears under several dates with one game_pk
    seen: dict[int, dict] = {g["gamePk"]: g for g in schedule}
    schedule = sorted(seen.values(), key=lambda g: (g["officialDate"], g["gamePk"]))
    if limit:
        schedule = schedule[:limit]

    already_done = set(session.scalars(
        select(Game.game_pk).where(Game.season == season, Game.boxscore_ingested.is_(True))
    ))
    log.info("Sezóna %d: %d zápasů v rozpisu, %d už hotovo.",
             season, len(schedule), len(already_done))

    stats: Counter = Counter()
    total = len(schedule)
    for i, sched_game in enumerate(schedule, start=1):
        game_pk = sched_game["gamePk"]
        if game_pk in already_done:
            stats["skipped"] += 1
        else:
            status = parse_schedule_game(sched_game)["status"]
            if status == "final":
                status = ingest_game_feed(session, api, game_pk)
            else:
                ingest_schedule_row(session, api, sched_game)
            stats[status] += 1
        if i % COMMIT_EVERY == 0:
            session.commit()
        if i % 100 == 0 or i == total:
            log.info("sezóna %d: %d/%d zápasů", season, i, total)
    session.commit()
    return stats


# ---------------------------------------------------------------------------
# summary
# ---------------------------------------------------------------------------

def print_summary(session: Session) -> None:
    log.info("=== Souhrn databáze ===")
    per_season = session.execute(
        select(Game.season, Game.game_type, func.count()).group_by(Game.season, Game.game_type)
    ).all()
    for season, game_type, n in sorted(per_season):
        label = "regular" if game_type == "R" else f"playoff ({game_type})"
        log.info("  games %d %-12s %5d", season, label, n)
    for model in (PitcherStart, TeamGameBatting, BullpenAppearance, Pitcher, Team, Venue):
        n = session.scalar(select(func.count()).select_from(model))
        log.info("  %-22s %7d řádků", model.__tablename__, n)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def parse_seasons(arg: str) -> list[int]:
    if "-" in arg:
        a, b = arg.split("-")
        return list(range(int(a), int(b) + 1))
    return [int(s) for s in arg.split(",")]


def main() -> None:
    parser = argparse.ArgumentParser(description="Backfill historických MLB dat.")
    parser.add_argument("--seasons", default="2019-2025",
                        help="např. 2024 nebo 2019-2025 nebo 2019,2021")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--limit", type=int, default=None,
                        help="jen prvních N zápasů sezóny (rychlý test)")
    parser.add_argument("--skip-statcast", action="store_true")
    parser.add_argument("--only-reference", action="store_true",
                        help="jen obnov týmy/stadiony/park factors a skonči")
    args = parser.parse_args()

    setup_logging("backfill.log")
    seasons = parse_seasons(args.seasons)
    engine = get_engine(args.db)
    create_all(engine)
    api = MlbApi()

    with Session(engine) as session:
        ingest_reference_data(session, api, seasons)
        if args.only_reference:
            return
        for season in seasons:
            stats = backfill_season(session, api, season, limit=args.limit)
            log.info("Sezóna %d hotová: %s", season, dict(stats))
            if season == 2020:
                log.info("Pozn.: sezóna 2020 je zkrácená (COVID, 60 zápasů) — "
                         "pro trénink modelu ji možná vyloučíme filtrem season != 2020.")
        print_summary(session)

    if not args.skip_statcast:
        from .statcast import backfill_statcast
        backfill_statcast(args.db, seasons)

    log.info("Backfill dokončen. Spusť kontrolu: python -m src.quality_checks --db %s", args.db)


if __name__ == "__main__":
    main()
