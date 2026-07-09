import pandas as pd

from src.statcast import aggregate_pitcher_games


def _pitch(desc, pitch_type="FF", speed=95.0, lsa=None, xba=None, xslg=None):
    return {
        "game_pk": 745804, "pitcher": 543037, "description": desc,
        "pitch_type": pitch_type, "release_speed": speed,
        "launch_speed_angle": lsa,
        "estimated_ba_using_speedangle": xba,
        "estimated_slg_using_speedangle": xslg,
    }


def test_aggregate_basic_rates():
    pitches = pd.DataFrame([
        _pitch("called_strike", speed=96.0),
        _pitch("swinging_strike", speed=95.0),
        _pitch("ball", speed=94.0),
        _pitch("foul", speed=97.0),
        _pitch("hit_into_play", speed=93.0, lsa=6, xba=0.9, xslg=1.8),  # barrel
        _pitch("hit_into_play", pitch_type="SL", speed=85.0, lsa=3, xba=0.1, xslg=0.1),
    ])
    agg = aggregate_pitcher_games(pitches)
    assert len(agg) == 1
    row = agg.iloc[0]

    assert row["pitch_count"] == 6
    # swings: swinging_strike, foul, 2x hit_into_play = 4; whiffs = 1
    assert row["whiff_rate"] == 0.25
    # CSW: called_strike + swinging_strike = 2 / 6
    assert row["csw_rate"] == round(2 / 6, 4)
    # fastball velo: only FF pitches (5 of them: 96,95,94,97,93)
    assert row["avg_velocity_fastball"] == 95.0
    # batted balls: 2, one barrel
    assert row["barrel_rate_against"] == 0.5
    assert row["xba_against"] == 0.5   # mean(0.9, 0.1)
    assert row["xslg_against"] == 0.95  # mean(1.8, 0.1)


def test_automatic_balls_are_not_pitches():
    """Intentional walks (automatic_ball) are Savant rows but no pitch was
    thrown - they must not count into pitch_count nor dilute CSW."""
    pitches = pd.DataFrame([
        _pitch("called_strike"),
        _pitch("automatic_ball", pitch_type=None, speed=None),
        _pitch("automatic_ball", pitch_type=None, speed=None),
    ])
    agg = aggregate_pitcher_games(pitches)
    row = agg.iloc[0]
    assert row["pitch_count"] == 1
    assert row["csw_rate"] == 1.0


def test_aggregate_groups_by_game_and_pitcher():
    rows = [_pitch("called_strike"), _pitch("ball")]
    other = dict(_pitch("swinging_strike"), pitcher=601713)
    agg = aggregate_pitcher_games(pd.DataFrame(rows + [other]))
    assert len(agg) == 2
    assert set(agg["pitcher_id"]) == {543037, 601713}
