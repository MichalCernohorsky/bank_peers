# MLB Betting Data Pipeline — fáze 1 (data + features)

Datový základ pro predikční model MLB (totály, týmové totály, strikeout props).
Fáze 1 = historická databáze 2019–2025 + denní automatický update + feature
vrstva pro budoucí XGBoost model. Žádné predikce, žádné kurzy (tabulka `odds`
je připravená, ale prázdná).

## Instalace

```bash
cd mlb-data
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Vyžaduje Python 3.11+ a přístup na internet
(`statsapi.mlb.com` a `baseballsavant.mlb.com` přes pybaseball).

## 1) Jednorázový backfill historie 2019–2025

```bash
python -m src.backfill                    # všechno (několik hodin, ~17 000 zápasů)
python -m src.backfill --seasons 2024     # jen jedna sezóna
python -m src.backfill --limit 50         # rychlá zkouška na 50 zápasech
python -m src.backfill --skip-statcast    # bez Statcast dat (rychlejší)
```

- Skript je **resumovatelný**: po přerušení ho prostě spusť znovu, hotové
  zápasy přeskočí (`sezóna 2023: 1450/2430 zápasů` v logu ukazuje postup).
- Statcast se stahuje po měsících s pauzami a cachuje se do
  `data/statcast_cache/` — opakované spuštění nestahuje znovu.
- Na konci vypíše souhrn počtu řádků všech tabulek po sezónách.
- Sezóna 2020 je uložená, ale je to zkrácená covidová sezóna (60 zápasů) —
  ve features má příznak `is_covid_season`, pro trénink ji lze vyloučit.

## 2) Denní update (cron 11:00 CET)

```bash
python -m src.daily_update
```

Udělá: (a) dohraje finální výsledky ze včerejška i předevčírka, (b) stáhne
dnešní rozpis s ohlášenými startéry, (c) doplní Statcast za včerejšek,
(d) přepočítá features a spustí quality checks. Loguje do
`logs/daily_YYYY-MM-DD.log`. Všechny zápisy jsou idempotentní upserty —
opakované spuštění nic nerozbije.

### Nastavení cronu

```bash
crontab -e
```

a přidej řádek (uprav cestu k projektu):

```cron
CRON_TZ=Europe/Prague
0 11 * * * cd /cesta/k/mlb-data && .venv/bin/python -m src.daily_update >> logs/cron.log 2>&1
```

Pokud tvůj cron neumí `CRON_TZ`, nastav čas v UTC: `0 10 * * *` (v zimě `0 10`,
v létě `0 9`; jednodušší je nechat obě hodiny: `0 9,10 * * *` — druhý běh jen
potvrdí, že je vše hotové, díky idempotenci nic nerozbije).

## 3) Features pro model

```bash
python -m src.features
```

Přepočítá materializované tabulky (kompletně, bez data leakage — každý řádek
používá výhradně zápasy PŘED daným zápasem):

| tabulka | řádek | obsah |
|---|---|---|
| `v_pitcher_form` | start | K/9, BB/9, HR/9, xFIP, velo, whiff%, CSW%, nadhozy/start za posledních 5 / 10 startů / sezónu |
| `v_team_offense` | tým+zápas | runs/game L15/L30, K% a BB% pálkařů, runs/game proti L/R startérům |
| `v_bullpen_fatigue` | tým+zápas | nadhozy bullpenu za 1/2/3 dny zpět, počet reliéfů 2 dny po sobě |
| `v_game_features` | zápas | finální join: oba startéři, obě ofenzivy, bullpeny, park factors, počasí, odpočinek + cílové proměnné (`total_runs`, skóre, strikeouty startérů) |

Poznámky k metrikám (vědomé aproximace, viz komentáře v kódu):
- xFIP se počítá ze složek; fly bally se aproximují jako `airOuts + HR`
  (boxscore neobsahuje batted-ball typy), liga HR/FB = 10,5 %.
- xBA/xSLG proti jsou průměr očekávaných hodnot na odpálené míče (bez K).

## 4) Kontroly kvality

```bash
python -m src.quality_checks                       # plná kontrola
python -m src.quality_checks --skip-season-counts  # částečná data (uprostřed sezóny)
```

Kontroluje: počty zápasů na sezónu (±5), duplicity, NULL skóre u finálních
zápasů, kompletnost boxscore (2 startéři + 2 batting řádky na zápas), soulad
runs vs. skóre, rozsahy hodnot (IP 0–11, fastball 85–105 mph, teplota,
totály) a soulad Statcast pitch countu s boxscore. Nesrovnalosti vypisuje
konkrétně po `game_pk`. Exit code 0/1 → vhodné do cronu/CI.

## Testy

```bash
python -m pytest tests/ -q
```

15 testů běží offline (fixture = reálná struktura MLB API + syntetická
mini-liga), včetně důkazu **žádného data leakage**: featury zápasu se nezmění,
když se smažou všechna data z pozdějších dnů.

## Struktura databáze (SQLite `data/mlb.db`)

`teams`, `venues` (vč. park factors a typu střechy), `games` (jádro — 1 řádek
na zápas vč. počasí a startérů), `pitchers`, `pitcher_starts` (1 řádek na
start), `pitcher_starts_statcast` (velo/whiff/CSW/xBA/xSLG/barrel%),
`team_game_batting` (ofenziva týmu po zápasech vč. ruky soupeřova startéra),
`bullpen_appearances` (každý výstup reliéfa), `odds` (prázdná, generická —
sloupec `sport` pojme i NBA).

Schéma je definované přes SQLAlchemy bez SQLite-specifik — migrace na
PostgreSQL = změna connection stringu v `src/schema.py:get_engine`
(jediné dialektové místo je upsert helper, který PostgreSQL už podporuje).

## Park factors

Statická tabulka v `src/park_factors.py` (index 100 = neutrální prostředí),
orientační hodnoty z veřejných 3letých park factors. Aktualizace: přepiš čísla
a spusť `python -m src.backfill --only-reference`.
