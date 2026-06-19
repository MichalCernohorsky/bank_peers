web: uvicorn api.app:app --host 0.0.0.0 --port ${PORT:-8000}
worker: python -m pipeline.scheduler --cron "0 6 * * *"
release: python -m pipeline.seed --if-empty
