#!/usr/bin/env python3
"""
seed.py — naplní cílovou databázi (DATABASE_URL) z verzovaného SQLite snapshotu.

K čemu: čerstvý produkční Postgres se naseeduje z prebuilt `data/cs_financials.db`
bez nutnosti zdrojových xlsx. Vhodné jako one-off / release krok při nasazení.
`--if-empty` přeskočí seed, pokud cíl už data má (bezpečné při re-deploy).

  python -m pipeline.seed [--from data/cs_financials.db] [--to <DATABASE_URL>] [--if-empty]
"""
import argparse
import sqlite3
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from pipeline.build_db import _schema_sql  # noqa: E402
from pipeline.db import Conn, dialect_of, normalize_url, sqlite_path  # noqa: E402
from pipeline.settings import get_settings  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SNAPSHOT = ROOT / "data" / "cs_financials.db"
# pořadí kvůli cizím klíčům (bank -> source/period -> fact)
TABLES = ["bank", "metric", "source", "period", "fact", "ingestion_run"]


def _has_data(url) -> bool:
    try:
        con = Conn(url)
        try:
            row = con.query_one("SELECT COUNT(*) AS n FROM bank")
            return bool(row and row["n"])
        finally:
            con.close()
    except Exception:
        return False   # schéma ještě neexistuje -> ber jako prázdné


def seed(src_sqlite, target_url, if_empty=False) -> int:
    url = normalize_url(target_url)
    if if_empty and _has_data(url):
        print(f"Cíl {dialect_of(url)} už má data — seed přeskočen.")
        return 0

    if dialect_of(url) == "sqlite":
        p = Path(sqlite_path(url))
        if p.resolve() != Path(src_sqlite).resolve() and p.exists():
            p.unlink()
        p.parent.mkdir(parents=True, exist_ok=True)

    src = sqlite3.connect(src_sqlite)
    src.row_factory = sqlite3.Row
    con = Conn(url)
    con.executescript(_schema_sql(con.dialect))

    n = 0
    for t in TABLES:
        rows = [dict(r) for r in src.execute(f"SELECT * FROM {t}").fetchall()]
        if not rows:
            continue
        cols = list(rows[0].keys())
        collist = ",".join(cols)
        ph = ",".join(["?"] * len(cols))
        for r in rows:
            con.execute(f"INSERT INTO {t}({collist}) VALUES({ph})", [r[c] for c in cols])
            n += 1
    con.commit()
    con.close()
    src.close()
    return n


def main():
    ap = argparse.ArgumentParser(description="Seed cílové DB z prebuilt SQLite snapshotu.")
    ap.add_argument("--from", dest="src", default=str(DEFAULT_SNAPSHOT))
    ap.add_argument("--to", dest="target", default=None, help="DATABASE_URL (default z env/.env)")
    ap.add_argument("--if-empty", action="store_true", help="seeduj jen když cíl nemá data")
    args = ap.parse_args()
    target = args.target or get_settings().database_url
    n = seed(args.src, target, if_empty=args.if_empty)
    print(f"Seed hotov: {n} řádků -> {dialect_of(normalize_url(target))}")


if __name__ == "__main__":
    main()
