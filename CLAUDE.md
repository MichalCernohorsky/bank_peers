# CLAUDE.md — Přehled finančních výsledků bank

Webová aplikace, která pravidelně stahuje finanční výsledky hlavních českých bank,
ukládá je do databáze a vykresluje konfigurací řízené dashboardy. Rozšiřitelné o další
banky a pohledy přidáním konfigurace, ne kódu.

## Struktura
```
config/
  metrics.yaml          kanonický katalog metrik = jediný zdroj pravdy (metric tabulka + dashboard)
  sources/cs.yaml       mapování metrik na řádky zdrojových výkazů ČS
schema/001_init.sql     DDL (bank, metric, period, fact, source, ingestion_run)
pipeline/
  ingest.py             parsování xlsx -> sloučená data (dle source mapy)
  build_db.py           schéma -> seed -> load -> FY rollup -> derivace -> validace
data/cs_financials.db   výstup (SQLite, dev)
api/                    backend (FastAPI) — TODO
web/                    frontend dashboard — TODO
```

## Datový model (klíčová pravidla)
- **fact** je „tidy" tabulka: 1 řádek = (banka, metrika, období, báze). Přidání metriky = řádek do `metric`, žádná migrace.
- **period** je explicitně `Q` (čtvrtletí) i `FY` (rok). Roční pohled = filtr `period_type='FY'`.
- **type** metriky řídí výpočet:
  - `flow` (výsledovka) — ve zdroji KUMULATIVNĚ YTD. Ukládá se samostatné čtvrtletí `value` (= YTD_n − YTD_(n−1)) a původní `value_ytd` jako audit. FY = Q4 YTD.
  - `stock` (rozvaha) — stav k datu, nikdy se neodečítá.
  - `ratio` — přebírá se (NIM, NPL, kap. přiměřenost) nebo dopočítává (LTD, C/I); interim poměry vyžadují anualizaci (`annualize` flag).
- **basis**: `reported` (z xlsx, kanonické) vs `adjusted` (peer-comparable z PDF). Most je na slide 51 peer PDF.
- **provenance**: každý fakt má `source_id`; `derived=1` = dopočítáno.

## Zdroj dat ČS
`key_figures_q1_2026.xlsx` (IR, reported IFRS, wide time series). Tři listy:
`Fin_Statements_IFRS9` (2018+, hlavní), `Fin_statements` (2013–2017, IAS39),
`Key_figures` (KPI 2002+, popisky ve sloupci B). Pozor: net profit = „attributable to owners";
náklady jsou záporné (flip_to_pos); net trading je ve 2 řádcích (sčítat).

## Spuštění
```
pip install openpyxl pyyaml
python -m pipeline.build_db config <xlsx> data/cs_financials.db
```
Pipeline na konci proběhne validací (rekonciliace P&L, součet čtvrtletí = FY, bilanční identita, kotva na headline).

## Stav
- HOTOVO: katalog metrik, source-mapping ČS, schéma, ingest+build pipeline, FY rollup, derivace (total_liabilities, LTD), validace (vše prochází). 30 ingestovaných + 2 odvozené metriky, 2002–Q1 2026.
- GAP (doplnit z reportů/PDF/Pillar3/Erste/ČNB): CET1, Tier1, RWA, leverage, LCR, NPL coverage, ROTE, EPS, gross loans, počet klientů, objemy úvěrů dle produktu, AUM, cost_of_risk (chybí gross loans).

## Další kroky (roadmapa)
3. Doplnit GAP metriky (extrakce z PDF/výkazů, LLM-asistovaně + validace).
4. Backend API (FastAPI) nad fact tabulkou — dotazy banka/metrika/období/báze.
5. Frontend na živá data (prototyp dashboardu -> volání API, vykreslení z `headline` + dashboard configu).
6. Další banky (KB, ČSOB, Moneta) — vlastní source-map per banka. [HOTOVO: config-driven multi-source; KB adjusted; ČSOB/Moneta čekají na data]
7. Scheduler navázaný na finanční kalendář, idempotentní běh, alerty. [HOTOVO: pipeline/watch.py + scheduler.py + .github/workflows/ingest.yml; staging→promote brána, checksum idempotence, vintage]; monitoring, deploy zbývá.

## Konvence
- Žádné natvrdo zadané hodnoty v kódu — vše z `config/`.
- Každý parser/derivace má mít test (fixture = reálný xlsx).
- Mapování zdroj→metrika je per banka v `config/sources/<bank>.yaml`.
