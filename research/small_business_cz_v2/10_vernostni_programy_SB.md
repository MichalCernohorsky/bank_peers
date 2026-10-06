# Věrnostní programy pro podnikatele a firmy – ČR, Evropa, svět
## Existují věrnostní programy i pro firemní svět, a co z toho plyne pro Českou spořitelnu?
Praha, 6. října 2026 · navazuje na `FINAL_small_business_CZ_deep_dive_v2.md` (2. 10. 2026) a deck A01–B78 · podklady: `10_vernostni_programy_db.csv` (125 záznamů), `10_vernostni_programy_cases.md` (7 případových studií), pracovní soubory `loyalty_data/`

> **Pravidla ověření.** Každé číslo a tvrzení nese značku:
> - `[FACT]`: ověřeno ve zdroji s URL a datem. Plný text externích stránek nebyl v prostředí dostupný (síťová politika blokuje přímé načtení stránek), proto FACT znamená ověřeno ve výtahu výsledku vyhledávání s URL.
> - `[EST]`: odhad nebo výpočet se vzorcem.
> - `[STALE: MM/RRRR]`: zdroj k nabídce starší než 06/2026, nebo bez data. Nevydává se za současný stav.
> - `[CLAIM]`: tvrzení firmy, PR nebo marketing.
> - `[DATA GAP]`: nenalezeno, u položky je uvedeno, kde hledat.
>
> Žádné číslo nepochází z paměti modelu. Rešerše: 151 vyhledávání ve 4 workstreamech, 0 načtení stránek. Měny jsou v originále, na Kč se nepřepočítává, protože kurz ČNB k datu nebyl ověřen. Sizing segmentu, ceny účtů a benchmark bank se přebírají z v2 a nepřepočítávají se.

---

# 1. Odpověď na jednu stránku

**Ano, věrnostní programy existují i pro firmy, ale jen dole na velikostní škále. Se stoupající velikostí firmy se mění v něco jiného.**

| Segment | Existují? | Jakou mají podobu | Doklad |
|---|---|---|---|
| **FOP / mikro** | **Ano** | Retailové mechaniky na podnikatelské kartě nebo účtu: cashback 0,1–1,5 % v EU a 1,5–2 % flat v USA, body, nabídky obchodníků v aplikaci. U neobank cashback roste s placeným tarifem. | 26 programů v Evropě a 27 ve světě, otevřených podnikatelům (DB). Např. N26 Business 0,1 % / 0,5 % `[STALE: datum neznámé]`, bunq 0,5–1 % podle tarifu `[STALE]`, Chase Ink Business Unlimited 1,5 % `[FACT]`. |
| **SME** | **Částečně** | Cashback a body zůstávají, ale podmiňuje je **vztah** (zůstatek, úvěr, stáří firmy) nebo je násobí **tier podle zůstatků**. | Allica (UK): 1 % / 1,5 % jen pro firmy 12+ měsíců se zůstatkem 50 000 GBP+ nebo úvěrem `[FACT, STALE: datum neznámé]`. BofA Preferred Rewards for Business: tiery 20 / 50 / 100 tis. USD `[FACT 2026]`. VÚB: Money back jen ke kreditní kartě s úvěrovým limitem od 1. 7. 2026 `[FACT]`. |
| **Mid / large corporate** | **Ne v klasickém smyslu** | Body nahrazují smluvní **rebaty z firemních karet** v bps (podle objemu a rychlosti úhrady), **earnings credit** na zůstatky, **relationship pricing** a RM. | GSA SmartPay FY2025: 471 mil. USD refundů z útraty 39,4 mld. USD `[FACT]` = 1,20 % `[EST]`. Bodový program pro velké korporace se v rešerši nenašel. |

**Pět hlavních zjištění**
1. **Česká banka s uceleným programem pro podnikatele neexistuje a trh se v roce 2026 spíš stahuje.**
   - Plošný 1 % cashback na podnikatelské kartě nabízí KB (Kreditní karta Business, garance do 31. 12. 2026) `[FACT]` a MONETA (Business Card, bez stropu) `[FACT/STALE: datum neznámé]`. mBank ho dává jen na pozvání `[STALE: 03/2026]`.
   - **Air Bank cashback 1 % pro podnikatele ukončila k 30. 6. 2026** `[FACT]`.
   - ČS má pro podnikatele jen slevy financované Visou pro držitele Visa Business `[FACT/STALE: datum neznámé]`.
2. **Retailové programy podnikatelské karty často vylučují, a tlačí tak podnikatele k osobní kartě.**
   - SLSP (Erste) Moneyback vylučuje debetní karty k podnikatelským účtům `[FACT 07/2025]`.
   - ČS Moneyback podle článku vyžaduje soukromou kartu ČS `[CLAIM]`. Podmínky ČS Odměn podnikatelskou kartu nezmiňují `[DATA GAP]`.
   - Výjimkou je MONETA Program Odměny, výslovně otevřený FOP včetně karet Business (PO ne) `[FACT/STALE: 06/2025]`.
3. **Ekonomika na straně banky je silná, protože podnikatelská karta nemá regulovanou interchange.**
   - IFR 2015/751 vyjímá commercial karty ze stropů 0,2 % / 0,3 % (čl. 1 odst. 3 písm. a)). Definice zahrnuje i OSVČ s kartou účtovanou na podnikatelský účet `[FACT]`.
   - Mastercard Corporate v ČR: 2,10 % `[STALE: 03/2022]`, tedy cca **10,5× víc** než strop spotřebitelské debetní karty `[EST = 2,10 / 0,20]`.
   - Riziko: obchodníci v 05/2026 žádají zastropování commercial karet `[CLAIM]`.
4. **Vrstva financovaná obchodníky je hotová a v CEE už běží.**
   - Mastercard Business Savings / Business Bonus mají NatWest (cca 1 mil. držitelů debetních karet, k 05/2024) `[FACT, STALE]`, bunq v 5 zemích (01/2025) `[FACT]`, OTP HU a Intesa RS `[STALE]`.
   - Dostupnost v ČR a emitenti bodové verze Business Bonus Ultimate jsou `[DATA GAP]`.
5. **Kauzální důkaz, že program zvyšuje retenci SME, chybí.**
   - J.D. Power (N = 3 728) řadí „rewards earning" na 6. místo ze 7 dimenzí podle váhy `[FACT 12/2025]`.
   - McKinsey mezi důvody změny banky uvádí digitál, servis a úvěr, odměny ne `[FACT, STALE: datum neznámé]`.
   - BofA Preferred Rewards (všechny segmenty) hlásí 99% retenci u 11,4 mil. členů `[CLAIM, metodika neuvedena]`.
   - **Odměna je pro SME hygienický a diferenciační faktor karty, ne hlavní důvod volby banky** `[EST – interpretace]`.

**Co z toho plyne pro ČS:** vzorem není „retailový Moneyback pro firmy“, ale **vztahový tier** (BofA, Allica), který podle zůstatku a úvěru odpouští poplatky, zlevňuje úvěr a násobí cashback na podnikatelské kartě. K tomu schémová vrstva nabídek bez vlastního rozpočtu. Detail v kap. 9.

---

# 2. Definice a taxonomie: osm mechanik A–H pokrývá praxi beze zbytku

**Věrnostní program** = opakovaná mechanika, která odměňuje klienta za setrvání, aktivitu nebo rozsah vztahu. Jednorázové akviziční bonusy jsou v DB evidované zvlášť jako `AKV` (13 záznamů, v souhrnech se nepočítají).

| Kód | Mechanika | Záznamů v DB (hlavní mechanika, bez AKV a DATA GAP) | Typický příklad |
|---|---|---|---|
| A | Karetní odměny (body, míle, cashback) | 42 | Chase Ink, KB 1 %, VÚB Money back |
| B | Cashback nebo úrok na účtu za aktivitu | 4 | Allica Business Rewards, DBS Advance+ |
| C | Vztahový / tierový program | 6 | BofA Preferred Rewards for Business, ECR |
| D | Odměny financované obchodníky | 24 | Mastercard Business Savings, Visa SavingsEdge, MONETA Odměny |
| E | Cena 0 výměnou za aktivitu | 1 | (Fio – model nulových poplatků bez odměn) |
| F | Nefinanční benefity a služby | 7 | ČS Visa Business benefity, Amex Business Gold kredit 240 USD |
| G | Rebaty u korporátních karet | 9 | GSA SmartPay, P-card kontrakty JPM, BofA, U.S. Bank |
| H | Nebankovní B2B programy | 14 | PartnerPlusBenefit, MAKRO Gold, Qantas Business Rewards, SAS |

**Ověření taxonomie (L1):** Přehledové zdroje (Mastercard Europe 10/2024, Visa SavingsEdge, BofA, McKinsey, Alvarez & Marsal, Amex) nenesou žádnou mechaniku, která by do A–H nepatřila. Pro rozhodování ČS doporučujeme taxonomii **upřesnit**, ne měnit:
- **Atribut „booster C → A/B“:** tier sám nic nevyplácí, jen násobí kartové odměny a úrok (BofA +25 / 50 / 75 %). Kódováním „C + A“ by se ztratilo, že C je páka na vklady.
- **Atribut „provozovatel ≠ vydavatel“:** Mastercard Business Bonus a Visa SavingsEdge provozuje schéma. Rozhoduje to o rozpočtu i o tom, komu patří vztah s klientem.
- **Podtypy G:** G1 objem, G2 rychlost úhrady (Texas/Citi: +0,75 bp za každý den dřívější úhrady `[FACT, STALE: 07/2024]`), G3 large ticket.
- **F rozdělit:** F1 služby a software (účetnictví, expense management), F2 přístup a status (RM, lounge).
- **Kategorie I (odměny v acquiringu) jen podmíněně.** Podnikatel je u banky často zároveň obchodníkem, doložený příklad se ale nenašel `[DATA GAP: ceníky acquiringu ČS, KB, ČSOB, GP, SumUp]`.

---

# 3. Hypotézy H1–H7: pět platí částečně nebo převážně, dvě plně

| # | Hypotéza | Verdikt | Klíčový důkaz |
|---|---|---|---|
| **H1** | U FOP a mikro fungují programy jako v retailu, protože rozhoduje majitel jako spotřebitel | **Částečně potvrzeno** (forma ano, účinnost nedoložena) | Mechaniky jsou retailové: cashback na kartě (N26, bunq, Finom, Wise, KB, MONETA), body (Amex Business Gold UK/DE/FR) a nabídky obchodníků (Tide Rewards, Revolut Business Rewards, MONETA Odměny pro FOP) `[FACT/STALE]`. Amex DE umožňuje čerpat body soukromě `[CLAIM]`, což ukazuje, že rozhoduje majitel. Rozdíl proti retailu: u neobank cashback roste s placeným tarifem (bunq 0,5 % vs. 1 %, N26 0,1 % vs. 0,5 %, Finom 1 % vs. 3 % se stropem 10–90 EUR/měs.) `[STALE/CLAIM]`, takže ho financuje poplatek. Že programy „fungují“, nikdo nedokládá `[DATA GAP]`. Air Bank svůj ukončila `[FACT]`. |
| **H2** | S velikostí mizí body a cashback a nahrazuje je vztahový pricing, rebaty a balíčky | **Potvrzeno** | SME: cashback podmíněný vztahem (Allica: 12+ měsíců a 50 000 GBP+ nebo úvěr; VÚB: kreditní karta s úvěrovým limitem) `[FACT]` a tier podle zůstatku (BofA 20 / 50 / 100 tis. USD) `[FACT]`. Corporate: rebaty v bps (GSA 1,20 % `[EST]`; JPM–NYS 180,5–43 bps; BofA–NC 1,99–2,18 % `[STALE]`), ECR, relationship pricing `[FACT/CLAIM]`. Výhrada: fintechové corporate karty (Brex, Ramp) drží body i pro rostoucí firmy `[FACT/CLAIM]`. |
| **H3** | U velkých korporací klasický věrnostní program téměř není | **Potvrzeno** | Žádný bodový program pro large corporate nenalezen. Loajalitu nese rebate (smluvní revenue share), ECR (zůstatky kompenzují poplatky, AFP `[FACT]`), relationship pricing a RM (McKinsey: cca 5 % strategických klientů tvoří polovinu výnosů banky `[CLAIM]`). Emirates Business Rewards výslovně cílí na firmy **bez** korporátní cestovní smlouvy `[STALE]`. |
| **H4** | Motorem odměn u firemních karet je vyšší interchange, IFR stropy se na commercial karty nevztahují, proto jsou odměny v USA velkorysejší | **Částečně potvrzeno** (první dvě části ano, vysvětlení rozdílu EU–USA upravit) | IFR čl. 1 odst. 3 písm. a) vyjímá commercial karty `[FACT]`. Commercial interchange v EU: 1,3–2,4 % `[CLAIM – EuroCommerce 05/2026]`; Mastercard ČR Corporate 2,10 % `[STALE: 03/2022]`. V USA: Visa commercial 1,75–2,95 % + 0,10 USD `[FACT, účinnost 18. 4. 2026]`. Úrovně jsou tedy podobné, takže **samotná výjimka rozdíl nevysvětluje**. Velkorysost v USA dělá hlavně neregulovaný kredit obecně: Reg II omezuje jen debetní karty vydavatelů s aktivy ≥ 10 mld. USD `[FACT]`. Kontrast: OCBC Singapur 0,2 % na SGD útratě `[STALE]`. |
| **H5** | Existuje vrstva odměn financovaná obchodníky, kterou banka převezme bez vlastního rozpočtu | **Částečně potvrzeno** | Existuje: Visa SavingsEdge (relaunch 06/2024, USA a Kanada) `[FACT]`, Mastercard Easy Savings `[CLAIM/STALE]`, Mastercard Business Savings/Bonus (NatWest, Mettle, bunq, OTP, Intesa) `[FACT/STALE]`, Revolut Business Rewards („third-party merchant partners“ `[FACT T&C]`), Amex Offers, Cardlytics. „Bez rozpočtu“ ale platí jen pro nabídky obchodníků. Body v Business Bonus Ultimate nese emitent `[CLAIM]`. Evropská obdoba SavingsEdge od Visy nenalezena `[DATA GAP]`. U SavingsEdge vlastní vztah schéma, ne banka. |
| **H6** | Podnikatelé používají osobní produkty, mj. kvůli odměnám, takže retailový program ovlivňuje i SB | **Částečně potvrzeno** | Mastercard: 80 % z > 10 000 SME používá osobní bankovní produkty, téměř třetina kvůli odměnám `[CLAIM, STALE: 10/2024, metodika nezveřejněna]`. USA: 26 % malých zaměstnavatelských firem vede business výdaje přes osobní kartu `[CLAIM – sekundární citace Fed SBCS 2026; EST kontrola 62 % × (34 % + 8 %)]`. ČR: přísně odděluje finance jen zhruba čtvrtina podnikatelů `[CLAIM, datum neznámé]`. Mechanismus je doložen: retailové programy podnikatelské karty vylučují (SLSP `[FACT]`, ČS Moneyback `[CLAIM]`, Sparkasse + Payback, DNB, Danske `[STALE]`). |
| **H7** | V ČR žádná banka nemá ucelený program pro podnikatele, jen cashback | **Převážně potvrzeno** | U žádné z 12 bank tierový ani vztahový program pro podnikatele. Dominuje 1 % cashback na kartě (KB, MONETA, mBank na pozvání; Air Bank do 30. 6. 2026) `[FACT/STALE]`. Výhrady: MONETA otevírá FOP i card-linked Program Odměny (D) `[FACT/STALE: 06/2025]`. ČS a ČSOB dávají nefinanční benefity (Visa Business slevy, pojištění) `[FACT/STALE]`. |

---

# 4. ČR: z 12 bank nabízí podnikatelům trvalou odměnu jen pět, žádná nemá tier

**Inventura (detail: DB CZ-01 až CZ-37)**

| Banka | Program pro podnikatele | Retailový program otevřený podnikatelům? | Hodnocení |
|---|---|---|---|
| **Česká spořitelna** | Jen „Benefity pro firmy“: slevy pro Visa Business (Bolt Business 70 % na prvních 20 jízd, EasyPark Business 2 měsíce zdarma, foodora 60 %, wflow 25 % na 6 měsíců) `[FACT/STALE: datum neznámé]`. Business kreditní karty bez odměn. | Odměny / Moneyback: podmínky „klient ČS, George, 18+“, podnikatelská karta nezmíněna `[DATA GAP]`. Článek uvádí soukromou kartu `[CLAIM]`. | **Nemá vlastní program**. Retailový program pravděpodobně táhne FOP k osobní kartě. |
| KB | Kreditní karta Business: 1 % zpět, garance do 31. 12. 2026 `[FACT]`. Strop „29 000 Kč měsíčně“ je nejasný `[DATA GAP]`. | „Klub věrnosti“ jen v článku `[CLAIM/DATA GAP]` | Cashback na kreditní kartě |
| ČSOB | Pojištění k podnikatelským kartám `[STALE: 11/2025]` | Svět odměn ukončen 31. 12. 2024. Platnost Kate Coins pro podnikatele `[DATA GAP]`. | Nemá |
| Raiffeisenbank | Nenalezeno | Program výhod KK (od 1. 5. 2026) jen pro retailové karty `[STALE: 05/2026]` | Nemá |
| **MONETA** | Business Card: 1 % zpět bez stropu `[FACT/STALE]`. Kampaně 5 % PHM / hobby markety (AKV). | **Program Odměny otevřený FOP vč. karet Business CZK / Premium, PO ne** (podmínky od 22. 6. 2025) `[FACT/STALE: 06/2025]` | Nejširší nabídka, bez tierů |
| UniCredit | „Benefitní program k platebním kartám“ `[CLAIM]` | U-šetřete: zapojení podnikatelských karet `[DATA GAP]` | Nejasné |
| **Air Bank** | **1 % zpět z podnikatelské karty ukončeno k 30. 6. 2026** `[FACT]` | „Odměny za placení“ `[DATA GAP]` | Program zrušen |
| Fio | Nenalezeno (model nulových poplatků) | Nenalezeno | Nemá |
| Creditas | Nenalezeno (jen úrok) | Nenalezeno | Nemá |
| mBank | 1 % zpět, 2. 3.–31. 12. 2026, jen na telefonickou pozvánku `[STALE: 03/2026]` | – | Cílená retence |
| Revolut Business | V ČR jen akviziční odměny (Revolut Pro). Trvalý cashback ověřen jen v USA `[FACT]`. | – | Nemá (v ČR) |
| Wise Business | Cashback 0,5 % jen pro firmy z UK `[FACT/STALE]` | – | Nemá (v ČR) |
| Partners, Trinity, Oberbank | – | – | `[DATA GAP]` |

**Nebankovní B2B programy dostupné v ČR (≥ 5, splněno 8):**
- PartnerPlusBenefit (Lufthansa Group, existuje česká verze webu) `[FACT/STALE]`
- BlueBiz (AF-KLM) `[CLAIM]`
- Qatar Beyond Business (5 tierů) `[STALE: 10/2021]`
- **MAKRO Blue / Silver / Gold: Gold od měsíčního obratu nad 33 333 Kč, jen s IČO, nefinanční výhody** `[FACT/STALE]`
- Palivové karty: CCS (sleva 0,40–1,50 Kč/l `[CLAIM]`), Shell Card + ClubSmart, Benzina Tankarta `[STALE: 03/2021]`
- T-Mobile svůj bodový B2B program ukončil koncem roku 2013 `[STALE: 12/2013]`

Amex podle článku vydávání komerčních produktů v ČR ukončil `[STALE: datum neznámé]`.

**Hodnocení:** Český trh zná jen dva vzorce:
- **(a) 1 % na podnikatelské kartě** (KB, MONETA, mBank). Nástroj bez vztahové podmínky. Air Bank ho zrušila, mBank ho dává jen vybraným.
- **(b) slevy financované schématem** (ČS Visa Business benefity, MONETA Odměny).

Tierovou logiku podle obratu mají v ČR jen nebankovní hráči (MAKRO, Qatar). **Prostor pro vztahový program podnikatelů je volný.**

**Aktualizace dat z v2:**
- „Air Bank 0 Kč + 1 % cashback“ (v2 `[STALE 03/2026]`) už neplatí `[FACT]`. Deck v2 (slidy B27 a B37) a kap. 4 dokumentu v2 to potřebují upravit.
- v2 uvádí u SLSP „1 % cashback“ (kap. 6.2 a BP4). Tato rešerše ho pro podnikatele **nepotvrdila** a Moneyback SLSP podnikatelské debetní karty vylučuje `[FACT 07/2025]`. Doporučujeme ověřit ve skupině Erste.

---

# 5. Evropa: 26 programů pro podnikatele z 8 zemí (rešerše 12 zemí), téměř všechny pro FOP a malé SME

**Inventura (DB EU-01 až EU-47; 26 programů otevřených podnikatelům, 8 AKV, 5 retailových kvůli H6, 4 DATA GAP)**
- **UK (nejbohatší trh):**
  - Allica Business Rewards (B+C)
  - Tide Rewards (D, 100+ značek, od 7. 8. 2025 `[FACT]`)
  - Capital on Tap (1 %)
  - Amex Business Gold a Platinum
  - Barclaycard Premium Plus
  - NatWest Business Plus (0,5–3 % podle kategorie, strop 600 GBP/rok `[STALE]`)
  - Mastercard Business Savings (NatWest/RBS/Ulster)
  - Mettle + Mastercard Business Bonus
  - Wise (0,5 %)
  - Starling a Monzo vlastní program nemají `[STALE]`
- **NL:** bunq cashback 0,5–1 % `[STALE]`, bunq + Mastercard Business Bonus (NL/DE/FR/ES/IT od 15. 1. 2025 `[FACT]`). Rabobank, ING a ABN AMRO nic `[DATA GAP]`.
- **DE:** Finom (1–3 %, strop 10–90 EUR/měs. `[CLAIM]`), Commerzbank Business Card Premium (0,55 % p.a. za 79,90 EUR/rok `[STALE]`), N26 Business (0,1 % / 0,5 %), Amex Gold DE. Sparkasse + Payback (od 07/2025) jen retail.
- **FR:** Amex Business Gold. Shine a BNP Hello Pro bez odměn.
- **ES, PL:** jen akviziční bonusy „v kabátu loyalty“:
  - BBVA až 1 200 EUR v 1. roce za domiciliaci, kartu a Bizum, do 31. 12. 2026 `[FACT]`
  - CaixaBank refund daní až 600 EUR, ukončeno 16. 6. 2026 `[FACT]`
  - PKO až 3 600 zł `[STALE/CLAIM]`
  - Santander PL 3 %, max. 150 zł/měs., do 30. 11. 2025 `[STALE]`
- **AT:** George Business bez bonusového programu `[DATA GAP: s Bonus pro Unternehmer]`. Raiffeisen Bonus Premium je retail.
- **SK:** **VÚB Money back pro Mastercard Business World od 1. 7. 2026** (FO podnikatelé i PO s úvěrovým limitem, měsíčně) `[FACT]`. Sazba `[DATA GAP]`. SLSP Moneyback podnikatelské debetní karty vylučuje `[FACT 07/2025]`.
- **Severské země:** SAS EuroBonus Executive Business Card (oznámena 27. 5. 2026, start na podzim 2026, emitent Nordiska; 25 bodů za 100 SEK/DKK/NOK, 20 000 level bodů ročně) `[FACT/CLAIM]`. Nordea Business Mastercard bez odměn `[STALE]`.
- **HU, RS:** OTP a Banca Intesa: Mastercard Business Bonus `[STALE]`.
- **Pan-EU:** Revolut Business Rewards (merchant-funded, nová verze T&C ~06/2026 `[EST z URL]`, obsah neověřen), Mastercard Business Bonus Ultimate (white-label body pro emitenty, 2024 `[CLAIM]`).

**Čtyři nejzajímavější případy** (detail v `10_vernostni_programy_cases.md`):
1. **Allica Bank – cashback jako odměna za vztah.**
   - 1 % / 1,5 % jen pro firmy 12+ měsíců se zůstatkem 50 000 GBP+ nebo úvěrem `[FACT, STALE: datum neznámé]`.
   - Aktivní klienti účtu vzrostli z 6 000+ na 14 000+ (FY25) `[CLAIM]`.
   - Práh pro 1,5 % je ve zdrojích 10 000 GBP (KPI), resp. 4 000 GBP (tisk FY25). Hodnota 15 000 GBP z výchozích stop se nepotvrdila.
2. **Mastercard Business Savings / Bonus – hotová vrstva D v Evropě.** NatWest: cca 1 mil. držitelů debetních karet, 1 000+ nabídek, automatický zápis `[FACT, STALE: 05/2024]`. bunq v 5 zemích `[FACT]`. OTP HU a Intesa RS `[STALE]`.
3. **VÚB vs. SLSP – přímý benchmark pro Erste.** VÚB přesouvá hodnotu od pojištění a lounge k cashbacku na firemní kreditce (1. 7. 2026) `[FACT]`, SLSP podnikatele z Moneyback vylučuje `[FACT]`.
4. **SAS – disintermediace.** Aerolinka si s emitentem jako službou staví vlastní firemní kartu a bere SME klienta bankám, které dříve vydávaly co-brand (SEB Kort, Amex Nordics, Lunar) `[FACT/CLAIM]`.

---

# 6. Svět: 27 programů mimo Evropu; v USA je 1,5–2 % cashback na business kartě standard

**Inventura (DB WD-01 až WD-29)**
- **USA – banky:**
  - Chase Ink Business Unlimited 1,5 % bez stropu `[FACT]`, Ink Business Cash 5 % do 25 000 USD/rok `[FACT]`, Ink Preferred 3x do 150 000 USD `[CLAIM]`
  - Capital One Spark Cash Plus 2 % `[STALE]`
  - Wells Fargo Signify Business Cash 2 % `[STALE]`
  - U.S. Bank Triple Cash 3 % / 1 % `[STALE]`
  - Amex Blue Business Plus 2x do 50 000 USD `[CLAIM]`, Amex Business Gold kredit až 240 USD/rok `[FACT 2026]`, Amex Offers (D)
- **USA – vztahový program:** **BofA Preferred Rewards for Business** (C).
  - Tiery podle 3měsíčního průměrného zůstatku: Gold 20 000, Platinum 50 000, Platinum Honors 100 000 USD `[FACT 2026]`.
  - Benefity: +25 / 50 / 75 % ke kartovým odměnám, odpuštění poplatků až na 4 + 4 účtech, sleva 0,25 p.b. z úvěrů, −0,05 % na merchant services `[STALE: datum neznámé]`.
  - Program pokračuje i po nahrazení retailového Preferred Rewards programem BofA Rewards (27. 5. 2026) `[FACT, 02/2026]`.
- **USA – fintechy:** Brex (body 7x / 4x / 3x / 2x / 1x, výplata na Brex účet `[FACT 08/2026]`), Ramp (cashback na Ramp účet, sazba `[DATA GAP]`). Odměna slouží jako háček pro celou platformu.
- **Schémata:** Visa SavingsEdge (relaunch 12.–13. 6. 2024, USA a Kanada, Visa Business kredit, debet i prepaid) `[FACT]`. Mastercard Easy Savings: aktivní (Novo 06/2026 `[FACT]`), evropské mutace (MT, UA), dostupnost v ČR `[DATA GAP]`.
- **Kanada:** RBC Avion Business (body lze slučovat s osobní kartou, tedy H6) `[STALE]`, TD Business Travel `[STALE]`.
- **Austrálie:** Qantas Business Rewards (firma dostane 20 / 30 / 40 bodů na každých 100 bodů cestujících, vstup 89,50 AUD) `[STALE]`. Na něj se napojují CommBank, NAB (+50 000 bodů při ponechání účtu 15 měsíců), Westpac a ANZ `[STALE]`.
- **Singapur a UAE:** SIA HighFlyer (5 bodů/SGD), Emirates Business Rewards (1 bod/USD, „30 000+ MSME“ `[CLAIM]`), DBS (1 % při útratě ≥ 2 000 SGD/měs.), OCBC (1 % / 0,2 %) `[STALE]`.

**Čtyři nejzajímavější případy:**
1. **BofA Preferred Rewards for Business – nejbližší vzor pro tier v BP5 a BB2.** Detail v cases.
2. **Visa SavingsEdge / Mastercard Easy Savings.** Vrstva D bez rozpočtu banky. U SavingsEdge ale vztah drží schéma.
3. **Qantas Business Rewards a bankovní co-brand.** Dvojí sběr: firma i cestující. Banky se na B2B program napojují, místo aby stavěly vlastní.
4. **Brex / Ramp.** Odměna se vyplácí jen na vlastní účet, takže z karty se stává akviziční kanál pro primární účet.

---

# 7. Ekonomika: podnikatelská karta nese 4–12× vyšší interchange než spotřebitelská `[EST]`, a z toho se odměny platí

**Kdo programy financuje**

| Zdroj | Doklad | Kdo to využívá |
|---|---|---|
| **Interchange** | EU commercial 1,3–2,4 % `[CLAIM – EuroCommerce 05/2026]`. Mastercard intra-EEA Corporate 1,90 %, BusinessCard 1,65 % `[STALE: 01/2021]`. ČR Corporate 2,10 % / bezkontaktně 1,70 % `[STALE: 03/2022]`. Sazebník ČR k 1. 1. 2026 existuje, hodnoty `[DATA GAP]`. USA Visa commercial 1,75–2,95 % + 0,10 USD `[FACT 04/2026]`. | Kartové odměny A, rebaty G |
| **Obchodníci** | SavingsEdge, Mastercard Business Savings/Bonus, Amex Offers, Cardlytics (cca 400 bank `[STALE]`, od 05/2025 i mimo banky `[CLAIM]`) | Nabídky D |
| **Marže z vkladů a úvěrů** | BofA: vstup od 20 000 USD průměrného zůstatku. Allica: 50 000 GBP+ nebo úvěr. ECR (USA): průměr 76–79 bps vs. 300+ bps u úročených účtů `[STALE: 01/2024; CLAIM Curinos]` | Tier C, cashback B podmíněný vztahem |
| **Poplatek za tarif** | bunq, N26 a Finom zvyšují cashback s placeným tarifem `[STALE/CLAIM]`. Commerzbank 79,90 EUR/rok `[STALE]`. | Neobanky, placené tiery |

**IFR a interchange (H4):**
- Stropy 0,2 % (debet) a 0,3 % (kredit) neplatí pro commercial karty `[FACT]`.
- **Commercial card** = karta vydaná podniku, veřejnému subjektu nebo **OSVČ**, určená pro podnikatelské výdaje a účtovaná přímo na jejich účet `[FACT]`.
- **Důsledek pro ČS:** výjimka se zřejmě týká i debetní karty OSVČ k podnikatelskému účtu, ne ale osobní karty OSVČ `[interpretace textu IFR, ne FACT]`. Jak české banky karty klasifikují, je `[DATA GAP]`.

**Ekonomika na kartě (`[EST]`, ilustrace na 10 000 Kč útraty):**
- Spotřebitelská debetní karta: 10 000 × 0,20 % = **20 Kč** interchange.
- Podnikatelská karta Corporate v ČR: 10 000 × 2,10 % = **210 Kč** `[vstup STALE: 03/2022]`.
- Cashback 1 % (KB, MONETA): **100 Kč**. Banka si tedy i po cashbacku ponechá zhruba 110 Kč, tj. 5,5× víc než u osobní karty. Odečíst je třeba schémové poplatky a náklady (`[DATA GAP]`).

Z toho plyne: **převést výdaje FOP z osobní na podnikatelskou kartu má hodnotu sama o sobě**. Program, který FOP vylučuje (Moneyback), působí proti tomu.

**Regulační riziko:** EuroCommerce a obchodníci (22. 5. 2026) žádají vypuštění výjimky pro commercial karty a „přeplatek“ za 2025 vyčíslují na ≥ 4 mld. EUR `[CLAIM]`. Legislativní návrh Komise nenalezen `[DATA GAP]`. **Program postavený jen na commercial interchange je proto nejcitlivější variantou.**

**Doložené dopady (L5)**

| Zdroj | Zjištění | Síla důkazu |
|---|---|---|
| J.D. Power 2025 U.S. Small Business Credit Card Study | Index 716 (+8). „Rewards earning“ je 6. ze 7 dimenzí podle váhy. N = 3 728. | `[FACT 12/2025]` – korelační |
| McKinsey (SME banking) | 13 % SME změnilo primární banku za 24 měsíců (2023). Důvody: digitál, servis, úvěr. RM jako kritérium uvádí 47 %. | `[FACT, STALE: datum neznámé]` |
| BofA ARS FY2025 | Preferred Rewards (všechny segmenty) 11,4 mil. členů, 99% retence, ~500 USD odměn na klienta ročně | `[CLAIM, bez kontrolní skupiny]` |
| Allica FY25 | Klienti Rewards účtu 6 000+ → 14 000+, vklady banky +29 % na 5,7 mld. GBP | `[CLAIM]`, kauzalita neprokázána |
| Amex Q2 2025 | SME = 82 % objemů Commercial Services | `[FACT, STALE: 07/2025]` |
| Mastercard (> 10 000 SME) | 80 % používá osobní produkty, ~1/3 kvůli odměnám | `[CLAIM, STALE: 10/2024]` |

**Závěr:** Retenci, share of wallet ani ARPU nedokládá žádná studie s kontrolní skupinou `[DATA GAP]`. Statistiky agregátorů typu „X % firem s loyalty má o Y % vyšší retenci“ byly vyřazeny.

---

# 8. Corporate: loajalitu kupuje rebate v bps, earnings credit a relationship pricing, ne body

- **Rebaty z commercial, purchasing a travel karet (G):**
  - Smluvní roční revenue share podle objemu a rychlosti úhrady.
  - GSA SmartPay FY2025: útrata 39,4 mld. USD, refundy 471 mil. USD (82 mil. transakcí, 4,2 mil. účtů) `[FACT]` = **1,20 %** `[EST = 471 / 39 400]`.
  - Státní kontrakty: JPM–NYS 180,5–43 bps podle tieru, BofA–NC cca 1,99–2,18 % podle objemu (350–550+ mil. USD) a doby úhrady, U.S. Bank–NASPO 34,75 bps `[STALE]`.
  - US Commerce: týdenní výpis 157–168 bps vs. 109–120 bps `[STALE: 2017–2021]`.
  - Citi–Texas: 1,93 % + 0,75 bp/den za dřívější úhradu `[FACT, STALE: 07/2024]`.
- **Earnings credit rate (C):** zůstatky na neúročeném účtu generují kredit, který kompenzuje poplatky za cash management `[FACT – AFP]`. Je to korporátní obdoba „aktivitní nuly“, jen řízená zůstatkem.
- **Relationship pricing a RM (C, F):**
  - Klienti s primárním vztahem mají ROE zhruba o 20 p.b. vyšší než klienti jen s úvěrem `[CLAIM – McKinsey]`.
  - Oliver Wyman (2023): banky zkoušejí subscription pricing `[CLAIM]`. BCG (2018): špatně nastavený balíček vede ke ztrátě `[CLAIM]`.
  - BofA Employee Banking & Investing dává benefity zaměstnancům korporátních klientů `[STALE: 02/2024, CLAIM]`. Loajalitu firmy tak nese HR benefit, ne body pro firmu.
- **Pro ČR:** commercial karty jsou z IFR vyňaty, takže rebate je i v EU ekonomicky možný. Český trh commercial karet je ale malý a B2B platby jdou převodem. Objem commercial karet v ČR `[DATA GAP: ČNB, Visa/MC CZ]`. Pro mid/large corporate je přenositelnější **transparentní relationship pricing typu ECR** (zůstatek → odpuštění poplatků) než bodový program.

---

# 9. Implikace pro ČS: vztahový tier místo „Moneybacku pro firmy“

Čísla z v2 přebíráme beze změny:
- BB2: 40–85 mil. Kč/rok `[EST]`
- BP3 tier: 149–299 Kč/měs. `[EST]`
- ČS FOP klienti v bázi: ~110–140 tis. `[EST]`
- PO klienti: ~60–80 tis. `[EST]`
- BP4: 30–36 tis. nových klientů/rok `[EST]`
- BP5: 50–100 mil. Kč/rok `[EST]`

Všechny nové odhady níže jsou `[EST]` se vzorcem. Parametry označené P jsou předpoklady k ověření na interních datech (Q7 v2).

| # | Varianta | Mechanika | Vazba | Hrubá ekonomika `[EST]` | Hlavní rizika | Doporučení |
|---|---|---|---|---|---|---|
| **V1** | **Schémová vrstva nabídek pro podnikatelské karty** (rozšířit Visa Business benefity a ověřit Mastercard Business Bonus / Easy Savings pro CZ) | D (+F) | BP4 (hodnota „0 Kč účtu“ bez ceny), BB2 | Rozpočet odměn ≈ 0 (financují obchodníci). Náklad = integrace do George Business a komunikace `[DATA GAP: podmínky schémat pro vydavatele]`. Přínos = hygiena a aktivita karet, diferenciace nízká (komukoli se stejnou kartou). | Vztah drží schéma, nízká exkluzivita | **Ano – quick win 0–6 m** |
| **V2** | **„George Business Preferred“: vztahový tier pro FOP a PO** podle zůstatku + úvěru (BofA / Allica model) | C jako booster (→ A, B, F) | **BP5** (tier George Business One), **BB2**, BB1 (sleva z úvěru) | Náklad na klienta v tieru = odpuštěné poplatky + sleva z úvěru × úvěr + bonus ke cashbacku. Ilustrace: sleva 0,25 p.b. (BofA) z úvěru 1 mil. Kč = 2 500 Kč/rok. Přínos = vkladová marže × přírůstek zůstatků + udržení primárního vztahu. Pro kalibraci prahů nutná interní data `[DATA GAP: distribuce zůstatků SB klientů ČS]`. Prahy BofA (20 000 USD) nelze převzít mechanicky. | Kanibalizace poplatků, kalibrace prahů, governance Retail vs. Corporate | **Ano – jádro, mid-term 6–18 m** (spolu s M4 v2) |
| **V3** | **Cashback na podnikatelské kartě podmíněný vztahem** (Allica / VÚB model: 1 % jen pro klienty s úvěrem nebo zůstatkem nad prahem) | A/B s branou C | BB2, BP3, BP4 (převedení útraty z osobní karty) | Na 10 000 Kč útraty: interchange 210 Kč (2,10 % `[STALE: 03/2022]`) − cashback 100 Kč = 110 Kč pro banku vs. 20 Kč na osobní debetní kartě. Při P = 20 000 klientů × P = 30 000 Kč měsíční útraty × 12 × 1 % = **72 mil. Kč/rok** nákladu cashbacku a ≈ 151 mil. Kč interchange `[EST = 20 000 × 30 000 × 12 × 2,10 %]`. Před schémovými poplatky. | **Revize IFR (obchodníci 05/2026)**. Air Bank cashback zrušila. Plošný cashback bez brány je drahý. | **Ano, ale jen jako booster uvnitř V2**, ne samostatně |
| **V4** | **Placený tier s benefity místo bodů** (rozšíření BP3: daňový pot, účetní SaaS, pojištění, schémové nabídky, vyšší cashback) | F + A (tarif financuje cashback, model bunq / N26 / Finom) | **BP3, BB2** | Výnos z v2 BB2: 40–85 mil. Kč/rok. Cashback booster v tieru (např. +0,5 p.b.) z útraty tier klientů: P = 17–35 tis. platících (v2) × P = 20 000 Kč/měs. × 12 × 0,5 % = 20–42 mil. Kč/rok nákladu, krytého interchange `[EST]`. | Ochota platit `[DATA GAP – research Q7 v2]`, kanibalizace Maxi | **Ano – sloučit s V2** do jedné architektury: 0 Kč základ → placený tier → vztahový tier |
| **V5** | **Partnerství s nebankovními B2B programy** (letecký, palivový, velkoobchod) | H (co-brand) | BP5 (PO s cestovními výdaji) | Náklad bodů nese banka při co-brandu. Ekonomika `[DATA GAP]`. | Disintermediace (příklad SAS), nízký dopad na mikro | **Monitorovat, ne investovat** |

**Doporučená architektura:**
1. **Základ 0 Kč** (Živnostník bez podmínek, v2 Q2).
2. **Schémové nabídky pro všechny podnikatelské karty** (V1).
3. **Placený tier s daňovým potem a SaaS** (V4 = BP3).
4. **Vztahový tier podle zůstatku a úvěru**, který odpouští poplatky, zlevňuje úvěr a násobí cashback na podnikatelské kartě (V2 + V3 = BP5 / BB2).

**Pro corporate program nestavět.** Místo něj transparentní relationship pricing typu „zůstatek kompenzuje poplatky“.

**Kroky bez lítosti:**
- Ověřit, zda podnikatelské karty ČS jsou v Odměnách / Moneybacku, a pokud ne, otevřít je FOP (model MONETA Odměny).
- Ověřit u Mastercardu dostupnost Business Bonus pro CZ.
- Změřit podíl útraty FOP na osobních kartách ČS (H6) na interních datech.

---

# 10. Otevřené otázky: 14 mezer, většinu odemknou interní data ČS a schémata

| # | Otázka | Proč je důležitá | Kde odemknout |
|---|---|---|---|
| 1 | Jsou podnikatelské karty ČS v Odměnách / Moneybacku? Účinnost podmínek 1. 8. 2025 vs. 8. 1. 2026? | Rozhoduje o H6 a V1 | Plné PDF odmeny_podminky.pdf, interně ČS |
| 2 | Podíl útraty FOP na osobních vs. podnikatelských kartách ČS | Velikost interchange páky (V3) | Interní data ČS |
| 3 | Distribuce zůstatků a úvěrů SB klientů ČS | Kalibrace prahů tieru (V2) | Interní data ČS (Q1/Q7 v2) |
| 4 | Commercial interchange ČR k 1. 1. 2026 (Visa, Mastercard) a klasifikace karet ČS jako commercial | Ekonomika V3 | Sazebníky schémat, karetní tým ČS |
| 5 | Mastercard Business Bonus / Ultimate a Easy Savings: dostupnost v ČR, podmínky pro vydavatele | V1 | Mastercard CEE |
| 6 | Visa: evropská obdoba SavingsEdge | V1 | Visa Europe |
| 7 | Revize IFR: návrh Komise, antimonopolní šetření scheme fees | Riziko V3 | EUR-Lex, DG COMP / FISMA |
| 8 | VÚB Money back: sazba. SLSP: cashback pro podnikatele. | Benchmark Erste / Intesa | Štatút VÚB 1. 7. 2026, slsp.sk, Erste skupina |
| 9 | KB „Klub věrnosti“, ČSOB Kate Coins, UniCredit U-šetřete, RB business karty: otevřenost podnikatelům | Úplnost inventury ČR | Podmínky bank |
| 10 | Důvod ukončení cashbacku Air Bank | Ekonomika plošného cashbacku | Air Bank, rozhovory |
| 11 | Kauzální dopad programů na retenci a share of wallet u SME | Business case všech variant | Interní A/B pilot ČS, case studies schémat, J.D. Power Small Business Banking Study |
| 12 | Počet členů a dopad BofA Preferred Rewards for Business | Nejbližší vzor V2 | BofA 10-K, earnings |
| 13 | Ochota českých podnikatelů platit za tier s benefity | V4 | Customer research n ≈ 500 (Q7 v2) |
| 14 | Partners, Trinity, Oberbank; telco a SaaS B2B programy | Úplnost | Weby a podmínky |

---

# 11. QA: všechna akceptační kritéria splněna; slabinou je ověření z výtahů a vysoký podíl STALE

| Kritérium | Výsledek | Doklad |
|---|---|---|
| Odpověď po segmentech na první stránce | **Splněno** | Kap. 1 |
| H1–H7 s verdiktem a důkazem | **Splněno** | Kap. 3 |
| ≥ 12 bank ČR | **Splněno (12)** | CZ-01 až CZ-25 (ČS, KB, ČSOB, RB, MONETA, UCB, Air Bank, Fio, Creditas, mBank, Revolut, Wise) |
| ≥ 5 nebankovních v ČR | **Splněno (8)** | CZ-29 až CZ-36 |
| ≥ 25 programů v Evropě z ≥ 8 zemí | **Splněno (26 z 8 zemí + pan-EU)** | UK, NL, DE, FR, SK, SE/NO/DK, HU, RS + pan-EU |
| ≥ 15 ve světě | **Splněno (27 + 10 corporate + 2 schémová)** | WD-01 až WD-28, CO-01 až CO-10, SC-04, SC-05 |
| Každý řádek DB má URL, datum zdroje a značku | **Splněno s výhradou** | 125 řádků × 22 polí. Datum zdroje „neznámé“ → STALE. 4 řádky jsou explicitní DATA GAP. |
| Kdo financuje, IFR pro commercial karty | **Splněno** | Kap. 7 (IFR čl. 1 odst. 3 písm. a) `[FACT]`) |
| 3–5 variant pro ČS s vazbou na BP3/BP4/BP5/BB2, EST se vzorcem | **Splněno (5)** | Kap. 9 |
| Rozpočet | 151 vyhledávání (plán ~150). Načtení stránek 0 z 80 plánovaných (síťová politika blokuje). | Ověření jen z výtahů |

**Značky v DB (125 řádků, řádek může nést více značek):** STALE 97 · FACT 38 · CLAIM 29 · DATA GAP 19 · EST 1. Podle regionu: CZ 37 řádků (31 věrnostních, 5 AKV, 1 DATA GAP), EU 47 (35 / 8 / 4), WORLD 41 (41 / 0 / 0). Duplicity sloučeny: Mastercard BBU, Visa SavingsEdge a BofA PRB z WS L5 jsou vedené pod EU-44, WD-15 a WD-01.

**Značky v textu reportu:** FACT 77 · EST 19 · STALE 48 · CLAIM 33 · DATA GAP 27. V případových studiích: FACT 22 · EST 7 · STALE 5 · CLAIM 9 · DATA GAP 12.

**Výjimky z cut-offu 06/2026 (STALE, nevydávané za současný stav):**
- většina produktových stránek bez data ve výtahu (USA, Kanada, Austrálie, UK karty);
- Mastercard Business Savings (05/2024), Business Bonus Ultimate (2024), průzkum Mastercard (10/2024);
- interchange ČR (03/2022) a intra-EEA (01/2021);
- MONETA Program Odměny (06/2025), SLSP Moneyback (07/2025), mBank (03/2026);
- Qatar Beyond Business (10/2021), Benzina Tankarta (03/2021).

**Známé slabiny (nezakrývat):**
1. Ověřeno z výtahů, ne z plných textů. 78 % řádků DB (97 ze 125) nese STALE, protože ve výtahu chybí datum.
2. Dopady programů nedokládá žádná studie s kontrolní skupinou.
3. Ekonomika V3 stojí na sazbě Mastercard ČR z 03/2022.
4. Nejisté jsou klíčové fakty o ČS (otevřenost Moneybacku podnikatelům, datum podmínek).
5. Rozpory se stopami ze zadání: Allica 15 000 GBP nepotvrzeno (10 000 / 4 000 GBP), SLSP 1 % pro podnikatele nepotvrzeno, ČS podmínky datum 1. 8. 2025 vs. 8. 1. 2026.
6. Pokrytí ES, PL a AT je jen akviziční. Indie, Brazílie, UOB a Amex Canada nehledány.

---

## Shrnutí pro CEO (≤ 250 slov)

**Odpověď:** Věrnostní programy pro firmy existují, ale jen pro živnostníky a malé firmy. U nich jsou retailové: cashback 0,1–1,5 % v Evropě, 1,5–2 % v USA, body a nabídky obchodníků. U zavedených SME se odměna váže na vztah: Allica dává cashback jen klientům se zůstatkem 50 000 GBP+ nebo úvěrem, Bank of America odstupňovává podle zůstatku 20 / 50 / 100 tis. USD. U korporací body nejsou, loajalitu kupuje rebate z firemních karet (~1,2 %), kompenzace poplatků zůstatky a vztahový pricing. V ČR nemá žádná banka ucelený program pro podnikatele. KB a MONETA dávají 1 % na podnikatelskou kartu, Air Bank svůj cashback k 30. 6. 2026 zrušila. Retailový Moneyback ČS je podle dostupných zdrojů vázaný na soukromou kartu. Podnikatelská karta přitom nese až ~10× vyšší interchange než osobní, protože firemní karty nepodléhají stropům IFR.

**Tři doporučení:**
1. **Hned:** otevřít podnikatelským kartám nabídky obchodníků (Visa / Mastercard, Moneyback). Rozpočet odměn ≈ 0.
2. **Do 18 měsíců:** postavit vztahový tier George Business podle zůstatku a úvěru (odpuštění poplatků, sleva z úvěru, cashback jen pro klienty v tieru) a spojit ho s placeným tierem z BB2.
3. **Nestavět** plošný cashback ani bodový program pro korporace.

**Co rozhodnout:** zda podnikatelský tier ponese program BB2/BP5 jako jednu cenovou architekturu „0 Kč základ → placený tier → vztahový tier“. A zda ČS přijme regulační riziko interchange (obchodníci žádají zastropování firemních karet).
