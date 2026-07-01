"""CLI orchestrátor ad-hoc analýzy ekonomických subjektů v ČR.

Idempotentní a resumovatelné: každý krok si drží stav v DuckDB a cache na disku.
Kroky lze pouštět nezávisle a opakovaně.

Použití:
    python -m src.build init
    python -m src.build layer-a            # RES/ARES bulk -> univerzum
    python -m src.build layer-b            # ISIR -> insolvence
    python -m src.build coverage --n 500   # milník: měření coverage vrstvy C
    python -m src.build layer-c [--limit N]# extrakce úvěrů z PDF (dle rozhodnutí)
    python -m src.build export
    python -m src.build status             # přehled stavu
"""
from __future__ import annotations

import argparse
import logging
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from src import db  # noqa: E402

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("czech_entities.build")


def cmd_init(args):
    con = db.connect(args.db)
    db.init_schema(con)
    log.info("schéma inicializováno v %s", args.db)


def cmd_layer_a(args):
    from src import layer_a_res
    con = db.connect(args.db)
    db.init_schema(con)
    layer_a_res.ingest(con, args.config, cache_dir=args.cache, force=args.force,
                       sample=args.sample, file=args.file, source=args.source)


def cmd_enrich(args):
    from src import ares_rest
    con = db.connect(args.db)
    db.init_schema(con)
    ares_rest.enrich(con, args.config, cache_dir=args.cache,
                     ico_file=args.ico_file, limit=args.limit)


def cmd_layer_b(args):
    from src import layer_b_isir
    con = db.connect(args.db)
    db.init_schema(con)
    layer_b_isir.ingest(con, args.config, cache_dir=args.cache, force=args.force)


def cmd_coverage(args):
    from src import layer_c_coverage
    con = db.connect(args.db)
    db.init_schema(con)
    layer_c_coverage.measure(con, args.config, cache_dir=args.cache, n=args.n)


def cmd_layer_c(args):
    from src import layer_c_extract
    con = db.connect(args.db)
    db.init_schema(con)
    layer_c_extract.run(con, args.config, cache_dir=args.cache, limit=args.limit)


def cmd_export(args):
    from src import export
    con = db.connect(args.db)
    res = export.export(con, args.out)
    log.info("hotovo: %s", res)


def cmd_status(args):
    con = db.connect(args.db)
    db.init_schema(con)
    def count(t):
        try:
            return con.execute(f"SELECT COUNT(*) FROM {t}").fetchone()[0]
        except Exception:
            return "-"
    print("=== STAV ===")
    for t in ["subjekt", "insolvence", "zaverka_meta", "pdf_job", "uver", "coverage_sample"]:
        print(f"  {t:16} {count(t):>12}")
    print("--- běhy ---")
    for r in con.execute(
        "SELECT vrstva, stav, pocet_radku, pocet_chyb FROM ingestion_run ORDER BY run_id"
    ).fetchall():
        print(f"  {r[0]:12} {r[1]:8} radku={r[2]} chyb={r[3]}")


def main(argv=None):
    p = argparse.ArgumentParser(prog="czech_entities")
    p.add_argument("--db", default=str(db.DEFAULT_DB))
    p.add_argument("--config", default=str(Path(__file__).resolve().parent.parent / "config" / "sources.yaml"))
    p.add_argument("--cache", default=str(Path(__file__).resolve().parent.parent / "data" / "cache"))
    sub = p.add_subparsers(dest="cmd", required=True)

    sub.add_parser("init").set_defaults(func=cmd_init)

    a = sub.add_parser("layer-a"); a.add_argument("--force", action="store_true")
    a.add_argument("--sample", type=int, default=0, metavar="N",
                   help="jen vypíše strukturu prvních N záznamů (ladění mapování)")
    a.add_argument("--file", default=None,
                   help="lokální bulk soubor (BEZ egressu): .csv/.csv.gz/.zip nebo VREO .tar.gz")
    a.add_argument("--source", choices=["auto", "vreo", "csv"], default="auto",
                   help="formát zdroje (auto = dle přípony)")
    a.set_defaults(func=cmd_layer_a)
    en = sub.add_parser("enrich", help="doplnit atributy k seznamu IČO přes ARES REST v3")
    en.add_argument("--ico-file", default=None, help="soubor se seznamem IČO (1 na řádek)")
    en.add_argument("--limit", type=int, default=None)
    en.set_defaults(func=cmd_enrich)

    b = sub.add_parser("layer-b"); b.add_argument("--force", action="store_true"); b.set_defaults(func=cmd_layer_b)
    c = sub.add_parser("coverage"); c.add_argument("--n", type=int, default=500); c.set_defaults(func=cmd_coverage)
    d = sub.add_parser("layer-c"); d.add_argument("--limit", type=int, default=None); d.set_defaults(func=cmd_layer_c)
    e = sub.add_parser("export"); e.add_argument("--out", default=str(Path(__file__).resolve().parent.parent / "data")); e.set_defaults(func=cmd_export)
    sub.add_parser("status").set_defaults(func=cmd_status)

    args = p.parse_args(argv)
    args.func(args)


if __name__ == "__main__":
    main()
