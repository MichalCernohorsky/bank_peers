"""
db.py — tenká vrstva nad SQLite i PostgreSQL se sjednoceným API.

Cíl: zbytek kódu (build_db, api) píše jeden dialekt SQL s `?` placeholdery a
tahle vrstva ho přeloží na cílovou databázi podle DATABASE_URL:

  sqlite:///data/cs_financials.db        -> sqlite3
  postgresql://user:pass@host:5432/db    -> psycopg (v3)

Překlady pro Postgres:
  - `?`                 -> `%s`
  - `INSERT OR IGNORE`  -> `INSERT ... ON CONFLICT DO NOTHING`
  - `lastrowid`         -> `RETURNING id` (viz Conn.insert)
  - NULL-safe `IS`      -> `IS NOT DISTINCT FROM` (řeší si volající přes Conn.null_eq)

Bez bare hodnot v kódu: connection string vždy z configu/env (viz settings.py).
"""
import datetime as dt
import sqlite3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SQLITE_PATH = ROOT / "data" / "cs_financials.db"

# globální adaptér: ukládej datetime jako ISO text (sqlite3 už vlastní nemá od py3.12)
sqlite3.register_adapter(dt.datetime, lambda d: d.isoformat(timespec="seconds"))


def normalize_url(url: str | None) -> str:
    """Holou cestu ber jako sqlite soubor; jinak nech URL tak jak je."""
    if not url:
        return f"sqlite:///{DEFAULT_SQLITE_PATH}"
    if "://" in url:
        return url
    return f"sqlite:///{url}"


def dialect_of(url: str) -> str:
    return "postgres" if url.startswith(("postgres://", "postgresql://")) else "sqlite"


def sqlite_path(url: str) -> str:
    """Vytáhne souborovou cestu z sqlite URL (sqlite:///rel nebo sqlite:////abs)."""
    if url.startswith("sqlite:///"):
        return url[len("sqlite:///"):]
    if url.startswith("sqlite://"):
        return url[len("sqlite://"):]
    return url


class Conn:
    """Spojení s jednotným API přes oba dialekty."""

    def __init__(self, url: str | None):
        self.url = normalize_url(url)
        self.dialect = dialect_of(self.url)
        if self.dialect == "sqlite":
            con = sqlite3.connect(sqlite_path(self.url))
            con.row_factory = sqlite3.Row
            self._con = con
        else:
            import psycopg
            from psycopg.rows import dict_row
            self._con = psycopg.connect(self.url, row_factory=dict_row)

    # NULL-safe rovnost pro daný dialekt (sloupec {op} ?)
    @property
    def null_eq(self) -> str:
        return "IS NOT DISTINCT FROM" if self.dialect == "postgres" else "IS"

    def _translate(self, sql: str) -> str:
        if self.dialect != "postgres":
            return sql
        if "INSERT OR IGNORE INTO" in sql:
            sql = sql.replace("INSERT OR IGNORE INTO", "INSERT INTO")
            if "ON CONFLICT" not in sql.upper():
                sql = sql.rstrip().rstrip(";") + " ON CONFLICT DO NOTHING"
        return sql.replace("?", "%s")

    def execute(self, sql: str, params=()):
        cur = self._con.cursor()
        cur.execute(self._translate(sql), tuple(params))
        return cur

    def query(self, sql: str, params=()) -> list[dict]:
        cur = self.execute(sql, params)
        rows = cur.fetchall()
        cur.close()
        return [dict(r) for r in rows]

    def query_one(self, sql: str, params=()):
        rows = self.query(sql, params)
        return rows[0] if rows else None

    def insert(self, sql: str, params=()) -> int:
        """INSERT vracející nové id (lastrowid v sqlite, RETURNING id v pg)."""
        if self.dialect == "postgres":
            s = self._translate(sql).rstrip().rstrip(";")
            if "RETURNING" not in s.upper():
                s += " RETURNING id"
            cur = self._con.cursor()
            cur.execute(s, tuple(params))
            new_id = cur.fetchone()["id"]
            cur.close()
            return new_id
        cur = self.execute(sql, params)
        return cur.lastrowid

    def executescript(self, sql: str) -> None:
        if self.dialect == "sqlite":
            self._con.executescript(sql)
        else:
            with self._con.cursor() as cur:
                cur.execute(sql)

    def commit(self) -> None:
        self._con.commit()

    def close(self) -> None:
        self._con.close()
