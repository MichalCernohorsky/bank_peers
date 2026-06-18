-- Schéma: přehled finančních výsledků bank
-- SQLite (dev). Pro Postgres: INTEGER PRIMARY KEY -> SERIAL/IDENTITY, TEXT timestamps -> timestamptz.

CREATE TABLE bank (
    id                 INTEGER PRIMARY KEY,
    code               TEXT UNIQUE NOT NULL,        -- 'cs', 'kb', 'csob', ...
    name               TEXT NOT NULL,
    parent_group       TEXT,                        -- 'Erste Group', ...
    country            TEXT DEFAULT 'CZ',
    reporting_currency TEXT DEFAULT 'CZK'
);

-- Kanonický katalog metrik (seed z config/metrics.yaml)
CREATE TABLE metric (
    code          TEXT PRIMARY KEY,
    label_cs      TEXT,
    label_en      TEXT,
    category      TEXT,                              -- income_statement | balance_sheet | capital | asset_quality | ratios | business_volume
    unit          TEXT,                              -- CZK_m | percent | bps | count | ratio
    type          TEXT,                              -- flow | stock | ratio
    interim_basis TEXT,                              -- ytd_cumulative | point_in_time | ratio
    quarter_calc  TEXT,
    annual_calc   TEXT,
    annualize     INTEGER DEFAULT 0,
    formula       TEXT,
    headline      INTEGER DEFAULT 0
);

-- Provenance: odkud hodnota pochází
CREATE TABLE source (
    id           INTEGER PRIMARY KEY,
    bank_id      INTEGER REFERENCES bank(id),
    doc_type     TEXT,                               -- xlsx_ifrs9 | xlsx_kpi | xlsx_ias39 | report | peer_pdf | derived
    file         TEXT,
    sheet        TEXT,
    retrieved_at TEXT
);

-- Období: explicitně kvartál (Q) i rok (FY)
CREATE TABLE period (
    id          INTEGER PRIMARY KEY,
    bank_id     INTEGER REFERENCES bank(id),
    fiscal_year INTEGER NOT NULL,
    period_type TEXT NOT NULL,                       -- 'Q' | 'FY'
    quarter     INTEGER,                             -- 1..4, NULL pro FY
    period_end  TEXT,
    UNIQUE(bank_id, fiscal_year, period_type, quarter)
);

-- Centrální "tidy" tabulka faktů: 1 řádek = (banka, metrika, období, báze)
CREATE TABLE fact (
    id         INTEGER PRIMARY KEY,
    bank_id    INTEGER REFERENCES bank(id),
    code       TEXT REFERENCES metric(code),
    period_id  INTEGER REFERENCES period(id),
    basis      TEXT NOT NULL DEFAULT 'reported',     -- reported | adjusted
    value      REAL,                                 -- flow: samostatné čtvrtletí (Q) nebo rok (FY); stock: stav; ratio: hodnota
    value_ytd  REAL,                                 -- jen flow/Q: původní YTD hodnota (audit stopa)
    source_id  INTEGER REFERENCES source(id),
    derived    INTEGER DEFAULT 0,                    -- 0 = z dat, 1 = dopočítáno
    UNIQUE(bank_id, code, period_id, basis)
);

CREATE TABLE ingestion_run (
    id          INTEGER PRIMARY KEY,
    started_at  TEXT,
    finished_at TEXT,
    status      TEXT,
    rows_loaded INTEGER,
    log         TEXT
);

CREATE INDEX idx_fact_lookup ON fact(bank_id, code, basis);
CREATE INDEX idx_period_lookup ON period(bank_id, fiscal_year, period_type);
