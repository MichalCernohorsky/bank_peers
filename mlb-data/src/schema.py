"""Database schema for the MLB betting data pipeline.

Design rules (see CLAUDE.md):
- Portable SQLAlchemy constructs only, so a later move to PostgreSQL is trivial.
- Every table has explicit primary keys / unique constraints -> no duplicates.
- All writes go through `upsert()` so every script is idempotent.
"""
from __future__ import annotations

import datetime
from pathlib import Path

from sqlalchemy import (
    Boolean,
    Date,
    DateTime,
    Float,
    ForeignKey,
    Index,
    Integer,
    String,
    UniqueConstraint,
    create_engine,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column

DEFAULT_DB_PATH = Path(__file__).resolve().parent.parent / "data" / "mlb.db"


class Base(DeclarativeBase):
    pass


class Team(Base):
    __tablename__ = "teams"

    team_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # official MLB id
    name: Mapped[str] = mapped_column(String(64))
    abbreviation: Mapped[str] = mapped_column(String(8))
    league: Mapped[str | None] = mapped_column(String(32))
    division: Mapped[str | None] = mapped_column(String(32))
    venue_id: Mapped[int | None] = mapped_column(ForeignKey("venues.venue_id"))


class Venue(Base):
    __tablename__ = "venues"

    venue_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # official MLB id
    name: Mapped[str] = mapped_column(String(64))
    city: Mapped[str | None] = mapped_column(String(64))
    roof_type: Mapped[str | None] = mapped_column(String(16))  # open / dome / retractable
    elevation: Mapped[int | None] = mapped_column(Integer)  # feet above sea level
    park_factor_runs: Mapped[float | None] = mapped_column(Float)  # index, 100 = neutral
    park_factor_hr: Mapped[float | None] = mapped_column(Float)


class Game(Base):
    """Core table - one row per scheduled MLB game."""

    __tablename__ = "games"

    game_pk: Mapped[int] = mapped_column(Integer, primary_key=True)  # official MLB id
    season: Mapped[int] = mapped_column(Integer, index=True)
    game_date: Mapped[datetime.date] = mapped_column(Date, index=True)
    game_datetime_utc: Mapped[datetime.datetime | None] = mapped_column(DateTime)
    home_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    away_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    venue_id: Mapped[int | None] = mapped_column(ForeignKey("venues.venue_id"))
    home_score: Mapped[int | None] = mapped_column(Integer)
    away_score: Mapped[int | None] = mapped_column(Integer)
    total_runs: Mapped[int | None] = mapped_column(Integer)
    # scheduled / live / final / postponed / suspended / cancelled
    status: Mapped[str] = mapped_column(String(16), index=True)
    day_night: Mapped[str | None] = mapped_column(String(8))
    # scheduled games carry the announced probable pitcher, final games the actual starter
    home_starter_id: Mapped[int | None] = mapped_column(ForeignKey("pitchers.pitcher_id"))
    away_starter_id: Mapped[int | None] = mapped_column(ForeignKey("pitchers.pitcher_id"))
    temperature_f: Mapped[int | None] = mapped_column(Integer)
    wind_speed_mph: Mapped[int | None] = mapped_column(Integer)
    wind_direction: Mapped[str | None] = mapped_column(String(32))  # e.g. "Out To CF"
    weather_condition: Mapped[str | None] = mapped_column(String(32))
    # 'R' = regular season; playoffs stored too but flagged: 'F','D','L','W' etc.
    game_type: Mapped[str] = mapped_column(String(2), index=True)
    game_number: Mapped[int | None] = mapped_column(Integer)  # 1/2 for doubleheaders
    double_header: Mapped[str | None] = mapped_column(String(1))  # N / Y / S (split)
    # True once the boxscore detail (starts, batting, bullpen) is stored -> resume marker
    boxscore_ingested: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (
        Index("ix_games_season_date", "season", "game_date"),
        Index("ix_games_home_team_date", "home_team_id", "game_date"),
        Index("ix_games_away_team_date", "away_team_id", "game_date"),
    )


class Pitcher(Base):
    __tablename__ = "pitchers"

    pitcher_id: Mapped[int] = mapped_column(Integer, primary_key=True)  # official MLB id
    full_name: Mapped[str] = mapped_column(String(64))
    throws: Mapped[str | None] = mapped_column(String(1))  # L / R / S
    birth_date: Mapped[datetime.date | None] = mapped_column(Date)


class PitcherStart(Base):
    """One row per starting-pitcher appearance (the key table for K props)."""

    __tablename__ = "pitcher_starts"

    game_pk: Mapped[int] = mapped_column(ForeignKey("games.game_pk"), primary_key=True)
    pitcher_id: Mapped[int] = mapped_column(ForeignKey("pitchers.pitcher_id"), primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    opponent_team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    is_home: Mapped[bool] = mapped_column(Boolean)
    innings_pitched: Mapped[float | None] = mapped_column(Float)  # true fraction: 5.2 IP -> 5.667
    outs_recorded: Mapped[int | None] = mapped_column(Integer)  # exact integer form of IP
    batters_faced: Mapped[int | None] = mapped_column(Integer)
    hits: Mapped[int | None] = mapped_column(Integer)
    runs: Mapped[int | None] = mapped_column(Integer)
    earned_runs: Mapped[int | None] = mapped_column(Integer)
    walks: Mapped[int | None] = mapped_column(Integer)
    strikeouts: Mapped[int | None] = mapped_column(Integer)
    home_runs: Mapped[int | None] = mapped_column(Integer)
    pitches_thrown: Mapped[int | None] = mapped_column(Integer)
    strikes: Mapped[int | None] = mapped_column(Integer)
    ground_outs: Mapped[int | None] = mapped_column(Integer)
    fly_outs: Mapped[int | None] = mapped_column(Integer)  # airOuts in the MLB boxscore

    __table_args__ = (
        # one starter per team and game
        UniqueConstraint("game_pk", "team_id", name="uq_pitcher_starts_game_team"),
        Index("ix_pitcher_starts_pitcher", "pitcher_id"),
    )


class PitcherStartStatcast(Base):
    """Statcast enrichment of a start (pybaseball), joined via game_pk + pitcher_id."""

    __tablename__ = "pitcher_starts_statcast"

    game_pk: Mapped[int] = mapped_column(ForeignKey("games.game_pk"), primary_key=True)
    pitcher_id: Mapped[int] = mapped_column(ForeignKey("pitchers.pitcher_id"), primary_key=True)
    avg_velocity_fastball: Mapped[float | None] = mapped_column(Float)  # FF/SI, mph
    whiff_rate: Mapped[float | None] = mapped_column(Float)  # whiffs / swings
    csw_rate: Mapped[float | None] = mapped_column(Float)  # (called + swinging strikes) / pitches
    xba_against: Mapped[float | None] = mapped_column(Float)
    xslg_against: Mapped[float | None] = mapped_column(Float)
    barrel_rate_against: Mapped[float | None] = mapped_column(Float)  # barrels / batted balls
    pitch_count: Mapped[int | None] = mapped_column(Integer)  # sanity anchor vs pitches_thrown


class TeamGameBatting(Base):
    """Team offense per game."""

    __tablename__ = "team_game_batting"

    game_pk: Mapped[int] = mapped_column(ForeignKey("games.game_pk"), primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"), primary_key=True)
    runs: Mapped[int | None] = mapped_column(Integer)
    hits: Mapped[int | None] = mapped_column(Integer)
    home_runs: Mapped[int | None] = mapped_column(Integer)
    walks: Mapped[int | None] = mapped_column(Integer)
    strikeouts: Mapped[int | None] = mapped_column(Integer)
    left_on_base: Mapped[int | None] = mapped_column(Integer)
    at_bats: Mapped[int | None] = mapped_column(Integer)
    opposing_starter_throws: Mapped[str | None] = mapped_column(String(1))  # L / R splits later

    __table_args__ = (Index("ix_team_game_batting_team", "team_id"),)


class BullpenAppearance(Base):
    """Every relief outing - the basis for bullpen-fatigue features."""

    __tablename__ = "bullpen_appearances"

    game_pk: Mapped[int] = mapped_column(ForeignKey("games.game_pk"), primary_key=True)
    pitcher_id: Mapped[int] = mapped_column(ForeignKey("pitchers.pitcher_id"), primary_key=True)
    team_id: Mapped[int] = mapped_column(ForeignKey("teams.team_id"))
    game_date: Mapped[datetime.date] = mapped_column(Date, index=True)
    innings_pitched: Mapped[float | None] = mapped_column(Float)
    outs_recorded: Mapped[int | None] = mapped_column(Integer)
    pitches_thrown: Mapped[int | None] = mapped_column(Integer)
    earned_runs: Mapped[int | None] = mapped_column(Integer)
    strikeouts: Mapped[int | None] = mapped_column(Integer)
    walks: Mapped[int | None] = mapped_column(Integer)

    __table_args__ = (Index("ix_bullpen_team_date", "team_id", "game_date"),)


class Odds(Base):
    """Betting odds - intentionally generic (sport column) so NBA fits later.

    Stays empty in phase 1; the schema is prepared for line-history capture
    (multiple snapshots per market, `is_closing` marks the closing line).
    """

    __tablename__ = "odds"

    odds_id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    sport: Mapped[str] = mapped_column(String(8), default="mlb")
    game_pk: Mapped[int | None] = mapped_column(ForeignKey("games.game_pk"))
    event_ref: Mapped[str | None] = mapped_column(String(64))  # generic id for other sports
    bookmaker: Mapped[str] = mapped_column(String(32))
    # total / team_total_home / team_total_away / moneyline / strikeouts
    market: Mapped[str] = mapped_column(String(32))
    player_id: Mapped[int | None] = mapped_column(Integer)  # for player props (strikeouts)
    line: Mapped[float | None] = mapped_column(Float)
    over_price: Mapped[float | None] = mapped_column(Float)
    under_price: Mapped[float | None] = mapped_column(Float)
    captured_at: Mapped[datetime.datetime] = mapped_column(DateTime)
    is_closing: Mapped[bool] = mapped_column(Boolean, default=False)

    __table_args__ = (
        UniqueConstraint(
            "sport", "game_pk", "event_ref", "bookmaker", "market", "player_id", "captured_at",
            name="uq_odds_snapshot",
        ),
    )


# --------------------------------------------------------------------------
# engine / session helpers
# --------------------------------------------------------------------------

def get_engine(db_path: str | Path = DEFAULT_DB_PATH, echo: bool = False):
    """Engine for the SQLite dev database (swap the URL for PostgreSQL later)."""
    db_path = Path(db_path)
    db_path.parent.mkdir(parents=True, exist_ok=True)
    return create_engine(f"sqlite:///{db_path}", echo=echo)


def create_all(engine) -> None:
    Base.metadata.create_all(engine)


def upsert(session: Session, model, rows: list[dict], key_cols: list[str]) -> int:
    """Idempotent bulk write: INSERT ... ON CONFLICT(key) DO UPDATE.

    Works on SQLite and PostgreSQL (the only dialect-specific piece of the
    whole codebase, isolated here on purpose). Returns number of rows written.
    """
    if not rows:
        return 0
    dialect = session.get_bind().dialect.name
    if dialect == "sqlite":
        from sqlalchemy.dialects.sqlite import insert as dialect_insert
    elif dialect == "postgresql":
        from sqlalchemy.dialects.postgresql import insert as dialect_insert
    else:
        raise NotImplementedError(f"upsert() not implemented for dialect {dialect!r}")

    table = model.__table__
    stmt = dialect_insert(table).values(rows)
    update_cols = {
        c.name: getattr(stmt.excluded, c.name)
        for c in table.columns
        if c.name not in key_cols and c.name in rows[0]
    }
    if update_cols:
        stmt = stmt.on_conflict_do_update(index_elements=key_cols, set_=update_cols)
    else:
        stmt = stmt.on_conflict_do_nothing(index_elements=key_cols)
    session.execute(stmt)
    return len(rows)
