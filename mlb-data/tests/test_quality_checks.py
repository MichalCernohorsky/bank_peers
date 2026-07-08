from sqlalchemy import text

from src.quality_checks import run_checks
from src.schema import get_engine
from tests.synthetic import build_synthetic_db


def test_clean_synthetic_db_passes(tmp_path):
    db_path = tmp_path / "mlb_qc.db"
    build_synthetic_db(db_path)
    # season counts are skipped: the synthetic mini-league is not a full season
    assert run_checks(db_path, check_season_counts=False) == 0


def test_corrupted_db_fails(tmp_path):
    db_path = tmp_path / "mlb_qc_bad.db"
    build_synthetic_db(db_path)
    engine = get_engine(db_path)
    with engine.connect() as conn:
        # break identity: batting runs no longer match the game score
        conn.execute(text(
            "UPDATE team_game_batting SET runs = runs + 1 "
            "WHERE game_pk = (SELECT MIN(game_pk) FROM games) "
            "AND team_id = (SELECT home_team_id FROM games "
            "               WHERE game_pk = (SELECT MIN(game_pk) FROM games))"))
        # and one final game loses its score
        conn.execute(text(
            "UPDATE games SET home_score = NULL "
            "WHERE game_pk = (SELECT MAX(game_pk) FROM games)"))
        conn.commit()
    assert run_checks(db_path, check_season_counts=False) == 1
