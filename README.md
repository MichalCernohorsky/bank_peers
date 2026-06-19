# Bank Results Dashboard

Stahuje finanční výsledky hlavních českých bank, ukládá je do databáze a vykresluje
konfigurací řízené dashboardy. Viz `CLAUDE.md` pro architekturu a konvence.

## Quick start
```bash
pip install openpyxl pyyaml
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

## Stav
Hotová datová vrstva pro ČS (2002–Q1 2026), validace prochází (SQLite i PostgreSQL).
Backend API + sloučený frontend (`web/app.html`) běží ze stejného originu — viz roadmapa v `CLAUDE.md`.
