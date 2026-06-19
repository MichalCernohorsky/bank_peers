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

from pipeline.watch import run_once


def main():
    ap = argparse.ArgumentParser(description="Scheduler pro ingestion automatiku.")
    ap.add_argument("--cron", default="0 6 * * *", help="cron výraz (min hod den měs den_v_týdnu)")
    ap.add_argument("--now", action="store_true", help="spusť jednou hned a skonči")
    args = ap.parse_args()

    if args.now:
        run_once()
        return

    try:
        from apscheduler.schedulers.blocking import BlockingScheduler
        from apscheduler.triggers.cron import CronTrigger
    except ImportError:
        raise SystemExit("Chybí APScheduler: pip install apscheduler (nebo použij GitHub Actions schedule).")

    sched = BlockingScheduler()
    sched.add_job(run_once, CronTrigger.from_crontab(args.cron), id="ingest")
    print(f"Scheduler běží (cron '{args.cron}'). Ctrl-C ukončí.")
    try:
        sched.start()
    except (KeyboardInterrupt, SystemExit):
        pass


if __name__ == "__main__":
    main()
