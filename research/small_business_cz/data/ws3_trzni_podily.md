# WS3 – Datová tabulka: tržní podíly v segmentu small business (účty, úvěry, vklady) – [EST] s intervaly
Stav k 2026-09-08. Jmenovatel (trh dle ČNB) je `[DATA GAP]` – viz `ws3_uvery_zivnostnici_male_podniky.md`. Tabulka proto uvádí ověřené čitatele a podíl jako **podmíněný interval** (citlivost na jmenovatel), případně `[DATA GAP]`.

## T1. Počet podnikatelských klientů / účtů podle bank (čitatele)
| Banka | Ukazatel | Hodnota | Datum | Jistota | Zdroj |
|---|---|---|---|---|---|
| Komerční banka | Klienti KB celkem − fyzické osoby (= podnikatelé, firmy, municipality, NNO) | **242 tis.** (stabilní 241–244 tis. v 2021–2026; 257 tis. 2019) | 3/2026 | `[EST – dopočet z FACT]` | KB F&F 1Q 2026, list Business |
| Moneta | Komerční klienti (small business + SME + korporace) | **125 tis.** (93,5 tis. v 2016) | ~2022 | `[FACT – snippet TZ Moneta]` | TZ Moneta (URL v `ws3_kotvy_banky.md`) |
| Česká spořitelna | Klienti celkem (bez rozpadu na podnikatele) | 4 565 tis. | 3/2026 | `[FACT]` | peer PDF s31 |
| Česká spořitelna | Počet podnikatelů / malých firem | `[DATA GAP]` | | | Výroční zpráva ČS 2025 (https://www.csas.cz/cs/o-nas/pro-investory), TZ ČS (https://www.csas.cz/cs/o-nas/pro-media/tiskove-zpravy) |
| ČSOB | Počet podnikatelů / SME klientů | `[DATA GAP]` | | | Výroční zpráva ČSOB 2025 (https://www.csob.cz/portal/o-csob/vztahy-s-investory) |
| Raiffeisenbank / UniCredit / Air Bank / Fio / Creditas | Počet podnikatelských účtů | `[DATA GAP]` | | | výroční zprávy 2025, TZ; Fio (https://www.fio.cz/o-nas/tiskove-zpravy), Air Bank (https://www.airbank.cz/o-air-bank/pro-media) |
| Revolut / Wise | Počet business klientů v ČR | `[DATA GAP]` | | | TZ Revolut CZ |
Trh (jmenovatel): počet aktivních FOP + PO = výstup WS1 `[DATA GAP v tomto WS]`. Pokud by segment čítal ~1,0–1,4 mil. aktivních subjektů (rozpětí hypotéz H1.1–H1.2 plánu, neověřeno zde), pak KB s ≤242 tis. ne-fyzickými klienty drží **≤17–24 %** subjektů (horní hranice – číslo obsahuje i korporace/municipality) a Moneta se 125 tis. komerčními klienty **≤9–13 %** `[EST – podmíněné]`.
Průzkumy k doplnění: SME Banking Club (https://www.smebanking.club/), Datank „Banka roku – podnikatelé", Ipsos ČR (https://www.ipsos.com/cs-cz), ČBA/Ipsos „Bankovnictví očima podnikatelů" – vše `[DATA GAP]` (fetch blokován, WebSearch kvóta vyčerpána).

## T2. Úvěry segmentu – čitatele a podmíněné podíly
| Banka | Ukazatel (definice banky) | 12/2025 (mld. Kč) | Podíl při trhu 150 mld. | při 200 mld. | při 250 mld. | Jistota |
|---|---|---|---|---|---|---|
| KB | Loans to small businesses (KB+ESSOX) | 50,3 | 34 % | 25 % | 20 % | čitatel `[FACT]`, podíl `[EST – podmíněný]` |
| Moneta | Nezajištěné SB úvěry + KTK (Commercial) | 20,5 | 14 % | 10 % | 8 % | dtto (podhodnoceno – bez investičních úvěrů SB) |
| Moneta | Commercial celkem (vč. SME/korp.) | 104,0 | – | – | – | `[FACT]`, nesrovnatelné |
| ČSOB | SME loans (širší definice) | 115,4 | – | – | – | `[FACT]`, nesrovnatelné |
| ČS | Úvěry small business | `[DATA GAP]` | | | | VZ ČS 2025 / Erste factbook |
| Trh (ČNB živnostníci + malé PO) | | `[DATA GAP]` | | | | ARAD |
Jmenovatele 150/200/250 mld. Kč jsou **pouze citlivostní scénáře** (`[EST]` bez opory v ČNB datech): odvozeny tak, že KB+Moneta (≈71 mld. Kč v porovnatelných definicích) by drželo 28–47 % segmentu. Skutečný jmenovatel doplnit z ARAD (úvěry živnostníkům + nové obchody do 7,5 mil. Kč / úvěry mikro-podnikům dle ZFS).

## T3. Vklady segmentu – čitatele
| Banka | Ukazatel | Hodnota (mld. Kč) | Datum | Jistota |
|---|---|---|---|---|
| Moneta | Commercial vklady (vč. SME/korp.) | 109,3 | 3/2026 | `[FACT]` |
| KB | Běžné účty (všichni klienti) | 584,6 | 3/2026 | `[FACT]` – bez rozpadu |
| ČSOB | Klientské vklady – běžné účty (všichni) | 607,9 | 3/2026 | `[FACT]` – bez rozpadu |
| ČS | Klientské vklady (všichni) | 1 654,9 | 3/2026 | `[FACT]` – bez rozpadu |
| Trh: vklady živnostníků + nefin. podniků (ČNB) | | `[DATA GAP]` | | ARAD |
Podíly na vkladech segmentu: `[DATA GAP]` (žádná banka nezveřejňuje vklady podnikatelů do 25 mil. Kč obratu; ČNB sektorové členění je nutná kotva).
