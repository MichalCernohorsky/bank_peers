# 04 – WS3b: Challengeři a niche hráči v segmentu small business (FOP + PO do 25 mil. Kč obratu)
Stav 2025/2026 + vývoj od 2021 · perspektiva benchmark Česká spořitelna vs. trh · datum zpracování 2026-09-08

> **Metodická poznámka k tomuto běhu (čti před použitím čísel).** Výzkum byl proveden v prostředí, kde (i) egress proxy blokovala přímé načtení všech webů bank, ceníků, PDF výročních zpráv i médií (airbank.cz, fio.cz/fio.sk, creditas.cz, unicreditbank.cz, partnersbanka.cz, wise.com, revolut.com, trinitybank.cz, mbank.cz, mesec.cz, finex.cz, finmag.cz, banky.cz, cs.wikipedia.org, web.archive.org, r.jina.ai – všechny 403 CONNECT; ověřeno WebFetch i curl přes proxy), a (ii) sdílený limit WebSearch relace (200 dotazů) byl vyčerpán po 14 úspěšných dotazech tohoto workstreamu. Všechna čísla níže pocházejí **výhradně ze strojově shrnutých výsledků vyhledávání** (snippet + název + URL zdroje), nikoli z plného textu zdroje. Proto používám značku `[FACT-S]` = fakt potvrzený ve snippetu vyhledávače s odkazem na primární zdroj, ale neověřený v plném textu. Vše, co se nepodařilo dohledat, je `[DATA GAP]` s návodem, kde hledat. Body zadání 3 (ratingy aplikací), 8 (průzkumy a ankety) a 9 (NPS, finanční arbitr) jsou z výše uvedených důvodů **nepokryté** a musí být doplněny v navazujícím běhu s obnoveným rozpočtem vyhledávání (viz sekce F).

---

## A. Hypotézy WS3b (co ověřujeme)

| # | Hypotéza | Stav po tomto běhu |
|---|---|---|
| H3b.1 | Air Bank se od 5/2023 stala nejrychleji rostoucím akvizitérem nových FOP (cíl: „každý čtvrtý nový OSVČ"), ale obsluhuje jen jednoduché entity (FOP, jednočlenné/vícečlenné s.r.o. s FO společníky), nemá kontokorent ani firemní úvěr. | Částečně potvrzeno `[FACT-S]` + `[CLAIM]` (viz B1). |
| H3b.2 | Fio banka je největší challenger v počtu podnikatelských klientů díky účtu zdarma, otevřenému API a nejhustší pobočkové síti mezi challengery; nereportuje však počet podnikatelů. | Kvalitativně podpořeno; počet podnikatelů `[DATA GAP]`. |
| H3b.3 | Creditas po fúzi s Max bankou (10/2024) přesouvá těžiště z retailových vkladů k firemnímu bankovnictví; ve small business soutěží hlavně úročením vkladů, ne úvěry. | Částečně (fúze `[FACT-S]`, úročení firemního spoření 1,40 % `[FACT-S]`, úvěry `[DATA GAP]`). |
| H3b.4 | UniCredit obsluhuje small business jako „podnikatelé a menší firmy" s klasickou trojicí balíčků (START/OPEN/TOP) a soutěží bonusovým úročením, nikoli cenou účtu. | Potvrzeno `[FACT-S]` (kampaň 1/2025: bonus 2,50 % p.a.). |
| H3b.5 | Revolut Business a Wise odčerpávají FX/zahraniční platby, ale nejsou „hlavní bankou" FOP; Partners Banka zatím podnikatele neobsluhuje. | Revolut: růst MAU firem +31 % `[FACT-S]`; Partners: plán 2026 `[FACT-S]`; Wise `[DATA GAP]`. |
| H3b.6 | Cenová hladina challengerů: účet 0 Kč je hygienický standard (Air Bank, Fio, Creditas); diferenciace se přesunula k úročení zůstatku/spoření (Air Bank 2,6 %, UniCredit 2,5 % bonus, Creditas 1,4 %). | Potvrzeno pro 2025/26 `[FACT-S]`; vývoj 2021–2024 `[DATA GAP]`. |

---

## B. Profily bank (datové tabulky + poznámky)

### B1. Air Bank (skupina PPF) – „účet pro OSVČ zdarma, nyní i s.r.o."

| Dimenze | Zjištění | Jistota / zdroj |
|---|---|---|
| Definice segmentu | Produkt „Podnikatelský účet" pro fyzické osoby podnikající (od 16 let); od 2025 rozšířen na jednočlenné s.r.o., od 23. 1. 2026 i na **vícečlenné s.r.o.** za podmínky, že jednatelé jednají samostatně a všichni společníci jsou fyzické osoby. Žádná obratová hranice není publikována. | `[FACT-S]` Air Bank, tisková zpráva 23. 1. 2026 [Z1]; Finex 2026 [Z5] |
| FOP vs. PO | FOP ano; PO pouze s.r.o. (jedno- i vícečlenné, jen FO společníci); a.s., družstva, spolky **ne**. Air Bank uvádí, že jednočlenné s.r.o. tvoří „až 75 % všech obchodních společností v ČR". | `[FACT-S]` [Z1]; podíl 75 % = `[CLAIM]` banky, ověřit v ČSÚ RES |
| Cena účtu | 0 Kč, bez podmínek: tuzemské úhrady, SEPA, okamžité platby, trvalé příkazy, inkasa zdarma; 2 plastové + až 10 virtuálních karet zdarma; přidání disponenta bez návštěvy pobočky. | `[FACT-S]` [Z1], [Z2], [Z5] |
| Úročení | Podnikatelský spořicí účet: bonusová sazba **2,6 % p.a. do 300 tis. Kč**, podmínka ≥ 5 plateb kartou/mobilem měsíčně; jinak základní sazba 0 %. | `[FACT-S]` Air Bank / Finex, stav 2026 [Z5], [Z6] |
| Úvěry | **Kontokorent neposkytuje**; umí pouze převést kontokorent z jiné banky na půjčku. Provozní/investiční firemní úvěr: nenalezen → pravděpodobně nenabízí. | `[FACT-S]` [Z7]; firemní úvěr `[DATA GAP]` (ověřit airbank.cz/produkty) |
| Fakturace / integrace | Fakturace přímo v mobilní aplikaci; klienti vystaví **> 30 000 faktur měsíčně** (rekord 287 faktur za den); automatické podklady pro DPH a daň z příjmů v aplikaci. | `[FACT-S]` [Z1] |
| Terminál / brána, API, účetní SW | `[DATA GAP]` – nenalezeno; ověřit na airbank.cz (sekce podnikatelé) a v Apple/Google store popisu. | |
| Digitální onboarding | Založení účtu online (pro FOP i s.r.o. bez pobočky dle textace „bez nutnosti návštěvy pobočky" u disponenta); čas onboardingu `[DATA GAP]`. | `[FACT-S]`/`[DATA GAP]` [Z2] |
| Rating aplikace | `[DATA GAP]` – App Store / Google Play (nefetchovatelné v tomto běhu). | |
| Distribuce | Počet poboček `[DATA GAP]` (odhad z veřejně známé sítě ~30 `[EST]`, neověřeno). | |
| Klienti-podnikatelé | **> 65 000** uživatelů podnikatelského účtu (od spuštění 5/2023 do 1/2026). | `[FACT-S]` [Z1] |
| Akvizice nových FOP | V roce 2025 vzniklo v ČR 91 615 nových OSVČ; „každý čtvrtý" si vybral účet Air Bank. Implikace: ≈ 23 tis. nových FOP-klientů v 2025 `[EST]` (0,25 × 91 615). | Počet OSVČ: `[FACT-S]` dle Air Bank citující veřejnou statistiku [Z3]; podíl ¼ = `[CLAIM]` banky |
| Finanční metriky skupiny 2025 | Čistý zisk > 3,8 mld. Kč (ROE > 24 %); klienti skupiny > 2 mil. (+12 %), samotná Air Bank +~185 tis. klientů; úvěrové portfolio +~20 % na ~131,3 mld. Kč; vklady +13 % na 191,3 mld. Kč; nové spotřebitelské úvěry ~64 mld. Kč (> 30 % podíl trhu). Segment podnikatelů samostatně nereportován. | `[FACT-S]` Air Bank, neauditované výsledky 2025 [Z4]; Forbes [Z8]; e15 (H1 2025: 2,1 mil. klientů, zisk ~1,9 mld.) [Z9] |
| Strategie 2023–2026 | Vstup do segmentu 5/2023 s argumentem vlastního průzkumu „každý druhý živnostník není spokojený se svou bankou"; 2025 rozšíření na jednočlenné s.r.o.; 1/2026 na vícečlenné s.r.o.; cíl být „nejlepším podnikatelským účtem na trhu". | `[CLAIM]` tituly tiskových zpráv Air Bank [Z10], [Z11]; detail průzkumu (vzorek, agentura) `[DATA GAP]` |
| Cenový vývoj 2021→2026 | 2021–4/2023 produkt neexistoval; od 5/2023 účet 0 Kč; úročení „podobné jako u konta pro spotřebitele" (Měšec, 5/2023) → 2026 bonus 2,6 % do 300 tis. Kč. Sazby v mezidobí `[DATA GAP]`. | `[FACT-S]` Měšec [Z12] (titulek), Finex [Z5] |

**Komentář:** Air Bank je jediný challenger, který v tomto běhu prokazatelně zveřejňuje počet podnikatelských klientů (65 tis.). Její model je „retail-like": účet zdarma, fakturace, karty, spoření – ale **bez kontokorentu a bez firemního úvěru**, tedy bez produktu, který u FOP generuje největší výnos na klienta. To definuje její konkurenční tlak na ČS jako tlak na **akvizici a primární účet nových FOP**, nikoli na úvěrovou knihu.

### B2. Fio banka – „účet zdarma, otevřené API, nejhustší síť mezi challengery"

| Dimenze | Zjištění | Jistota / zdroj |
|---|---|---|
| Definice segmentu | „Podnikatelský účet" bez poplatků a bez podmínek; dle zadání pro FOP i PO (s.r.o., a.s., spolky). Segmentové hranice (obrat) nepublikovány. | Eligibilita PO v tomto běhu neověřena na stránce → `[DATA GAP – ověřit]` [Z13] |
| Cena účtu | Založení i vedení běžného podnikatelského účtu bez poplatků. | `[FACT-S]` [Z13] |
| Úročení zůstatku | `[DATA GAP]` – Fio spořicí účet pro podnikatele / úročení běžného účtu 2023–2026 (hledat fio.cz/urokove-sazby, Finex, Peníze.cz). | |
| Kontokorent | Produkt „Podnikatelský kontokorent" existuje; limity, sazba, rychlost `[DATA GAP]`. | `[FACT-S]` existence [Z14] |
| Provozní/investiční úvěr | `[DATA GAP]` (Fio nabízí podnikatelské úvěry na pobočkách; parametry ověřit). | |
| Terminál / brána | Fio nabízí **vlastní platební terminály a platební bránu** (ne GoPay); terminál doručen „do několika pracovních dní od podpisu smlouvy". GoPay integrace se týká Fakturoidu, ne Fio. | `[FACT-S]` [Z15], [Z16] |
| API / účetní SW | **Fio API Bankovnictví**: automatizované zpracování výpisů a pohybů, data o karetních transakcích (terminály, brána) v XML/CSV; napojení Fakturoid (párování plateb přes token, tarify „Na každý den" a „Na maximum"), iÚčto a další. | `[FACT-S]` [Z17], [Z18], [Z19] |
| Digitální onboarding | `[DATA GAP]` (online založení FOP ano/ne, s.r.o. ano/ne, čas). | |
| Rating aplikace | `[DATA GAP]`. | |
| Distribuce | ČR: počet poboček `[DATA GAP]` (veřejně uváděno ~80 `[EST]`, neověřeno v tomto běhu); SR: síť rozšířena na **27** obchodních míst. | `[FACT-S]` SR [Z20] |
| Klienti | **1,55 mil. klientů** (2/2025, u příležitosti 15 let banky); Wikipedie uvádí „téměř 1,5 mil." (2/2025) – rozdíl = zaokrouhlení / okamžik měření. Počet podnikatelů `[DATA GAP]` (Fio nereportuje). | `[FACT-S]` Fio TZ [Z21], Kurzy [Z22] |
| Finanční metriky 2024 | Čistý zisk **6,07 mld. Kč** (−5 % y/y); vklady +20 % na **289 mld. Kč**; bilanční suma **> 314 mld. Kč**. Úvěry klientům `[DATA GAP]` (ve VZ 2024, s. rozvaha). Segmentové členění nereportováno. | `[FACT-S]` Seznam Zprávy [Z23], Kurzy [Z22]; VZ 2024/2025 [Z24], [Z25] nefetchovatelné |
| Strategie | `[DATA GAP]` – výroky managementu k podnikatelům 2023–2026 (hledat rozhovory J. Mrázek / Fio v HN, E15). | |
| Cenový vývoj | Účet 0 Kč konzistentně (model banky od 2010); úroky `[DATA GAP]`. | `[EST]` |

**Komentář:** Fio je „infrastrukturní" challenger: hodnota pro small business je v otevřeném API, vlastní akceptaci karet a pobočkách, ne v ceně kapitálu. Absence jakéhokoli reportingu podnikatelských klientů je největší datová mezera pro odhad tržních podílů (viz D).

### B3. Banka Creditas (skupina Creditas, P. Hubáček) – „vkladový challenger s firemní ambicí po fúzi s Max bankou"

| Dimenze | Zjištění | Jistota / zdroj |
|---|---|---|
| Definice segmentu | Produkt „Firemní účet" pro FOP i PO (Spořicí účet+ výslovně „fyzickým osobám podnikatelům nebo právnickým osobám"). Obratové hranice `[DATA GAP]`. | `[FACT-S]` [Z26], [Z27] |
| Cena účtu | Založení a vedení zdarma; elektronické bankovnictví a e-výpis zdarma; příchozí i odchozí tuzemské elektronické platby, trvalé příkazy, inkasa zdarma. | `[FACT-S]` [Z27], [Z28] |
| Úročení | **Spořicí účet+ pro firmy a podnikatele: 1,40 % p.a. bez omezení výše vkladu**, bez výpovědní lhůty, zdarma (2026). Úročení běžného firemního účtu `[DATA GAP]`. | `[FACT-S]` Finex 2026 [Z26] |
| Úvěry (kontokorent, provozní, investiční) | `[DATA GAP]` – ověřit creditas.cz/firmy (Creditas historicky cílí na financování nemovitostí a středních firem). | |
| Terminál/brána, API, účetní SW | `[DATA GAP]`. | |
| Digitální onboarding, rating aplikace | `[DATA GAP]`. | |
| Distribuce | Počet poboček `[DATA GAP]`; po fúzi 10/2024 síť Max banky integrována. | |
| Klienti | Po fúzi s Max bankou (1. 10. 2024) **> 250 tis. klientů**, bilanční suma **~200 mld. Kč**. Novější údaje se rozcházejí: „cca 400 000" (TOP.cz 2026) vs. „260 000" (2025) – rozdíl pravděpodobně skupina vs. banka / různý okamžik → `[DATA GAP – ověřit ve VZ 2025]`. Počet podnikatelů `[DATA GAP]`. | `[FACT-S]` e15 [Z29], Forbes [Z30], Měšec [Z31]; TOP.cz [Z32] |
| Finanční metriky | e15: „Banka Creditas šestinásobně zvýšila zisk, pomohly jí nákupy v zahraničí" (titulek, rok výsledků neurčen ve snippetu). Zisk, úvěry, vklady segmentu `[DATA GAP]`. | `[FACT-S]` titulek [Z33] |
| Strategie | Fúze Max banka (ex-Expobank CZ) → Creditas dokončena 1. 10. 2024; klientům zůstala čísla účtů, změnil se kód banky a IBAN. HN: „Generační obměna a expanze skupiny Creditas" (kontext skupiny). Výroky k small business `[DATA GAP]`. | `[FACT-S]` [Z29]–[Z31]; HN [Z34] |
| Cenový vývoj | Spořicí sazby 2023–2024 (hypotéza: mezi nejvyššími na trhu) `[DATA GAP]` – ověřit historii na Finex/Peníze.cz „Creditas spořicí účet" + ARAD; stav 2026 = 1,40 % (firmy). | |

**Komentář:** Creditas soutěží o zůstatky podnikatelů (spoření 1,40 % bez limitu – jediný ze sledovaných bez stropu objemu), ale o transakčním a úvěrovém produktu pro FOP chybí veřejná data. Riziko pro ČS je odliv **volné likvidity firem**, ne primárního účtu.

### B4. UniCredit Bank Czech Republic and Slovakia – „univerzální banka s balíčky START/OPEN/TOP a bonusovým úročením"

| Dimenze | Zjištění | Jistota / zdroj |
|---|---|---|
| Definice segmentu | Web: „Podnikatelé a menší firmy" (podsekce „Začínám podnikat"); historicky sazebník „Část Small Business" (2015). Obratová hranice small business vs. SME `[DATA GAP]` (ověřit ve VZ 2025 – segmentová poznámka). | `[FACT-S]` [Z35], [Z36] |
| FOP vs. PO | Obě skupiny (balíčky Business pro podnikatele i firmy). | `[FACT-S]` Finex [Z37] |
| Cena účtu | **Business START** – vedení zdarma; **Business OPEN** – zdarma 12 měsíců, poté podmínky; **Business TOP** – 350 Kč/měs., odpuštěno při min. měsíčním bezhotovostním kreditním obratu 20 000 Kč nebo průměrném zůstatku ≥ 250 000 Kč. | `[FACT-S]` Finex [Z37], Wise blog [Z38] (přesná textace podmínky TOP ověřit v ceníku) |
| Úročení | Kampaň od 1. 1. 2025: balíčky START/OPEN/TOP otevřené od 1. 1. 2025 mají kombinovanou sazbu (základní + bonus); **bonus 2,50 % p.a.** při aktivním používání (min. měsíční kreditní obrat 20 000 Kč). Strop objemu, základní sazba, trvání kampaně `[DATA GAP]` (PDF nefetchovatelné). | `[FACT-S]` UCB, podmínky kampaně 1/2025 [Z39] |
| Úvěry, terminály | Sekce „Účty a platební terminály" existuje; parametry kontokorentu/úvěrů, terminálů `[DATA GAP]`. | `[FACT-S]` existence [Z35] |
| API / účetní SW, bankovní identita, ESG | `[DATA GAP]`. | |
| Digitální onboarding, rating aplikace | `[DATA GAP]`. | |
| Distribuce | Počet poboček ČR `[DATA GAP]` (VZ 2025). | |
| Klienti | **~450 000** klientů (ČR, banky.cz – rok neuveden); počet podnikatelů `[DATA GAP]`. | `[FACT-S]` [Z40] |
| Finanční metriky | Pololetní zpráva 2025: růst úvěrového portfolia „se nadále soustředí na retailové segmenty a malé a střední podniky". Segmentové objemy `[DATA GAP]` (VZ 2025, segmentová analýza). | `[FACT-S]` [Z41]; VZ 2025 [Z42] nefetchovatelné |
| Strategie | Titul VZ 2025 „Acceleration in action – Od ambice k neomezeným možnostem"; výroky k small business `[DATA GAP]`. | [Z42] |
| Cenový vývoj | 2021–2024 ceny balíčků `[DATA GAP]` (Finparáda/Měšec archiv); 2025 přechod na „bonusové úročení" jako akviziční nástroj. | |

**Komentář:** UniCredit je jediný z primární čtveřice s tradičním „balíčkovým" ceníkem (placený TOP tarif s odpuštěním podle obratu) – strukturálně nejblíže modelu ČS/KB/ČSOB. Bonus 2,50 % p.a. od 1/2025 je přímou odpovědí na Air Bank (2,6 %) a signalizuje, že **cena zůstatku, ne cena účtu, je novým bojištěm**.

### B5. Sekundární vrstva

| Hráč | Obsluhuje small business? | Zjištění (tento běh) | Jistota |
|---|---|---|---|
| **Revolut Business** | Ano (s.r.o. i OSVČ dle zadání; eligibilita v ČR neověřena) | Revolut ČR: > 1 mil. zákazníků (3/2025), > 1,2 mil. (konec 2025), 1,3 mil. (2026); klientské zůstatky v ČR 2025 +~50 %. **Revolut Business ČR: počet měsíčně aktivních firem +31 % y/y (2025)** – absolutní číslo nezveřejněno. Globálně: firemní klienti +33 % na **767 tis.**; skupina 2025 zisk 2 mld. EUR, tržby 5,3 mld. EUR. Ceník tarifů v CZK `[DATA GAP]`. | `[FACT-S]` cc.cz [Z43], [Z44]; Newstream [Z45]; Kurzy [Z46]; HN [Z47] |
| **Wise Business** | Ano (dle zadání) | `[DATA GAP]` – nevyhledáno (rozpočet). Hledat: wise.com/cz/business ceník (poplatek za registraci firmy, FX marže), Wise plc annual report (počet business customers, CZ neuvádí). | |
| **Trinity Bank** | Ano (podnikatelské účty/vklady) | `[DATA GAP]` – nevyhledáno. Hledat: trinitybank.cz/podnikatele, sazby spořicích vkladů pro FO podnikající 2023–2026 (hypotéza: mezi nejvyššími 2023–24). | |
| **Partners Banka** | **Zatím ne** | Služby výhradně pro fyzické osoby-spotřebitele; spuštění pro OSVČ, podnikatele a firmy plánováno „nejdříve od 2026"; banka připravuje propozici pro SME na 2026. Stav k 9/2026 `[DATA GAP – ověřit]`. | `[FACT-S]` Peníze.cz [Z48], TOP.cz [Z49], bankycr.cz [Z50] |
| **mBank** | Ano (mBusiness konto, historicky FOP i s.r.o.) | `[DATA GAP]` – nevyhledáno. Hledat: mbank.cz/firemni, ceník mBusiness Konto, VZ mBank S.A. (CZ/SK segment). | |

---

## C. Souhrnné tabulky

### C1. Banka × dimenze (skóre 1 = slabé … 5 = silné; **`[EST]` expertní hodnocení na základě ověřených bodů výše, nízká spolehlivost tam, kde je `[DATA GAP]`**)

| Dimenze | Air Bank | Fio | Creditas | UniCredit | Revolut Bus. | Partners |
|---|---|---|---|---|---|---|
| Šíře segmentu (FOP + PO) | 3 (FOP + s.r.o. s FO společníky) | 4–5 (FOP i PO; neověřeno) | 4 (FOP i PO) | 5 (plný rozsah) | 4 (s.r.o., OSVČ) | 1 (neobsluhuje) |
| Cena účtu | 5 (0 Kč bez podmínek) | 5 (0 Kč) | 5 (0 Kč) | 3 (START zdarma, TOP 350 Kč s odpuštěním) | n/a `[DATA GAP]` | n/a |
| Úročení zůstatku/spoření | 4 (2,6 % do 300 tis., podmínka karty) | `[DATA GAP]` | 4 (1,40 % bez limitu) | 4 (bonus 2,50 % od 1/2025, podmínka obratu) | `[DATA GAP]` | n/a |
| Úvěry pro podnikatele | 1 (bez kontokorentu/úvěru) | 3 (kontokorent existuje; detail `[DATA GAP]`) | `[DATA GAP]` | 4 (univerzální nabídka; detail `[DATA GAP]`) | 1–2 | n/a |
| Akceptace karet / brána | `[DATA GAP]` | 4 (vlastní terminály + brána) | `[DATA GAP]` | 3–4 (terminály v nabídce) | 3 (vlastní řešení; ČR neověřeno) | n/a |
| API / účetní integrace | 3 (fakturace v appce) | 5 (otevřené API, Fakturoid, iÚčto) | `[DATA GAP]` | `[DATA GAP]` | 4 (globální API) | n/a |
| Digitální onboarding | 4 (online, s.r.o. bez pobočky) | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | 5 | n/a |
| Pobočková síť | 2 (~30 `[EST]`) | 4 (~80 `[EST]`) | 2–3 `[DATA GAP]` | 3 `[DATA GAP]` | 1 (žádná) | 2 (poradci Partners) |
| Transparentnost dat o segmentu | 4 (65 tis. klientů, ¼ nových OSVČ) | 1 | 1 | 2 | 2 (růst MAU +31 %) | n/a |

**Komentář ke skóre:** Jediné dvě dimenze, kde lze skórovat na ověřených datech napříč všemi čtyřmi primárními bankami, jsou *cena účtu* a *úročení* – a právě tam se challengeři sjednotili na „0 Kč + 1,4–2,6 %". Diferenciace se přesouvá k úvěru (Air Bank 1 vs. UniCredit 4) a k integracím (Fio 5). Skóre pro úvěry, onboarding a pobočky jsou z větší části `[EST]`/`[DATA GAP]` a nesmí se používat v exekutivním shrnutí bez doplnění.

### C2. Tržní podíly na podnikatelských účtech – co lze a nelze odvodit

| Hráč | Podíl na podnikatelských účtech | Interval nejistoty | Metoda / zdroj |
|---|---|---|---|
| Air Bank | **~5–6 % registrovaných OSVČ** má účet Air Bank | 4–8 % | `[EST]` 65 tis. podnikatelských klientů [Z1] ÷ ~1,17 mil. evidovaných OSVČ (ČSSZ 12/2025 – převzato z WS1 / brief; vč. vedlejší činnosti; **nesrovnatelná definice**: jmenovatel = registrovaní OSVČ, čitatel = FOP + s.r.o., část klientů může mít účet jako sekundární). Na bázi *aktivních* FOP (hlavní činnost ~650–700 tis., WS1 hypotéza) by podíl byl ~9–10 % `[EXTRAP]`. |
| Air Bank – podíl na **nové** akvizici 2025 | ~25 % nových OSVČ | 15–25 % | `[CLAIM]` banky [Z3]; horní mez = výrok banky; dolní mez = konzervativní korekce za duplicitní účty (vlastní odhad). ≈ 23 tis. nových FOP-klientů/rok `[EST]`. |
| Fio | `[DATA GAP]` | — | Nereportuje. Alternativní cesta: (i) průzkum SME Banking Club „Czech SME Banking" (podíl hlavní banky), (ii) Datank/Ipsos pro ČBA, (iii) odhad z počtu FOP v anketách Podnikatel.cz. Kvalitativně: nejčastěji uváděný challenger v srovnáních účtů 2021–2026 (Finmag, Banky.cz, Finex – tituly [Z51]–[Z53]). |
| Creditas | `[DATA GAP]` | — | > 250 tis. klientů celkem (10/2024) [Z29]; podíl podnikatelů neznámý. |
| UniCredit | `[DATA GAP]` | — | ~450 tis. klientů celkem [Z40]; podíl podnikatelů neznámý (VZ 2025 segmentová poznámka). |
| Revolut Business | `[DATA GAP]` | — | Pouze růst MAU +31 % (2025) [Z44]. |
| ČS / KB / ČSOB / Moneta / RB (pro kontext) | `[DATA GAP]` v tomto WS | — | Předmět WS3a; doporučená triangulace: SME Banking Club + Ipsos/ČBA + výroční zprávy (ČS uvádí počet klientů-podnikatelů v investor prezentacích). |

**Závěr k podílům:** Jediný pevný bod je Air Bank (65 tis. ≈ 5–6 % registrovaných OSVČ po 32 měsících). Vše ostatní vyžaduje průzkumová data (bod 8 zadání), která nebyla v tomto běhu dostupná.

### C3. Ocenění a ankety 2021–2025 (Zlatá koruna – podnikatelský účet, Banka roku – podnikatelé, Finparáda, HN „Nejlepší banka pro podnikatele", Měšec)

| Rok | Zlatá koruna – podnikatelský účet | Banka roku (podnikatelé) | Finparáda / HN / Měšec |
|---|---|---|---|
| 2021–2025 | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` |

Nevyhledáno (rozpočet). Kde hledat: zlatakoruna.info/vysledky (kategorie „Podnikatelský účet" po ročnících), bankaroku.cz (kategorie „Banka roku pro podnikatele"/„Bankéř roku"), finparada.cz/ceny, HN „Nejlepší banka" (Sdružení CZECH TOP 100/HN), mesec.cz „Účet roku". Očekávaný obraz (hypotéza, **neověřeno**): Fio a Air Bank dominují klientským hlasováním; ČS/KB odborným porotám.

### C4. Zákaznická zkušenost (NPS podnikatelů, spokojenost, finanční arbitr)

| Metrika | Zjištění | Zdroj |
|---|---|---|
| Spokojenost živnostníků s bankou | „Každý druhý živnostník není podle průzkumu spokojený se svou bankou" – průzkum zadaný Air Bank při vstupu do segmentu (5/2023); metodika, vzorek, agentura `[DATA GAP]`. | `[CLAIM]` [Z10] |
| NPS podnikatelů dle bank | `[DATA GAP]` – hledat: Deloitte Digital Banking Maturity (CZ), KPMG Customer Experience Excellence CZ (banky), Ipsos pro ČBA „Češi a banky", SME Banking Club. | |
| Stížnosti u finančního arbitra (podnikatelé) | `[DATA GAP]` – finarbitr.cz, výroční zpráva FA 2021–2025 (pozn.: arbitr řeší spory spotřebitelů; podnikatelé spadají jen omezeně → metrika má malou vypovídací hodnotu pro PO). | |

---

## D. Analýza / zjištění (action titles)

**D1. „Účet zdarma" přestal být diferenciátorem; challengeři soutěží o zůstatek.** Air Bank (0 Kč), Fio (0 Kč) a Creditas (0 Kč) mají shodnou cenu účtu `[FACT-S]`; UniCredit má START zdarma a TOP 350 Kč s odpuštěním podle obratu `[FACT-S]`. Reálná cenová soutěž 2025/26 probíhá v úročení: Air Bank 2,6 % (do 300 tis., 5 karetních plateb), UniCredit bonus 2,50 % (obrat ≥ 20 tis. Kč/měs.), Creditas 1,40 % bez stropu `[FACT-S]`. Pro ČS to znamená, že cenový benchmark „účet za X Kč" je zastaralý – relevantní je **efektivní výnos klienta ze zůstatku do ~300 tis. Kč**.

**D2. Air Bank je jediný challenger s prokazatelně masovou akvizicí nových FOP – ale bez úvěru.** 65 tis. podnikatelských klientů za 32 měsíců `[FACT-S]` a deklarovaná ¼ nových OSVČ v roce 2025 `[CLAIM]` znamenají řádově 20–25 tis. nových FOP ročně `[EST]`. Zároveň Air Bank kontokorent neposkytuje `[FACT-S]` a firemní úvěr nebyl nalezen. Model je „primární účet + fakturace + spoření", tj. zásah do **fee/float** ekonomiky ČS u začínajících FOP, nikoli do úvěrové marže. Rozšíření na vícečlenné s.r.o. (1/2026) posouvá hrozbu z FOP do nejmenších PO.

**D3. Fio konkuruje infrastrukturou (API, terminály, pobočky), nikoli sazbou – a je datově neviditelné.** Otevřené API s napojením na Fakturoid/iÚčto a vlastní akceptace karet `[FACT-S]` dělají z Fio přirozenou „účetní banku" digitálně zdatných FOP. Banka ale nereportuje počet podnikatelů, úvěry ani segmentové výnosy – 1,55 mil. klientů, 289 mld. Kč vkladů a 6,07 mld. Kč zisku (2024) `[FACT-S]` jsou jediné kotvy. Odhad jejího podílu je bez průzkumových dat nemožný.

**D4. Creditas po fúzi s Max bankou (10/2024) je vkladový, ne úvěrový konkurent ve small business.** > 250 tis. klientů, ~200 mld. Kč bilance `[FACT-S]`; produktově ověřen jen účet zdarma a Spořicí účet+ 1,40 % bez limitu `[FACT-S]`. Chybí důkaz o transakčních/úvěrových produktech pro FOP → hrozba pro ČS = odliv volné firemní likvidity, zejména PO s vyššími zůstatky (bez stropu objemu).

**D5. UniCredit kopíruje model velké čtyřky a reaguje bonusovým úročením.** Trojice balíčků a odpouštění poplatku podle obratu/zůstatku `[FACT-S]` je totožná logika jako u ČS/KB/ČSOB; novinkou od 1/2025 je bonus 2,50 % p.a. `[FACT-S]`. UniCredit tak vytváří „most" mezi incumbent ceníkem a challenger úročením – je nejbližším benchmarkem pro případnou reakci ČS.

**D6. Fintech vrstva roste rychle, ale bez zveřejněné české báze firem.** Revolut ČR > 1,2 mil. zákazníků (2025) a MAU firem +31 % `[FACT-S]`; absolutní počet českých firemních klientů, ani ceník v CZK, nejsou veřejné. Partners Banka podnikatele neobsluhuje; plán 2026 `[FACT-S]` – stav k 9/2026 nutno ověřit. Wise, Trinity, mBank zůstávají nepokryté.

**D7. Největší datová mezera celého WS3b jsou průzkumová data (bod 8) a ratingy aplikací (bod 3).** Bez SME Banking Club / Ipsos-ČBA / Zlaté koruny nelze sestavit tabulku podílů ani anket; toto je první úkol navazujícího běhu.

---

## E. „So what" pro Českou spořitelnu

1. **Přeceňte cenový benchmark z „poplatek za účet" na „výnos ze zůstatku do 300 tis. Kč".** Tři challengeři mají účet za 0 Kč a úročí 1,4–2,6 % `[FACT-S]`; pokud ČS nabízí podnikatelům 0 % na běžném účtu, ztrácí argument u FOP s průměrnou volnou likviditou v řádu desítek až stovek tisíc Kč.
2. **Bránit „first account" nových FOP.** Air Bank deklaruje ¼ nových OSVČ (2025) `[CLAIM]`, ~23 tis. ročně `[EST]`. ČS by měla měřit vlastní podíl na nově registrovaných OSVČ (RŽP × onboarding) a cílit start-up FOP onboardingem srovnatelné rychlosti (Air Bank: bez pobočky i pro s.r.o.).
3. **Využít úvěrovou mezeru challengerů.** Air Bank bez kontokorentu `[FACT-S]`, Creditas/Fio bez veřejných parametrů; ČS má šanci pozicovat rychlý předschválený kontokorent/úvěr jako důvod pro primární účet – zejména u FOP, kteří „dorostou" z Air Bank.
4. **Integrace jako obranný příkop:** Fio API + Fakturoid/iÚčto `[FACT-S]` je standard, který digitální FOP očekávají; ČS by měla ověřit paritu (API, párování plateb, fakturace v aplikaci jako Air Bank – 30 tis. faktur/měs.).
5. **Sledovat rozšiřování Air Bank na s.r.o. a vstup Partners Banky (2026).** Obě zprávy signalizují, že se cenový tlak „0 Kč + úrok" přesune z FOP do mikro-PO, kde ČS dnes drží vyšší fee-income.

---

## F. Log odhadů a datových mezer

| ID | Položka | Typ | Postup / kde dohledat |
|---|---|---|---|
| G1 | Fio: počet podnikatelských klientů, úvěry, pobočky ČR, úročení | `[DATA GAP]` | fio.cz/tiskove-zpravy; VZ 2024/2025 [Z24], [Z25]; Finex „Fio spořicí účet"; kontaktní údaje poboček (fio.cz/kontakty – spočítat). |
| G2 | Creditas: úvěry pro FOP/PO, pobočky, zisk 2024/2025, počet klientů 2025 (250 vs. 260 vs. 400 tis.) | `[DATA GAP]` | creditas.cz/o-bance/vyrocni-zpravy; e15 [Z33]; justice.cz sbírka listin. |
| G3 | UniCredit: hranice segmentu small business, pobočky, segmentové úvěry/vklady, základní sazba a strop bonusu 2,50 % | `[DATA GAP]` | VZ 2025 [Z42] (segmentová analýza), kampaňové podmínky [Z39]. |
| G4 | Air Bank: pobočky, firemní úvěr, terminál/brána, API, čas onboardingu, metodika průzkumu 2023 | `[DATA GAP]` | airbank.cz/produkty, TZ 5/2023 [Z10], VZ 2025 [Z54]. |
| G5 | Ratingy App Store / Google Play (všechny banky) | `[DATA GAP]` | apps.apple.com, play.google.com – k datu sběru uvést počet hodnocení. |
| G6 | Průzkumy podílů (SME Banking Club, Datank, Ipsos/ČBA, Deloitte DBM, EY, AMSP) | `[DATA GAP]` | smebanking.club (Czech SME Banking report), cbaonline.cz/vyzkumy, deloitte.com/cz DBM, amsp.cz „Banka roku podnikatelů". |
| G7 | Ankety 2021–2025 (Zlatá koruna, Banka roku, Finparáda, HN, Měšec) | `[DATA GAP]` | viz C3. |
| G8 | NPS podnikatelů, finanční arbitr | `[DATA GAP]` | viz C4. |
| G9 | Wise Business, Trinity Bank, mBank – kompletní profily | `[DATA GAP]` | wise.com/cz/business/pricing; trinitybank.cz; mbank.cz/firemni; Wise plc AR; mBank S.A. AR. |
| G11 | Přímé URL, které je nutné v navazujícím běhu znovu načíst (v tomto běhu blokovány proxy) | `[DATA GAP]` | https://www.revolut.com/cs-CZ/business/ ; https://www.trinitybank.cz/podnikatele ; https://www.mbank.cz/firemni/ ; https://www.airbank.cz/produkty/podnikatelsky-ucet/ ; https://www.fio.cz/bankovni-sluzby/bankovni-ucty/podnikatelsky-ucet ; https://www.creditas.cz/firemni-ucet ; https://www.unicreditbank.cz/cs/podnikatele-a-mensi-firmy/zacinam-podnikat/ucty-a-platebni-terminaly.html ; https://www.partnersbanka.cz/cenik-a-urokove-sazby ; https://wise.com/cz/business |
| G10 | Cenový vývoj 2021→2024 (účty, sazby úvěrů, vklady) u všech bank | `[DATA GAP]` | Archivy Finparáda/Měšec/Peníze.cz „srovnání podnikatelských účtů" 2021, 2022, 2023, 2024; ČNB ARAD (sazby vkladů nefin. podniků jako tržní kotva). |
| E1 | Air Bank ≈ 5–6 % registrovaných OSVČ | `[EST]` | 65 000 ÷ ~1 170 000 (ČSSZ 12/2025, vč. vedlejší; číslo převzato z briefu/WS1, v tomto běhu neověřeno); čitatel zahrnuje i s.r.o. a sekundární účty → spíše horní odhad. |
| E2 | Air Bank ≈ 23 tis. nových FOP/rok | `[EST]` | 0,25 × 91 615 (podíl = `[CLAIM]` banky). |
| E3 | Pobočky Air Bank ~30, Fio ~80 | `[EST]` | Obecně známé řády, v tomto běhu neověřeno; nahradit G1/G4. |
| E4 | Skóre v tabulce C1 | `[EST]` | Expertní hodnocení na ověřených bodech; u `[DATA GAP]` buněk nepoužívat. |

---

## G. Zdroje (přístup 2026-09-08; všechny přes výsledky vyhledávání, plný text nedostupný – viz metodická poznámka)

- [Z1] Air Bank – „Podnikatelský účet Air Bank je nově dostupný i pro vícečlenné s.r.o." (TZ, 23. 1. 2026): https://www.airbank.cz/novinky/podnikatelsky-ucet-od-air-bank-je-nove-dostupny-i-pro-viceclenne-s-r-o/
- [Z2] Air Bank – Podnikatelský účet zdarma (produktová stránka): https://www.airbank.cz/produkty/podnikatelsky-ucet/
- [Z3] Air Bank – „V loňském roce začalo podnikat nejvíce OSVČ za posledních 10 let…" (TZ, 1/2026): https://www.airbank.cz/novinky/v-lonskem-roce-zacalo-podnikat-nejvice-osvc-za-poslednich-10-let-mezi-nove-trendy-patri-digitalni-nomadstvi-i-rehabilitace-domacich-mazlicku/
- [Z4] Air Bank – Neauditované konsolidované výsledky skupiny za rok 2025: https://www.airbank.cz/novinky/neauditovane-konsolidovane-vysledky-hospodareni-skupiny-air-bank-za-kalendarni-rok-2025/
- [Z5] Finex – Air Bank podnikatelský účet, recenze a podmínky (2026): https://finex.cz/banka/air-bank/podnikatelsky-ucet-air-bank/
- [Z6] Finex – Air Bank podnikatelský spořicí účet (2026): https://finex.cz/banka/air-bank/air-bank-podnikatelsky-sporici-ucet/ ; Air Bank – Úročení podnikatelského spořicího účtu: https://www.airbank.cz/co-vas-nejvic-zajima/uroceni-podnikatelskeho-sporiciho-uctu/
- [Z7] 5nej.cz – Air Bank podnikatelský účet recenze 2026 (kontokorent): https://www.5nej.cz/air-bank-podnikatelsky-ucet-recenze/
- [Z8] Forbes – „Air Bank zvýšila zisk o 45 procent na 1,9 miliardy…": https://forbes.cz/air-bank-zvysila-zisk-o-45-procent-na-19-miliardy-pocet-klientu-a-objem-uveru-stoupl/ ; „Zisk Air Bank loni vzrostl o čtvrtinu. Počet klientů se zvýšil na dva miliony": https://forbes.cz/zisk-air-bank-loni-vzrostl-o-dvacet-tri-procent-pocet-klientu-se-skupine-zvysil-na-dva-miliony/
- [Z9] e15 – „Air Bank hlásí rekordní pololetí… klientů už má 2,1 milionu" (2025): https://www.e15.cz/byznys/finance-a-bankovnictvi/air-bank-hlasi-rekordni-pololeti-zisk-skocil-o-petinu-klientu-uz-ma-2-1-milionu-1435301
- [Z10] Air Bank – „Každý druhý živnostník není podle průzkumu spokojený se svou bankou…" (TZ, 5/2023): https://www.airbank.cz/novinky/kazdy-druhy-zivnostnik-neni-podle-pruzkumu-spokojeny-se-svou-bankou/
- [Z11] Air Bank – „Air Bank nově nabízí podnikatelský účet i malým s. r. o." (TZ, 2025): https://www.airbank.cz/novinky/air-bank-nove-nabizi-podnikatelsky-ucet-i-malym-s-r-o/
- [Z12] Měšec – „Air Bank začíná s podnikatelským účtem. Podmínky i úročení budou podobné jako u konta pro spotřebitele" (5/2023): https://www.mesec.cz/aktuality/air-bank-zacina-s-podnikatelskym-uctem-podminky-i-uroceni-budou-podobne-jako-u-konta-pro-spotrebitele/
- [Z13] Fio banka – Podnikatelský bankovní účet bez poplatků: https://www.fio.cz/bankovni-sluzby/bankovni-ucty/podnikatelsky-ucet
- [Z14] Fio banka – Podnikatelský kontokorent: https://www.fio.cz/bankovni-sluzby/uvery/kontokorent-podnikatel
- [Z15] Fio banka – Platební terminály a platební brána: https://www.fio.cz/bankovni-sluzby/platebni-karty/platebni-terminaly-brana
- [Z16] Fakturoid – Propojení s platební bránou GoPay: https://www.fakturoid.cz/podpora/automatizace/platebni-brana-gopay
- [Z17] Fio banka – API Bankovnictví: https://www.fio.cz/bankovni-sluzby/api-bankovnictvi ; dokumentace: https://www.fio.cz/docs/cz/API_Bankovnictvi.pdf
- [Z18] Fakturoid – Automatické párování plateb z Fio banky (API): https://www.fakturoid.cz/podpora/parovani/fio-api
- [Z19] iÚčto – Propojení s Fio bankou: https://www.iucto.cz/funkce/integrace-fio-bankou/
- [Z20] Fio banka – VZ 2025 (SK verze, nefetchovatelné): https://www.fio.sk/docs/sk/Fio_banka_VZ_ZoV_2025.pdf
- [Z21] Fio banka – TZ „Fio bance je 15 let, má 1,55 milionu klientů a vydává hospodářské výsledky" (2/2025): https://www.fio.cz/spolecnost-fio/media/tiskove-zpravy/310050-fio-bance-je-15-let-ma-1-55-milionu-klientu-a-vydava-hospodarske-vysledky
- [Z22] Kurzy.cz – „Fio bance je 15 let, má 1,55 milionu klientů a za rok 2024 vydělala čistého 6,07 mld. Kč": https://zpravy.kurzy.cz/810535-fio-bance-je-15-let-ma-1-55-milionu-klientu-a-za-rok-2024-vydelala-cisteho-6-07-mld-kc/
- [Z23] Seznam Zprávy – „Čistý zisk Fio banky loni klesl o pět procent na 6,1 miliardy korun": https://www.seznamzpravy.cz/clanek/ekonomika-firmy-cisty-zisk-fio-banky-loni-klesl-o-pet-procent-na-61-miliardy-kc-276025
- [Z24] Fio banka – Výroční zpráva 2024 (nefetchovatelné): https://www.fio.cz/docs/cz/Fio_banka_vyrocni_zprava_2024.pdf
- [Z25] Wikipedie – Fio banka: https://cs.wikipedia.org/wiki/Fio_banka
- [Z26] Finex – Creditas Spořicí účet+ pro firmy a podnikatele (2026): https://finex.cz/banka/creditas/sporici-ucet-pro-firmy-podnikatele-creditas/
- [Z27] Peníze.cz – Banka CREDITAS Firemní účet: https://www.penize.cz/osobni-ucty/319327-banka-creditas-firemni-ucet
- [Z28] Pujcka.co – Banka CREDITAS Firemní účet: https://www.pujcka.co/banka-creditas-firemni-ucet
- [Z29] e15 – „Sloučení Banky Creditas s Max Bankou dokončeno…" (10/2024): https://www.e15.cz/finexpert/banky-a-ucty/slouceni-banky-creditas-s-max-bankou-dokonceno-internetove-bankovnictvi-docasne-nefunguje-1418962
- [Z30] Forbes – „Max banka končí. Ode dneška se plně sloučila s Bankou Creditas" (1. 10. 2024): https://forbes.cz/max-banka-konci-ode-dneska-se-plne-sloucila-s-bankou-creditas/
- [Z31] Měšec – „Max banka končí, od října se sloučí s Bankou CREDITAS…": https://www.mesec.cz/clanky/max-banka-konci-od-rijna-se-slouci-s-bankou-creditas/
- [Z32] TOP.cz – Banka CREDITAS recenze 2026: https://www.top.cz/banka-creditas-recenze
- [Z33] e15 – „Banka Creditas šestinásobně zvýšila zisk, pomohly jí nákupy v zahraničí": https://www.e15.cz/byznys/finance-a-bankovnictvi/banka-creditas-sestinasobne-zvysila-zisk-pomohly-ji-nakupy-v-zahranici-1431972
- [Z34] HN – „Generační obměna a expanze skupiny Creditas": https://ai.hn.cz/kontext/6834981d86e14ce587c71b8f/generacni-obmena-a-expanze-skupiny-creditas
- [Z35] UniCredit Bank – Podnikatelé a menší firmy › Účty a platební terminály: https://www.unicreditbank.cz/cs/podnikatele-a-mensi-firmy/zacinam-podnikat/ucty-a-platebni-terminaly.html
- [Z36] UniCredit Bank – Sazebník, Část Small Business (4/2015, historický): https://www.unicreditbank.cz/content/dam/cee2020-pws-cz/cz-dokumenty/dokumenty-produkty/sazebniky/UCB_Sazebnik_SB_04_2015.pdf
- [Z37] Finex – UniCredit Bank Business účty, recenze a podmínky: https://finex.cz/banka/unicredit-bank/business-ucty-unicredit-bank/
- [Z38] Wise blog – UniCredit podnikatelský účet: typy, poplatky, založení: https://wise.com/cz/blog/unicredit-podnikatelsky-ucet
- [Z39] UniCredit Bank – Podmínky marketingové kampaně, účty Business START/OPEN/TOP – bonusová sazba (1. 1. 2025): https://www.unicreditbank.cz/content/dam/cee2020-pws-cz/cz-dokumenty/kampane/Podminky-marketingove-kampane-business-ucty-bonusova-sazba-01012025.pdf
- [Z40] Banky.cz – UniCredit Bank, kontakty a info: https://www.banky.cz/banky/unicredit-bank/
- [Z41] UniCredit Bank CZ&SK – Pololetní finanční zpráva 2025: https://www.unicreditbank.cz/content/dam/cee2020-pws-cz/cz-dokumenty/o-bance/vyrocni-zpravy/Pololetni-zprava-2025-CZE.pdf
- [Z42] UniCredit Bank CZ&SK – Výroční zpráva 2025 „Acceleration in action": https://www.unicreditbank.cz/content/dam/cee2020-pws-cz/cz-dokumenty/o-bance/vyrocni-zpravy/VZ-2025-CZ.pdf
- [Z43] CzechCrunch – „Revolut v Česku raketově roste, překonal milion uživatelů…" (3/2025): https://cc.cz/revolut-v-cesku-raketove-roste-prekonal-milion-uzivatelu-a-nechava-za-sebou-i-velka-bankovni-jmena/
- [Z44] CzechCrunch – „Revolut v Česku dál roste. Má 1,3 milionu uživatelů…" (2026): https://cc.cz/revolut-v-cesku-dal-roste-ma-13-milionu-uzivatelu-kteri-s-nim-uz-zdaleka-neplati-jen-v-zahranici/
- [Z45] Newstream – „Revolut dosáhl rekordních výsledků. V Česku má milion klientů": https://www.newstream.cz/zpravy-z-firem/revolut-dosahl-rekordnich-vysledku-v-cesku-ma-milion-klientu
- [Z46] Kurzy.cz – „Revolut hlásí za rok 2025 rekordní zisk 2 mld. eur, tržby 5,3 mld. eur": https://zpravy.kurzy.cz/854356-revolut-hlasi-za-rok-2025-rekordni-zisk-ve-vysi-2-mld-eur-zatimco-trzby-vzrostly-na-5-3-mld-eur/
- [Z47] HN – „Revolut vloni zaznamenal rekordní výsledky… jaké bankovní produkty chystá v Česku": https://archiv.hn.cz/c1-67858670-revolut-vloni-zaznamenal-rekordni-financni-vysledky-na-cem-primarne-vydelava-a-jake-bankovni-produkty-chysta-v-cesku
- [Z48] Peníze.cz – „Další plány Partners Banky? Balíček pro cestovatele, multiměnový účet nebo investice": https://www.penize.cz/osobni-ucty/468192-dalsi-plany-partners-banky-balicek-pro-cestovatele-multimenovy-ucet-nebo-investice
- [Z49] TOP.cz – Partners Banka recenze 2026: https://www.top.cz/partners-banka-recenze
- [Z50] bankycr.cz – Partners Banka, detailní analýza: https://bankycr.cz/banks/partners-banka
- [Z51] Finmag – „Podnikatelské účty 2026: Vyplatí se vám? Přehled výhod, poplatků a nabídek bank": https://www.finmag.cz/finance/485143-podnikatelske-ucty-2026-vyplati-se-vam-prehled-vyhod-poplatku-a-nabidek-bank
- [Z52] Banky.cz – Srovnání nejlepších podnikatelských účtů pro OSVČ 2026: https://www.banky.cz/prehled-a-porovnani/bezny-ucet/podnikatelsky-ucet/
- [Z53] Finex – Podnikatelské účty: srovnání 2026: https://finex.cz/rubrika/banky/bankovni-ucty/podnikatelske-ucty/
- [Z54] Air Bank – Konsolidovaná výroční zpráva 2025 (nefetchovatelné): https://www.airbank.cz/file-download/5120-vyrocni-zprava-2025.pdf
- [Z55] Wise blog – Air Bank podnikatelský účet, co umí a kolik stojí: https://wise.com/cz/blog/podnikatelsky-ucet-air-bank
