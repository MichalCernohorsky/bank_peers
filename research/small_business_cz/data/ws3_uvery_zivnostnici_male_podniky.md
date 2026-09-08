# WS3 – Datová tabulka: úvěry a vklady živnostníků a malých podniků 2019–2026 (trh, ČNB)
Stav k 2026-09-08. **Upozornění:** přístup na www.cnb.cz (ARAD, měnová statistika, ZFS), kurzy.cz (zrcadlo ARAD) a cbamonitor.cz byl v této relaci blokován síťovou proxy; WebSearch kvóta vyčerpána. Řádky s trhem ČNB jsou proto `[DATA GAP]` s přesným umístěním sestavy k doplnění. Bankovní kotvy viz `ws3_kotvy_banky.md`.

## T1. Úvěry živnostníkům (ČNB, sektor domácností – podsektor S.14 „živnostníci"), stav ke konci období, mld. Kč, hrubé (Kč + cizí měna)
| Období | Stav úvěrů živnostníkům | y/y | z toho se selháním (NPL) | Nové úvěry živnostníkům (objem, rok) | Prům. sazba nových úvěrů |
|---|---|---|---|---|---|
| 12/2019 | `[DATA GAP]` | | | | |
| 12/2020 | `[DATA GAP]` | | | | |
| 12/2021 | `[DATA GAP]` | | | | |
| 12/2022 | `[DATA GAP]` | | | | |
| 12/2023 | `[DATA GAP]` | | 5,10 % (9/2023, ČBA Monitor) `[FACT]` | | |
| 12/2024 | `[DATA GAP]` | | | | |
| 12/2025 | `[DATA GAP]` | | | | |
| 7/2026 (poslední) | `[DATA GAP]` | | | | |
Kde doplnit: ČNB ARAD → Měnová a finanční statistika → Měnové finanční instituce → Úvěry → „Klientské úvěry podle sektorového hlediska (Kč + cizí měna)" (řádek „Domácnosti – živnostníci") a „Úvěry se selháním podle sektorů"; sazby: „Úrokové sazby korunových úvěrů poskytnutých bankami domácnostem – živnostníci (nové obchody)". URL: https://www.cnb.cz/cs/statistika/arad-system-casovych-rad/ ; měsíční PDF „Měnová statistika" (tab. „Úvěry domácnostem podle účelu/podsektoru"): https://www.cnb.cz/cs/statistika/menova_bankovni_stat/publikace-menove-statistiky/ (např. https://www.cnb.cz/export/sites/cnb/cs/statistika/.galleries/menova_bankovni_stat/menova_stat_publ/2025/menstat_2025-12_CZ.pdf). Sekundárně: ČBA Monitor https://www.cbamonitor.cz/statistika/nove-uvery-nefinancnim-podnikum a měsíční komentáře „Bankovní statistika za …" (https://www.cbamonitor.cz/aktuality/bankovni-statistika-za-zari-2025).
Definice: ČNB „živnostníci" = fyzické osoby podnikatelé (sektor domácností), bez ohledu na obrat; nezahrnuje s.r.o. Naše vymezení (obrat do 25 mil. Kč) je užší u FOP s vysokým obratem (zanedbatelné) a širší o malé PO (ty jsou v ČNB v „nefinančních podnicích").

## T2. Úvěry nefinančním podnikům (ČNB), stav, mld. Kč
| Období | Nefinanční podniky celkem | z toho malé podniky (dle velikosti – ověřit dostupnost) | Nové obchody do 7,5 mil. Kč (objem/rok) | Nové obchody 7,5–30 mil. Kč (objem/rok) |
|---|---|---|---|---|
| 12/2019–7/2026 | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` |
Ověřené útržky `[FACT – snippet, ČNB Měnová statistika 12/2024]`: meziroční tempo růstu úvěrů nefinančním podnikům 12/2024 **3,6 %**; úvěrů soukromému sektoru **5,5 %**; domácnostem **6,1 %** (zdroj: https://www.cnb.cz/export/sites/cnb/cs/statistika/.galleries/menova_bankovni_stat/menova_stat_publ/2025/menstat_2025-01_CZ.pdf, přes WebSearch). ČNB cnblog „Trendy v zadluženosti (nejen) nefinančních podniků": cizoměnové úvěry směřují primárně velkým a středním podnikům (https://www.cnb.cz/cs/o_cnb/cnblog/Trendy-v-zadluzenosti-nejen-nefinancnich-podniku/).
Poznámka k definici: ČNB v ARAD člení úvěry nefinančním podnikům podle **velikosti úvěru** (nové obchody do 7,5 mil. Kč / 7,5–30 mil. Kč / nad 30 mil. Kč – harmonizovaná statistika MIR) a v bankovní statistice podle **odvětví CZ-NACE**; členění podle **velikosti podniku** (mikro/malé/střední) je k dispozici jen v ZFS/analýzách ČNB (registr CRÚ), ne jako standardní sestava – `[DATA GAP – ověřit v ARAD „Úvěry nefinančním podnikům podle velikosti podniku"]`. Kategorie „nové obchody do 7,5 mil. Kč" je nejlepší dostupné proxy pro úvěry malým podnikům.

## T3. Vklady živnostníků a nefinančních podniků (ČNB), stav, mld. Kč
| Období | Vklady živnostníků (S.14 živn.) | Vklady nefinančních podniků | z toho jednodenní (běžné účty) |
|---|---|---|---|
| 12/2019–7/2026 | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` |
Kde: ARAD „Vklady klientů podle sektorového hlediska" (řádek Domácnosti – živnostníci; Nefinanční podniky). Bankovní kotvy: Moneta Commercial vklady 109,3 mld. Kč (3/2026), ČSOB klientské vklady 1 320 mld. (3/2026), KB běžné účty 585 mld. (3/2026) – viz kotvy.

## T4. Bankovní kotvy pro segment (mld. Kč, konec roku) – srovnatelnost omezená definicemi
| Rok | KB „Loans to small businesses" | ČSOB „SME loans" | Moneta Commercial celkem | Moneta nezajištěné SB úvěry + KTK | Moneta nové SB splátkové úvěry (rok) |
|---|---|---|---|---|---|
| 2020 | 45,9 | n.a. | n.a. | n.a. | n.a. |
| 2021 | 47,9 | n.a. | n.a. | n.a. | n.a. |
| 2022 | 46,8 | n.a. | 82,8 | 12,1 | n.a. |
| 2023 | 47,5 | n.a. | 83,8 | 13,5 | 4,0 |
| 2024 | 47,9 | 105,2 | 92,6 | 16,2 | 6,4 |
| 2025 | 50,3 | 115,4 | 104,0 | 20,5 | 8,4 |
| 1Q/2026 | 51,2 | 120,1 | 109,1 | 21,5 | 2,1 (1Q) |
Zdroj: IR fact sheety (lokální). Všechna `[FACT]`.
