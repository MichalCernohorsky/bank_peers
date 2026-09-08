# 04 – WS3a: Profily 5 velkých bank v segmentu small business (FOP + PO do 25 mil. Kč obratu)
Stav 2025/2026 + vývoj od 2021 · Česká spořitelna (Erste), ČSOB (KBC), Komerční banka (SocGen), Raiffeisenbank (RBI), MONETA Money Bank · datum přístupu ke všem zdrojům: 2026-09-08

> **Metodická poznámka k omezením sběru dat (čti první).** V prostředí, kde tento soubor vznikal, byl (a) vyčerpán sdílený limit WebSearch po ~18 dotazech pro tento workstream a (b) síťová proxy blokovala přímý WebFetch na všechny testované domény bank a médií (csas.cz, kb.cz, csob.cz, rb.cz, moneta.cz, investors.moneta.cz, erstegroup.com, finmag.cz, mesec.cz, penize.cz, banky.cz, top.cz, wise.com, apps.apple.com, play.google.com, smlouvy.gov.cz, kurzy.cz, patria.cz, web.archive.org). Fakta níže pocházejí ze dvou typů zdrojů: **(1) primární IR data z lokálních souborů projektu** – `KB-Facts-and-Figures-2026-1Q.xlsx`, `csob-fact-sheet.xlsx` (1Q 2026), `mmb-1q2026-basic-financial-data.xlsx`, `mmb-4q2024-basic-financial-data.xlsx`, `key_figures_q1_2026.xlsx` (ČS) – tato čísla jsou plně ověřená [FACT]; **(2) úryvky z výsledků vyhledávání** (snippety stránek bank a médií) – označeny [FACT/snippet], protože plný text stránky nebyl načten a datum aktualizace stránky nelze potvrdit. Vše, co se nepodařilo ověřit, je [DATA GAP] s konkrétní URL, kde to dohledat. **Žádné číslo v tomto souboru není odhadnuto bez označení [EST].**

---

## (a) Hypotézy WS3a (a stav jejich ověření)

| # | Hypotéza | Stav po researchi |
|---|---|---|
| H3a.1 | Základní podnikatelský účet je u challengerů 0 Kč bez podmínek; z velké pětky ho zdarma bez podmínek dávají jen Moneta a Raiffeisenbank; ČS, KB a ČSOB drží podmíněné/placené modely. | **Potvrzeno** (ceníky/snippety 2025–2026): Moneta Konto PRO podnikání 0 Kč, RB CHYTRÝ účet 0 Kč, ČSOB základní firemní konto 0 Kč; ČS 0/75/149 Kč dle podmínek, KB 99 Kč s Profi programem. |
| H3a.2 | ČS v 2026 zdražila podnikatelské účty a jde proti trhu. | **Částečně potvrzeno**: Finmag 2026 uvádí, že „rozšířené verze" účtu ČS stojí od března 2026 599 a 899 Kč, „o stovku víc než do února 2026". Změna základní varianty [DATA GAP]. |
| H3a.3 | Nejsilnější online nezajištěný úvěr pro FOP má Moneta (Expres Business), KB (Profi úvěr) a ČSOB (Rychlý úvěr) drží pobočkově-hybridní model. | **Potvrzeno** v parametrech (Moneta 2,5 mil. Kč bez zajištění, 600 tis. Kč online za 15 min; ČSOB 150 tis. Kč bez zajištění, limit 1,5 mil. Kč; KB 1 mil. Kč bez dokládání příjmů, 5 mil. Kč celkem). |
| H3a.4 | Segment small business explicitně reportuje jen Moneta (nové objemy „Small Business Instalment Loans") a KB („Loans to small businesses"); ČS, ČSOB, RB ho v IR datech nevyčleňují. | **Potvrzeno** z IR souborů: Moneta a KB ano; ČSOB jen „SME loans" (širší), ČS jen „SME" v tiskové zprávě bez čísel za mikro; RB [DATA GAP]. |
| H3a.5 | Všechny velké banky zredukovaly pobočkovou síť 2021→2025 o 15–25 %, KB nejvíc. | **Potvrzeno**: ČS −17,8 % (400→329), KB −22,8 % (241→186), Moneta −20,3 % (153→122, 2022→2025); ČSOB a RB [DATA GAP]. |
| H3a.6 | Moneta má small business jako explicitní strategickou prioritu a roste v něm nejrychleji. | **Potvrzeno**: nové úvěry živnostníkům a malým firmám +31,4 % v 2025 (tisková zpráva FY2025, triangulováno s IR xlsx: 6 362 → 8 357 mil. Kč). |

---

## (b) Datové tabulky

### B1. Podnikatelský účet – cenové parametry (stav 2025/2026)

| Banka | Produkt (základní varianta pro FOP/malé PO) | Měsíční cena | Podmínky pro 0 Kč | Co je v ceně | Jistota / zdroj |
|---|---|---|---|---|---|
| Česká spořitelna | Podnikatelský účet **Živnostník** (dále Klasik, Maxi) | **149 Kč**; **75 Kč** při příjmu ≥ 10 000 Kč/měs. a současně aktivním úvěru/kontokorentu/hypotéce na stejné IČO; **0 Kč** 2 roky pro firmy do 6 měsíců od založení | viz vlevo | 50 elektronických transakcí zdarma, další tuzemská platba 7 Kč | [FACT/snippet] csas.cz/cs/firmy/ucty-podnikatele-firmy + Finmag 2026 |
| Česká spořitelna | „Rozšířené verze" (Klasik/Maxi – přiřazení variant k cenám [DATA GAP]) | **599 Kč a 899 Kč** od 1. 3. 2026 (+100 Kč vs. únor 2026) | – | [DATA GAP] | [FACT/snippet] Finmag 2026 |
| ČSOB | ČSOB Podnikatelské konto (FOP: základní + varianta s pojištěním); Firemní konto (PO: základní / širší / Extra) | **0 Kč** základní; **129 Kč** širší; Extra individuálně | základní bez podmínek | [DATA GAP] – sazebník csob.cz/firmy/poplatky-a-sazby | [FACT/snippet] Finmag 2026 |
| Komerční banka | **Profi účet** (Profi účet Gold = vyšší varianta) | **99 Kč**; 0 Kč při splnění podmínek **Profi programu** | Začínající podnikatelé (do 2 let od zahájení podnikání): 99 Kč vráceno následující měsíc při ≥ 1 aktivní transakci/měs. po dobu 2 let; ve 3.–4. roce bonus 70 Kč/měs. (Sazebník KB platný od 1. 5. 2025); web KB: „vedení zdarma 3 roky" pro začínající | KB+ aplikace, sdílení účtu s účetní (práva jen náhled / plná správa) | [FACT/snippet] kb.cz + Sazebník KB (PDF, smlouvy.gov.cz) |
| Raiffeisenbank | **CHYTRÝ účet pro podnikatele** / AKTIVNÍ / EXKLUZIVNÍ | **0 Kč** / **99 Kč** / **299 Kč** | CHYTRÝ: bez podmínek | výběry ze všech bankomatů v ČR i zahraničí zdarma, neomezené tuzemské a EUR platby, 1–2 debetní karty; AKTIVNÍ: 2 karty Mastercard Business, hromadné platby; až 17 měn | [FACT/snippet] rb.cz, Ceník FOP účinný od 1. 2. 2025 (rb.cz/attachments/podminky/2025/02/cenik-fop-po-1.pdf), Finex |
| MONETA | **Konto PRO podnikání** (FOP na IČO i PO); **Tom Plus** (FO/živnostník na rodné číslo) | **0 Kč** bez podmínek | – | 2 debetní karty zdarma, neomezené elektronické transakce, výběry z bankomatů Moneta/sdílených v ČR i zahraničí zdarma, elektronické výpisy | [FACT/snippet] moneta.cz/ucty-a-karty/konto-pro-podnikani |

Poznámka k definici: ceny se týkají „základního" balíčku; u ČS a KB je reálná cena pro typického aktivního FOP s úvěrem 75 Kč resp. 0 Kč, pro pasivního FOP bez úvěru 149 Kč resp. 99 Kč. Úrok na běžném účtu: u žádné z pěti bank nebyl v dostupných úryvcích uveden nenulový úrok [DATA GAP – sazebníky úroků].

### B2. Nezajištěný provozní/investiční úvěr pro FOP a malé PO

| Banka | Produkt | Max. bez zajištění | Celkový limit / splatnost | Sazba | Online / rychlost | Podmínky | Jistota / zdroj |
|---|---|---|---|---|---|---|---|
| ČS | Neúčelový nezajištěný úvěr pro začínající podnikatele (do 3 let od založení, bez dokládání historie) | **1,2 mil. Kč** | až 7 let | [DATA GAP] | žádost přes George / George Business | do 3 let od založení | [FACT/snippet] czechstartups.gov.cz, csas.cz/cs/firmy/uvery |
| ČS | Standardní nezajištěný podnikatelský úvěr | **500 tis. Kč** (nad to zajištění) | [DATA GAP] | [DATA GAP] | George Business | [DATA GAP] | [FACT/snippet] csas.cz/cs/firmy/uvery/specializovane-uvery – ověřit |
| ČSOB | **Rychlý úvěr na podnikání** | **150 tis. Kč** (peníze ihned po podpisu) | min. 50 tis. Kč, **limit 1,5 mil. Kč**, až 5 let, anuitní splátky | [DATA GAP] | žádost online, dořešení telefon/pobočka | podnikání ≥ 1 rok, účel se nedokládá | [FACT/snippet] Měšec/Peníze.cz TZ ČSOB, csob.cz |
| ČSOB | Podnikatelský úvěr (širší) | – | **až 10 mil. Kč** bez dokládání účelu | **od 6,9 % p. a.** (zvýhodněná) | online žádost | – | [FACT/snippet] csob.cz/firmy/uver |
| KB | **Profi úvěr** (+ Profi úvěr revolvingový, Profi úvěr Start) | **500 tis. Kč** (revolving); krátkodobý Profi úvěr **1 mil. Kč bez ověřování příjmů** (limit zvýšen z 500 tis.) | **až 5 mil. Kč**, 1–7 let; střednědobý do 3 let max. 500 tis. Kč | **od 5,9 % p. a.** | sjednání online v internetovém bankovnictví (stávající klienti) | klient s účtem 6 (příp. 12) měsíců bez výkazů a daňového přiznání | [FACT/snippet] kb.cz/…/profi-uver, Měšec TZ KB (datum TZ [DATA GAP]) |
| Raiffeisenbank | **Podnikatelská rychlá půjčka** | [DATA GAP] | [DATA GAP] | [DATA GAP] | [DATA GAP] | [DATA GAP] | penize.cz/podnikatelske-uvery/7685-raiffeisenbank-podnikatelska-rychla-pujcka; rb.cz/podnikatele. Vyhledávání vracelo jen retailovou Minutovou půjčku (5 tis.–1,2 mil. Kč, od 4,9 % p. a.) – **nepoužívat pro FOP** |
| MONETA | **Expres Business** (+ Zelený Expres Business, Program Expanze/NRB) | **2,5 mil. Kč** | [DATA GAP splatnost] | **„garance nejnižšího úroku na trhu"** – od 16. 3. 2026 dorovnání konkurenční nabídky | **online do 600 tis. Kč, výsledek do 15 min**, podpis online, peníze ihned; účet k úvěru zdarma | IČO, 12 měsíců podnikání, 2 doklady + orientační příjem, bez výkazů | [FACT/snippet] moneta.cz/pujcky-a-uvery/business-uver-nezajisteny |

Kontokorent (limit, sazba) a vývoj sazby vs. 2T repo ČNB: **[DATA GAP] u všech pěti bank** – dohledat v sazebnících úrokových sazeb (csas.cz/cs/podnikatele-firmy/ceniky; kb.cz Sazebník; csob.cz/firmy/poplatky-a-sazby; rb.cz ceník FOP; moneta.cz sazebník živnostníci a firmy) a ARAD ČNB (2T repo: 7,00 % 6/2022–12/2023, postupné snižování 2024–2025 – přesná řada [DATA GAP], viz WS4/ČNB).

### B3. Distribuce – pobočky, klienti, digitální uživatelé (primární IR data)

| Banka | Pobočky 12/2021 | 12/2022 | 12/2023 | 12/2024 | 12/2025 | 3/2026 | Δ 2021→2025 | Zdroj |
|---|---|---|---|---|---|---|---|---|
| Česká spořitelna (fyzické pobočky) | **400** | 398 | 366 | 337 | **329** | 324 | **−17,8 %** | [FACT] key_figures_q1_2026.xlsx, list Key_figures (od 6/2022 = fyzické pobočky, restated od 12/2018) |
| Komerční banka (retail branches vč. privátní, bez remote) | **241** | 217 | 210 | 204 | **186** | 172 | **−22,8 %** | [FACT] KB-Facts-and-Figures-2026-1Q.xlsx, list Operations |
| KB Poradenství outlets (síť KB Poradenství) | n.a. | n.a. | n.a. | 187 | 193 | 203 | – | [FACT] tamtéž |
| ČSOB | [DATA GAP] | | | | | | | csob.cz/o-csob/vyrocni-zpravy (fact sheet pobočky neuvádí) |
| Raiffeisenbank | [DATA GAP] | | | | | | | rb.cz/o-nas/vyrocni-zpravy |
| MONETA | n.a. | **153** | 134 | 124 | **122** | 123 | −20,3 % (2022→25) | [FACT] mmb-4q2024 + mmb-1q2026 basic-financial-data.xlsx, KPIs |

Doplňkové ukazatele [FACT]:
- ČS: FTE skupiny 9 711 (12/2021) → 9 483 (12/2025) → 9 299 (3/2026); aktivní platební karty 3 146 tis. (12/2021) → 4 380 tis. (12/2025). Klienti: „cca 4,6 mil." (Patria/VZ 2025 snippet) vs. „více než 5 mil." (csas.cz „Who we are") – **rozdíl definic (aktivní vs. celkoví klienti), nemíchat**.
- KB: klienti KB 1 625 tis. (12/2021) → 1 777 tis. (12/2025) → 1 798 tis. (3/2026); z toho fyzické osoby 1 383 tis. → 1 536 tis. → 1 556 tis.; **uživatelé KB+ 1 673 tis. (3/2026)**, 137 tis. (12/2023). [EST] Klienti KB mimo fyzické osoby (= podnikatelé, firmy, veřejný sektor): 242 tis. (12/2021) → 241 tis. (12/2025) → 242 tis. (3/2026) – výpočet „KB clients − individual clients"; **stagnace počtu ne-retailových klientů KB za 4 roky**. Pozn.: „individual clients" KB pravděpodobně zahrnují i FOP na rodné číslo – definici ověřit v KB F&F příloze. FTE KB (metodika ČSÚ) 6 694 (12/2021) → 5 617 (3/2026).
- Moneta: klienti skupiny 1,6 mil. (3/2025, +8,3 % y/y; Investiční web); FTE průměr 2 479 (4Q 2025).
- Business bankéři / RM: [DATA GAP] u všech bank – dohledat ve výročních zprávách (kapitola „Distribuce") nebo v tiskových zprávách o transformaci sítě (KB 2023–2025 „nová KB", ČS „poradenská centra").

### B4. Finanční metriky segmentu – co banky skutečně reportují (primární IR data)

| Banka | Reportovaná položka nejbližší našemu segmentu | 12/2021 | 12/2022 | 12/2023 | 12/2024 | 12/2025 | 3/2026 | Definice vs. naše (obrat ≤ 25 mil. Kč) |
|---|---|---|---|---|---|---|---|---|
| **KB** | „Loans to small businesses (KB + ESSOX)", mld. Kč, vč. ESSOX retail úvěrů podnikatelům | **47,9** | 46,8 | 47,5 | 47,9 | **50,3** | **51,2** | KB interní segment „small business" (hranice nezveřejněna v F&F, [DATA GAP]); růst 2021→2025 jen **+5,0 %**, 1Q26 y/y +6,9 % |
| **MONETA** | „Total Commercial" net loans, mld. Kč | n.a. | 82,8 | 83,8 | 92,6 | **104,0** | **109,1** | Commercial = SME + živnostníci + finanční a veřejné instituce → **širší než náš segment** |
| MONETA | z toho „Unsecured Instalment Loans and Overdraft" (commercial), mld. Kč | n.a. | 12,1 | 13,5 | 16,2 | **20,5** | **21,5** | nejbližší proxy pro small business úvěry; +69 % 2022→2025 |
| MONETA | Nové objemy „Small Business Instalment Loans", mil. Kč / rok | n.a. | 918 (jen 4Q) | **3 990** | **6 362** | **8 357** | 2 138 (1Q) | **jediná explicitní small-business řada z pětky**; +59,4 % (2024), **+31,4 % (2025)** – shoduje se s TZ Moneta FY2025 „nové úvěry živnostníkům a malým firmám +31,4 %" → triangulováno; 1Q26 y/y +20,0 % |
| MONETA | Commercial deposits, mld. Kč | n.a. | 77,2 | 85,8 | 105,8 | **109,2** | 109,3 | |
| MONETA | Podíl segmentu Commercial na provozních výnosech | | | | **37,0 %** (4 778 / 12 911 mil. Kč) | [DATA GAP FY25] | 36,7 % (1Q26) | |
| MONETA | Náklady rizika Commercial | | | | net impairment −16 mil. Kč na ø 88 mld. Kč ≈ **0,02 %** [EST, výpočet] | [DATA GAP] | +22 mil. Kč (rozpuštění) | NPL Commercial ~1 % (xlsx zaokrouhleno, přesná hodnota [DATA GAP]) |
| **ČSOB** | „SME loans / Úvěry malým a středním podnikům", mld. Kč | [DATA GAP] | [DATA GAP] | [DATA GAP] | **105,2** | **115,4** | **120,1** | SME ≠ small business (zahrnuje i střední firmy); +9,7 % 2025; 10,9 % úvěrového portfolia (1 060,9 mld. Kč) |
| **ČS** | Firemní úvěry celkem (TZ 2025): +7,7 % na 427,3 mld. Kč (CZ TZ) / +7,6 % na 444,4 mld. Kč vč. dceřiných spol. (EN TZ, SME +7,7 %, large corp +8,9 %, public +16,1 %) | | | | | ✔ | | **ČS segment „micro/small business" ve veřejných IR datech nevyčleňuje** → [DATA GAP]; dohledat: Erste Group Factbook (segment „Czech Republic – Retail / Corporates", položka „Micros"), VZ ČS 2025 (vz-2025-cs.pdf), sekce segmentové výkaznictví |
| **Raiffeisenbank** | [DATA GAP] | | | | | | | RB a.s. nereportuje segment; RBI reportuje jen „Czech Republic" jako celek – dohledat VZ RB 2023–2025 a RBI Investor Presentation |

Poznámka: NIM, cost of risk a NPL **za segment small business** nezveřejňuje žádná z pěti bank (Moneta jen na úrovni Commercial). Celobankovní NPL/CoR jsou v `data/cs_financials.db` a IR xlsx, ale pro segment nejsou vypovídající.

### B5. Digitální platforma (stav 2026)

| Banka | Aplikace pro podnikatele | Online založení FOP / s.r.o. | Hodnocení App Store / Google Play | Pokrytí funkcí (z dostupných zdrojů) |
|---|---|---|---|---|
| ČS | **George** (FOP na RČ i IČO) + **George Business** (samostatná aplikace pro firmy; Google Play `cz.csas.georgego.business`, App Store id6479615359, Huawei AppGallery) | ANO (web uvádí online založení účtu; čas [DATA GAP]); s.r.o. [DATA GAP] | **[DATA GAP]** – obchody blokovány; URL: apps.apple.com/cz/app/george-business-česko/id6479615359, play.google.com/store/apps/details?id=cz.csas.georgego.business | platby tuzemské/SEPA/SWIFT/inkaso, autorizace, historie, přepínání více firem, správa karet, biometrie [FACT/snippet csas.cz] |
| KB | **KB+** (jedna aplikace pro retail i podnikatele, 1 673 tis. uživatelů 3/2026 [FACT F&F]) | ANO – Profi účet lze otevřít a spravovat „na pár kliknutí" v KB+; s.r.o. [DATA GAP] | **[DATA GAP]** | pojmenování účtu, disponenti, **sdílení účtu s účetní s granularitou práv**, sjednání Profi úvěru online [FACT/snippet kb.cz] |
| ČSOB | ČSOB Smart (FOP), CEB / ČSOB Business Connector (PO) | ANO – „podnikatelský účet online" (Finmag 2026) | **[DATA GAP]** | [DATA GAP] |
| Raiffeisenbank | Raiffeisenbank mobilní aplikace (jedna pro FOP i PO) | [DATA GAP] | **[DATA GAP]** | až 17 měn, hromadné platby/import (AKTIVNÍ) [FACT/snippet] |
| MONETA | **Smart Banka** | **ANO – „zařízený plně online"** (Konto PRO podnikání); Expres Business celý proces online vč. podpisu | **[DATA GAP]** | online směnárna a cizoměnový účet pro podnikatele [FACT/snippet moneta.cz] |

Propojení na účetní SW (Fakturoid, iDoklad, Pohoda, Money S3), API/PSD2, bankovní identita, platební terminály/brány (ČS–Global Payments, KB SmartPay, ČSOB, Moneta), kreditní karty, factoring, leasing (dcery), pojištění, FX/zahraniční platby, ESG produkty: **[DATA GAP] pro všechny banky** kromě: Moneta „Zelený Expres Business" (ESG varianta úvěru, [FACT/snippet]), Moneta online směnárna [FACT/snippet], KB Factoring 13,0 mld. Kč a SGEF (leasing) 39,5 mld. Kč portfolio 3/2026 [FACT F&F – skupinové, ne segmentové], ČSOB Leasing 59,3 mld. Kč a Factoring 7,4 mld. Kč 3/2026 [FACT fact sheet – skupinové].

### B6. Cenový vývoj 2021 → 2023 → 2026 (základní podnikatelský účet)

| Banka | 2021 | 2023 | 2025 | 2026 | Zdroj / gap |
|---|---|---|---|---|---|
| ČS Živnostník | [DATA GAP] | [DATA GAP] | [DATA GAP] | 149 / 75 / 0 Kč; vyšší varianty 599 / 899 Kč od 3/2026 (+100 Kč) | Finmag 2025 (finmag.cz/finance/470899-…) nebylo možné načíst; archiv ceníků csas.cz/cs/podnikatele-firmy/ceniky; web.archive.org |
| KB Profi účet | [DATA GAP] | [DATA GAP] | 99 Kč (Sazebník 1. 5. 2025) | 99 Kč / 0 Kč Profi program | Sazebník KB 2021/2023 na web.archive.org |
| ČSOB Podnikatelské konto | [DATA GAP] | [DATA GAP] | [DATA GAP] | 0 Kč základní; 129 Kč širší (PO) | Finmag 2025/2026 |
| RB CHYTRÝ / AKTIVNÍ | [DATA GAP] | [DATA GAP] | 0 / 99 / 299 Kč (ceník 1. 2. 2025) | 0 / 99 / 299 Kč | ceník FOP 2/2025 |
| Moneta Konto PRO podnikání | [DATA GAP] | [DATA GAP] | 0 Kč | 0 Kč | – |

Sazby kontokorentu vs. repo: [DATA GAP] (viz B2).

---

## (c) Profily bank

### C1. Česká spořitelna (Erste Group) – největší síť a nejdražší základní účet z pětky; segment mikrofirem v IR datech neviditelný

- **Definice segmentu:** ČS na webu odděluje „Účty pro podnikatele a malé firmy" (Živnostník / Klasik / Maxi) od „firem" [FACT/snippet]. Obratová hranice segmentu a obsluhový model (pobočka vs. business bankéř vs. digitál) nebyly v dostupných úryvcích uvedeny → [DATA GAP]; dohledat ve VZ 2025 (csas.cz/banka/content/inet/internet/cs/vz-2025-cs.pdf, kapitola segmenty) a v Erste Group Factbook (segment CZ, „Micros" bývá součástí Retail).
- **Produkt:** účet 149 Kč / 75 Kč (příjem ≥ 10 tis. Kč + aktivní úvěr) / 0 Kč (start-up do 6 měsíců, 2 roky); 50 e-transakcí zdarma, dále 7 Kč [FACT/snippet]. Úvěry: nezajištěný úvěr pro začínající podnikatele do **1,2 mil. Kč** na 7 let bez historie (do 3 let od založení) [FACT/snippet czechstartups.gov.cz]; standardní nezajištěný limit 500 tis. Kč [FACT/snippet – ověřit]; žádosti přes George Business. Sazby, kontokorent, terminály (partnerství s Global Payments), účetní integrace: [DATA GAP].
- **Digitál:** George + samostatný George Business (tři app stores) [FACT/snippet]; hodnocení [DATA GAP].
- **Distribuce:** 400 → 329 fyzických poboček (12/2021 → 12/2025), 324 v 3/2026 [FACT]; stále **největší síť z pětky** (KB 186, Moneta 122). FTE 9 483 (12/2025).
- **Finance segmentu:** FY2025 čistý zisk 27,8 mld. Kč, provozní zisk 33,9 mld. Kč; firemní úvěry +7,7 % na 427,3 mld. Kč (CZ TZ) resp. +7,6 % na 444,4 mld. Kč vč. dcer s SME +7,7 % (EN TZ) [FACT/snippet, dva zdroje – rozdíl = konsolidační obvod]. **Mikro/small business ČS nevyčleňuje** → [DATA GAP]. Podíl trhu dle thebanks.eu 18,30 % (2025, „2. největší banka") – metodika nejasná, nepoužívat bez ověření [CLAIM].
- **Strategie:** tisková zpráva FY2025 zdůrazňuje investice a hypotéky jako tahouny [FACT/snippet]; veřejné výroky managementu ke small business 2023–2026 [DATA GAP] (dohledat: csas.cz/cs/o-nas/pro-media, rozhovory CEO/člena představenstva pro firemní bankovnictví).
- **Cenový vývoj:** +100 Kč u vyšších variant od 3/2026 [FACT/snippet Finmag]; historie 2021/2023 [DATA GAP].

### C2. ČSOB (KBC) – bezplatné základní konto a hybridní „Rychlý úvěr"; SME kniha 115 mld. Kč roste ~10 %, small business zvlášť nereportuje

- **Definice:** web rozlišuje účty pro podnikatele (FOP, 2 varianty) a pro firmy (3 varianty) [FACT/snippet Finmag 2026]; hranice segmentu a obsluhový model [DATA GAP].
- **Produkt:** základní konto 0 Kč, širší 129 Kč, Extra individuálně [FACT/snippet]. **Rychlý úvěr na podnikání**: 50 tis.–1,5 mil. Kč, do 150 tis. Kč bez zajištění s výplatou ihned po podpisu, až 5 let, podnikání ≥ 1 rok, účel se nedokládá; žádost online, dokončení telefon/pobočka [FACT/snippet TZ ČSOB]. Širší nabídka až 10 mil. Kč od 6,9 % p. a. bez dokládání účelu [FACT/snippet csob.cz/firmy/uver]. „Úvěr pro obchodníky" (proti obratu na terminálu) existuje [FACT/snippet URL]. ČSOB má vlastní portál „Průvodce podnikáním" (pruvodcepodnikanim.cz) [FACT/snippet].
- **Digitál:** ČSOB Smart / CEB; online založení podnikatelského účtu ANO [FACT/snippet]; ratingy [DATA GAP].
- **Distribuce:** [DATA GAP] pobočky (fact sheet neuvádí; ČSOB navíc sdílí síť s Poštovní spořitelnou/Českou poštou – definici ověřit).
- **Finance:** SME loans 105,2 → 115,4 → 120,1 mld. Kč (12/2024 → 12/2025 → 3/2026), +9,7 % 2025, 10,9 % úvěrového portfolia [FACT fact sheet]; leasing 57,9 mld. Kč, factoring 6,9 mld. Kč (12/2025) [FACT]. Celoskupinový NPL ~1 %, C/I 49 % (2025) [FACT]. Small business jako podsegment [DATA GAP] (KBC reportuje „Czech Republic business unit" bez rozpadu na mikro).
- **Strategie:** [DATA GAP] – dohledat KBC strategy update a VZ ČSOB 2025.

### C3. Komerční banka (Société Générale) – nejlépe strukturovaná nabídka pro FOP (Profi program, Profi úvěr, KB+), ale kniha small business stagnuje

- **Definice:** KB reportuje ve Facts & Figures samostatnou řadu „Loans to small businesses (KB + ESSOX)" [FACT]; hranice segmentu (obrat/expozice) v F&F neuvedena [DATA GAP – VZ KB, sekce segmentů: Retail vs. Corporate; small business je v KB součástí Retail).
- **Produkt:** Profi účet 99 Kč / 0 Kč v Profi programu; pro začínající 2 roky 99 Kč zpět při ≥ 1 transakci, 3.–4. rok bonus 70 Kč (Sazebník 1. 5. 2025) [FACT/snippet]; Profi účet Gold; Profi program pro členy profesních komor [FACT/snippet URL]. **Profi úvěr** až 5 mil. Kč, 1–7 let, od 5,9 % p. a.; 500 tis. Kč bez zajištění (revolving); krátkodobý Profi úvěr **1 mil. Kč bez ověřování příjmů** (zvýšeno z 500 tis.); online v bankovnictví; klient s účtem 6/12 měsíců bez výkazů [FACT/snippet]. Profi úvěr Start (začínající), Profi úvěr pro začínající zemědělce [FACT/snippet URL]. Terminály KB SmartPay, factoring (KB Factoring 13,0 mld. Kč), leasing SGEF (39,5 mld. Kč) – skupinová čísla 3/2026 [FACT F&F].
- **Digitál:** KB+ 1 673 tis. uživatelů (3/2026) z 1 798 tis. klientů = **93 % penetrace** [FACT + výpočet]; sdílení účtu s účetní s granulárními právy [FACT/snippet]; ratingy [DATA GAP].
- **Distribuce:** 241 → 186 retail poboček (2021→2025), 172 v 3/2026; **+ síť KB Poradenství 203 outletů (3/2026)** [FACT]. FTE 6 694 → 5 617 [FACT].
- **Finance segmentu:** úvěry small business 47,9 (12/2021) → 47,9 (12/2024) → 50,3 mld. Kč (12/2025) → 51,2 (3/2026) [FACT]: **čtyři roky stagnace, oživení až 2025 (+5,0 %) a 1Q26 (+6,9 % y/y)**. Ne-retailoví klienti KB ~241–242 tis. beze změny 2021→2026 [EST, výpočet]. Vklady/marže/CoR segmentu [DATA GAP].
- **Strategie:** transformace „KB Change 2025" a migrace na KB+ dokončena (137 tis. → 1 673 tis. uživatelů za 9 kvartálů) [FACT F&F]; explicitní výroky ke small business [DATA GAP].

### C4. Raiffeisenbank (RBI) – cenově nejagresivnější z „velkých" (CHYTRÝ účet 0 Kč, bankomaty zdarma globálně), ale datově nejméně transparentní

- **Definice:** web sekce „podnikatelé a malé firmy" [FACT/snippet URL]; hranice a obsluhový model [DATA GAP].
- **Produkt:** CHYTRÝ 0 Kč bez podmínek / AKTIVNÍ 99 Kč / EXKLUZIVNÍ 299 Kč; výběry ze všech bankomatů na světě zdarma, neomezené tuzemské a EUR platby, až 17 měn, hromadné platby [FACT/snippet, ceník FOP 1. 2. 2025]. **Podnikatelská rychlá půjčka: parametry [DATA GAP]** (vyhledávání vracelo jen retail Minutovou půjčku). Terminály, factoring, leasing (Raiffeisen-Leasing), pojištění, integrace: [DATA GAP].
- **Digitál / distribuce / finance / strategie:** [DATA GAP] – RB a.s. nezveřejňuje fact sheet s pobočkami/segmenty v projektu; dohledat VZ RB 2021–2025 (rb.cz/o-nas), RBI Investor Presentation (segment Czech Republic), tiskové zprávy RB.

### C5. MONETA Money Bank – jediná z pětky, která small business explicitně reportuje; nejrychlejší růst a nejagresivnější online úvěr

- **Definice:** segment **Commercial** = SME, živnostníci, finanční a veřejné instituce (37 % provozních výnosů 2024) [FACT xlsx + snippet]; small business jako produktová řada („Small Business Instalment Loans") [FACT]. Hranice small business (obrat) [DATA GAP – VZ Moneta 2025, mmb-annual-financial-report-2025-en.pdf].
- **Produkt:** Konto PRO podnikání 0 Kč bez podmínek, 2 karty, neomezené e-transakce [FACT/snippet]; **Expres Business** do 2,5 mil. Kč bez zajištění, online do 600 tis. Kč s rozhodnutím do 15 min a podpisem online, účet zdarma, 12 měsíců podnikání, bez výkazů; **„garance nejnižšího úroku"** (dorovnání konkurenční nabídky) od 16. 3. 2026 [FACT/snippet]; Zelený Expres Business (ESG), Program Expanze (NRB záruky), Juridica Business Program (profese), živnostenská hypotéka, online směnárna a cizoměnový účet [FACT/snippet URL].
- **Digitál:** Smart Banka; plně online založení účtu i úvěru [FACT/snippet]; ratingy [DATA GAP].
- **Distribuce:** 153 → 122 poboček (12/2022 → 12/2025), 123 v 3/2026; bankomaty 563 → 541 [FACT].
- **Finance segmentu [FACT]:** Commercial net loans 82,8 → 104,0 mld. Kč (2022→2025, +25,6 %), 109,1 (3/2026); nezajištěné splátkové úvěry a kontokorenty commercial 12,1 → 20,5 mld. Kč (+69 %); **nové small business splátkové úvěry 3,99 → 6,36 → 8,36 mld. Kč (2023→2024→2025; +59 %, +31 %)**, 1Q26 +20 % y/y; commercial vklady 105,8 → 109,2 mld. Kč; commercial cost of risk ≈ 0,02 % (2024) [EST]; FY2025 čistý zisk 6,5 mld. Kč (+11,9 %), komerční úvěry +12,4 % na 104 mld. Kč [FACT/snippet TZ – shoda s xlsx 103 987 mil. Kč]. EIB linka 100 mil. EUR (2,5 mld. Kč) na SME (2024) [FACT/snippet].
- **Strategie:** management opakovaně uvádí živnostníky a malé firmy jako tahouna růstu (TZ 1Q25: +19 %; TZ FY25: +31,4 %); střednědobý výhled kumulovaný čistý zisk ≥ 33,3 mld. Kč do 2029 a „ambiciózní výhled 2030" (Patria) [FACT/snippet, detail plánu pro segment DATA GAP].

---

## (d) Souhrnná tabulka Banka × dimenze (1 = slabé, 5 = nejlepší v pětce)

| Dimenze | ČS | ČSOB | KB | RB | Moneta | Komentář / jistota |
|---|---|---|---|---|---|---|
| Definice & přehlednost nabídky | 3 | 3 | **4** | 3 | **4** | KB (Profi řada) a Moneta (Konto PRO / Expres Business) mají nejčitelnější architekturu; ČS třístupňová řada + podmíněná sleva je složitější. [EST – kvalitativní] |
| Produkt (účet + úvěr) | 3 | 3 | **4** | 2* | **5** | Moneta: nejvyšší nezajištěný limit (2,5 mil.) a nejrychlejší online proces; KB: 5 mil. Kč, 1 mil. bez příjmů; ČSOB: jen 150 tis. bez zajištění; ČS: 500 tis. (1,2 mil. start-up). *RB: úvěr [DATA GAP] |
| Digitál | 3* | 3* | **4** | 2* | **4** | KB+ 93% penetrace + sdílení s účetní; Moneta plně online onboarding i úvěr. *Ratingy app stores u všech [DATA GAP] → skóre předběžné |
| Cena základního účtu | **1** | 4 | 3 | **5** | **5** | ČS jediná se 149 Kč bez podmíněné slevy a zdražením 3/2026; RB a Moneta 0 Kč bez podmínek |
| Distribuce (fyzická síť) | **5** | 3* | 4 | 2* | 2 | ČS 329 poboček; KB 186 + 203 KB Poradenství; Moneta 122. *ČSOB, RB [DATA GAP] |
| Finanční síla v segmentu (objem/růst) | 3* | 4 | 3 | 2* | **5** | Moneta +31 % nové SB úvěry; ČSOB SME +9,7 %; KB SB kniha +5 % za 4 roky; ČS SME +7,7 % (nerozlišuje mikro). *ČS/RB bez segmentových dat |
| Strategická priorita segmentu | 2* | 3* | 3 | 2* | **5** | Moneta jediná explicitně komunikuje small business jako motor růstu; ČS TZ FY25 zdůrazňuje investice a hypotéky. *Výroky managementu ČS/ČSOB/RB [DATA GAP] |
| **Součet (orientační)** | 20 | 23 | 25 | 18 | **30** | Skóre je [EST] – syntéza ověřených faktů, u hvězdičkou označených buněk chybí data |

---

## (e) Analýza / zjištění (action titles)

**1. Cenová hladina základního účtu se v pětce rozdělila na „0 Kč bez podmínek" (Moneta, RB, ČSOB základní) a „podmíněné 0 Kč" (KB) – ČS je jediná, kdo v 2026 zdražuje a drží 149 Kč pro pasivní FOP.** Reálná cena pro aktivního FOP s úvěrem u ČS je 75 Kč, tj. stále nad všemi konkurenty. Zdražení vyšších variant o 100 Kč (3/2026) jde proti trhu, kde Finmag konstatuje, že „základní služby jsou u většiny bank zdarma" [FACT/snippet].

**2. V nezajištěném online úvěru pro FOP definuje standard Moneta (2,5 mil. Kč / 600 tis. online za 15 min / garance sazby) a KB (1 mil. bez dokládání příjmů, 5 mil. celkem, od 5,9 %); ČS má nižší nezajištěný limit (500 tis., 1,2 mil. jen pro start-upy) a nezveřejňuje sazbu ani rychlost.** ČSOB drží hybrid (150 tis. ihned, zbytek přes bankéře).

**3. Small business je ve výkaznictví „neviditelný" u ČS, ČSOB a RB; jen Moneta a KB dávají trhu měřitelná čísla – a ta ukazují, že Moneta roste (nové SB úvěry +31 % 2025, +20 % 1Q26), zatímco KB kniha 4 roky stagnovala (47,9 → 47,9 mld. Kč 2021–2024) a ožila až 2025 (+5 %).** ČSOB SME kniha (+9,7 %) je širší definice a nelze ji přímo srovnat.

**4. Fyzická síť se všude ztenčila o pětinu, ale ČS si drží 1,8× síť KB a 2,7× síť Monety – to je aktivum pro obsluhu FOP mimo Prahu, pokud je v pobočkách kapacita business bankéřů (počet RM [DATA GAP]).** KB síť redefinovala (186 poboček + 203 KB Poradenství), Moneta jde na 122 poboček s plně online onboardingem.

**5. Digitální migrace KB (KB+ 93 % klientů za 9 kvartálů) a plně online onboarding Monety zvyšují laťku; ČS má oddělený George Business, jehož hodnocení a pokrytí funkcí nebylo možné ověřit.** Riziko: bez integrace na účetní SW a bez online s.r.o. onboardingu se diferenciace ČS opírá jen o síť.

---

## (f) „So what" pro Českou spořitelnu

1. **Cena je zjevný handicap v akvizici FOP:** 149/75 Kč vs. 0 Kč u Monety, RB i ČSOB. Zvážit „0 Kč při aktivitě" (transakce nebo příjem), ne jen při úvěru – jinak zdražení 3/2026 posílí odliv nových FOP k challengerům (hypotéza H3.1 z plánu).
2. **Zvednout nezajištěný online limit a zveřejnit sazbu/rychlost:** konkurence komunikuje 600 tis.–1 mil. Kč online bez výkazů a „do 15 minut"; ČS 500 tis. Kč bez zveřejněné sazby je v srovnávačích neviditelná.
3. **Začít segment reportovat (interně i externě):** Moneta a KB umí říct, kolik small business úvěrů poskytly; ČS ne. Bez čísla nelze řídit ani obhájit prioritu. Minimálně doplnit do IR factbooku řadu „micro/small business loans & clients" (Erste Factbook má formát).
4. **Monetizovat síť 329 poboček jako diferenciátor pro s.r.o. a regionální FOP** (poradenství, úvěry nad 1 mil. Kč, terminály), zatímco jednoduchý FOP účet a mikroúvěr přesunout plně do George Business.
5. **Uzavřít datové mezery před finální diagnostikou** (viz g): ratingy aplikací, kontokorent vs. repo, ceníky 2021/2023 z archivu, Erste Factbook micro segment, VZ RB.

---

## (g) Seznam zdrojů (datum přístupu 2026-09-08)

Primární data (lokální soubory projektu, IR banky):
- Česká spořitelna, *Key figures Q1 2026* (`key_figures_q1_2026.xlsx`, list Key_figures) – pobočky, FTE, úvěry, vklady, karty. Původ: csas.cz/cs/o-nas/pro-investory.
- Komerční banka, *Facts and Figures 1Q 2026* (`KB-Facts-and-Figures-2026-1Q.xlsx`, listy Business, Operations) – klienti, KB+ uživatelé, loans to small businesses, pobočky, KB Poradenství, FTE. Původ: kb.cz/cs/o-bance/vztahy-s-investory.
- ČSOB, *Fact sheet 1Q 2026* (`csob-fact-sheet.xlsx`, listy Business volumes, Additional information) – SME loans, leasing, factoring, NPL, C/I. Původ: csob.cz/o-csob/vztahy-s-investory.
- MONETA Money Bank, *Basic financial data 4Q 2024 a 1Q 2026* (`mmb-4q2024-…xlsx`, `mmb-1q2026-…xlsx`, listy Portfolio, New Business Volumes, Total deposits, Segment analysis, KPIs) – commercial portfolio, small business instalment loans, vklady, pobočky, segmentové výnosy. Původ: investors.moneta.cz/financial-results.

Webové zdroje (pouze úryvky z vyhledávání; plný text nebyl dostupný):
- csas.cz/cs/firmy/ucty-podnikatele-firmy; …/ucet-zivnostnik; …/ucet-klasik; csas.cz/cs/podnikatele-firmy/ceniky; csas.cz/banka/content/inet/internet/cs/cenik_podnikatelsky_ucet_zivnostnik.pdf; csas.cz/cs/firmy/uvery/specializovane-uvery; csas.cz/cs/firmy/internetove-bankovnictvi/george-business; csas.cz/cs/o-nas/pro-media/tiskove-zpravy/2026/02/26/…; csas.cz/en/about-us/for-the-media/2026/investments-and-mortgages-powered-…; csas.cz/banka/content/inet/internet/cs/vz-2025-cs.pdf
- czechstartups.gov.cz/chci_financovani/firemni-uver-start-up-ceske-sporitelny/
- finmag.cz/finance/485143-podnikatelske-ucty-2026-… (2026); finmag.cz/finance/470899-podnikatelske-ucty-2025-… (2025)
- csob.cz/firmy/poplatky-a-sazby; csob.cz/firmy/uver; csob.cz/firmy/uvery-a-financovani/uver-pro-obchodniky; mesec.cz/tiskove-zpravy/csob-uvadi-rychly-uver-na-podnikani/; penize.cz/zpravy-z-trhu/229974-…; bankovnipoplatky.cz/csob-rychly-uver-na-podnikani-…-18675.html; pruvodcepodnikanim.cz/clanek/podnikatelsky-uver/
- kb.cz/cs/podnikatele-a-firmy/ucty/bezne-ucty/profi-ucet-pro-podnikatele; …/profi-ucet-pro-zacinajici-podnikatele; …/profi-ucet-gold; kb.cz/cs/podnikatele-a-firmy/ucty/specializovane-ucty/profi-program1; kb.cz/cs/podnikatele-a-firmy/uvery/na-cokoliv/profi-uver; …/profi-uver-revolvingovy; …/profi-uver-start; kb.cz/getmedia/59e77e23-27b2-4de8-ad6c-5ecb250f821c/kb-sazebnik-podnikatele.pdf; smlouvy.gov.cz/smlouva/soubor/41384609/kb-sazebnik-podnikatele.pdf; mesec.cz/tiskove-zpravy/podnikatelsky-uver-od-komercni-banky/
- rb.cz/podnikatele/ucty-a-platebni-styk/podnikatelske-bezne-ucty; rb.cz/promo/chytry-ucet-pro-podnikatele; rb.cz/attachments/podminky/2025/02/cenik-fop-po-1.pdf; finex.cz/banka/raiffeisenbank/ucty-pro-podnikatele-a-male-firmy-raiffeisenbank/; penize.cz/podnikatelske-uvery/7685-raiffeisenbank-podnikatelska-rychla-pujcka
- moneta.cz/ucty-a-karty/konto-pro-podnikani; moneta.cz/pujcky-a-uvery/business-uver-nezajisteny; moneta.cz/pujcky-a-uvery/zeleny-expres-business; moneta.cz/pujcky-a-uvery/program-expanze; moneta.cz/ucty-a-karty/juridica-business-program; moneta.cz/ucty-a-karty/cizomenovy-ucet-pro-podnikani; moneta.cz/servis-pro-media/tiskove-zpravy/detail/moneta-vykazala-za-rok-2024-…; zpravy.kurzy.cz/847540-moneta-vykazala-za-rok-2025-…; patria.cz/zpravodajstvi/6794910/…; investicniweb.cz/prazska-burza/303756-…; eib.org/en/press/all/2024-133-…; carbonaccountingfinancials.com/files/institutions_downloads/mmb-annual-financial-report-2025-en.pdf
- apps.apple.com/cz/app/george-business-česko/id6479615359; play.google.com/store/apps/details?id=cz.csas.georgego.business (neotevřeno)
- thebanks.eu/banks/10961 (podíl trhu ČS – metodika neověřena, [CLAIM])

---

## (h) Log odhadů a mezer

Odhady [EST]:
- KB ne-retailoví klienti 241–242 tis. = „KB clients − individual clients" (F&F); nejde o čistý počet podnikatelů (zahrnuje korporace, municipality; FOP na RČ mohou být v „individual").
- Moneta commercial cost of risk 2024 ≈ 0,02 % = net impairment −16 mil. Kč / průměr net commercial loans 2023–2024 (88,2 mld. Kč).
- Skóre 1–5 v tabulce (d) je kvalitativní syntéza; buňky s * stojí na neúplných datech.
- Roční součty nových Small Business Instalment Loans Moneta = součet čtvrtletí z IR xlsx (2025: 8 357 mil. Kč; ověřeno shodou +31,4 % s TZ).

Mezery [DATA GAP] – kde dohledat:
1. Hranice segmentu (obrat/expozice) a obsluhový model u všech 5 bank → VZ 2025 (kapitola segmenty), Erste Factbook, KBC/RBI investor prezentace.
2. Kontokorent (limit, sazba) a vývoj sazeb 2021–2026 vs. 2T repo → sazebníky úrokových sazeb bank, ČNB ARAD.
3. Ceny účtů 2021 a 2023 → web.archive.org (ceníky), Finmag 2025, Finparáda, Měšec archiv.
4. Ratingy aplikací (George Business, KB+, ČSOB Smart, RB, Smart Banka) → App Store / Google Play (blokováno).
5. Platební terminály/brány, účetní integrace (Fakturoid, iDoklad, Pohoda), bankovní identita, ESG produkty, pojištění, FX → produktové stránky bank.
6. Pobočky ČSOB a RB 2021–2025; počty business bankéřů/RM všech bank → VZ.
7. Segmentová finanční data ČS (micro), ČSOB (small business), RB (vše) → Erste Factbook, KBC segment reporting, RBI CZ.
8. Výroky managementu ke small business (ČS, ČSOB, KB, RB) 2023–2026 → tiskové zprávy, rozhovory (Hospodářské noviny, E15, Ekonom).
9. Parametry RB Podnikatelské rychlé půjčky → rb.cz/podnikatele/uvery, penize.cz.
10. ČS: přiřazení cen 599/899 Kč k variantám Klasik/Maxi a potvrzení, zda se zdražení 3/2026 týkalo i Živnostníka → ceník ČS platný od 1. 3. 2026.
