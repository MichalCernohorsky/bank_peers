# WS L4 (SVĚT mimo Evropu) + L6 (CORPORATE) – věrnostní programy pro podnikatele a firmy

Stav k 6. 10. 2026 · cut-off aktuální nabídky 06/2026 · metoda: pouze WebSearch (výtahy výsledků), WebFetch nepoužit · 38/38 vyhledávání
Data: `L4_svet.csv` (29 řádků WD-xx = programy mimo Evropu, 10 řádků CO-xx = corporate rebaty a pricing).

Upozornění k metodě: FACT znamená, že číslo je ve výtahu výsledku vyhledávání s uvedenou URL. Většina produktových stránek nemá ve výtahu datum, a proto má dle briefu značku `[STALE: datum neznámé]`, i když jde o živé produktové stránky. Měny jsou v originále, na Kč nepřepočítávám (kurz ČNB v tomto běhu neověřen).

---

## 1. Shrnutí (7 bodů)

1. **Ve světě se pro FOP/mikro a SME věrnostní programy běžně používají a jsou retailové v mechanice.** Body nebo cashback na business kartách nabízí každá velká banka v USA, Kanadě, Austrálii a Singapuru (v CSV 22 karetních a vztahových programů bank a neobank, k tomu 2 programy karetních schémat a 3 nebankovní). Typické sazby v USA jsou 1,5–2 % flat (Chase Ink Unlimited 1,5 % `[FACT]`, Capital One Spark Cash Plus a Wells Fargo Signify Business Cash 2 % `[STALE: datum neznámé]`), kategorie 3–5 % se stropy (Ink Business Cash 5 % do 25 000 USD/rok `[FACT]`).
2. **Bank of America Preferred Rewards for Business je nejčistší ucelený vztahový program pro podnikatele.** Tiery jsou podle 3měsíčního průměrného zůstatku: Gold 20 000, Platinum 50 000, Platinum Honors 100 000 USD `[FACT, 2026]`. Benefity: +25/50/75 % ke karetním odměnám, odpuštěné poplatky až 4+4 účtů, sleva 0,25 p.b. z úvěrů, sleva 0,05 % na merchant services `[STALE: datum neznámé]`. Program pokračuje samostatně i po nahrazení retailového Preferred Rewards programem BofA Rewards (27. 5. 2026) `[FACT, 02/2026]`.
3. **Karetní schémata provozují vrstvu odměn financovaných obchodníky pro malé firmy.** Visa SavingsEdge (relaunch 13. 6. 2024, USA a Kanada, Visa Business kreditní, debetní i předplacené karty, kredit na výpisu) `[FACT; STALE: 06/2024 pro současný stav]`. Mastercard Easy Savings (rebaty „až 20 %“, „50 000+ lokací“) `[CLAIM]` je dle Novo stále aktivní `[FACT, 06/2026]` a má stránky i pro Maltu a spuštění pro Ukrajinu 2024. Je tedy dostupný i v Evropě, dostupnost v ČR je `[DATA GAP]`.
4. **Nebankovní B2B věrnost jsou hlavně aerolinky.** Qantas Business Rewards (firma získá 20/30/40 bodů na každých 100 bodů cestujících, vstupní poplatek 89,50 AUD), SIA HighFlyer (5 bodů/SGD, zdarma) a Emirates Business Rewards (1 bod/USD, zdarma, „30 000+ MSME“ `[CLAIM]`). Emirates program výslovně cílí na firmy **bez** korporátní cestovní smlouvy `[STALE: datum neznámé]`. To je nepřímý doklad H3.
5. **U mid a large corporate se klasické body nevyskytují.** Loajalitu nesou (a) smluvní **rebaty u commercial karet** podle objemu a rychlosti úhrady, (b) **earnings credit rate** (ECR), kdy zůstatky kompenzují poplatky za cash management, a (c) **relationship-based pricing** přes RM. Příklad: GSA SmartPay ve FY2025 vrátil 471 mil. USD z útraty 39,4 mld. USD `[FACT]`, tj. efektivně **1,20 %** `[EST: 471/39 400]`.
6. **Rebaty u commercial karet jsou tierované v bps.** Na státních kontraktech USA: JPM pro stát NY 180,5–43 bps dle tieru, BofA pro NC cca 1,99–2,18 % dle objemu (350–550+ mil. USD) a doby úhrady (2–25 dní), U.S. Bank/NASPO 34,75 bps národní objemový incentive `[STALE: datum neznámé]`. Interchange Visa USA pro commercial karty (od 18. 4. 2026) je 1,75–2,95 % + 0,10 USD, u large ticket 1,30 % + 35 USD `[FACT]`. Odtud se rebaty financují `[EST – odvozeno]`.
7. **Regulace:** IFR 2015/751 vyjímá commercial karty (vydané podniku, OSVČ nebo veřejnému subjektu, jen pro business výdaje, účtované přímo na jeho účet) z kapitoly II se stropy `[FACT, EUR-Lex 2015]`. Srovnání interchange consumer vs. commercial v USA se v tomto běhu nepodařilo získat `[DATA GAP]`.

---

## 2. L4 – přehled podle regionů

### 2.1 USA – banky

| ID | Program | Mechanika | Klíčová čísla | Značka |
|---|---|---|---|---|
| WD-01 | BofA **Preferred Rewards for Business** | C (+A, E) | tiery 20/50/100 tis. USD, bonus 25/50/75 % ke karetním odměnám | FACT (tiery, 2026) / STALE (benefity) |
| WD-03 | Chase **Ink Business Preferred** | A | 3x do 150 000 USD/rok v kategoriích, poplatek 95 USD | CLAIM (srovnávače) |
| WD-04 | Chase **Ink Business Cash** | A | 5 % do 25 000 USD (kancelář, telco), 2 % do 25 000 USD (PHM, restaurace), 1 % | FACT (chase.com) |
| WD-05 | Chase **Ink Business Unlimited** | A | 1,5 % bez stropu, bez ročního poplatku | FACT |
| WD-06 | Chase **Ink Business Premier** | A | 2,5 % velké nákupy / 2 % ostatní | STALE |
| WD-07 | Amex **Blue Business Plus** (Membership Rewards) | A (+D) | 2x MR do 50 000 USD/rok, bez poplatku | CLAIM/STALE |
| WD-08 | Amex **Business Gold** – Flexible Business Credit | F/A | až 20 USD/měsíc (240 USD/rok) za FedEx, Grubhub, kancelář (FedEx do 1. 10. 2026) | FACT (2026) |
| WD-09 | **Amex Offers** (business) | D | kredit na výpisu nebo body MR, financují obchodníci | STALE |
| WD-10 | Capital One **Spark Cash Plus** | A | 2 % bez stropu, 5 % hotely a auta přes portál, poplatek 150 USD vrácen při útratě ≥ 150 000 USD | STALE |
| WD-11 | Wells Fargo **Signify Business Cash** | A | 2 % bez stropu, bez poplatku | STALE |
| WD-12 | U.S. Bank **Triple Cash Rewards Visa Business** | A (+F) | 3 % v kategoriích / 1 %, kredit 100 USD na software | STALE |
| WD-29 | Chase Offers na Ink | D | neověřeno | DATA GAP |

Poznámka k Chase Ink Business Preferred: AKV bonus 100 000 bodů po útratě 8 000 USD za 3 měsíce `[CLAIM]` evidován jako akviziční bonus, ne jako loajalita. Další AKV bonusy: U.S. Bank 750 USD, Amex BBP 15 000 bodů.

### 2.2 USA – fintechy (corporate karty)

- **Brex (WD-13):** 7x rideshare, 4x lety a hotely přes Brex Travel, 3x restaurace, 2x opakovaný software, 1x ostatní. Bez stropu a bez expirace, body lze vyplatit na Brex business účet `[FACT, brex.com 08/2026]`. „Partner perks v hodnotě 350 000+ USD“ `[CLAIM]`.
- **Ramp (WD-14):** flat cashback, bez ročního poplatku, bez osobního ručení, cashback lze převést na Ramp Checking Account. „Až 5 % úspor“ `[CLAIM]`. **Výše cashbacku `[DATA GAP: support.ramp.com / T&C Ramp card]`.**
- Vzorec u obou fintechů: odměna je napojená na **vlastní účet nebo spend platformu**. Karta slouží jako akviziční háček pro celou expense/AP platformu. Je to tentýž princip jako u vztahového balíčku banky.

### 2.3 Karetní schémata (USA, globálně)

- **Visa SavingsEdge (WD-15):** relaunch 12.–13. 6. 2024 pro USA a Kanadu. Funguje pro Visa Business kreditní, debetní i předplacené karty. Nabízí dvě cesty: Instant Coupons (kód u pokladny) a Cashback Offers (kredit na budoucím výpisu po registraci karty). Novinky relaunche jsou stovky nových nabídek, real-time notifikace a cash-back tracker `[FACT 06/2024; současný stav STALE: 06/2024]`.
- **Mastercard Easy Savings (WD-16):** „global small business loyalty program“, automatické rebaty bez kuponů a kódů, bez ročního poplatku, sleduje se v aplikaci a na výpisu `[STALE: datum neznámé]`. Rebaty „až 20 %“ a „50 000+ lokací“ jsou `[CLAIM]`. Mastercard program prezentuje jako nástroj, který vydavatelům pomáhá „attract and retain“ klienty. Program nabízí i neobanka Novo (USA) `[FACT, 06/2026]`. Stránky Mastercard existují pro SG, IN, MY, MT a MEA a v roce 2024 byl program spuštěn na Ukrajině.

### 2.4 Kanada

- **RBC Avion Visa Business / Avion Visa Infinite Business (WD-17):** 1 bod/CAD, resp. 1,25 bodu/CAD do 75 000 CAD/rok. Body ze zaměstnaneckých karet se sdružují na jeden účet a lze je **slučovat s osobní Avion kartou** (relevantní pro H6). Partnerství s Petro-Canada: sleva 3 c/l a +20 % bodů `[STALE: datum neznámé]`.
- **TD Business Travel Visa (WD-18):** 9/6/2 body TD Rewards na 1 CAD podle kategorie `[STALE: datum neznámé]`.
- Amex Canada Business: v tomto běhu neověřeno `[DATA GAP]`.

### 2.5 Austrálie

- **Qantas Business Rewards (WD-19, nebankovní):** firma získá 20/30/40 bodů na každých 100 bodů, které nalétají její cestující (Level 1/2/3). Cestující dostane +250 bodů za rezervaci s ABN firmy. Vstupní poplatek je jednorázově 89,50 AUD, roční poplatek není `[STALE: datum neznámé]`. Na program se napojují banky:
- **CommBank Business Awards (WD-20):** 1 bod Awards/AUD, nebo 0,4 bodu Qantas za opt-in 30 AUD/rok. T&C CommBank Awards datované 28. 9. 2026 `[FACT]`, stránka karty `[STALE]`. **CommBank Qantas Business Rewards card (WD-21):** 0,60 bodu/AUD domácí, 1,25 bodu/AUD zahraniční, strop 100 000 AUD útraty za výpisové období `[STALE]`.
- **NAB Qantas Business Signature (WD-22):** 1 bod za 1,50 AUD včetně vládních plateb. Retenční prvek: +50 000 bodů, pokud klient ponechá účet 15 měsíců `[STALE]`.
- **Westpac Altitude Business (WD-23):** až 2 body/AUD, volba Altitude nebo Qantas `[STALE]`. **ANZ Business Black (WD-24):** 1,5 bodu/AUD do 10 000 AUD za výpisové období, nad tuto částku 1 bod `[STALE]`.

### 2.6 Singapur / Asie / Blízký východ

- **SIA HighFlyer (WD-25):** spuštěn 4. 7. 2017 `[FACT]`. Firma získá 5 bodů/SGD (Gold a Platinum 6), zaměstnanci KrisFlyer míle, členství je zdarma, body platí 3 roky, 4 tiery `[STALE: datum neznámé]`.
- **Emirates Business Rewards (WD-26):** 1 bod/USD z base fare, zdarma, bez minimální útraty, určeno firmám bez corporate travel agreement `[STALE]`. „30 000+ MSME“ `[CLAIM]`.
- **DBS (WD-27):** Business Advance+ Debit dává 1 % cashback bez stropu při útratě ≥ 2 000 SGD/měsíc na vybrané B2B výdaje. Platinum Business přidává +2 % na AI útratu `[STALE]`.
- **OCBC (WD-28):** debetní karta 1 % v business kategoriích (e-commerce, digitální marketing, software, AI, cestování) a 0,2 % ostatní, kreditní karta 3 % u eco obchodníků, 1 % FX a 0,2 % SGD `[STALE]`. Nízká základní sazba 0,2 % kontrastuje se sazbou 2 % v USA (viz H4).
- UOB, Indie, Brazílie: neověřeno `[DATA GAP]`.

**Akceptační minimum L4 splněno:** 29 řádků mimo Evropu, z toho 28 identifikovaných programů (WD-29 je DATA GAP). Pokrytí USA, Kanady, Austrálie, Singapuru a UAE.

---

## 3. L6 – Corporate (mid a large)

### 3.1 Rebaty u commercial / purchasing / travel karet (G)

- **Mechanika:** rebate je smluvní revenue share z karetní útraty. Výše závisí na **objemu** (tiery) a na **rychlosti úhrady** (payment days, frekvence výpisu). J.P. Morgan: „At the end of the contract period, you'll receive a rebate based on your spend volume and your contractually negotiated rebate rates. Rebates are typically paid annually.“ `[STALE: datum neznámé, jpmorgan.com]`
- **GSA SmartPay (CO-01):** FY2025 útrata 39,4 mld. USD, refundy 471 mil. USD, 82 mil. transakcí, 4,2 mil. účtů, od vzniku 7,2 mld. USD refundů `[FACT, smartpay.gsa.gov]`. Efektivní sazba 1,20 % `[EST = 471/39 400]`. GSA v 04/2026 vyhlásila RFI k modernizaci programu `[FACT]`.
- **Státní kontrakty (CO-04 až CO-06):** JPM–NYS 180,5–43 bps dle čtvrtletní útraty, BofA–NC cca 1,99–2,18 % dle objemu a splatnosti, U.S. Bank–NASPO 34,75 bps národní objemový incentive `[STALE: datum neznámé]`. Starší dokumenty US Department of Commerce (2017–2021) uvádějí purchase 109–120 bps, travel 75–89 bps a při týdenním výpisu 157–168 bps `[STALE: 2017–2021]`.
- **Citi VCA / ePayables (CO-03):** přesun plateb dodavatelům ze šeků na virtuální karty zvyšuje rebate, „travel spend is often a significant contributor“ `[CLAIM; STALE]`.
- Corpay: mid-market virtual card 1,0–1,5 %, až 2,0 % `[CLAIM – agregátor, metodika neznámá]`. Nepoužito jako FACT.
- **Financování:** z interchange. Visa USA od 18. 4. 2026 účtuje commercial card present 2,50 % + 0,10 USD, CNP 2,70 % + 0,10 USD, Commercial Product 3 1,75 % + 0,10 USD, large ticket 1,30 % + 35 USD, Large Purchase Advantage 0,70 % + 49,50 USD až 0,40 % + 58,50 USD `[FACT]`. Rebaty kolem 1–2 % jsou tedy krytelné jen díky vysokému interchange `[EST – odvozeno]`.

### 3.2 Earnings credit rate a account analysis (C)

- **Mechanika (CO-07):** banka měsíčně počítá imputovaný úrok (earnings credit) z průměrných denních zůstatků na DDA účtech podle vyjednané, často tierované sazby ECR. Earnings credit se odečte od poplatků za služby. Když earnings credit převýší poplatky, klient neplatí nic `[FACT – definice AFP, financialprofessionals.org]`. Zůstatky tak „platí“ cash management. Je to korporátní obdoba „aktivitní nuly“, jen řízená zůstatky.
- **Úroveň:** podle Curinos byl průměr ECR 79 bps (09/2023, beta 10 %) a 76 bps (01/2024), zatímco úročené DDA a MMDA přesáhly 300 bps `[STALE: 01/2024; CLAIM – Curinos, metodika částečně známá]`. Banky nabízejí **hybridní účty**: ECR pokryje poplatky a nad tuto částku se platí hard interest `[STALE: datum neznámé]`.

### 3.3 Relationship-based pricing, balíčky, RM (C, F)

- McKinsey: „about 5 percent of strategic clients account for half of a bank's revenues and almost two-thirds of its economic profit“. Relationship-based pricing oceňuje celý dlouhodobý vztah. Klienti s primárním vztahem mají ROE zhruba o 20 p.b. vyšší než klienti jen s úvěrem. Doporučuje zjednodušený pricing s balíčky a pricing engine, který RM dává guidance proti odchodu klienta `[CLAIM – poradenská firma; STALE: datum neznámé]`.
- Oliver Wyman (2023): přední banky zavádějí relationship pricing modely a experimentují se subscription pricingem `[CLAIM; STALE: 2023]`. BCG (2018): bundling pomáhá cross-sellu, ale špatně nastavený balíček vede ke ztrátě, když klient přestane kupovat ziskové produkty a zůstane mu cena balíčku `[CLAIM; STALE: 2018]`.
- **BofA Employee Banking & Investing (CO-09):** benefity a odměny pro zaměstnance korporátních klientů. Podle titulku press release jde o 4 mil. zaměstnanců `[STALE: 02/2024; CLAIM; obsah DATA GAP]`. Loajalita korporace se tu buduje přes benefit, který nese HR klienta, a ne přes body pro firmu.

---

## 4. Případové studie do hloubky

### 4.1 Bank of America – Preferred Rewards for Business (povinná)
- **Mechanika:** vztahový tierový program (C) nad business běžným účtem. Kvalifikuje **kombinovaný průměrný denní zůstatek za 3 celé kalendářní měsíce** na business vkladech BofA a/nebo investičních účtech Merrill. Tiery Gold ≥ 20 000, Platinum ≥ 50 000 a Platinum Honors ≥ 100 000 USD. Upgrade je automatický po kterémkoli měsíci, benefity se drží **min. 1 rok** i při dočasném poklesu zůstatku `[FACT]`. Program je bez poplatku a otevřený klientům Business Banking, Merrill Business a Private Bank Business `[FACT]`.
- **Odměny** `[STALE: datum neznámé, business.bankofamerica.com]`:
  - +25/50/75 % ke karetním odměnám (příklad BofA: nákup 100 USD se 3 % dává 3,00 USD a v tierech 3,75, 4,50 a 5,25 USD),
  - bez měsíčních poplatků až na 4 business běžných a 4 spořicích účtech a bez dalších drobných poplatků (náhradní karta, šekové služby, příchozí domácí wire, stop payment),
  - 5% booster úroku na Business Advantage Savings,
  - sleva 0,25 p.b. z úrokové sazby nových úvěrových linek, termínovaných a zajištěných úvěrů,
  - sleva 0,05 % z ceny Merchant Services (Simplified Pricing Plan).
- **Kdo financuje:** banka. Logika je cross-subsidy z vkladové marže `[EST – odvozeno, NIM BofA na business vkladech DATA GAP]`. Ilustrace: firma v tieru Platinum (≥ 50 000 USD) utratí 100 000 USD na kartě s 1,5 %. Základní odměna je 1 500 USD, bonus 50 % = 750 USD/rok `[EST = 100 000 × 1,5 % × 50 %]`. Bonus je tedy úměrný útratě, ne zůstatku. Banka „kupuje“ zůstatek a primární vztah (účet + karta + úvěr + akceptace) za jeden balíček slev.
- **Důkaz dopadu:** počet členů, retence ani přírůstek vkladů za business program **nejsou veřejně ve výtazích** `[DATA GAP: BofA earnings presentations, Consumer/Global Banking segment, 10-K]`. Nepřímé doklady: BofA ponechal business program beze změny, když retail přecházel na BofA Rewards (27. 5. 2026) `[FACT, 02/2026]`. Retailový BofA Rewards získal 3 mil.+ zapsaných za 7 týdnů `[FACT, press release 07/2026]` (jen retail).
- **Přenositelnost do ČR: 5/5.** Mechanika nepotřebuje obchodníky ani schéma, jen data o zůstatcích a ceník. ČS má podnikatelský účet, kartu, úvěry, akceptaci i investice, takže umí postavit „Gold/Platinum“ s odpuštěním poplatků, slevou z úvěru a bonusem na kartu. Rizika: kanibalizace poplatkových výnosů a nutnost kalibrovat prahy na český trh (20 000 USD nelze převzít mechanicky).

### 4.2 Commercial card rebaty (GSA SmartPay + státní kontrakty + J.P. Morgan)
- **Mechanika:** smluvní roční rebate v bps z karetní útraty, tierovaný podle objemu a zrychlený rychlejší úhradou (týdenní nebo denní výpis zvyšuje sazbu). Doklady: NC/BofA (payment days 2–25), Commerce (týdenní výpis 157–168 bps vs. 109–120 bps) `[STALE]`.
- **Kdo financuje:** interchange placený obchodníkem. Na commercial kartách v USA je 1,30–2,95 % + fix `[FACT 04/2026]`, rebate klientovi cca 1,2 % (GSA) `[EST]`. Zbytek je marže vydavatele (bez úvěrových ztrát a nákladů) `[EST – odvozeno]`.
- **Ekonomika a důkaz dopadu:** GSA 471 mil. USD/rok (FY2025) `[FACT]`. J.P. Morgan uvádí case Ashton Woods s +98 % útraty a +303 % rebate `[CLAIM]`. Rebate funguje jako „věrnost“: tiery motivují koncentrovat útratu u jedné banky a rebate se vyplácí na konci smluvního období.
- **Přenositelnost do ČR: 2/5.** Commercial karty jsou z IFR stropů vyňaty `[FACT]`, ekonomicky je tedy rebate v EU možný. Český trh commercial karet je ale malý, B2B platby jdou převodem a rebate musí konkurovat ceně převodu. Dávalo by smysl pro velké klienty s velkým objemem cestovních výdajů nebo nákupů (virtuální karty v AP). Objem commercial karet v ČR je `[DATA GAP: ČNB/Visa/MC CZ]`.

### 4.3 Earnings credit rate (account analysis)
- **Mechanika:** zůstatky na neúročeném účtu generují kredit, který kompenzuje poplatky za cash management `[FACT – AFP]`.
- **Kdo financuje:** banka z vkladového spreadu. Klient „platí“ ušlým úrokem. Při ECR cca 76–79 bps vs. 300+ bps u úročených účtů (2023–24) `[STALE; CLAIM Curinos]` jde pro banku o levný funding. Klient získá pohodlí a nulový ceník.
- **Důkaz dopadu:** kvantifikace retence `[DATA GAP]`. Curinos sám upozorňuje na riziko odlivu (excess ECR) `[STALE]`.
- **Přenositelnost do ČR: 3/5.** V ČR se korporátní cash management oceňuje individuálně. Explicitní kompenzace „zůstatek → poplatky“ je přenositelná jako transparentní forma relationship pricingu pro mid-corporate (a SME s vysokými zůstatky). Daňové a účetní dopady jsou `[DATA GAP]`.

### 4.4 Visa SavingsEdge / Mastercard Easy Savings (odměny financované obchodníky)
- **Mechanika:** schéma agreguje nabídky obchodníků pro business karty. Odměna je automatický rebate nebo kredit na výpisu `[FACT/STALE viz 2.3]`.
- **Kdo financuje:** obchodníci (sleva jako akviziční kanál B2B). Vydavatel nemusí mít vlastní rozpočet `[EST – odvozeno z popisu, smluvní model vydavatel–schéma DATA GAP]`.
- **Důkaz dopadu:** veřejná data o zapojení a dopadu chybí `[DATA GAP]`. U SavingsEdge proběhl relaunch po předchozí verzi programu, což ukazuje, že Visa produkt udržuje `[FACT 06/2024]`.
- **Přenositelnost do ČR: 4/5.** Easy Savings má evropské mutace (MT, UA). Ověřit dostupnost pro CZ BIN range a podmínky pro vydavatele `[DATA GAP: Mastercard CZ account manager]`. Rychlá výhra bez vlastního rozpočtu, ale bez diferenciace: dostupné komukoli s kartou daného schématu.

### 4.5 Aerolinkové business programy (Qantas, SIA, Emirates)
- **Mechanika:** firma získává body za lety zaměstnanců, zaměstnanci si ponechávají osobní míle. Doprovází je co-brand bankovní karty (CommBank, NAB, Westpac, Amex SIA) `[STALE]`.
- **Kdo financuje:** aerolinka (a partneři). Banka platí za body při co-brandu `[EST – odvozeno]`.
- **H3 doklad:** Emirates Business Rewards je určen firmám **bez** corporate travel agreement. Velké firmy dostávají smluvní ceny místo bodů `[STALE: datum neznámé]`.
- **Přenositelnost do ČR: 3/5.** Partnerství ČS s nebankovním B2B programem (letecký, palivový nebo telco) by stálo na existujících programech v ČR/EU, to je předmět jiných WS.

---

## 5. Verdikty k hypotézám

- **H2 – S rostoucí velikostí mizí body a cashback, nahrazuje je vztahový pricing, rebaty a balíčky: PODPOŘENO.** FOP/SME karty v USA, CA, AU a SG nesou body nebo cashback (WD-03 až WD-28). Pro corporate jsou doloženy rebaty v bps s objemovými tiery (CO-01 až CO-06), ECR (CO-07) a relationship pricing (CO-08). Přechodový článek je BofA PRB for Business (C pro SME/Merrill Business), který kombinuje oba světy. Výhrada: fintech corporate karty (Brex, Ramp) drží body/cashback i pro rostoucí firmy, takže hranice je spíš „karta pro FOP/SME a startupy vs. smluvní program pro corporate“ než čistě velikost.
- **H3 – Ve velkých korporacích klasický věrnostní program téměř není: PODPOŘENO.** V žádném zdroji nebyl nalezen bodový program pro large corporate. Loajalitu nese rebate (smluvní revenue share), ECR, pricing a RM (McKinsey `[CLAIM]`). Emirates explicitně odlišuje SME program od corporate smluv `[STALE]`. Nuance: rebate je fakticky tierovaná objemová odměna, tedy funkčně „věrnostní“, ale vyjednává se smluvně a individuálně.
- **H4 (část USA) – Motorem odměn je vyšší interchange: ČÁSTEČNĚ PODPOŘENO.** Interchange Visa USA pro commercial karty je 1,75–2,95 % + 0,10 USD (large ticket 1,30 % + 35 USD) `[FACT 04/2026]` a rebate GSA ≈ 1,20 % `[EST]`. Business karty v USA dávají 1,5–2 % flat, což je odměna krytelná jen z interchange výrazně nad 1 % `[EST – odvozeno]`. Amex 10-K FY2025: náklady na Membership Rewards a cashback vzrostly o 1 234 mil. USD, co-brand o 576 mil. USD, „primarily driven by higher billed business“ `[FACT]`, takže odměny rostou s útratou financovanou z merchant fees. Kontrast: OCBC Singapur 0,2 % na SGD útratě `[STALE]`. IFR výjimka pro commercial karty `[FACT]`. **Nepotvrzeno:** srovnání consumer vs. commercial interchange v USA (consumer credit v USA také není regulován stropem, proto velkorysost US odměn nelze přičíst jen výjimce pro commercial) `[DATA GAP: Visa USA IRF PDF – consumer tabulky, Fed Regulation II pro debit]`.
- **H5 – Existuje vrstva odměn financovaných obchodníky, kterou banka převezme bez rozpočtu: PODPOŘENO (s výhradou ekonomiky).** Visa SavingsEdge (USA a Kanada, 2024) `[FACT]`, Mastercard Easy Savings (globálně, včetně evropských mutací) `[STALE/CLAIM]`, Amex Offers (merchant-funded, uzavřené schéma) `[STALE]`, Brex/Ramp partner perks `[CLAIM]`. Výhrada: obchodní podmínky pro vydavatele (poplatky, opt-in, data) nejsou veřejné `[DATA GAP]` a v Evropě je SavingsEdge nedoložen.

---

## 6. DATA GAP

1. Počet členů, retence a vkladový efekt **BofA Preferred Rewards for Business**: BofA quarterly earnings presentation, segment Consumer Banking / Global Banking, 10-K.
2. Aktuální datace benefitů BofA PRB for Business (25/50/75 %, 0,25 p.b. apod.): business.bankofamerica.com (bez data ve výtahu), T&C PDF programu.
3. **Ramp** – výše cashbacku: support.ramp.com, Ramp card T&C.
4. **Chase Offers** na business kartách: chase.com/offers, Ink T&C.
5. **Amex Canada Business, UOB, Indie (HDFC/Amex India), Brazílie**: neověřeno kvůli rozpočtu vyhledávání.
6. Visa SavingsEdge – stav po 06/2024, dostupnost mimo USA a Kanadu, financování: Visa Business Solutions, vydavatelé.
7. Mastercard Easy Savings – dostupnost v ČR a model pro vydavatele: Mastercard CEE.
8. **Consumer vs. commercial interchange v USA** (pro H4): Visa USA Interchange Reimbursement Fees PDF (consumer tabulky), Mastercard U.S. interchange, Fed Regulation II.
9. Výše stropů IFR a aplikace výjimky pro commercial karty v ČR: EUR-Lex čl. 3–4, ČNB. Čísla záměrně neuvádím z paměti.
10. Rebate tabulky státních kontraktů: aktuální verze a směr tierů (NY OGS PDF), přímé čtení PDF.
11. NAPCP benchmark rebate (bps podle objemu): NAPCP členská data nebyla ve výtazích, nahrazeno státními kontrakty a GSA.
12. Kvantifikovaný dopad ECR a relationship pricingu na retenci (nezávislá studie s metodikou): AFP Treasury Management Fee Survey, Curinos.
13. Obsah programu BofA Employee Banking & Investing (02/2024): ověřen jen titulek.
14. Commercial karty v ČR (objem, rebaty, vydavatelé): ČNB statistiky platebních karet, Visa/MC CZ.

---

## 7. Log zdrojů (datum přístupu u všech 2026-10-06)

| # | URL | Datum zdroje | Co z něj |
|---|---|---|---|
| 1 | https://business.bankofamerica.com/preferred-rewards-business.html | neznámé | Benefity PRB for Business (25/50/75 %, poplatky, 0,25 p.b., 5% booster, 0,05 %) |
| 2 | https://bankofamerica.com/preferred-rewards/business-advantage/faq | 2026 (zmiňuje 27. 5. 2026) | Tiery 20/50/100 tis. USD, zachování business programu |
| 3 | https://www-pt1-helix.ecnp.bankofamerica.com/preferred-rewards/business-advantage/faq | neznámé | 3měsíční průměr, automatický upgrade, benefity na 1 rok (testovací doména BofA, jen stopa) |
| 4 | https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/02/new-bofa-rewards--program-to-reach-millions-more-clients-with-ex.html | 2026-02-18 | BofA Rewards nahrazuje retailový PR, business zůstává |
| 5 | https://newsroom.bankofamerica.com/content/newsroom/press-releases/2026/07/3-million--clients-enroll-in-new-bofa-rewards--program-in-first-.html | 2026-07 | 3 mil.+ zapsaných za 7 týdnů (retail) |
| 6 | https://newsroom.bankofamerica.com/content/newsroom/press-releases/2024/02/bofa-program-delivers-banking---investing-benefits-and-rewards-t.html | 2024-02 | Titulek: benefity pro 4 mil. zaměstnanců korporátních klientů |
| 7 | https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20711.html | 2024-06-12/13 | Relaunch Visa SavingsEdge |
| 8 | https://www.mastercard.com/us/en/business/industry-segment/small-medium-business/easy-savings.html | neznámé | Easy Savings popis, 50 000+ lokací, až 20 % |
| 9 | https://www.novo.co/help/how-does-mastercard-easy-savings-work | 2026-06 (dle výtahu) | Easy Savings aktivní u Novo |
| 10 | https://www.mastercard.com/news/eemea/uk-ua/... (Easy Savings Ukrajina) | 2024 | Evropská dostupnost |
| 11 | https://creditcards.chase.com/business-credit-cards/ink/cash | neznámé (URL kampaně 0626) | Ink Business Cash 5/2/1 % a stropy |
| 12 | https://creditcards.chase.com/business-credit-cards/ink/unlimited, .../premier | neznámé (srovnání 0926) | 1,5 % / 2,5 % a 2 % |
| 13 | https://onemileatatime.com/reviews/credit-cards/chase/chase-ink-business-preferred/ (a travelupdate.com) | neznámé | Ink Preferred 3x/150 000, 95 USD, AKV (CLAIM) |
| 14 | https://awardwallet.com/blog/amex-blue-business-plus ; https://www.doctorofcredit.com/american-express-launches-new-blue-business-plus-card-2x-purchases-50000-per-year-no-annual-fee | neznámé | BBP 2x do 50 000 USD |
| 15 | https://www.americanexpress.com/en-us/benefits/offers/ | neznámé | Amex Offers mechanika |
| 16 | https://global.americanexpress.com/card-benefits/detail/240-flexible-business-credit/business-gold | 2026 | 20 USD/měsíc, do 1. 10. 2026 |
| 17 | https://www.capitalone.com/small-business/credit-cards/spark-cash-plus/ | neznámé | 2 %, 150 USD, vrácení při ≥ 150 000 USD |
| 18 | https://www.wellsfargo.com/biz/business-credit/credit-cards/signify-business-cash-credit-card-terms-conditions/ | neznámé | 2 % cash rewards, vyloučení |
| 19 | https://www.usbank.com/business-banking/business-credit-cards/business-triple-cash-back-credit-card.html | neznámé | 3 %/1 %, 100 USD software, AKV 750 USD |
| 20 | https://www.brex.com/spend-trends/corporate-credit-cards/corporate-credit-card-rewards | 2026-08 | Body 7x/4x/3x/2x/1x, redeem na účet |
| 21 | https://ramp.com/corporate-cards ; https://support.ramp.com/how-to-use-cashback-rewards | neznámé / 2026 (blog) | Ramp bez poplatku, cashback na Ramp Checking (sazba GAP) |
| 22 | https://www.rbcroyalbank.com/business/credit-cards/small-business-credit-cards/rbc-avion-visa-business.html | neznámé | Avion 1 / 1,25 bodu, pooling |
| 23 | https://www.td.com/ca/en/business-banking/small-business/credit-cards/business-travel-visa-card | neznámé | 9/6/2 body |
| 24 | https://www.qantas.com/au/en/business-rewards/faqs/about.html | neznámé | 89,50 AUD, Level 1–3: 20/30/40 |
| 25 | https://commbank.com.au/business/business-credit-cards/business-awards-credit-cards/business-awards-credit-card.html ; CommBank Awards T&C | neznámé / 2026-09-28 | 1 bod / 0,4 Qantas, 30 AUD |
| 26 | https://www.commbank.com.au/business/cards/qantas-business-rewards-credit-card-terms-conditions.pdf | neznámé | 0,60 / 1,25 bodu, strop 100 000 AUD |
| 27 | https://www.nab.com.au/business/business-credit-cards/nab-qantas-business-signature-card | neznámé | 1 bod / 1,50 AUD, retence 15 měsíců |
| 28 | https://www.westpac.com.au/business-banking/credit-cards/rewards-cards/ | neznámé | až 2 body/AUD |
| 29 | https://www.anz.com.au/business/credit-cards/ | neznámé | 1,5 / 1 bod |
| 30 | https://www.singaporeair.com/en_UK/sg/corporate/highflyer/highflyer-programme/ ; press release 2017 | neznámé / 2017-07-04 | HighFlyer 5–6 bodů/SGD |
| 31 | https://www.emirates.com/english/business-rewards/ ; media centre MSME | neznámé | 1 bod/USD, 30 000+ MSME |
| 32 | https://www.dbs.com.sg/sme/day-to-day/business-cards/dbs-visa-business-advance-plus-debit-card | neznámé | 1 % při ≥ 2 000 SGD |
| 33 | https://www.ocbc.com/business-banking/smes/transactions/business-debit-card ; .../business-credit-card | neznámé | 1 % / 0,2 %, 3 % eco |
| 34 | https://www.financialprofessionals.org/training-resources/resources/articles/Details/what-is-the-earnings-credit ; AFP glossary | neznámé | Definice ECR a account analysis |
| 35 | https://www.curinos.com/insights/according-to-the-data-earnings-credit-rates-moving-up (+ curinos.com „excess ECR“) | 2023-09 / 2024-01 | ECR 79 bps, 76 bps, excess ECR 21 % |
| 36 | https://smartpay.gsa.gov/about/statistics/ ; https://www.gsa.gov/about-gsa/newsroom/news-releases/gsa-seeks-innovative-solutions-for-gsa-smartpay-04032026 | FY2025 / 2026-04-03 | 39,4 mld. USD útrata, 471 mil. USD refundy, 7,2 mld. USD kumulativně |
| 37 | https://www.jpmorgan.com/payments/solutions/commercial-cards/ts-purchasing-card ; .../ts-one-card ; Ashton Woods case | neznámé | Rebate mechanika, case +98 %/+303 % |
| 38 | https://www.citibank.com/tts/solutions/commercial-cards/products/ (+ case studies 2013) | neznámé / 2013 | VCA/ePayables rebate |
| 39 | https://online.ogs.ny.gov/purchase/snt/awardnotes/7900823217Pricing.pdf | neznámé | JPM–NYS 180,5–43 bps |
| 40 | https://www.doa.nc.gov/pc-stc-946a-rebateincentiveprogram-schedulepdf/open | neznámé | BofA–NC 1,99–2,18 % |
| 41 | https://apps.des.wa.gov/contracting/00719%20US%20Bank%20Amd%202.pdf | neznámé | U.S. Bank NASPO 34,75 bps |
| 42 | https://2017-2021.commerce.gov/sites/default/files/ofm/Purchase_Card_Develop_Process_to_Pay_Weekly-Daily.pdf | 2017–2021 | 109–120 / 75–89 / 157–168 bps |
| 43 | https://www.corpay.com/resources/blog/virtual-card-rebates | neznámé | 1,0–1,5 % (CLAIM agregátor) |
| 44 | https://usa.visa.com/content/dam/VCOM/download/merchants/visa-usa-interchange-reimbursement-fees.pdf | 2026-04-18 (účinnost) | Commercial interchange sazby |
| 45 | https://eur-lex.europa.eu/eli/reg/2015/751/oj/eng | 2015 | Definice commercial karty, výjimka z kap. II |
| 46 | https://www.sec.gov/Archives/edgar/data/4962/000000496226000080/axp-20251231.htm | FY2025 (10-K 2026) | Rewards expense +1 234 / +576 mil. USD, URR 96 % |
| 47 | https://www.mckinsey.com/industries/financial-services/our-insights/charting-a-path-to-increasing-transaction-banking-value-by-50-percent ; .../winning-in-corporate-deposits-through-transaction-banking ; .../firing-on-all-cylinders-in-north-american-commercial-banking | neznámé / 2020 | Relationship pricing, 5 % klientů, ROE +20 p.b. |
| 48 | https://www.oliverwyman.com/our-expertise/insights/2023/feb/corporate-and-transaction-banking-2023.html | 2023-02 | Relationship a subscription pricing |
| 49 | https://www.bcg.com/publications/2018/redefining-corporate-banking-relationships-digital-world | 2018 | Digitalizace RM, riziko bundlingu |

**Počet vyhledávání:** 38 z 38 (WebSearch). WebFetch: 0 pokusů. Kvůli rozpočtu nebyly provedeny dotazy na Amex Canada, UOB, Indii, Brazílii, NAPCP primární data, Chase Offers business a sazbu Ramp (viz DATA GAP).
