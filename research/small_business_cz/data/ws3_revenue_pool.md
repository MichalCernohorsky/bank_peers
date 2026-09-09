# WS3 – Datová tabulka: revenue pool segmentu small business (FOP + PO do 25 mil. Kč obratu) – [EST]
Stav k 2026-09-08. Model je **parametrický**: každý vstup je označen jistotou; výstup je jen tak dobrý, jak dobré jsou vstupy. Vstupy z ČNB (`[DATA GAP]`) nahradit po zpřístupnění ARAD, počty subjektů převzít z WS1.

## Postup
Revenue pool (roční provozní výnosy bank ze segmentu) = 
(1) NII z úvěrů = stav úvěrů segmentu × čistá úroková marže úvěrů (vč. funding benefitu) 
+ (2) NII z vkladů = stav vkladů segmentu × depozitní marže (repo − placená sazba, vážené dle mixu běžné/spořicí) 
+ (3) Poplatky = počet aktivních podnikatelských účtů × fee-ARPU (vedení účtu, platby, karty, FX, ostatní).
Bez pojištění, leasingu, investic (mimo bankovní účet a úvěr).

## Vstupy a jejich opora
| Vstup | Nízký | Střední | Vysoký | Opora / jistota |
|---|---|---|---|---|
| (1a) Stav úvěrů segmentu, mld. Kč | 120 | 180 | 250 | `[EST]` – KB SB 50,3 + Moneta SB 20,5 mld. (12/2025, `[FACT]`) = 71 mld.; scénáře odpovídají podílu KB+Moneta 59 % / 39 % / 28 %. **ČNB jmenovatel `[DATA GAP]`.** |
| (1b) Čistá úroková marže úvěrů vč. funding benefitu | 3,0 % | 3,5 % | 4,0 % | `[EST]` – Moneta Commercial NII/prům. úvěry 4,37 % (FY24) a 3,89 % (1Q26 anualiz.) `[FACT-dopočet]`, obsahuje i vkladovou marži segmentu → horní kotva; spread nových SME úvěrů (7,5–30 mil.) nad repo ≈ 1,6–1,9 pb (2025) `[FACT-snippet]` + funding benefit vkladů ≈ 1,5–2 pb. |
| (2a) Stav vkladů segmentu, mld. Kč | 250 | 350 | 450 | `[EST]` – Moneta Commercial vklady 109 mld. (3/2026, vč. SME/korp.) `[FACT]`; poměr vklady/úvěry v komerčním segmentu Moneta ≈ 1,0 (109/109), u KB celkem 1,25 (L/D 0,80) → pro small business (přebytek likvidity, nízká úvěrová penetrace) předpoklad vklady ≈ 1,8–2,1× úvěry. **ČNB jmenovatel `[DATA GAP]`.** |
| (2b) Depozitní marže (2026, repo 3,75 %) | 1,0 % | 1,5 % | 2,0 % | `[EST]` – běžné účty podnikatelů neúročené (marže ≈ repo 3,75 %) vs. spořicí/termínové (marže 0,5–1 pb); mix 50/50 (Moneta Commercial 3/2026: 48 % běžné / 52 % spořicí+term. `[FACT]`) → vážený 2,1–2,4 %; nízký scénář zohledňuje pokles repo a konkurenci o vklady. Moneta cost of funds na vkladech 1,99 % (1Q26) `[FACT]`. |
| (3a) Počet aktivních podnikatelských účtů (mil.) | 0,9 | 1,1 | 1,3 | `[EST]` – převzít z WS1 (aktivní FOP + PO × penetrace samostatného podnikatelského účtu). KB ne-fyzičtí klienti 242 tis. + Moneta komerční 125 tis. `[FACT/EST]` = 367 tis. u dvou bank. |
| (3b) Fee-ARPU (tis. Kč / účet / rok) | 2,0 | 3,5 | 5,0 | `[EST]` – Moneta Commercial poplatky 5,5 tis. Kč/klient (FY24, vč. SME/korp. → horní hranice) `[EST-dopočet]`; KB transakční+depozitní poplatky 1,35 tis. Kč/klient napříč všemi klienty `[EST-dopočet]`; podnikatelské účty jsou dražší než osobní (Finmag 2026 `[FACT-snippet]`). |

## Výsledek (mld. Kč / rok, 2026 běh)
| Složka | Nízký | Střední | Vysoký |
|---|---|---|---|
| (1) NII z úvěrů | 120 × 3,0 % = **3,6** | 180 × 3,5 % = **6,3** | 250 × 4,0 % = **10,0** |
| (2) NII z vkladů | 250 × 1,0 % = **2,5** | 350 × 1,5 % = **5,3** | 450 × 2,0 % = **9,0** |
| (3) Poplatky | 0,9 × 2,0 = **1,8** | 1,1 × 3,5 = **3,9** | 1,3 × 5,0 = **6,5** |
| **Revenue pool celkem** | **≈ 8** | **≈ 15** | **≈ 25** |
| Struktura (střední) | | úvěry 41 % / vklady 34 % / poplatky 25 % | |
Kontrola řádu `[EST]`: střední scénář 15 mld. Kč ≈ 6–7 % součtu provozních výnosů čtyř největších bank (ČS 59,2 + ČSOB 48,4 + KB 36,9 + Moneta 13,8 = ≈ 158 mld. Kč, FY 2025 `[FACT]` z fact sheetů: ČS key figures; ČSOB list P&L Ytd.; KB „Net banking income" součet čtvrtletí 2025; Moneta „Total operating income" součet čtvrtletí 2025) a ≈ 3× provozní výnosy celého Commercial segmentu Moneta (4,8 mld. Kč FY 2024 `[FACT]`, který zahrnuje i SME a korporace). Řád je konzistentní; přesnost ± 40 %.
Citlivost: ±1 pb depozitní marže = ±3,5 mld. Kč (střední); ±50 mld. Kč úvěrů = ±1,75 mld. Kč; ±1 tis. Kč fee-ARPU = ±1,1 mld. Kč. **Největší páka = vklady (cena peněz) – v prostředí repo 3,75 % je depozitní marže podnikatelských běžných účtů největší jednotlivá složka poolu.**

## Log odhadů
1. Všechny jmenovatele trhu (úvěry, vklady, účty) jsou předpoklady bez ČNB opory → doplnit ARAD (sektor domácnosti–živnostníci; nefinanční podniky – nové obchody do 7,5 mil. Kč; vklady dle sektorů) a WS1 (počty subjektů).
2. Unit economics kotveny na Moneta Commercial (obsahuje SME/korporace → nadhodnocuje NII/úvěry i fee/klient pro čisté small business) a KB (celobankovní poplatky → podhodnocuje).
3. Model neobsahuje výnosy z FX (významné pro Revolut/Wise) ani pojištění/leasing.
