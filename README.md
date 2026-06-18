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

## Stav
Hotová datová vrstva pro ČS (2002–Q1 2026), validace prochází.
Backend API a frontend jsou další na řadě — viz roadmapa v `CLAUDE.md`.
