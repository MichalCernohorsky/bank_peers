# WS3 – Datová tabulka: kotvy z investorských výkazů bank (KB, ČSOB, Moneta, ČS)
Zdroj: lokální investorské soubory v repozitáři (`KB-Facts-and-Figures-2026-1Q.xlsx`, `csob-fact-sheet.xlsx`, `mmb-1q2026-basic-financial-data.xlsx`, `mmb-4q2024-basic-financial-data.xlsx`, `key_figures_q1_2026.xlsx` + `data/cs_financials.db`). Všechna čísla `[FACT]` (primární zdroj – IR fact sheety bank), pokud není uvedeno jinak. Přístup 2026-09-08.
Poznámka k definicím: každá banka definuje „small business/SME" jinak – KB „Loans to small businesses (KB + ESSOX)" (vč. retailových úvěrů podnikajícím klientům ESSOX), ČSOB „SME loans" (malé A střední podniky – širší než náš segment do 25 mil. Kč obratu), Moneta „Commercial" segment (small business + SME + korporace + veřejný sektor). Žádná z nich neodpovídá přesně vymezení „obrat do 25 mil. Kč".

## T1. KB – klienti a úvěry malým podnikům (konec období, mil. Kč / počet)
| Období | Klienti KB celkem | z toho fyzické osoby | **Ne-fyzické osoby (podnikatelé, firmy, ostatní) – dopočet** | Úvěry malým podnikům (KB+ESSOX) | Podíl na úvěrech skupiny KB | Skupina KB – úvěry celkem (bez repo) |
|---|---|---|---|---|---|---|
| 4Q 2019 | 1 664 000 | 1 407 000 | 257 000 `[EST – rozdíl]` | n.a. | – | 654 000 |
| 4Q 2020 | 1 641 000 | 1 389 000 | 252 000 | 45 900 | 6,6 % | 691 400 |
| 4Q 2021 | 1 625 000 | 1 383 000 | 242 000 | 47 900 | 6,5 % | 738 900 |
| 4Q 2022 | 1 652 000 | 1 408 000 | 244 000 | 46 800 | 6,0 % | 784 900 |
| 4Q 2023 | 1 664 000 | 1 422 000 | 242 000 | 47 500 | 5,7 % | 827 700 |
| 4Q 2024 | 1 727 000 | 1 485 000 | 242 000 | 47 900 | 5,6 % | 848 300 |
| 4Q 2025 | 1 777 000 | 1 536 000 | 241 000 | 50 300 | 5,6 % | 905 800 |
| 1Q 2026 | 1 798 000 | 1 556 000 | 242 000 | 51 200 | 5,6 % | 914 100 |
Zdroj: KB Facts & Figures 1Q 2026, list „Business" (řádky Clients / Loan portfolio). „Ne-fyzické osoby" = KB celkem − Individual clients (dopočet; zahrnuje i korporace, municipality, neziskové organizace – horní hranice pro počet podnikatelských klientů KB). Poznámka KB: „** Including ESSOX retail loans to entrepreneuring clients".
Odvozeno: úvěry malým podnikům KB rostly 4Q 2020→4Q 2025 CAGR jen **1,9 % p.a.**; meziročně 1Q 2026 **+6,9 %** (zrychlení). Podíl na skupinovém portfoliu klesl z 6,6 % (2020) na 5,6 % (2025).

## T2. KB – struktura poplatků relevantní pro účty/platby (mil. Kč, čtvrtletně)
| Položka | 2021 (Σ) | 2022 (Σ) | 2023 (Σ) | 2024 (Σ) | 2025 (Σ) | 1Q 2026 |
|---|---|---|---|---|---|---|
| Transakční poplatky | 1 606 | 1 806 | 1 816 | 1 843 | 1 641 | 386 |
| Poplatky z depozitních produktů | 788 | 784 | 804 | 720 | 754 | 203 |
| Poplatky z úvěrů | 449 | 415 | 431 | 445 | 374 | 90 |
| Čisté poplatky a provize celkem | 5 712 | 6 122 | 6 414 | 7 291 | 6 954 | 1 638 |
Zdroj: KB Facts & Figures 1Q 2026, list „NFC structure" (součty čtvrtletí; 1Q–2Q 2025 restated). Poznámka: bez rozpadu na podnikatele – slouží jen jako kotva pro odhad fee-ARPU (transakční + depozitní poplatky 2025 = 2 395 mil. Kč / 1,78 mil. klientů ≈ **1,35 tis. Kč na klienta a rok** napříč všemi klienty `[EST – dopočet]`).

## T3. ČSOB – úvěry malým a středním podnikům a vklady (mld. Kč, konsolidováno)
| Datum | Úvěrové portfolio celkem | **SME loans** | Korporátní úvěry | Klientské vklady | z toho běžné účty | z toho spořicí | NPL ratio (ČNB metodika) | NIM (Ytd, anualiz.) |
|---|---|---|---|---|---|---|---|---|
| 31.12.2024 | 979,2 | 105,2 | 225,4 | 1 298,1 | 620,0 | 341,6 | 1,35 % | 2,42 % |
| 31.3.2025 | 1 009,5 | 108,1 | 242,3 | 1 296,8 | 604,3 | 372,2 | 1,34 % | 2,44 % |
| 30.6.2025 | 1 019,6 | 110,7 | 235,5 | 1 297,9 | 614,0 | 388,0 | 1,32 % | 2,43 % |
| 30.9.2025 | 1 042,4 | 113,2 | 236,9 | 1 311,4 | 606,0 | 399,7 | 1,29 % | 2,42 % |
| 31.12.2025 | 1 060,9 | 115,4 | 237,5 | 1 319,4 | 610,2 | 411,8 | 1,30 % | 2,41 % |
| 31.3.2026 | 1 084,0 | 120,1 | 242,4 | 1 319,7 | 607,9 | 421,3 | 1,28 % | 2,45 % |
Zdroj: ČSOB fact sheet (listy „Business volumes", „Additional information"). SME = malé a střední podniky (ČSOB nezveřejňuje hranici obratu ve fact sheetu – `[DATA GAP]` definice, hledat ve výroční zprávě ČSOB 2025, sekce segmenty). Odvozeno: SME úvěry ČSOB **+9,7 % (12/2024→12/2025)**, **+11,1 % y/y (3/2026)** – rostou rychleji než celé portfolio (+8,3 % / +7,4 %). Časová řada před 12/2024 v lokálním souboru není `[DATA GAP]`.

## T4. Moneta – segment Commercial (mil. Kč, konec období, čisté úvěry)
| Období | Commercial úvěry celkem | z toho Investiční | z toho Provozní (WC) | **z toho Nezajištěné splátkové + kontokorenty (small business)** | Commercial vklady | z toho běžné účty | NPL ratio Commercial |
|---|---|---|---|---|---|---|---|
| 4Q 2022 | 82 781 | 46 030 | 14 138 | 12 101 | 77 234 | 43 437 | 1,1 % |
| 4Q 2023 | 83 819 | 45 073 | 15 326 | 13 499 | 85 809 | 41 624 | 1,2 % |
| 4Q 2024 | 92 564 | 49 972 | 16 494 | 16 197 | 105 784 | 53 018 | 1,2 % |
| 4Q 2025 | 103 987 | 57 076 | 16 119 | 20 457 | 109 231 | 54 047 | 1,0 % |
| 1Q 2026 | 109 070 | 60 469 | 16 522 | 21 515 | 109 289 | 52 763 | 0,9 % |
Zdroj: Moneta basic financial data 4Q 2024 a 1Q 2026 (listy „Portfolio_Net loans", „Total deposits", „KPIs"). Odvozeno: nezajištěné small-business úvěry Moneta **+26,3 % y/y (4Q 2025)**, CAGR 4Q 2022→4Q 2025 **+19,1 %** – nejrychleji rostoucí produktová linie segmentu u sledovaných bank.

## T5. Moneta – nové objemy (mil. Kč, nerevolvingové produkty)
| Rok | Small Business Instalment Loans (nové) | Commercial nové objemy celkem | Podíl SB |
|---|---|---|---|
| 2023 | 3 990 | 17 523 | 22,8 % |
| 2024 | 6 362 | 25 493 | 25,0 % |
| 2025 | 8 357 | 31 548 | 26,5 % |
| 1Q 2026 | 2 138 | 9 168 | 23,3 % |
Zdroj: Moneta basic financial data, list „New Business Volumes" (součet čtvrtletí). Nové SB splátkové úvěry Moneta **2023→2025 více než 2×** (+109 %).

## T6. Moneta – ekonomika segmentu Commercial (mil. Kč)
| Položka | FY 2024 | 1Q 2026 (×4 anualizace `[EST]`) |
|---|---|---|
| Čistý úrokový výnos (NII) | 3 852 | 1 037 (4 148) |
| Čisté poplatky a provize | 686 | 196 (784) |
| Provozní výnosy celkem | 4 778 | 1 298 (5 192) |
| Znehodnocení (impairment) | −16 | +22 (rozpuštění) |
| Průměrné úvěry segmentu (dopočet) | 88 192 | 106 529 |
| **NII / prům. úvěry** `[EST – dopočet]` | **4,37 %** | **3,89 %** |
| Poplatky / prům. úvěry | 0,78 % | 0,74 % |
| Provozní výnosy / prům. úvěry | 5,42 % | 4,87 % |
| Cost of funds na klientských vkladech (banka celkem) | 2,25 % (4Q 2024) | 1,99 % (1Q 2026) |
Zdroj: Moneta basic financial data, list „Segment analysis", „KPIs". Segment obsahuje i SME/korporace – jednotkové hodnoty jsou kotva, ne přímo hodnota small business.
Počet komerčních klientů Moneta: 93,5 tis. (2016, IPO) → **125 tis.** (tisková zpráva Moneta „Od vstupu na burzu MONETA dosáhla 34% růstu v počtu komerčních klientů", cca 2022; https://www.moneta.cz/servis-pro-media/tiskove-zpravy/detail/od-vstupu-na-burzu-moneta-dosahla-34-rustu-v-poctu-komercnich-klientu-podil-na-tom-ma-digitalizace-produktove-nabidky-i-spoluprace-s-podpurnymi-programy – nalezeno přes WebSearch snippet, plný text nenačten (proxy)) `[FACT – snippet]`. Aktuální počet 2025/2026 `[DATA GAP]` (výroční zpráva Moneta 2025, investors.moneta.cz).
Dopočet `[EST]`: provozní výnosy Commercial FY 2024 / 125 tis. klientů ≈ **38 tis. Kč na komerčního klienta a rok** (z toho poplatky ≈ 5,5 tis. Kč, NII ≈ 31 tis. Kč) – horní hranice pro small business (segment obsahuje i větší firmy).

## T7. Česká spořitelna – skupinové kotvy (mil. Kč, reported IFRS)
| Rok | NII | Čisté poplatky | Provozní výnosy | Čisté klientské úvěry | Klientské vklady | NIM | NPL ratio | Pobočky |
|---|---|---|---|---|---|---|---|---|
| 2019 | 30 261 | 8 591 | 41 899 | 720 739 | 996 815 | 2,12 % | 1,8 % | 463 |
| 2020 | 29 099 | 8 243 | 40 147 | 749 415 | 1 100 450 | 1,94 % | 2,2 % | 424 |
| 2021 | 31 083 | 9 186 | 42 354 | 821 840 | 1 184 543 | 1,95 % | 2,1 % | 400 |
| 2022 | 36 719 | 9 504 | 49 875 | 900 534 | 1 256 795 | 2,13 % | 1,9 % | 398 |
| 2023 | 34 583 | 10 894 | 48 365 | 996 818 | 1 366 038 | 1,95 % | 1,8 % | 366 |
| 2024 | 39 811 | 12 778 | 56 486 | 1 076 242 | 1 483 174 | 2,03 % | 1,8 % | 337 |
| 2025 | 42 108 | 13 170 | 59 160 | 1 162 968 | 1 529 840 | 2,12 % | 1,6 % | 329 |
| 1Q 2026 | 10 723 | 3 396 | 15 398 | 1 190 553 | 1 654 880 | 2,11 % | 1,5 % | 324 |
Zdroj: ČS key figures Q1 2026 (`data/cs_financials.db`, basis reported). Počet klientů ČS 4 565 tis. (1Q 2026, peer PDF s31) a ~4,6 mil. (6/2025, ČTK: https://www.ceskenoviny.cz/zpravy/2704339). Korporátní úvěry ČS 493 mld. Kč (1Q 2026, peer PDF s21). **ČS nezveřejňuje ve fact sheetu počet podnikatelských klientů ani objem úvěrů small business – `[DATA GAP]` (výroční zpráva ČS 2025 – segment „Retail/SME", Erste Group factbook „Czech Republic – segment reporting").**
