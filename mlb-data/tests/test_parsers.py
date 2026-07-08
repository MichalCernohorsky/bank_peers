import datetime
import json
from pathlib import Path

from src.parsers import (
    innings_to_outs,
    map_status,
    outs_to_innings,
    parse_game_feed,
    parse_schedule_game,
    parse_wind,
)

FIXTURES = Path(__file__).parent / "fixtures"


def load_fixture(name: str) -> dict:
    return json.loads((FIXTURES / name).read_text())


def test_innings_notation():
    assert innings_to_outs("6.2") == 20
    assert innings_to_outs("0.1") == 1
    assert innings_to_outs("9") == 27
    assert innings_to_outs(None) is None
    assert outs_to_innings(20) == round(20 / 3, 4)


def test_parse_wind():
    assert parse_wind("11 mph, Out To CF") == (11, "Out To CF")
    assert parse_wind("Calm") == (0, "Calm")
    assert parse_wind(None) == (None, None)


def test_map_status():
    assert map_status({"abstractGameState": "Final", "detailedState": "Final"}) == "final"
    assert map_status({"abstractGameState": "Final",
                       "detailedState": "Postponed"}) == "postponed"
    assert map_status({"abstractGameState": "Preview",
                       "detailedState": "Scheduled"}) == "scheduled"


def test_parse_game_feed_final():
    parsed = parse_game_feed(load_fixture("feed_live_final.json"))
    game = parsed["game"]

    assert game["game_pk"] == 745804
    assert game["season"] == 2024
    assert game["game_date"] == datetime.date(2024, 6, 15)
    assert game["status"] == "final"
    assert game["home_score"] == 3 and game["away_score"] == 5
    assert game["total_runs"] == 8
    assert game["temperature_f"] == 68
    assert game["wind_speed_mph"] == 11 and game["wind_direction"] == "Out To CF"
    assert game["home_starter_id"] == 601713  # actual starter from boxscore
    assert game["away_starter_id"] == 543037
    assert game["boxscore_ingested"] is True

    starts = {s["pitcher_id"]: s for s in parsed["pitcher_starts"]}
    assert set(starts) == {543037, 601713}
    cole = starts[543037]
    assert cole["outs_recorded"] == 20  # "6.2" IP
    assert cole["strikeouts"] == 9
    assert cole["pitches_thrown"] == 101
    assert cole["is_home"] is False
    assert cole["opponent_team_id"] == 111

    # bullpen = everyone except the starters
    bullpen_ids = {b["pitcher_id"] for b in parsed["bullpen_appearances"]}
    assert bullpen_ids == {656756, 621244, 670102}

    batting = {b["team_id"]: b for b in parsed["team_game_batting"]}
    assert batting[111]["runs"] == 3 and batting[147]["runs"] == 5
    # BOS faced RHP Cole, NYY faced RHP Pivetta
    assert batting[111]["opposing_starter_throws"] == "R"
    assert batting[147]["opposing_starter_throws"] == "R"

    pitcher_ids = {p["pitcher_id"] for p in parsed["pitchers"]}
    assert {543037, 601713, 656756, 621244, 670102} <= pitcher_ids


def test_parse_schedule_game_probables():
    sched = {
        "gamePk": 999999, "season": "2025", "officialDate": "2025-07-08",
        "gameDate": "2025-07-08T18:05:00Z", "gameType": "R",
        "gameNumber": 1, "doubleHeader": "N", "dayNight": "day",
        "status": {"abstractGameState": "Preview", "detailedState": "Scheduled"},
        "venue": {"id": 3, "name": "Fenway Park"},
        "teams": {
            "home": {"team": {"id": 111}, "probablePitcher": {"id": 601713}},
            "away": {"team": {"id": 147}, "probablePitcher": {"id": 543037}},
        },
    }
    row = parse_schedule_game(sched)
    assert row["status"] == "scheduled"
    assert row["home_starter_id"] == 601713
    assert row["away_starter_id"] == 543037
    assert row["home_score"] is None and row["total_runs"] is None
