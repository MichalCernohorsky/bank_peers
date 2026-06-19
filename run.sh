#!/usr/bin/env bash
# Lokální spuštění BankPulse jedním příkazem: ./run.sh
# Vytvoří .venv, nainstaluje závislosti a spustí API + frontend (žádný cloud, žádný xlsx).
# Data nese verzovaná data/cs_financials.db (4 banky). Konfigurace přes .env (volitelně).
set -euo pipefail
cd "$(dirname "$0")"

PYBIN="${PYTHON:-python3}"
if [ ! -d .venv ]; then
  echo "› vytvářím .venv…"
  "$PYBIN" -m venv .venv
fi
# shellcheck disable=SC1091
. .venv/bin/activate

echo "› instaluji závislosti…"
pip install -q --upgrade pip
pip install -q -r requirements.txt

PORT="${PORT:-8000}"
echo
echo "  BankPulse běží na  →  http://localhost:${PORT}"
echo "  health-check       →  http://localhost:${PORT}/health"
echo "  (Ctrl-C ukončí)"
echo
exec uvicorn api.app:app --host 0.0.0.0 --port "${PORT}"
