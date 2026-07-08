"""Idempotency: running the same write twice must not duplicate or corrupt."""
import json
from pathlib import Path

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from src.parsers import parse_game_feed
from src.schema import (
    Game,
    Pitcher,
    PitcherStart,
    TeamGameBatting,
    create_all,
    get_engine,
    upsert,
)

FIXTURE = Path(__file__).parent / "fixtures" / "feed_live_final.json"


def _ingest(session):
    parsed = parse_game_feed(json.loads(FIXTURE.read_text()))
    upsert(session, Pitcher, parsed["pitchers"], ["pitcher_id"])
    upsert(session, Game, [parsed["game"]], ["game_pk"])
    upsert(session, PitcherStart, parsed["pitcher_starts"], ["game_pk", "pitcher_id"])
    upsert(session, TeamGameBatting, parsed["team_game_batting"], ["game_pk", "team_id"])
    session.commit()


def test_double_ingest_is_idempotent(tmp_path):
    engine = get_engine(tmp_path / "test.db")
    create_all(engine)
    with Session(engine) as session:
        _ingest(session)
        _ingest(session)  # second run must be a no-op update, not duplicates

        assert session.scalar(select(func.count()).select_from(Game)) == 1
        assert session.scalar(select(func.count()).select_from(PitcherStart)) == 2
        assert session.scalar(select(func.count()).select_from(TeamGameBatting)) == 2

        game = session.get(Game, 745804)
        assert game.total_runs == 8


def test_upsert_updates_changed_values(tmp_path):
    engine = get_engine(tmp_path / "test.db")
    create_all(engine)
    with Session(engine) as session:
        _ingest(session)
        # simulate a corrected feed arriving later (full row, new score)
        parsed = parse_game_feed(json.loads(FIXTURE.read_text()))
        corrected = dict(parsed["game"], home_score=4, total_runs=9)
        upsert(session, Game, [corrected], ["game_pk"])
        session.commit()
        game = session.get(Game, 745804)
        assert game.home_score == 4 and game.total_runs == 9
        # untouched columns keep their values
        assert game.temperature_f == 68
