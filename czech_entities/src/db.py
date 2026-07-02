"""Tenká vrstva nad DuckDB — připojení, schéma, provenance helpery."""
from __future__ import annotations

import datetime as dt
from pathlib import Path

import duckdb

SCHEMA_PATH = Path(__file__).resolve().parent.parent / "schema.sql"
DEFAULT_DB = Path(__file__).resolve().parent.parent / "data" / "entities.duckdb"


def connect(db_path: str | Path = DEFAULT_DB) -> duckdb.DuckDBPyConnection:
    Path(db_path).parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(db_path))


def init_schema(con: duckdb.DuckDBPyConnection) -> None:
    con.execute(SCHEMA_PATH.read_text(encoding="utf-8"))


def _next_id(con: duckdb.DuckDBPyConnection, table: str, col: str) -> int:
    row = con.execute(f"SELECT COALESCE(MAX({col}), 0) + 1 FROM {table}").fetchone()
    return int(row[0])


def register_source(
    con: duckdb.DuckDBPyConnection,
    zdroj: str,
    url: str | None = None,
    soubor: str | None = None,
    poznamka: str | None = None,
) -> int:
    sid = _next_id(con, "source", "source_id")
    con.execute(
        "INSERT INTO source VALUES (?,?,?,?,?,?)",
        [sid, zdroj, url, soubor, dt.datetime.now(), poznamka],
    )
    return sid


def start_run(con: duckdb.DuckDBPyConnection, vrstva: str) -> int:
    rid = _next_id(con, "ingestion_run", "run_id")
    con.execute(
        "INSERT INTO ingestion_run VALUES (?,?,?,?,?,?,?,?)",
        [rid, vrstva, dt.datetime.now(), None, None, None, "running", None],
    )
    return rid


def finish_run(
    con: duckdb.DuckDBPyConnection,
    run_id: int,
    pocet_radku: int,
    pocet_chyb: int,
    stav: str = "ok",
    poznamka: str | None = None,
) -> None:
    con.execute(
        """UPDATE ingestion_run
           SET dokonceno_at=?, pocet_radku=?, pocet_chyb=?, stav=?, poznamka=?
           WHERE run_id=?""",
        [dt.datetime.now(), pocet_radku, pocet_chyb, stav, poznamka, run_id],
    )
