# CLAUDE.md — MLB Betting Data Pipeline

Datový základ pro predikční model MLB (totály over/under, týmové totály,
strikeout props startérů). Fáze 1 = historická DB 2019–2025 + denní update +
feature vrstva. Fáze 2 (později) = XGBoost model nad `v_game_features`.

Uživatel neprogramuje → komunikace česky, malé ověřitelné kroky, ukázky dat
po každém kroku, srozumitelné logy (česky). Kód, komentáře a názvy v DB anglicky.

## Struktura
```
mlb-data/
├── requirements.txt      pandas, SQLAlchemy, requests, pybaseball, pytest
├── data/mlb.db           SQLite (negitované; rebuild z veřejných zdrojů)
├── data/statcast_cache/  surové měsíční Statcast extrakty (cache, negitované)
├── src/
│   ├── schema.py         tabulky (SQLAlchemy, bez SQLite-specifik) + upsert()
│   ├── mlb_api.py        klient MLB Stats API (retry, rate limit) — jediné místo se sítí
│   ├── parsers.py        čisté funkce feed/live JSON -> řádky tabulek (testovatelné offline)
│   ├── park_factors.py   statická tabulka park factors (index 100)
│   ├── backfill.py       resumovatelný backfill 2019–2025
│   ├── statcast.py       pybaseball po měsících + agregace na (game_pk, pitcher)
│   ├── daily_update.py   včera+předevčírem finály, dnešní rozpis, statcast, features, checks
│   ├── features.py       v_pitcher_form / v_team_offense / v_bullpen_fatigue / v_game_features
│   └── quality_checks.py report PASS/FAIL s konkrétními game_pk, exit code 0/1
├── logs/                 backfill.log, daily_YYYY-MM-DD.log, ...
└── tests/                15 offline testů; synthetic.py = deterministická mini-liga
```

## Klíčová pravidla
- **Idempotence**: všechny zápisy přes `schema.upsert()` (ON CONFLICT DO
  UPDATE, SQLite i PostgreSQL). Opakované spuštění čehokoli nesmí vytvořit
  duplicity. Upsertují se vždy CELÉ řádky (částečný řádek narazí na NOT NULL).
- **Žádný data leakage**: features počítají helpery `*_from_prior()`, které
  dostávají výhradně zápasy PŘED daným zápasem (dřívější datum, u
  doubleheaderů nižší game_pk). Stejné helpery slouží historickým i budoucím
  zápasům → jedna cesta kódu. Hlídá to `tests/test_features.py::test_no_data_leakage`.
- **IP notace**: MLB „5.2" = 5⅔; ukládáme `outs_recorded` (přesné) i
  `innings_pitched` (pravý zlomek 5.6667) — nikdy nesčítat notaci 5.2!
- **Starter** = první pitcher v boxscore poli `pitchers`; zbytek = bullpen.
- **Sezóna 2020**: uložená, ve features `is_covid_season` (zkrácená, 60 zápasů).
- **Playoffs**: ukládají se, `game_type` != 'R' je odliší (R/F/D/L/W).
- **Net vyžadující kroky**: statsapi.mlb.com + baseballsavant.mlb.com; v
  sandboxu bez sítě běží testy a syntetické demo (`tests/synthetic.py`).

## Vědomé aproximace (zdokumentované v kódu)
- xFIP: fly bally ≈ airOuts + HR, liga HR/FB = 10,5 % (`features.py` konstanty).
- xBA/xSLG against: průměr `estimated_*_using_speedangle` na odpálené míče.
- Fastball velo: FF, fallback FF+SI při <5 FF nadhozech.

## Stav fáze 1
- HOTOVO: schéma (9 tabulek), parsery, backfill (resumovatelný), statcast
  modul s cache, daily_update, features (103 sloupců v `v_game_features`),
  quality checks, 15 testů, README s cron návodem.
- ZBÝVÁ (vyžaduje síť): reálný backfill 2019–2025, 3 dny denních běhů,
  namátková kontrola 5 zápasů proti MLB.com.
- NEDĚLAT ve fázi 1: model, kurzy (odds zůstává prázdná), web/Discord.
