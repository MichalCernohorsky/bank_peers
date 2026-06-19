# Pohodlné zkratky. Nejdůležitější: `make run`.
.PHONY: run test lint compose seed

run:            ## spustí API + frontend lokálně (http://localhost:8000)
	./run.sh

test:           ## spustí testy
	. .venv/bin/activate && pytest -q

lint:           ## ruff lint
	. .venv/bin/activate && ruff check .

compose:        ## API + PostgreSQL přes Docker (bez cloudu)
	docker compose up --build

seed:           ## naseeduje cílovou DB (DATABASE_URL) z prebuilt snapshotu
	. .venv/bin/activate && python -m pipeline.seed --if-empty
