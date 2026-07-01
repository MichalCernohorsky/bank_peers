"""Rychlý přehled nad tabulkou subjekt (vrstva A) — počty a rozpady.

Použití: python -m src.prehled [--db data/entities.duckdb]
"""
from __future__ import annotations

import argparse

from src import db


def show(con) -> None:
    def q(sql):
        return con.execute(sql).fetchall()

    total = q("SELECT COUNT(*) FROM subjekt")[0][0]
    valid = q("SELECT COUNT(*) FROM subjekt WHERE ico_valid")[0][0]
    fo = q("SELECT COUNT(*) FROM subjekt WHERE je_fo")[0][0]
    print(f"=== PŘEHLED VRSTVY A ===")
    print(f"subjektů celkem:        {total:,}")
    print(f"  z toho platné IČO:    {valid:,}  ({100*valid/total:.2f} %)")
    print(f"  fyzické osoby (OSVČ):  {fo:,}  ({100*fo/total:.1f} %)")
    print(f"  právnické osoby:      {total-fo:,}  ({100*(total-fo)/total:.1f} %)")

    print("\n--- podle stavu ---")
    for stav, n in q("SELECT stav, COUNT(*) c FROM subjekt GROUP BY stav ORDER BY c DESC"):
        print(f"  {str(stav):18} {n:,}")

    print("\n--- TOP 10 krajů ---")
    for kraj, n in q("SELECT sidlo_kraj, COUNT(*) c FROM subjekt "
                     "GROUP BY sidlo_kraj ORDER BY c DESC LIMIT 10"):
        print(f"  {str(kraj):24} {n:,}")

    print("\n--- TOP 10 právních forem ---")
    for pf, n in q("SELECT pravni_forma, COUNT(*) c FROM subjekt "
                   "GROUP BY pravni_forma ORDER BY c DESC LIMIT 10"):
        print(f"  {str(pf):8} {n:,}")

    print("\n--- TOP 10 NACE ---")
    for nace, n in q("SELECT nace, COUNT(*) c FROM subjekt "
                     "WHERE nace IS NOT NULL GROUP BY nace ORDER BY c DESC LIMIT 10"):
        print(f"  {str(nace):10} {n:,}")

    print("\n--- rozsah datumu vzniku ---")
    lo, hi = q("SELECT MIN(datum_vzniku), MAX(datum_vzniku) FROM subjekt")[0]
    print(f"  {lo} … {hi}")


if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--db", default=str(db.DEFAULT_DB))
    args = p.parse_args()
    con = db.connect(args.db)
    show(con)
