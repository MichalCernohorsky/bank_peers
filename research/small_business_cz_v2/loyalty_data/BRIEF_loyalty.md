# Společný brief pro research agenty – věrnostní programy pro podnikatele a firmy (6. 10. 2026)

## Otázka
Existují věrnostní programy i pro firemní svět (FOP/mikro, SME, mid/large corporate), nebo jde čistě o retail? Jakou mají podobu, kdo je platí, fungují, a co z toho plyne pro Českou spořitelnu.

## Definice
**Věrnostní program** = opakovaná mechanika, která odměňuje klienta za setrvání, aktivitu nebo rozsah vztahu. Jednorázový akviziční bonus („X Kč za založení účtu") eviduj ZVLÁŠŤ (v poznámce nebo samostatném řádku s mechanikou „AKV"), nepočítej ho jako věrnostní program.

## Taxonomie (hlavní + případně vedlejší kategorie)
A karetní odměny (body, míle, cashback) na podnikatelské/firemní kartě · B cashback nebo úrok na podnikatelském účtu za aktivitu · C vztahový/tierový program (relationship pricing podle zůstatků/objemů) · D odměny financované obchodníky (card-linked offers) · E cena 0 výměnou za aktivitu („aktivitní nula") · F nefinanční benefity a služby jako odměna · G rebaty u korporátních karet (commercial/purchasing/travel) · H nebankovní B2B věrnostní programy (letecké, hotely, velkoobchod, palivo, telco, software).

Segmenty: FOP/mikro (do 10 zam.), SME, mid-corporate, large corporate; pokud program segment nedefinuje → „nedefinováno (odvozeno: …)".
Typ poskytovatele: banka, neobanka, karetní schéma, nebankovní firma.

## Pravidla ověřování (POVINNÉ)
- Značka u každého čísla a tvrzení: `[FACT]` (ověřeno ve zdroji s URL a datem), `[EST]` (výpočet, uveď vzorec), `[STALE: MM/RRRR]` (zdroj starší než 06/2026 – nesmí se vydávat za současný stav), `[CLAIM]` (tvrzení firmy, PR, marketing), `[DATA GAP: kde hledat]`.
- Cut-off 06/2026 pro popis aktuální nabídky. Zdroj bez data = `[STALE: datum neznámé]`.
- Primární zdroje mají přednost (produktové stránky, T&C, ceníky, výroční/IR zprávy). Články a srovnávače jen jako stopa; FACT jen pokud přímo citují podmínky.
- Žádná čísla z paměti modelu. Co nenajdeš = DATA GAP.
- Statistiky z agregátorů („X % firem s loyalty má o Y % vyšší retenci") bez metodiky zahoď, nebo označ `[CLAIM – agregátor, metodika neznámá]`.
- Měny v originále. Přepočet na Kč jen jako EST s kurzem ČNB a datem (pokud kurz nemáš ověřený, nepřepočítávej).
- **Prostředí:** WebFetch je blokovaný síťovou politikou (nezkoušej ho opakovaně – max. 1 pokus celkem). Používej WebSearch; FACT = ověřeno ve výtahu (snippetu) výsledku vyhledávání s URL. Datum zdroje uveď, pokud je ve výtahu/URL; jinak „datum neznámé" → u popisu nabídky STALE.
- Drž přidělený rozpočet vyhledávání. Pokud nestačí, uprav priority a zapiš, co zůstalo neověřeno.

## Formát výstupu agenta
1. Markdown soubor `<ws>.md` (česky): stručné shrnutí (5–8 bodů s čísly a značkami), pak sekce dle zadání, verdikty k relevantním hypotézám H1–H7, seznam DATA GAP, log zdrojů (URL · datum zdroje · datum přístupu 2026-10-06 · co z něj).
2. CSV soubor `<ws>.csv` (UTF-8, oddělovač `;`, hlavička přesně):
`id;region;zeme;poskytovatel;typ_poskytovatele;program;segment;mechanika_hlavni;mechanika_vedlejsi;co_se_odmenuje;forma_odmeny;kdo_financuje;podminka_vstupu_cena;tiery_prahy;datum_spusteni;stav;otevreny_podnikatelum;zdroj_url;datum_zdroje;datum_pristupu;znacka;poznamka`
   - region ∈ CZ / EU / WORLD; stav ∈ aktivni / ukonceny / nejasne; otevreny_podnikatelum ∈ ano / ne / nejasne.
   - V textových polích NEPOUŽÍVEJ středník; pokud je potřeba, použij čárku nebo „ / ".
   - id ve formátu prefix-číslo podle WS (CZ-01, EU-01, WD-01, CO-01 …).
   - Banka bez programu pro podnikatele v ČR = i tak řádek (program „žádný program pro podnikatele" nebo název retailového programu s otevreny_podnikatelum=ne/nejasne).
   - datum_pristupu = 2026-10-06.
3. Hypotézy:
- H1 U živnostníků a mikrofirem fungují věrnostní programy podobně jako v retailu (body, cashback, nabídky obchodníků), protože o bance rozhoduje majitel jako spotřebitel.
- H2 S rostoucí velikostí firmy mizí body a cashback a nahrazuje je vztahový pricing, rebaty na firemních kartách a balíčky služeb.
- H3 Ve velkých korporacích se věrnostní program v klasickém smyslu téměř nevyskytuje (loajalitu nese pricing, cash management, úvěr, RM).
- H4 Motorem odměn u firemních karet je vyšší interchange; stropy IFR 2015/751 se nevztahují na commercial karty → proto jsou odměny v USA velkorysejší než v EU.
- H5 Vedle bank vznikla vrstva odměn financovaných obchodníky (Visa, Mastercard, neobanky), kterou banka může převzít bez vlastního rozpočtu.
- H6 Mnoho podnikatelů používá pro byznys osobní bankovní produkty mj. kvůli odměnám → retailový program nepřímo ovlivňuje small business.
- H7 V ČR žádná banka nemá ucelený věrnostní program určený podnikatelům; konkurence používá jen cashback na podnikatelském účtu/kartě.
