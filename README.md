# Bank Results Dashboard

Stahuje finanční výsledky hlavních českých bank, ukládá je do databáze a vykresluje
konfigurací řízené dashboardy. Viz `CLAUDE.md` pro architekturu a konvence.

## Quick start (jeden příkaz, bez cloudu)
```bash
./run.sh          # nebo: make run
```
Vytvoří `.venv`, nainstaluje závislosti a spustí appku na **http://localhost:8000**
(data nese verzovaná `data/cs_financials.db` — 4 banky, žádný xlsx ani Postgres potřeba).

Bez cloudu jde appka provozovat i na vlastním VPS (`./run.sh`) nebo přes Docker
(`make compose` → API + PostgreSQL). Render/Fly/Railway jsou jen volitelné možnosti (viz Nasazení).

### Přestavba databáze ze zdroje (volitelné)
```bash
pip install -r requirements.txt
python -m pipeline.build_db config /cesta/key_figures_q1_2026.xlsx data/cs_financials.db
```

Pipeline:
1. vytvoří schéma (`schema/001_init.sql`)
2. naseedovat `bank` + `metric` z `config/metrics.yaml`
3. načte fakty z xlsx podle `config/sources/cs.yaml`
4. dopočítá samostatná čtvrtletí (z YTD) a roční (FY) řádky
5. odvodí `total_liabilities`, `loan_to_deposit_ratio`
6. proběhne validací a zapíše `ingestion_run`

## Příklad dotazu
```sql
-- Kvartální výsledovka ČS (samostatná čtvrtletí)
SELECT m.label_cs, p.fiscal_year, p.quarter, f.value
FROM fact f
JOIN metric m ON m.code=f.code
JOIN period p ON p.id=f.period_id
WHERE p.period_type='Q' AND m.category='income_statement' AND f.basis='reported'
ORDER BY p.fiscal_year, p.quarter;

-- Roční pohled (FY)
SELECT code, value FROM fact f JOIN period p ON p.id=f.period_id
WHERE p.period_type='FY' AND p.fiscal_year=2025;
```

## Konfigurace (env)
Vše z prostředí (`.env`, viz `.env.example`) přes `pydantic-settings`:

| proměnná | význam | default |
|---|---|---|
| `DATABASE_URL` | `sqlite:///…` nebo `postgresql://…` | `sqlite:///data/cs_financials.db` |
| `XLSX_PATH` | zdrojový ČS xlsx pro `build_db` | `key_figures_q1_2026.xlsx` |
| `ALLOWED_ORIGINS` | `*` nebo CSV originů (CORS) | `*` |

## PostgreSQL vedle SQLite
`build_db` i API cílí obě databáze podle `DATABASE_URL` (vrstva `pipeline/db.py`).
Schéma: `schema/001_init.sql` (SQLite) a `schema/001_init_postgres.sql` (IDENTITY, `timestamptz`).
```bash
# build proti Postgresu
python -m pipeline.build_db config key_figures_q1_2026.xlsx postgresql://bank:bank@localhost:5432/bank
DATABASE_URL=postgresql://bank:bank@localhost:5432/bank uvicorn api.app:app
```

## Docker
```bash
docker compose up --build      # api (8000) + postgres; build_db proběhne při startu
```
Pozn.: zdrojový `key_figures_q1_2026.xlsx` musí být v repo rootu (build kontext).

## Testy a lint
```bash
pip install -r requirements.txt
ruff check .
pytest -q          # pipeline (validace, YTD/FY derivace) + API nad fixture xlsx
```
Fixture: `tests/fixtures/key_figures_sample.xlsx`. CI (`.github/workflows/ci.yml`) = lint + pytest.

## Automatický ingest (watcher)
Navázaný na finanční kalendář `config/calendar.yaml`. Pro každou banku zkontroluje
nový dokument, ověří checksum (idempotence), postaví staging DB, projde validací
(brána) a teprve pak promotuje do produkce; provenance + vintage v registru, alerty
přes `SLACK_WEBHOOK_URL`.
```bash
python -m pipeline.watch --once --target sqlite:///data/cs_financials.db
# scheduler: GitHub Actions (.github/workflows/ingest.yml) nebo APScheduler:
python -m pipeline.scheduler --cron "0 6 * * *"
```
Validace je brána: nevalidní data se NEpromotují (exit 1 → alert). Idempotence: stejný
checksum se přeskočí; restatement téhož období = nový vintage.

**Kontrola kompletnosti + ruční fallback** (gate v `config/calendar.yaml`): před promote se
ověří, že máme data včetně všech metrik — povinné metriky pro nejnovější období
(`required_metrics`) a pokrytí očekávané sady ze source-mapy (`min_coverage`). Když to
neprojde nebo auto-zdroj selže, watcher pošle alert „NAHRAJ RUČNĚ" s výčtem chybějícího a
data se vezmou z drop-folderu `data/manual_drop/<bank>/` při dalším běhu.

## Nasazení (deploy)
API + frontend běží z jednoho originu; scheduler je samostatný worker; data v PostgreSQL.

- **Health-check:** `GET /health` (ověří DB, vrátí počet bank, poslední ingest) — pro load-balancer.
- **Logování:** `LOG_LEVEL` (default `info`); requesty + start se logují přes std logging.
- **Seed:** čerstvý Postgres se naplní z verzovaného snapshotu bez xlsx:
  `python -m pipeline.seed --to "$DATABASE_URL" --if-empty`.

**Render** (blueprint `render.yaml`): Dashboard → New → Blueprint → repo. Vznikne web (API,
healthCheck `/health`, preDeploy seed), worker (scheduler) a PostgreSQL; `DATABASE_URL` se
propojí automaticky. Nastav `SLACK_WEBHOOK_URL` pro alerty.

**Fly.io** (`fly.toml`): `fly launch --no-deploy` → `fly postgres create && fly postgres attach` →
`fly deploy`. Procesy `app` (web) + `scheduler` (worker), release seed, health-check `/health`.

**Railway / Heroku-like** (`Procfile`): `web` + `worker` + `release` (seed). Přidej PostgreSQL plugin.

**VPS / Docker** (`docker-compose.yml`): `docker compose up --build` (api + postgres). Scheduler
jako další služba/cron: `python -m pipeline.scheduler`.

Env: `DATABASE_URL`, `XLSX_PATH`, `ALLOWED_ORIGINS`, `LOG_LEVEL`, `SLACK_WEBHOOK_URL` (viz `.env.example`).
Ingest fresh dat řeší watcher/scheduler (viz výše); validace je brána, nevalidní data se nepromotují.

## Stav
Hotová datová vrstva pro ČS (2002–Q1 2026), validace prochází (SQLite i PostgreSQL).
Backend API + sloučený frontend (`web/app.html`) běží ze stejného originu — viz roadmapa v `CLAUDE.md`.
