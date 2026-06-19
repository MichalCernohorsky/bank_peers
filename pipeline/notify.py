"""
notify.py — alerty z ingest automatiky. Pluggable: log vždy, Slack webhook
volitelně (SLACK_WEBHOOK_URL). E-mail je TODO (vyžaduje SMTP konfiguraci).

Validace je brána: když rekonciliace neprojde, watcher NEpromotuje data a pošle
sem alert (level="alert").
"""
import json
import logging
import os
import urllib.request

log = logging.getLogger("ingest")
if not log.handlers:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")


def notify(subject: str, body: str = "", level: str = "info") -> str:
    """Zaloguje a (je-li nastaven SLACK_WEBHOOK_URL) pošle na Slack. Vrací zformátovaný řádek."""
    line = f"{subject} — {body}" if body else subject
    (log.error if level in ("alert", "error") else log.info)(f"[{level.upper()}] {line}")

    hook = os.environ.get("SLACK_WEBHOOK_URL")
    if hook:
        icon = ":rotating_light:" if level in ("alert", "error") else ":white_check_mark:"
        payload = json.dumps({"text": f"{icon} *{subject}*\n{body}"}).encode()
        try:
            req = urllib.request.Request(hook, data=payload, headers={"Content-Type": "application/json"})
            urllib.request.urlopen(req, timeout=10)
        except Exception as e:  # alert nesmí shodit běh
            log.warning(f"slack notify selhal: {e}")
    return line
