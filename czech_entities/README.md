# Ad-hoc analýza ekonomických subjektů v ČR

Jednorázová analýza: z veřejných registrů vytáhnout pro co nejširší množinu
ekonomických subjektů (vč. OSVČ) master data + rizikové příznaky + indicii
bankovního úvěru z účetní závěrky. Jeden běh → jeden dataset (parquet + xlsx).

**Není to produkt k opakovanému refreshi** — žádné servery, žádné delty. Vše
lokálně, idempotentně a resumovatelně (cache na disku, stav v DuckDB).

## ⚠️ Důležité zjištění k prostředí

Endpointy registrů byly ověřeny přes web (2026-07), ale **toto vývojové
prostředí má egress-politiku, která blokuje všechny cílové hosty**
(`ares.gov.cz`, `dataor.justice.cz`, `isir.justice.cz`, `or.justice.cz`,
`csu.gov.cz` → 403 na bráně). **Reálné stažení dat zde nelze provést** —
pipeline pusť ze stroje bez této blokace.

Kód je proto navržen tak, aby byl **plně funkční a offline otestovaný** na
syntetických vzorcích (viz `tests/`), a při reálném běhu jen doplnil data ze
sítě. Analytické jádro (parsování úvěru z rozvahy, validace IČO, join, export)
je ověřeno na reálných PDF/XML fixtures.

## Architektura (vrstvy dle obtížnosti a pokrytí)

| Vrstva | Zdroj | Obsah | Pokrytí |
|--------|-------|-------|---------|
| **A — master data** | ARES/RES bulk (VREO tar.gz) | IČO, název, právní forma, sídlo, NACE, datum vzniku, stav, DS | ~úplné |
| **B — rizika** | ISIR (SOAP) | `insolvence_flag`, stav řízení | subjekty v insolvenci |
| **C — úvěrová indicie** | sbírka listin (PDF) | `uver_flag`, `uver_castka` z rozvahy | částečné (jen PO se závěrkou) |

## Struktura
```
config/sources.yaml     endpointy + mapování polí (konvence: config, ne kód)
schema.sql              DuckDB schéma (subjekt, insolvence, zaverka_meta, uver, …)
src/
  ico.py                validace IČO (kontrolní číslice modulo 11)
  http_client.py        rate-limited stahování + retry/backoff + cache
  db.py                 DuckDB helpery + provenance (source, ingestion_run)
  layer_a_res.py        vrstva A: streamované parsování VREO tar.gz → subjekt
  layer_b_isir.py       vrstva B: ISIR SOAP inkrementální → insolvence
  justice_sbirka.py     klient sbírky listin (or.justice.cz HTML → PDF)
  pdf_extract.py        text z PDF + detekce skenu + OCR fallback (ocrmypdf)
  uver_parser.py        JÁDRO: extrakce úvěru z textu rozvahy
  layer_c_coverage.py   MILNÍK: coverage na vzorku 500 PO
  layer_c_extract.py    vrstva C: plná extrakce úvěru
  export.py             finální join → parquet + xlsx
  build.py              CLI orchestrátor
tests/                  offline testy všech vrstev (syntetické fixtures)
data/                   cache + DuckDB + výstupy (gitignored)
```

## Instalace
```bash
pip install -r requirements.txt
# pro OCR skenů (vrstva C) navíc systémově:
#   apt-get install ocrmypdf tesseract-ocr tesseract-ocr-ces
```

## Spuštění (pořadí dle SPEC)
```bash
cd czech_entities

python -m src.build init                 # schéma
python -m src.build layer-a --sample 5   # POZOR: nejdřív ověř XML mapování (viz níže)
python -m src.build layer-a              # RES/ARES bulk → univerzum (vrstva A)
python -m src.build layer-b              # ISIR → insolvence (vrstva B)
python -m src.build coverage --n 500     # MILNÍK: coverage vrstvy C na vzorku
#   → podle coverage % rozhodni rozsah vrstvy C
python -m src.build layer-c [--limit N]  # plná/omezená extrakce úvěru
python -m src.build export               # → data/ekonomicke_subjekty_cr.{parquet,xlsx}
python -m src.build status               # přehled stavu
```
Globální přepínače (`--db`, `--config`, `--cache`) se uvádějí **před** názvem
příkazu, např. `python -m src.build --db data/x.duckdb layer-a`.

### Ověření XML mapování VREO (nutné před vrstvou A na reálných datech)
Přesné názvy XML tagů ve VREO dumpu je nutné potvrdit proti reálnému vzorku:
```bash
python -m src.build layer-a --sample     # vypíše localname→hodnota prvních záznamů
```
Podle výpisu případně uprav `ares.vreo_field_map` v `config/sources.yaml`
(žádný zásah do kódu). Totéž platí pro HTML parsery v `justice_sbirka.py`
(parametry `subjektId`/`dokument` na or.justice.cz).

## Coverage milník (povinný před plnou vrstvou C)
`coverage --n 500` vezme náhodný vzorek právnických osob a změří:
- kolik má dohledatelnou účetní závěrku,
- kolik PDF je strojově čitelných vs. skenů (nutné OCR),
- úspěšnost extrakce položky úvěru.

Výstup je tabulka coverage % (konzole + tabulka `coverage_sample`). **Teprve
podle ní se rozhoduje, zda vrstvu C jet plošně.** Nepouštěj stahování/OCR
statisíců PDF bez tohoto měření.

## Výstup
Jeden dataset, jeden řádek na IČO. Sloupce:
`ico, nazev, pravni_forma, sidlo_kraj, sidlo_okres, nace, datum_vzniku, stav,
insolvence_flag, insolvence_stav, ma_zaverku_flag, posledni_rok_zaverky,
uver_flag, uver_castka, uver_rok, uver_zdroj, uver_confidence`

Provenance: každý fakt má dohledatelný zdroj (`source` / `*_zdroj`) a datum.
`uver_confidence` ∈ {`pdf_text`, `ocr`, `neurcito`}.

## Omezení (uveď uživateli)
- **Nelze** zjistit zůstatky úvěrů, kontokorenty, leasing bez zástavy ani
  bankovní produkty — jen rozvahový agregát k datu závěrky (bankovní tajemství).
- U **OSVČ a většiny neobchodních PO** je úvěrová vrstva prázdná (nemají
  uloženou závěrku v OR).
- **Zkrácený rozsah** rozvahy (mikro/malé jednotky) bankovní úvěry často
  nevyčleňuje → výsledek „nelze určit" (`uver_flag = NULL`). Neodhadujeme.
- **GDPR**: univerzum zahrnuje OSVČ (fyzické osoby). Zpracovávej jen nezbytné
  údaje a mysli na právní základ; filtrování polí u FO řeš v `export.py`.

## Rozhodnutí uživatele (z zadání)
- Prostředí plného běhu: **rozhodne se po coverage**.
- Roky závěrek ve vrstvě C: **poslední dostupný rok** (`roky_zpet: 1`).
- OSVČ: **zahrnuto vše**, GDPR filtrování na export fázi.

## Testy
```bash
python -m pytest tests -q          # nebo jednotlivě: python tests/test_*.py
```
Vše běží offline na syntetických fixtures (bez přístupu k síti).
