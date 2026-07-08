"""Feature layer for the model (phase 2 = XGBoost on top of these tables).

Builds materialized feature tables, fully recomputed on each run
(python -m src.features):

- v_pitcher_form     one row per (game_pk, pitcher) = starter form ENTERING the game
- v_team_offense     one row per (game_pk, team)    = offense form entering the game
- v_bullpen_fatigue  one row per (game_pk, team)    = bullpen usage in prior 1/2/3 days
- v_game_features    one row per game               = the model-ready join + targets

NO DATA LEAKAGE: every helper receives only rows strictly BEFORE the game
being described (earlier date, or same date with an earlier game_pk for
doubleheaders). The same helpers also serve scheduled (future) games, where
"prior" is simply everything known so far.
"""
from __future__ import annotations

import argparse
import datetime
import logging
from collections import defaultdict

import pandas as pd
from sqlalchemy import text

from .log_setup import setup_logging
from .schema import DEFAULT_DB_PATH, get_engine

log = logging.getLogger("features")

# xFIP = (13 * expected_HR + 3*BB - 2*K) / IP + constant
# expected_HR = fly_balls * league HR/FB rate. We approximate fly balls as
# airOuts + HR (documented approximation - no batted-ball type in boxscore).
LEAGUE_HR_PER_FB = 0.105
XFIP_CONSTANT = 3.10

FEATURE_TABLES = ("v_pitcher_form", "v_team_offense", "v_bullpen_fatigue", "v_game_features")


# ---------------------------------------------------------------------------
# generic helpers
# ---------------------------------------------------------------------------

def _safe_div(a, b):
    return round(a / b, 4) if b else None


def _order_key(df: pd.DataFrame) -> pd.DataFrame:
    """Chronological sort that keeps doubleheaders deterministic."""
    return df.sort_values(["game_date", "game_pk"]).reset_index(drop=True)


def _prior(df: pd.DataFrame, game_date, game_pk) -> pd.DataFrame:
    """Rows strictly before the given game (the anti-leakage filter)."""
    return df[(df["game_date"] < game_date)
              | ((df["game_date"] == game_date) & (df["game_pk"] < game_pk))]


# ---------------------------------------------------------------------------
# pitcher form
# ---------------------------------------------------------------------------

_PITCHER_SUM_COLS = ["outs_recorded", "strikeouts", "walks", "home_runs",
                     "fly_outs", "pitches_thrown"]
_PITCHER_MEAN_COLS = ["avg_velocity_fastball", "whiff_rate", "csw_rate"]


def _pitcher_window_stats(window: pd.DataFrame, suffix: str) -> dict:
    """K/9, BB/9, HR/9, xFIP, velo, whiff, CSW, pitches/start over a set of starts."""
    out = {f"n_starts_{suffix}": len(window)}
    if window.empty:
        for col in ("k9", "bb9", "hr9", "xfip", "pitches_per_start",
                    "velo", "whiff", "csw"):
            out[f"{col}_{suffix}"] = None
        return out
    s = window[_PITCHER_SUM_COLS].sum(min_count=1)
    outs = s["outs_recorded"] or 0
    ip = outs / 3.0
    out[f"k9_{suffix}"] = _safe_div(9 * s["strikeouts"], ip)
    out[f"bb9_{suffix}"] = _safe_div(9 * s["walks"], ip)
    out[f"hr9_{suffix}"] = _safe_div(9 * s["home_runs"], ip)
    fly_balls = (s["fly_outs"] or 0) + (s["home_runs"] or 0)
    out[f"xfip_{suffix}"] = (
        round((13 * fly_balls * LEAGUE_HR_PER_FB + 3 * (s["walks"] or 0)
               - 2 * (s["strikeouts"] or 0)) / ip + XFIP_CONSTANT, 3)
        if ip else None
    )
    out[f"pitches_per_start_{suffix}"] = _safe_div(s["pitches_thrown"], len(window))
    means = window[_PITCHER_MEAN_COLS].mean()
    out[f"velo_{suffix}"] = round(means["avg_velocity_fastball"], 2) \
        if pd.notna(means["avg_velocity_fastball"]) else None
    out[f"whiff_{suffix}"] = round(means["whiff_rate"], 4) \
        if pd.notna(means["whiff_rate"]) else None
    out[f"csw_{suffix}"] = round(means["csw_rate"], 4) \
        if pd.notna(means["csw_rate"]) else None
    return out


def pitcher_form_from_prior(prior_starts: pd.DataFrame, season: int) -> dict:
    """Form entering a game, given ALL of the pitcher's prior starts."""
    feats: dict = {}
    feats.update(_pitcher_window_stats(prior_starts.tail(5), "l5"))
    feats.update(_pitcher_window_stats(prior_starts.tail(10), "l10"))
    feats.update(_pitcher_window_stats(
        prior_starts[prior_starts["season"] == season], "season"))
    return feats


def _load_starts(engine) -> pd.DataFrame:
    q = """
        SELECT ps.*, g.game_date, g.season, g.game_type,
               sc.avg_velocity_fastball, sc.whiff_rate, sc.csw_rate
        FROM pitcher_starts ps
        JOIN games g ON g.game_pk = ps.game_pk
        LEFT JOIN pitcher_starts_statcast sc
               ON sc.game_pk = ps.game_pk AND sc.pitcher_id = ps.pitcher_id
    """
    df = pd.read_sql(q, engine, parse_dates=["game_date"])
    df["game_date"] = df["game_date"].dt.date
    return df


def build_pitcher_form(starts: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for pitcher_id, grp in starts.groupby("pitcher_id"):
        grp = _order_key(grp)
        for i, start in grp.iterrows():
            feats = pitcher_form_from_prior(grp.iloc[:i], start["season"])
            rows.append({
                "game_pk": start["game_pk"], "pitcher_id": pitcher_id,
                "game_date": start["game_date"], **feats,
            })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# team offense
# ---------------------------------------------------------------------------

def team_offense_from_prior(prior_games: pd.DataFrame) -> dict:
    last15, last30 = prior_games.tail(15), prior_games.tail(30)
    pa30 = (last30["at_bats"].sum() or 0) + (last30["walks"].sum() or 0)
    vs_l = last30[last30["opposing_starter_throws"] == "L"]
    vs_r = last30[last30["opposing_starter_throws"] == "R"]
    return {
        "rpg_l15": _safe_div(last15["runs"].sum(), len(last15)),
        "rpg_l30": _safe_div(last30["runs"].sum(), len(last30)),
        "k_pct_l30": _safe_div(last30["strikeouts"].sum(), pa30),
        "bb_pct_l30": _safe_div(last30["walks"].sum(), pa30),
        "rpg_vs_lhp_l30": _safe_div(vs_l["runs"].sum(), len(vs_l)),
        "rpg_vs_rhp_l30": _safe_div(vs_r["runs"].sum(), len(vs_r)),
        "n_games_l30": len(last30),
    }


def _load_team_games(engine) -> pd.DataFrame:
    q = """
        SELECT tb.*, g.game_date, g.season, g.game_type
        FROM team_game_batting tb
        JOIN games g ON g.game_pk = tb.game_pk
    """
    df = pd.read_sql(q, engine, parse_dates=["game_date"])
    df["game_date"] = df["game_date"].dt.date
    return df


def build_team_offense(team_games: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for team_id, grp in team_games.groupby("team_id"):
        grp = _order_key(grp)
        for i, game in grp.iterrows():
            rows.append({
                "game_pk": game["game_pk"], "team_id": team_id,
                "game_date": game["game_date"],
                **team_offense_from_prior(grp.iloc[:i]),
            })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# bullpen fatigue
# ---------------------------------------------------------------------------

def _bullpen_daily(engine) -> tuple[dict, dict]:
    """(team, date) -> total bullpen pitches; (team, date) -> set of reliever ids."""
    df = pd.read_sql(
        "SELECT team_id, game_date, pitcher_id, pitches_thrown FROM bullpen_appearances",
        engine, parse_dates=["game_date"])
    df["game_date"] = df["game_date"].dt.date
    pitches: dict = defaultdict(int)
    who: dict = defaultdict(set)
    for r in df.itertuples(index=False):
        pitches[(r.team_id, r.game_date)] += int(r.pitches_thrown or 0)
        who[(r.team_id, r.game_date)].add(r.pitcher_id)
    return dict(pitches), dict(who)


def bullpen_fatigue_for(team_id: int, game_date: datetime.date,
                        pitches: dict, who: dict) -> dict:
    days = [game_date - datetime.timedelta(days=d) for d in (1, 2, 3)]
    p = [pitches.get((team_id, d), 0) for d in days]
    b2b = len(who.get((team_id, days[0]), set()) & who.get((team_id, days[1]), set()))
    return {
        "bp_pitches_d1": p[0],
        "bp_pitches_d2": p[0] + p[1],
        "bp_pitches_d3": p[0] + p[1] + p[2],
        "bp_relievers_b2b": b2b,
    }


def build_bullpen_fatigue(engine, games: pd.DataFrame) -> pd.DataFrame:
    pitches, who = _bullpen_daily(engine)
    rows = []
    for g in games.itertuples(index=False):
        for team_id in (g.home_team_id, g.away_team_id):
            rows.append({
                "game_pk": g.game_pk, "team_id": team_id, "game_date": g.game_date,
                **bullpen_fatigue_for(team_id, g.game_date, pitches, who),
            })
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# final join: v_game_features
# ---------------------------------------------------------------------------

def _rest_days_lookup(games: pd.DataFrame) -> dict:
    """(game_pk, team_id) -> days since the team's previous game."""
    long = pd.concat([
        games.rename(columns={"home_team_id": "team_id"})[["game_pk", "team_id", "game_date"]],
        games.rename(columns={"away_team_id": "team_id"})[["game_pk", "team_id", "game_date"]],
    ])
    out: dict = {}
    for team_id, grp in long.groupby("team_id"):
        grp = _order_key(grp)
        prev_date = None
        for r in grp.itertuples(index=False):
            out[(r.game_pk, team_id)] = (r.game_date - prev_date).days \
                if prev_date is not None else None
            prev_date = r.game_date
    return out


def build_game_features(engine) -> pd.DataFrame:
    games = pd.read_sql("""
        SELECT g.*, v.park_factor_runs, v.park_factor_hr, v.roof_type, v.elevation
        FROM games g LEFT JOIN venues v ON v.venue_id = g.venue_id
        WHERE g.status IN ('final', 'scheduled', 'live')
    """, engine, parse_dates=["game_date"])
    games["game_date"] = games["game_date"].dt.date
    games = _order_key(games)

    starts = _load_starts(engine)
    team_games = _load_team_games(engine)
    starts_by_pitcher = {pid: _order_key(grp) for pid, grp in starts.groupby("pitcher_id")}
    games_by_team = {tid: _order_key(grp) for tid, grp in team_games.groupby("team_id")}
    starter_k = {(r.game_pk, r.pitcher_id): r.strikeouts for r in starts.itertuples(index=False)}
    pitches, who = _bullpen_daily(engine)
    rest = _rest_days_lookup(games)

    rows = []
    for g in games.itertuples(index=False):
        row = {
            "game_pk": g.game_pk, "season": g.season, "game_date": g.game_date,
            "status": g.status, "game_type": g.game_type,
            "is_covid_season": g.season == 2020,
            "home_team_id": g.home_team_id, "away_team_id": g.away_team_id,
            "venue_id": g.venue_id,
            "park_factor_runs": g.park_factor_runs, "park_factor_hr": g.park_factor_hr,
            "roof_type": g.roof_type, "elevation": g.elevation,
            "day_night": g.day_night, "temperature_f": g.temperature_f,
            "wind_speed_mph": g.wind_speed_mph, "wind_direction": g.wind_direction,
            "weather_condition": g.weather_condition,
            "home_rest_days": rest.get((g.game_pk, g.home_team_id)),
            "away_rest_days": rest.get((g.game_pk, g.away_team_id)),
            "home_starter_id": g.home_starter_id, "away_starter_id": g.away_starter_id,
        }

        for side, starter_id, team_id, opp_prefix in (
            ("home", g.home_starter_id, g.home_team_id, "hs"),
            ("away", g.away_starter_id, g.away_team_id, "as"),
        ):
            pit = starts_by_pitcher.get(starter_id)
            prior_starts = _prior(pit, g.game_date, g.game_pk) if pit is not None \
                else pd.DataFrame(columns=starts.columns)
            form = pitcher_form_from_prior(prior_starts, g.season)
            row.update({f"{opp_prefix}_{k}": v for k, v in form.items()})

            tg = games_by_team.get(team_id)
            prior_games = _prior(tg, g.game_date, g.game_pk) if tg is not None \
                else pd.DataFrame(columns=team_games.columns)
            off = team_offense_from_prior(prior_games)
            row.update({f"off_{side}_{k}": v for k, v in off.items()})

            fatigue = bullpen_fatigue_for(team_id, g.game_date, pitches, who)
            row.update({f"{side}_{k}": v for k, v in fatigue.items()})

        # targets (NULL for scheduled games)
        row["total_runs"] = g.total_runs
        row["home_runs_scored"] = g.home_score
        row["away_runs_scored"] = g.away_score
        row["home_starter_strikeouts"] = starter_k.get((g.game_pk, g.home_starter_id))
        row["away_starter_strikeouts"] = starter_k.get((g.game_pk, g.away_starter_id))
        rows.append(row)
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# orchestration
# ---------------------------------------------------------------------------

def rebuild_all(db_path=DEFAULT_DB_PATH) -> dict[str, int]:
    engine = get_engine(db_path)
    counts: dict[str, int] = {}

    log.info("Počítám v_pitcher_form ...")
    pf = build_pitcher_form(_load_starts(engine))
    pf.to_sql("v_pitcher_form", engine, if_exists="replace", index=False)
    counts["v_pitcher_form"] = len(pf)

    log.info("Počítám v_team_offense ...")
    to = build_team_offense(_load_team_games(engine))
    to.to_sql("v_team_offense", engine, if_exists="replace", index=False)
    counts["v_team_offense"] = len(to)

    log.info("Počítám v_bullpen_fatigue ...")
    games = pd.read_sql(
        "SELECT game_pk, game_date, home_team_id, away_team_id FROM games "
        "WHERE status IN ('final','scheduled','live')",
        engine, parse_dates=["game_date"])
    games["game_date"] = games["game_date"].dt.date
    bf = build_bullpen_fatigue(engine, games)
    bf.to_sql("v_bullpen_fatigue", engine, if_exists="replace", index=False)
    counts["v_bullpen_fatigue"] = len(bf)

    log.info("Počítám v_game_features ...")
    gf = build_game_features(engine)
    gf.to_sql("v_game_features", engine, if_exists="replace", index=False)
    counts["v_game_features"] = len(gf)

    with engine.connect() as conn:
        for table in FEATURE_TABLES:
            conn.execute(text(
                f"CREATE INDEX IF NOT EXISTS ix_{table}_game_pk ON {table}(game_pk)"))
        conn.commit()

    for name, n in counts.items():
        log.info("  %-20s %7d řádků", name, n)
    return counts


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Přepočet feature tabulek.")
    parser.add_argument("--db", default=str(DEFAULT_DB_PATH))
    args = parser.parse_args()
    setup_logging("features.log")
    rebuild_all(args.db)
