"""Feature-layer tests, most importantly the NO-DATA-LEAKAGE proof:
features of a game must not change when all data from later days is deleted.
"""
import pandas as pd
import pytest
from sqlalchemy import text

from src.features import build_game_features, rebuild_all
from src.schema import get_engine
from tests.synthetic import build_synthetic_db


@pytest.fixture(scope="module")
def synthetic_db(tmp_path_factory):
    db_path = tmp_path_factory.mktemp("db") / "mlb_test.db"
    build_synthetic_db(db_path)
    return db_path


def test_rebuild_all_row_counts(synthetic_db):
    counts = rebuild_all(synthetic_db)
    engine = get_engine(synthetic_db)
    n_games = pd.read_sql("SELECT COUNT(*) AS n FROM games", engine)["n"][0]
    n_starts = pd.read_sql("SELECT COUNT(*) AS n FROM pitcher_starts", engine)["n"][0]
    assert counts["v_game_features"] == n_games
    assert counts["v_pitcher_form"] == n_starts
    assert counts["v_team_offense"] == 2 * n_games
    assert counts["v_bullpen_fatigue"] == 2 * n_games


def test_pitcher_form_values_hand_checked(synthetic_db):
    """Recompute one pitcher's l5 K/9 by hand from raw tables."""
    engine = get_engine(synthetic_db)
    starts = pd.read_sql("""
        SELECT ps.pitcher_id, ps.game_pk, ps.outs_recorded, ps.strikeouts, g.game_date
        FROM pitcher_starts ps JOIN games g ON g.game_pk = ps.game_pk
        ORDER BY g.game_date, ps.game_pk
    """, engine)
    pid = starts["pitcher_id"].iloc[0]
    mine = starts[starts["pitcher_id"] == pid].reset_index(drop=True)
    assert len(mine) >= 7, "synthetic pitcher needs enough starts"

    target = mine.iloc[6]  # 7th start -> l5 window = starts 2..6
    window = mine.iloc[1:6]
    expected_k9 = round(9 * window["strikeouts"].sum() / (window["outs_recorded"].sum() / 3), 4)

    form = pd.read_sql(
        text("SELECT * FROM v_pitcher_form WHERE game_pk = :pk AND pitcher_id = :pid"),
        engine, params={"pk": int(target["game_pk"]), "pid": int(pid)})
    assert len(form) == 1
    assert form["n_starts_l5"][0] == 5
    assert form["k9_l5"][0] == pytest.approx(expected_k9, abs=1e-3)


def test_no_data_leakage(tmp_path):
    """Delete everything after a cutoff game -> its features must be identical.

    Uses its own DB copy because it destroys half the data.
    """
    db_path = tmp_path / "mlb_leak.db"
    build_synthetic_db(db_path)
    engine = get_engine(db_path)
    features_full = build_game_features(engine)
    features_full = features_full.sort_values("game_pk").reset_index(drop=True)

    # pick a game in the middle of the synthetic season
    cutoff = features_full.iloc[len(features_full) // 2]
    cutoff_pk, cutoff_date = int(cutoff["game_pk"]), cutoff["game_date"]

    with engine.connect() as conn:
        later = "SELECT game_pk FROM games WHERE game_date > :d OR " \
                "(game_date = :d AND game_pk > :pk)"
        for table in ("pitcher_starts", "pitcher_starts_statcast",
                      "team_game_batting", "bullpen_appearances"):
            conn.execute(text(
                f"DELETE FROM {table} WHERE game_pk IN ({later})"),
                {"d": str(cutoff_date), "pk": cutoff_pk})
        conn.execute(text(f"DELETE FROM games WHERE game_pk IN ({later})"),
                     {"d": str(cutoff_date), "pk": cutoff_pk})
        conn.commit()

    features_trimmed = build_game_features(engine)
    row_full = features_full[features_full["game_pk"] == cutoff_pk].reset_index(drop=True)
    row_trimmed = features_trimmed[features_trimmed["game_pk"] == cutoff_pk] \
        .reset_index(drop=True)

    assert len(row_trimmed) == 1
    pd.testing.assert_frame_equal(row_full, row_trimmed, check_dtype=False)


def test_key_feature_columns_not_null(synthetic_db):
    """Late-season games must have a complete feature row (no NULL in key cols)."""
    engine = get_engine(synthetic_db)
    gf = build_game_features(engine)
    late = gf.sort_values("game_date").tail(10)
    key_cols = [
        "hs_k9_l5", "hs_xfip_l10", "as_k9_l5", "as_xfip_l10",
        "off_home_rpg_l15", "off_away_rpg_l30",
        "home_bp_pitches_d3", "away_bp_pitches_d3",
        "park_factor_runs", "home_rest_days", "away_rest_days",
        "total_runs", "home_starter_strikeouts", "away_starter_strikeouts",
    ]
    for col in key_cols:
        assert late[col].notna().all(), f"NULL v klíčovém sloupci {col}"
