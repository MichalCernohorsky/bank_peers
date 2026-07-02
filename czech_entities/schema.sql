-- Schéma DuckDB pro ad-hoc analýzu ekonomických subjektů v ČR.
-- Jeden běh -> jeden dataset. Návrh je "one row per IČO" pro finální výstup,
-- ale vrstvy jsou drženy zvlášť kvůli provenance a resumovatelnosti.

-------------------------------------------------------------------------------
-- Provenance: každý zdrojový soubor / stažení má záznam.
-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS source (
    source_id     INTEGER PRIMARY KEY,
    zdroj         TEXT NOT NULL,      -- 'RES', 'ARES', 'ISIR', 'DATAOR', 'SBIRKA_LISTIN'
    url           TEXT,
    soubor        TEXT,               -- lokální cesta v cache
    stazeno_at    TIMESTAMP,          -- kdy staženo
    poznamka      TEXT
);

-- Log běhů ingestu jednotlivých vrstev (pozorovatelnost dle SPEC).
CREATE TABLE IF NOT EXISTS ingestion_run (
    run_id        INTEGER PRIMARY KEY,
    vrstva        TEXT NOT NULL,      -- 'A_master', 'B_risk', 'C_coverage', 'C_extract'
    zahajeno_at   TIMESTAMP,
    dokonceno_at  TIMESTAMP,
    pocet_radku   BIGINT,
    pocet_chyb    BIGINT,
    stav          TEXT,               -- 'running','ok','failed'
    poznamka      TEXT
);

-------------------------------------------------------------------------------
-- VRSTVA A — master data (RES/ARES bulk). Univerzum = řádky této tabulky.
-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS subjekt (
    ico              TEXT PRIMARY KEY,   -- normalizované na 8 číslic
    ico_valid        BOOLEAN,            -- kontrolní číslice modulo 11 sedí
    nazev            TEXT,
    pravni_forma     TEXT,               -- kód právní formy (číselník ČSÚ)
    pravni_forma_txt TEXT,               -- text, je-li ve zdroji
    je_fo            BOOLEAN,            -- fyzická osoba / OSVČ (odvozeno z právní formy)
    sidlo_kraj       TEXT,
    sidlo_okres      TEXT,
    sidlo_obec       TEXT,
    sidlo_text       TEXT,               -- celá adresa, je-li
    nace             TEXT,               -- hlavní NACE/CZ-NACE
    datum_vzniku     DATE,
    stav             TEXT,               -- aktivní / v likvidaci / zaniklý ...
    datova_schranka  TEXT,               -- ID DS, je-li veřejné
    source_id        INTEGER,
    ingest_at        TIMESTAMP
);

-------------------------------------------------------------------------------
-- VRSTVA B — rizikové příznaky (ISIR insolvence, likvidace).
-- Join podle IČO. Držíme zvlášť, do finálu se promítne jako flag.
-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS insolvence (
    ico              TEXT,
    insolvence_flag  BOOLEAN,
    insolvence_stav  TEXT,               -- stav řízení (vyhlášen úpadek, konkurs, ...)
    spisova_znacka   TEXT,
    posledni_udalost_at DATE,
    source_id        INTEGER,
    ingest_at        TIMESTAMP
);

-------------------------------------------------------------------------------
-- VRSTVA C — úvěrová indicie z účetní závěrky.
-- Metadata sbírky listin: které IČO má uloženou závěrku a za jaké roky.
-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS zaverka_meta (
    ico              TEXT,
    rok              INTEGER,            -- rok, za který je závěrka
    typ_listiny      TEXT,              -- 'účetní závěrka', 'výroční zpráva' ...
    listina_url      TEXT,              -- odkaz na PDF ve sbírce listin
    dostupne_pdf     BOOLEAN,
    source_id        INTEGER,
    ingest_at        TIMESTAMP
);

-- Stav stahování/parsování jednotlivých PDF (idempotence + resume).
CREATE TABLE IF NOT EXISTS pdf_job (
    ico              TEXT,
    rok              INTEGER,
    listina_url      TEXT,
    lokalni_soubor   TEXT,
    stav             TEXT,               -- 'pending','downloaded','parsed','ocr','failed'
    je_sken          BOOLEAN,            -- nemá textovou vrstvu -> nutné OCR
    chyba            TEXT,
    updated_at       TIMESTAMP
);

-- Extrahovaná úvěrová indicie z rozvahy.
CREATE TABLE IF NOT EXISTS uver (
    ico              TEXT,
    rok              INTEGER,            -- rok závěrky
    uver_flag        BOOLEAN,            -- nalezena položka bankovních úvěrů > 0
    uver_castka      DOUBLE,             -- v tis. Kč (dle výkazu), NULL = nelze určit
    polozka_text     TEXT,               -- nalezený řádek rozvahy
    confidence       TEXT,               -- 'pdf_text','ocr','neurcito'
    zdroj_url        TEXT,
    source_id        INTEGER,
    ingest_at        TIMESTAMP
);

-------------------------------------------------------------------------------
-- Coverage report (milník před plnou vrstvou C).
-------------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS coverage_sample (
    ico              TEXT,
    ma_zaverku       BOOLEAN,
    pdf_stazeno      BOOLEAN,
    strojove_citelne BOOLEAN,            -- text vs. sken
    uver_extrahovan  BOOLEAN,
    poznamka         TEXT
);
