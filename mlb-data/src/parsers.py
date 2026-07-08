"""Pure parsing functions: MLB feed/live JSON -> rows for our tables.

No network and no database access here, so everything is unit-testable
against JSON fixtures in tests/fixtures/.
"""
from __future__ import annotations

import datetime
import re
from typing import Any

# ---------------------------------------------------------------------------
# small helpers
# ---------------------------------------------------------------------------

def innings_to_outs(ip_str: str | None) -> int | None:
    """MLB notation '5.2' = 5 innings + 2 outs -> 17 outs."""
    if ip_str in (None, ""):
        return None
    whole, _, frac = str(ip_str).partition(".")
    outs = int(whole) * 3 + (int(frac) if frac else 0)
    return outs


def outs_to_innings(outs: int | None) -> float | None:
    """17 outs -> 5.667 (true fraction, safe to sum and divide)."""
    if outs is None:
        return None
    return round(outs / 3.0, 4)


def parse_wind(wind_str: str | None) -> tuple[int | None, str | None]:
    """'11 mph, Out To CF' -> (11, 'Out To CF'); 'Calm' -> (0, 'Calm')."""
    if not wind_str:
        return None, None
    m = re.match(r"\s*(\d+)\s*mph\s*,?\s*(.*)", wind_str)
    if m:
        return int(m.group(1)), (m.group(2).strip() or None)
    if wind_str.strip().lower() == "calm":
        return 0, "Calm"
    return None, wind_str.strip()


def parse_temperature(temp_str: str | None) -> int | None:
    if temp_str in (None, ""):
        return None
    try:
        return int(str(temp_str).strip())
    except ValueError:
        return None


_STATUS_MAP = {"final": "final", "preview": "scheduled", "live": "live"}


def map_status(status: dict) -> str:
    """Map the MLB status object to scheduled/live/final/postponed/..."""
    detailed = (status.get("detailedState") or "").lower()
    for keyword in ("postponed", "suspended", "cancelled"):
        if keyword in detailed:
            return keyword
    abstract = (status.get("abstractGameState") or "").lower()
    return _STATUS_MAP.get(abstract, abstract or "unknown")


def _parse_date(s: str | None) -> datetime.date | None:
    return datetime.date.fromisoformat(s) if s else None


def _parse_datetime_utc(s: str | None) -> datetime.datetime | None:
    if not s:
        return None
    return datetime.datetime.fromisoformat(s.replace("Z", "+00:00")).replace(tzinfo=None)


# ---------------------------------------------------------------------------
# feed/live -> rows
# ---------------------------------------------------------------------------

def parse_game_feed(feed: dict) -> dict[str, Any]:
    """Parse one /game/{pk}/feed/live payload into rows for all tables.

    Returns dict with keys: game, pitchers, pitcher_starts, team_game_batting,
    bullpen_appearances. Detail rows are only produced for final games.
    """
    game_data = feed["gameData"]
    live_data = feed.get("liveData", {})
    boxscore = live_data.get("boxscore", {})

    game_pk = feed.get("gamePk") or game_data["game"]["pk"]
    status = map_status(game_data.get("status", {}))
    game_info = game_data.get("game", {})
    teams_info = game_data.get("teams", {})
    home_id = teams_info["home"]["id"]
    away_id = teams_info["away"]["id"]

    weather = game_data.get("weather", {}) or {}
    wind_speed, wind_dir = parse_wind(weather.get("wind"))

    linescore = live_data.get("linescore", {}).get("teams", {})
    home_score = linescore.get("home", {}).get("runs")
    away_score = linescore.get("away", {}).get("runs")
    is_final = status == "final"

    game_row: dict[str, Any] = {
        "game_pk": game_pk,
        "season": int(game_info.get("season") or game_data["datetime"]["officialDate"][:4]),
        "game_date": _parse_date(game_data["datetime"].get("officialDate")),
        "game_datetime_utc": _parse_datetime_utc(game_data["datetime"].get("dateTime")),
        "home_team_id": home_id,
        "away_team_id": away_id,
        "venue_id": (game_data.get("venue") or {}).get("id"),
        "home_score": home_score if is_final else None,
        "away_score": away_score if is_final else None,
        "total_runs": (home_score + away_score)
        if is_final and home_score is not None and away_score is not None else None,
        "status": status,
        "day_night": game_data["datetime"].get("dayNight"),
        "temperature_f": parse_temperature(weather.get("temp")),
        "wind_speed_mph": wind_speed,
        "wind_direction": wind_dir,
        "weather_condition": weather.get("condition"),
        "game_type": game_info.get("type", "R"),
        "game_number": game_info.get("gameNumber"),
        "double_header": game_info.get("doubleHeader"),
        "home_starter_id": None,
        "away_starter_id": None,
        "boxscore_ingested": False,
    }

    # probable pitchers (useful for scheduled games)
    probables = game_data.get("probablePitchers", {}) or {}
    game_row["home_starter_id"] = (probables.get("home") or {}).get("id")
    game_row["away_starter_id"] = (probables.get("away") or {}).get("id")

    players = game_data.get("players", {}) or {}

    def player_meta(pid: int) -> dict:
        return players.get(f"ID{pid}", {})

    pitchers_rows: dict[int, dict] = {}

    def remember_pitcher(pid: int) -> None:
        meta = player_meta(pid)
        pitchers_rows[pid] = {
            "pitcher_id": pid,
            "full_name": meta.get("fullName", f"ID{pid}"),
            "throws": (meta.get("pitchHand") or {}).get("code"),
            "birth_date": _parse_date(meta.get("birthDate")),
        }

    pitcher_starts: list[dict] = []
    team_batting: list[dict] = []
    bullpen: list[dict] = []

    if is_final and boxscore:
        starter_throws: dict[str, str | None] = {}
        for side, team_id, opp_id in (("home", home_id, away_id), ("away", away_id, home_id)):
            box_team = boxscore["teams"][side]
            pitcher_ids: list[int] = box_team.get("pitchers", [])
            if not pitcher_ids:
                continue

            starter_id = pitcher_ids[0]
            game_row[f"{side}_starter_id"] = starter_id
            remember_pitcher(starter_id)
            starter_throws[side] = pitchers_rows[starter_id]["throws"]

            def pitching_stats(pid: int) -> dict:
                return (box_team.get("players", {})
                        .get(f"ID{pid}", {})
                        .get("stats", {})
                        .get("pitching", {}))

            st = pitching_stats(starter_id)
            outs = innings_to_outs(st.get("inningsPitched"))
            pitcher_starts.append({
                "game_pk": game_pk,
                "pitcher_id": starter_id,
                "team_id": team_id,
                "opponent_team_id": opp_id,
                "is_home": side == "home",
                "innings_pitched": outs_to_innings(outs),
                "outs_recorded": outs,
                "batters_faced": st.get("battersFaced"),
                "hits": st.get("hits"),
                "runs": st.get("runs"),
                "earned_runs": st.get("earnedRuns"),
                "walks": st.get("baseOnBalls"),
                "strikeouts": st.get("strikeOuts"),
                "home_runs": st.get("homeRuns"),
                "pitches_thrown": st.get("numberOfPitches") or st.get("pitchesThrown"),
                "strikes": st.get("strikes"),
                "ground_outs": st.get("groundOuts"),
                "fly_outs": st.get("airOuts"),
            })

            for pid in pitcher_ids[1:]:
                remember_pitcher(pid)
                st = pitching_stats(pid)
                outs = innings_to_outs(st.get("inningsPitched"))
                bullpen.append({
                    "game_pk": game_pk,
                    "pitcher_id": pid,
                    "team_id": team_id,
                    "game_date": game_row["game_date"],
                    "innings_pitched": outs_to_innings(outs),
                    "outs_recorded": outs,
                    "pitches_thrown": st.get("numberOfPitches") or st.get("pitchesThrown"),
                    "earned_runs": st.get("earnedRuns"),
                    "strikeouts": st.get("strikeOuts"),
                    "walks": st.get("baseOnBalls"),
                })

        for side, team_id in (("home", home_id), ("away", away_id)):
            batting = boxscore["teams"][side].get("teamStats", {}).get("batting", {})
            if not batting:
                continue
            opp_side = "away" if side == "home" else "home"
            team_batting.append({
                "game_pk": game_pk,
                "team_id": team_id,
                "runs": batting.get("runs"),
                "hits": batting.get("hits"),
                "home_runs": batting.get("homeRuns"),
                "walks": batting.get("baseOnBalls"),
                "strikeouts": batting.get("strikeOuts"),
                "left_on_base": batting.get("leftOnBase"),
                "at_bats": batting.get("atBats"),
                "opposing_starter_throws": starter_throws.get(opp_side),
            })

        game_row["boxscore_ingested"] = bool(pitcher_starts)

    # remember probable pitchers too (scheduled games)
    for pid in (game_row["home_starter_id"], game_row["away_starter_id"]):
        if pid and pid not in pitchers_rows:
            remember_pitcher(pid)

    return {
        "game": game_row,
        "pitchers": list(pitchers_rows.values()),
        "pitcher_starts": pitcher_starts,
        "team_game_batting": team_batting,
        "bullpen_appearances": bullpen,
    }


# ---------------------------------------------------------------------------
# other endpoints -> rows
# ---------------------------------------------------------------------------

def parse_schedule_game(g: dict) -> dict[str, Any]:
    """Minimal game row from a /schedule entry (no weather, no boxscore).

    Used for postponed/cancelled games (no feed needed) and for today's
    scheduled games incl. probable pitchers (hydrate=probablePitcher).
    """
    status = map_status(g.get("status", {}))
    home = g["teams"]["home"]
    away = g["teams"]["away"]
    is_final = status == "final"
    home_score = home.get("score") if is_final else None
    away_score = away.get("score") if is_final else None
    return {
        "game_pk": g["gamePk"],
        "season": int(g.get("season") or g["officialDate"][:4]),
        "game_date": _parse_date(g.get("officialDate")),
        "game_datetime_utc": _parse_datetime_utc(g.get("gameDate")),
        "home_team_id": home["team"]["id"],
        "away_team_id": away["team"]["id"],
        "venue_id": (g.get("venue") or {}).get("id"),
        "home_score": home_score,
        "away_score": away_score,
        "total_runs": (home_score + away_score)
        if home_score is not None and away_score is not None else None,
        "status": status,
        "day_night": g.get("dayNight"),
        "game_type": g.get("gameType", "R"),
        "game_number": g.get("gameNumber"),
        "double_header": g.get("doubleHeader"),
        "home_starter_id": (home.get("probablePitcher") or {}).get("id"),
        "away_starter_id": (away.get("probablePitcher") or {}).get("id"),
        "boxscore_ingested": False,
    }


def parse_team(team: dict) -> dict:
    return {
        "team_id": team["id"],
        "name": team.get("name", ""),
        "abbreviation": team.get("abbreviation", ""),
        "league": (team.get("league") or {}).get("name"),
        "division": (team.get("division") or {}).get("name"),
        "venue_id": (team.get("venue") or {}).get("id"),
    }


_ROOF_MAP = {"open": "open", "dome": "dome", "retractable": "retractable"}


def parse_venue(venue: dict) -> dict:
    field_info = venue.get("fieldInfo", {}) or {}
    location = venue.get("location", {}) or {}
    roof_raw = (field_info.get("roofType") or "").lower()
    roof = next((v for k, v in _ROOF_MAP.items() if k in roof_raw), None)
    return {
        "venue_id": venue["id"],
        "name": venue.get("name", ""),
        "city": location.get("city"),
        "roof_type": roof,
        "elevation": location.get("elevation"),
    }


def parse_person(person: dict) -> dict:
    return {
        "pitcher_id": person["id"],
        "full_name": person.get("fullName", ""),
        "throws": (person.get("pitchHand") or {}).get("code"),
        "birth_date": _parse_date(person.get("birthDate")),
    }
