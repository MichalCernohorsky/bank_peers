"""Data quality report - run after every backfill and daily update.

Each check prints PASS/FAIL plus the specific offending game_pks.
Exit code 0 = everything passed, 1 = at least one failure (cron-friendly).
"""
from __future__ import annotations

import argparse
import logging
import sys

import pandas as pd
from sqlalchemy import text

from .log_setup import setup_logging
from .schema import DEFAULT_DB_PATH, get_engine

log = logging.getLogger("quality")

# expected number of REGULAR SEASON games per season (known exceptions)
EXPECTED_GAMES = {
    2019: 2429,  # one Tigers/White Sox game cancelled outright
    2020: 898,   # COVID season (60-game schedule, 2 games unplayed)
    2021: 2429,
    2022: 2430,
    2023: 2430,
    2024: 2429,  # Braves/Mets rain-out pair squeezed to one cancelled game? tolerance covers it
    2025: 2430,
}
TOLERANCE = 5  # allowed deviation from expected counts

MAX_SAMPLES = 10  # how many offending game_pks to print per check


class Report:
    def __init__(self) -> None:
        self.failures = 0

    def check(self, name: str, offenders: list, detail: str = "") -> None:
        if offenders:
            self.failures += 1
            sample = ", ".join(str(o) for o in offenders[:MAX_SAMPLES])
            more = f" (+{len(offenders) - MAX_SAMPLES} dalších)" if len(offenders) > MAX_SAMPLES else ""
            log.error("FAIL  %s: %d případů%s -> %s%s",
                      name, len(offenders), f" ({detail})" if detail else "", sample, more)
        else:
            log.info("PASS  %s", name)

    def info(self, msg: str) -> None:
        log.info("      %s", msg)


def run_checks(db_path=DEFAULT_DB_PATH, check_season_counts: bool = True) -> int:
    """check_season_counts=False for partial datasets (mid-season, test runs)."""
    engine = get_engine(db_path)
    rep = Report()

    def q(sql: str) -> pd.DataFrame:
        return pd.read_sql(text(sql), engine)

    # 1. game counts per season vs expectation (final + postponed/cancelled = schedule)
    if check_season_counts:
        counts = q("""
            SELECT season, COUNT(*) AS n_final
            FROM games WHERE game_type = 'R' AND status = 'final'
            GROUP BY season ORDER BY season
        """)
        offenders = []
        for r in counts.itertuples(index=False):
            expected = EXPECTED_GAMES.get(r.season)
            if expected is None:
                continue
            if abs(r.n_final - expected) > TOLERANCE:
                offenders.append(f"sezóna {r.season}: {r.n_final} finálních "
                                 f"(očekáváno ~{expected})")
            else:
                rep.info(f"sezóna {r.season}: {r.n_final} finálních zápasů "
                         f"(očekáváno ~{expected}) OK")
        rep.check("počet zápasů na sezónu", offenders)

    # 2. duplicates (PKs prevent most; check the logical ones)
    dup_starts = q("""
        SELECT game_pk, team_id, COUNT(*) AS n FROM pitcher_starts
        GROUP BY game_pk, team_id HAVING n > 1
    """)
    rep.check("duplicitní pitcher_start (zápas+tým)", dup_starts["game_pk"].tolist())

    # 3. final games with NULL score
    null_scores = q("""
        SELECT game_pk FROM games
        WHERE status = 'final' AND (home_score IS NULL OR away_score IS NULL
                                    OR total_runs IS NULL)
    """)
    rep.check("finální zápasy s NULL skóre", null_scores["game_pk"].tolist())

    # 4. every final game has both starters + boxscore rows
    missing_starters = q("""
        SELECT game_pk FROM games
        WHERE status = 'final'
          AND (home_starter_id IS NULL OR away_starter_id IS NULL)
    """)
    rep.check("finální zápasy bez obou startérů", missing_starters["game_pk"].tolist())

    missing_box = q("""
        SELECT g.game_pk,
               (SELECT COUNT(*) FROM pitcher_starts ps WHERE ps.game_pk = g.game_pk) AS n_starts,
               (SELECT COUNT(*) FROM team_game_batting tb WHERE tb.game_pk = g.game_pk) AS n_bat
        FROM games g WHERE g.status = 'final'
    """)
    bad_box = missing_box[(missing_box["n_starts"] != 2) | (missing_box["n_bat"] != 2)]
    rep.check("finální zápasy bez kompletního boxscore (2 startéři + 2 batting řádky)",
              bad_box["game_pk"].tolist())

    # 5. team_game_batting runs match the game score
    score_mismatch = q("""
        SELECT g.game_pk FROM games g
        JOIN team_game_batting hb ON hb.game_pk = g.game_pk AND hb.team_id = g.home_team_id
        JOIN team_game_batting ab ON ab.game_pk = g.game_pk AND ab.team_id = g.away_team_id
        WHERE g.status = 'final'
          AND (hb.runs != g.home_score OR ab.runs != g.away_score)
    """)
    rep.check("nesoulad runs v team_game_batting vs. skóre v games",
              score_mismatch["game_pk"].tolist())

    # 6. value ranges make sense
    bad_ip = q("""
        SELECT game_pk FROM pitcher_starts
        WHERE innings_pitched < 0 OR innings_pitched > 11
    """)
    rep.check("startér s IP mimo rozsah 0-11", bad_ip["game_pk"].tolist())

    bad_velo = q("""
        SELECT game_pk FROM pitcher_starts_statcast
        WHERE avg_velocity_fastball IS NOT NULL
          AND (avg_velocity_fastball < 85 OR avg_velocity_fastball > 105)
    """)
    rep.check("rychlost fastballu mimo 85-105 mph", bad_velo["game_pk"].tolist())

    bad_totals = q("""
        SELECT game_pk FROM games
        WHERE status = 'final' AND (total_runs < 0 OR total_runs > 50
                                    OR total_runs != home_score + away_score)
    """)
    rep.check("total_runs mimo rozsah nebo != součet skóre", bad_totals["game_pk"].tolist())

    bad_temp = q("""
        SELECT game_pk FROM games
        WHERE temperature_f IS NOT NULL AND (temperature_f < -10 OR temperature_f > 120)
    """)
    rep.check("teplota mimo rozsah -10..120 F", bad_temp["game_pk"].tolist())

    # 7. statcast pitch counts roughly match the boxscore (when both exist)
    pitch_mismatch = q("""
        SELECT ps.game_pk FROM pitcher_starts ps
        JOIN pitcher_starts_statcast sc
          ON sc.game_pk = ps.game_pk AND sc.pitcher_id = ps.pitcher_id
        WHERE ps.pitches_thrown IS NOT NULL AND sc.pitch_count IS NOT NULL
          AND ABS(ps.pitches_thrown - sc.pitch_count) > 5
    """)
    rep.check("Statcast pitch_count vs. boxscore (tolerance 5)",
              pitch_mismatch["game_pk"].tolist())

    if rep.failures:
        log.error("Celkem %d kontrol selhalo.", rep.failures)
        return 1
    log.info("Všechny kontroly prošly.")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Kontroly kvality dat.")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    parser.add_argument("--skip-season-counts", action="store_true",
                        help="nekontrolovat počty zápasů (částečná data)")
    args = parser.parse_args()
    setup_logging("quality_checks.log")
    sys.exit(run_checks(args.db, check_season_counts=not args.skip_season_counts))
