#!/usr/bin/env python3
"""
scheduler.py — dlouhoběžící varianta watcheru přes APScheduler (alternativa k
GitHub Actions on schedule, viz .github/workflows/ingest.yml).

Spustí pipeline.watch.run_once na cron rozvrhu (default denně 06:00). Idempotence
zajišťuje, že opakované běhy nic nepřestaví, dokud nepřijde nový dokument.

  pip install apscheduler
  python -m pipeline.scheduler --cron "0 6 * * *"
"""
import argparse

from pipeline.offers import refresh as offers_refresh
from pipeline.watch import run_once


def main():
    ap = argparse.ArgumentParser(description="Scheduler pro ingestion automatiku + sazby.")
    ap.add_argument("--cron", default="0 6 * * *", help="cron pro ingest výsledků (finanční kalendář)")
    ap.add_argument("--offers-cron", default="0 7 * * *", help="cron pro obnovu sazeb produktů")
    ap.add_argument("--now", action="store_true", help="spusť jednou hned a skonči")
    args = ap.parse_args()

    if args.now:
        run_once()
        offers_refresh("savings_account")
        return

    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
        from apscheduler.triggers.cron import CronTrigger
    except ImportError:
        raise SystemExit("Chybí APScheduler: pip install apscheduler (nebo použij GitHub Actions schedule).")

    sched = BlockingScheduler()
    sched.add_job(run_once, CronTrigger.from_crontab(args.cron), id="ingest")
    sched.add_job(lambda: offers_refresh("savings_account"),
                  CronTrigger.from_crontab(args.offers_cron), id="offers")
    print(f"Scheduler běží (ingest '{args.cron}', sazby '{args.offers_cron}'). Ctrl-C ukončí.")
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
