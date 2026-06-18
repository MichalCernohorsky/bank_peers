# Handoff pro Claude Code — Bank Results Dashboard

Tento dokument předává projekt `banks-dashboard` (v archivu `banks-dashboard.zip`) do Claude Code.
Cíl: z hotové datové vrstvy + náhledů udělat jednu běžící aplikaci, pak ji rozšířit na další banky
a automatické plnění daty. Architektura a konvence jsou v `CLAUDE.md` v rootu projektu — **přečti ho první.**

---

## 1. Co je hotové (nepřepisovat, stavět na tom)

- **Datový model + pipeline**: `schema/001_init.sql`, `pipeline/ingest.py`, `pipeline/build_db.py`.
  Načítá ČS xlsx (reported IFRS, 2002–Q1 2026), dopočítává samostatná čtvrtletí z YTD,
  roční (FY) řádky, odvozené metriky a běží validací (vše prochází).
- **Konfigurace = zdroj pravdy**: `config/metrics.yaml` (katalog metrik), `config/banks.yaml`,
  `config/sources/cs.yaml` (mapování výkazů ČS), `config/manual/*.csv` (potvrzená data z PDF + adjusted peer vrstva).
- **Dvě banky**: ČS (`reported`, plná historie) a KB (`adjusted`, peer-comparable Q1 2025+2026).
- **Backend**: `api/app.py` (FastAPI) — `/api/banks`, `/api/metrics`, `/api/facts`, `/api/dashboard/{bank}`, `/api/compare`.
- **Frontend náhledy** (zatím samostatné HTML s vloženým snapshotem, s fallbackem na API):
  `web/index.html` (plný přehled jedné banky, 36 metrik) a `web/compare.html` (HBR srovnání dvou bank).

## 2. Co zbývá (tento handoff)

A) Sloučit oba pohledy do jedné aplikace s přepínačem a napojit na živé API.
B) Produkční tvrdost (Postgres, env, Docker, testy).
C) Později: další banky (KB plně, ČSOB, Moneta) a automatické plnění fresh daty.
D) Nasazení.

---

## 3. Jak projekt rozjet (ověř první)

```bash
cd banks-dashboard
python -m venv .venv && source .venv/bin/activate
pip install openpyxl pyyaml fastapi "uvicorn[standard]"

# postavit databázi z ČS xlsx (cesta k tvému key_figures_q1_2026.xlsx)
python -m pipeline.build_db config /cesta/key_figures_q1_2026.xlsx data/cs_financials.db
# na konci musí projít validace (4x OK)

# spustit API
uvicorn api.app:app --reload --port 8000
# zkontroluj: http://localhost:8000/api/dashboard/cs  a  /api/compare?banks=cs,kb&basis=adjusted
```

---

## 4. Prompty pro Claude Code (copy-paste, v pořadí)

### PROMPT 1 — Rozjetí a ověření
```
Přečti CLAUDE.md a README.md. Vytvoř .venv, nainstaluj závislosti (openpyxl, pyyaml, fastapi,
uvicorn[standard]) a do requirements.txt je zapiš. Spusť `python -m pipeline.build_db config
<xlsx> data/cs_financials.db` a ověř, že validace na konci projde (4 kontroly OK). Spusť API
a curl-ni /api/dashboard/cs a /api/compare. Když něco selže, oprav a vysvětli proč.
```

### PROMPT 2 — Sloučit pohledy do jedné aplikace na živých datech
```
Cíl: jedna SPA aplikace místo dvou samostatných HTML.
1) V api/app.py přimountuj statické soubory z web/ přes StaticFiles tak, aby se frontend
   servíroval ze stejného originu jako API (kvůli fetch bez CORS problémů). Root "/" ať vrací
   sloučený frontend.
2) Vytvoř web/app.html (nebo uprav index.html) s horní navigací: "Přehled banky" a "Srovnání",
   plus selector banky (cs, kb — načti z /api/banks). 
   - Pohled "Přehled banky" znovupoužij renderovací funkce z web/index.html (KPI, grafy,
     tabulky kategorií) a data ber z /api/dashboard/{bank}.
   - Pohled "Srovnání" znovupoužij renderovací funkce z web/compare.html (párové sloupce,
     dumbbell, slopegraph) a data ber z /api/compare?banks=cs,kb&basis=adjusted.
3) Odstraň vložené snapshoty jako primární zdroj — čti z API; vložený snapshot ponech jen jako
   fallback pro offline náhled.
Nezaváděj žádné natvrdo zadané hodnoty; vše z API. Zachovej stávající vizuální styl.
```

### PROMPT 3 — Produkční tvrdost
```
1) Přidej podporu PostgreSQL vedle SQLite: connection string z env (DATABASE_URL), schema/001_init.sql
   uprav na kompatibilní variantu (SERIAL/IDENTITY, timestamptz) nebo přidej 001_init_postgres.sql.
   build_db ať umí cílit obě DB.
2) Config z prostředí: .env (DATABASE_URL, XLSX_PATH, ALLOWED_ORIGINS) + pydantic-settings.
3) Dockerfile + docker-compose (api + postgres). 
4) Testy (pytest): 
   - ingest/build pipeline proti reálnému xlsx jako fixture (zkopíruj malý vzorek do tests/fixtures),
   - kontrola, že validace projde,
   - test derivací (ytd_diff, FY rollup) a API endpointů.
5) Minimal CI (GitHub Actions): lint + pytest.
Drž se konvencí v CLAUDE.md.
```

### PROMPT 4 — (později) Přidat banku
```
Přidej banku <KB|ČSOB|Moneta>:
- Doplň ji do config/banks.yaml.
- Pokud má strukturovaný zdroj (xlsx/XBRL) jako ČS: vytvoř config/sources/<bank>.yaml podle vzoru
  cs.yaml (mapování řádků výkazu na kanonické `code`, basis=reported) a rozšiř pipeline/ingest.py,
  aby uměl víc zdrojů (parametr banky + cesta).
- Pokud máš jen peer/PDF data: přidej řádky do config/manual/peer_adjusted.csv (basis=adjusted).
- Spusť build_db a ověř, že validace ČS dál prochází a nová banka má data.
Pravidlo: nikdy nemíchej reported a adjusted v jednom grafu — srovnání jede na adjusted, deep-dive na reported.
```

### PROMPT 5 — (později) Automatické plnění fresh daty
```
Postav ingestion automatiku:
1) Watcher/scheduler (cron, APScheduler nebo GitHub Actions on schedule) navázaný na finanční
   kalendář bank (data zveřejnění výsledků). Konfigurace kalendáře v config/.
2) Pro každou banku: zkontroluj IR stránku / známé URL vzory / RSS na nový dokument (xlsx/PDF).
   Nový dokument -> ulož + checksum; pokud checksum už známe, přeskoč (idempotence).
3) Spusť stávající pipeline (build_db / per-bank ingest) nad novým souborem; zapiš do ingestion_run.
4) Validace jako brána: když rekonciliace neprojde nebo chybí headline metrika, NEpouštěj data
   do produkce a pošli alert (e-mail/Slack).
5) Provenance: každý fakt musí mít source (dokument + datum stažení); restatementy řeš přes as_of/vintage.
Pozn.: strukturovaný zdroj (ČS xlsx) preferuj; PDF parsuj jen když není jinak, ideálně LLM-asistovaně
s následnou schématickou validací.
```

### PROMPT 6 — Nasazení
```
Nasaď API + frontend (např. Fly.io/Render/Railway nebo VPS) s PostgreSQL. Scheduler jako
samostatný worker/cron. Přidej health-check endpoint a základní logování. Dokumentuj deploy v README.
```

---

## 5. Na co dát pozor (časté pasti)

- **Reported vs adjusted**: pole `basis`. ČS má reported (přesné, plná historie) i adjusted (peer).
  KB má zatím jen adjusted. Srovnání bank vždy na `basis='adjusted'`; jednobankový deep-dive na `reported`.
- **YTD**: výsledovkové (flow) metriky jsou ve zdroji kumulativní YTD; samostatné čtvrtletí = `YTD_n − YTD_(n−1)`,
  FY = Q4 YTD. Rozvaha = stav k datu. Poměry = anualizace u interim (`annualize` flag).
- **Zdroj ČS xlsx**: list `Key_figures` má popisky ve sloupci B (ne A); net profit = „attributable to owners";
  náklady jsou záporné (flip_to_pos); net trading je ve 2 řádcích (sčítat); starý list má překlep „commision".
- **Mezery (GAP)**: CET1, Tier1, RWA, LCR, leverage, ROTE, EPS, cost_of_risk, loan_loss_allowances —
  nejsou ve zdrojích, čekají na výkaz ČS / Erste / Pillar 3. V UI je nezobrazuj jako 0, ale jako chybějící.
- **Validace je brána**: build_db i automatika musí na neúspěšné rekonciliaci zastavit, ne publikovat.

## 6. Krok s Claude Designem (vizuál)

Až bude sloučená apka stát (PROMPT 2), vezmi frontend (HTML/komponenty pohledů „Přehled" a „Srovnání")
do Claude Designu a vylaď vzhled — rozložení, typografii, branding, dotažení HBR exhibitu. Pak uprav
frontend zpět v Claude Code. Design řeší jen vzhled; data, API a logika zůstávají v Claude Code.
