"""Deterministic synthetic mini-league used by tests and the offline demo.

4 teams, ~2 months of a 2024 season, 3-man rotations, 3-man bullpens.
Numbers are drawn from a seeded RNG so tests are reproducible, and all
cross-table identities hold (batting runs == game score, etc.).
"""
from __future__ import annotations

import datetime
import random

from sqlalchemy.orm import Session

from src.schema import (
    BullpenAppearance,
    Game,
    Pitcher,
    PitcherStart,
    PitcherStartStatcast,
    Team,
    TeamGameBatting,
    Venue,
    create_all,
    get_engine,
    upsert,
)

TEAMS = [
    (101, "Test Bears", "BEA", 11),
    (102, "Test Wolves", "WOL", 12),
    (103, "Test Eagles", "EAG", 13),
    (104, "Test Sharks", "SHA", 14),
]
START_DATE = datetime.date(2024, 4, 1)
N_DAYS = 60


def build_synthetic_db(db_path) -> None:
    rng = random.Random(42)
    engine = get_engine(db_path)
    create_all(engine)

    venues = [{"venue_id": vid, "name": f"{name} Park", "city": name.split()[1],
               "roof_type": "open", "elevation": 500 + 100 * i,
               "park_factor_runs": 95 + 3 * i, "park_factor_hr": 98 + i}
              for i, (tid, name, abbr, vid) in enumerate(TEAMS)]
    teams = [{"team_id": tid, "name": name, "abbreviation": abbr,
              "league": "Test League", "division": "Test Division", "venue_id": vid}
             for tid, name, abbr, vid in TEAMS]

    pitchers, rotations, bullpens = [], {}, {}
    pid = 900000
    for tid, name, _, _ in TEAMS:
        rotations[tid], bullpens[tid] = [], []
        for j in range(3):
            pid += 1
            pitchers.append({"pitcher_id": pid, "full_name": f"{name} Starter {j+1}",
                             "throws": "L" if (pid % 3 == 0) else "R",
                             "birth_date": datetime.date(1995, 1, 1)})
            rotations[tid].append(pid)
        for j in range(3):
            pid += 1
            pitchers.append({"pitcher_id": pid, "full_name": f"{name} Reliever {j+1}",
                             "throws": "R", "birth_date": datetime.date(1996, 1, 1)})
            bullpens[tid].append(pid)

    throws = {p["pitcher_id"]: p["throws"] for p in pitchers}
    games, starts, batting, bullpen_rows, statcast_rows = [], [], [], [], []
    game_pk = 700000
    rotation_idx = {tid: 0 for tid, *_ in TEAMS}

    for day in range(N_DAYS):
        date = START_DATE + datetime.timedelta(days=day)
        if day % 7 == 6:
            continue  # league-wide off day
        # two games a day: (A vs B), (C vs D) with rotating home teams
        pairs = [(TEAMS[day % 2][0], TEAMS[(day + 1) % 2][0]),
                 (TEAMS[2 + day % 2][0], TEAMS[2 + (day + 1) % 2][0])]
        for home_id, away_id in pairs:
            game_pk += 1
            home_venue = next(t[3] for t in TEAMS if t[0] == home_id)
            home_score = rng.randint(0, 9)
            away_score = rng.randint(0, 9)
            starters = {}
            for side_team, opp_team, is_home, runs_allowed in (
                (home_id, away_id, True, away_score),
                (away_id, home_id, False, home_score),
            ):
                sid = rotations[side_team][rotation_idx[side_team] % 3]
                starters[side_team] = sid
                outs = rng.randint(12, 21)
                ks = rng.randint(2, 11)
                pitches = rng.randint(75, 110)
                starts.append({
                    "game_pk": game_pk, "pitcher_id": sid, "team_id": side_team,
                    "opponent_team_id": opp_team, "is_home": is_home,
                    "innings_pitched": round(outs / 3, 4), "outs_recorded": outs,
                    "batters_faced": outs + rng.randint(3, 9),
                    "hits": rng.randint(2, 10),
                    "runs": min(runs_allowed, rng.randint(0, 6)),
                    "earned_runs": min(runs_allowed, rng.randint(0, 5)),
                    "walks": rng.randint(0, 5), "strikeouts": ks,
                    "home_runs": rng.randint(0, 3), "pitches_thrown": pitches,
                    "strikes": int(pitches * 0.63),
                    "ground_outs": rng.randint(3, 9), "fly_outs": rng.randint(2, 8),
                })
                statcast_rows.append({
                    "game_pk": game_pk, "pitcher_id": sid,
                    "avg_velocity_fastball": round(rng.uniform(91, 99), 2),
                    "whiff_rate": round(rng.uniform(0.15, 0.40), 4),
                    "csw_rate": round(rng.uniform(0.22, 0.38), 4),
                    "xba_against": round(rng.uniform(0.180, 0.340), 4),
                    "xslg_against": round(rng.uniform(0.280, 0.560), 4),
                    "barrel_rate_against": round(rng.uniform(0.0, 0.15), 4),
                    "pitch_count": pitches,
                })
                rotation_idx[side_team] += 1
                for rel in rng.sample(bullpens[side_team], rng.randint(1, 3)):
                    bullpen_rows.append({
                        "game_pk": game_pk, "pitcher_id": rel, "team_id": side_team,
                        "game_date": date,
                        "innings_pitched": round(rng.randint(1, 6) / 3, 4),
                        "outs_recorded": rng.randint(1, 6),
                        "pitches_thrown": rng.randint(8, 35),
                        "earned_runs": rng.randint(0, 2),
                        "strikeouts": rng.randint(0, 3), "walks": rng.randint(0, 2),
                    })

            for team_id, opp_id, runs in ((home_id, away_id, home_score),
                                          (away_id, home_id, away_score)):
                ab = rng.randint(28, 38)
                batting.append({
                    "game_pk": game_pk, "team_id": team_id, "runs": runs,
                    "hits": max(runs, rng.randint(3, 12)),
                    "home_runs": min(runs, rng.randint(0, 3)),
                    "walks": rng.randint(1, 7), "strikeouts": rng.randint(4, 14),
                    "left_on_base": rng.randint(3, 11), "at_bats": ab,
                    "opposing_starter_throws": throws[starters[opp_id]],
                })

            games.append({
                "game_pk": game_pk, "season": 2024, "game_date": date,
                "game_datetime_utc": datetime.datetime(date.year, date.month, date.day, 23, 10),
                "home_team_id": home_id, "away_team_id": away_id,
                "venue_id": home_venue, "home_score": home_score,
                "away_score": away_score, "total_runs": home_score + away_score,
                "status": "final", "day_night": "night",
                "home_starter_id": starters[home_id], "away_starter_id": starters[away_id],
                "temperature_f": rng.randint(45, 95),
                "wind_speed_mph": rng.randint(0, 20), "wind_direction": "Out To CF",
                "weather_condition": "Clear", "game_type": "R",
                "game_number": 1, "double_header": "N", "boxscore_ingested": True,
            })

    with Session(engine) as session:
        upsert(session, Venue, venues, ["venue_id"])
        upsert(session, Team, teams, ["team_id"])
        upsert(session, Pitcher, pitchers, ["pitcher_id"])
        upsert(session, Game, games, ["game_pk"])
        upsert(session, PitcherStart, starts, ["game_pk", "pitcher_id"])
        upsert(session, PitcherStartStatcast, statcast_rows, ["game_pk", "pitcher_id"])
        upsert(session, TeamGameBatting, batting, ["game_pk", "team_id"])
        upsert(session, BullpenAppearance, bullpen_rows, ["game_pk", "pitcher_id"])
        session.commit()
