"""Daily update - run every day at 11:00 CET via cron (see README).

Steps:
 (a) re-ingest all games from yesterday AND the day before (safety net for
     late/suspended West Coast games),
 (b) download today's schedule incl. announced probable pitchers,
 (c) refresh Statcast data for yesterday,
 (d) run quality checks and rebuild the feature tables.

Logging goes to logs/daily_YYYY-MM-DD.log. Each game is committed in its own
transaction, so an API outage mid-run never leaves half-written games; simply
re-run the script (all writes are idempotent upserts).
"""
from __future__ import annotations

import argparse
import datetime
import logging
import sys

from sqlalchemy.orm import Session

from . import features, quality_checks
from .log_setup import setup_logging
from .mlb_api import MlbApi, MlbApiError
from .backfill import ingest_game_feed, ingest_schedule_row
from .parsers import map_status
from .schema import DEFAULT_DB_PATH, create_all, get_engine

log = logging.getLogger("daily")


def refresh_date(session: Session, api: MlbApi, date: datetime.date) -> dict:
    """(a)/(b): upsert all games of one date; boxscores for finished ones."""
    stats = {"final": 0, "other": 0}
    schedule = api.schedule(date=date.isoformat(), hydrate="probablePitcher")
    log.info("%s: %d zápasů v rozpisu.", date, len(schedule))
    for sched_game in schedule:
        status = map_status(sched_game.get("status", {}))
        if status == "final":
            ingest_game_feed(session, api, sched_game["gamePk"])
            stats["final"] += 1
        else:
            ingest_schedule_row(session, api, sched_game)
            stats["other"] += 1
        session.commit()
    return stats


def main() -> int:
    parser = argparse.ArgumentParser(description="Denní aktualizace MLB dat.")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--date", default=None,
                        help="referenční 'dnešek' YYYY-MM-DD (default: dnes UTC)")
    parser.add_argument("--skip-statcast", action="store_true")
    args = parser.parse_args()

    today = (datetime.date.fromisoformat(args.date) if args.date
             else datetime.datetime.now(datetime.timezone.utc).date())
    setup_logging(f"daily_{today.isoformat()}.log")
    log.info("=== Denní update, referenční den %s ===", today)

    engine = get_engine(args.db)
    create_all(engine)
    api = MlbApi()

    try:
        with Session(engine) as session:
            # (a) finalize yesterday + the day before
            for delta in (2, 1):
                d = today - datetime.timedelta(days=delta)
                stats = refresh_date(session, api, d)
                log.info("%s hotovo: %d finálních, %d ostatních.",
                         d, stats["final"], stats["other"])
            # (b) today's slate with probable pitchers
            stats = refresh_date(session, api, today)
            log.info("Dnešní rozpis uložen: %d zápasů.", sum(stats.values()))
    except MlbApiError as err:
        log.error("%s", err)
        log.error("Databáze zůstala konzistentní (poslední commit po celém zápase). "
                  "Po obnovení spojení spusť skript znovu.")
        return 2

    # (c) Statcast for yesterday
    if not args.skip_statcast:
        try:
            from .statcast import update_statcast_for_date
            update_statcast_for_date(args.db, today - datetime.timedelta(days=1))
        except Exception as err:  # Savant outage must not kill the core update
            log.error("Statcast update selhal (%s) - pokračuji bez něj, "
                      "doplní se při příštím běhu.", err)

    # (d) features + quality checks
    features.rebuild_all(args.db)
    rc = quality_checks.run_checks(args.db)
    log.info("=== Denní update dokončen (quality checks: %s) ===",
             "OK" if rc == 0 else "SELHALY")
    return rc


if __name__ == "__main__":
    sys.exit(main())
