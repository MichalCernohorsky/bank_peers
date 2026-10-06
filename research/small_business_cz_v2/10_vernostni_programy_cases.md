# Věrnostní programy pro podnikatele – případové studie (7)
6. října 2026 · navazuje na `10_vernostni_programy_SB.md` · značky jako v reportu (`[FACT]` = ověřeno ve výtahu zdroje s URL; `[STALE]` = zdroj starší než 06/2026 nebo bez data; `[CLAIM]` = tvrzení firmy; `[EST]` = výpočet; `[DATA GAP]` = nenalezeno) · zdroje u ID v `10_vernostni_programy_db.csv` a logy v `loyalty_data/`

Přenositelnost do ČR: 1 = nepřenositelné, 5 = přenositelné hned a bez partnerů.

| # | Případ | Typ | Segment | Přenositelnost | Co si ČS vezme |
|---|---|---|---|---|---|
| 1 | Bank of America – Preferred Rewards for Business (USA) | C (booster → A, B) | FOP/mikro + SME | **5** | architekturu vztahového tieru pro BP5/BB2 |
| 2 | Allica Bank – Business Rewards Account (UK) | B + C | zavedené SME | **4** | cashback jen jako odměnu za vztah |
| 3 | VÚB Money back vs. SLSP Moneyback (SK) | A | FOP + PO s úvěrem | **5** | zařadit podnikatele, ne je vyloučit |
| 4 | Mastercard Business Savings / Business Bonus (NatWest, bunq, OTP, Intesa) | D | FOP/mikro + SME | **5** (dostupnost v ČR `[DATA GAP]`) | vrstvu nabídek bez vlastního rozpočtu |
| 5 | Commercial card rebaty (GSA SmartPay, JPM, BofA, Citi) | G | mid/large corporate, veřejný sektor | **2** | pro corporate pricing, ne body |
| 6 | MONETA – Business Card 1 % + Program Odměny pro FOP (ČR) | A + D | FOP/mikro (+ firmy u karty) | **5** (domácí benchmark) | otevřít retailový program FOP |
| 7 | Air Bank – ukončení cashbacku pro podnikatele (ČR, negativní případ) | A | FOP/mikro | – (poučení) | plošný cashback bez vztahové brány nedělat |

---

## 1. Bank of America – Preferred Rewards for Business (USA) · ID WD-01 · přenositelnost 5/5

**Mechanika**
- Vztahový tier nad podnikatelským běžným účtem, zdarma. Kvalifikuje kombinovaný průměrný denní zůstatek za 3 kalendářní měsíce na business vkladech BofA a investicích Merrill.
- Tiery: Gold ≥ 20 000 USD, Platinum ≥ 50 000 USD, Platinum Honors ≥ 100 000 USD `[FACT 2026]`.
- Upgrade je automatický. Benefity se drží min. 1 rok i při dočasném poklesu zůstatku `[FACT]`.

**Benefity** `[STALE: datum neznámé]`:
- +25 / 50 / 75 % ke kartovým odměnám,
- bez měsíčních poplatků až na 4 business běžných a 4 spořicích účtech a bez drobných poplatků,
- booster úroku na Business Advantage Savings,
- sleva 0,25 p.b. z úrokové sazby nových úvěrových linek a úvěrů,
- sleva 0,05 % z ceny merchant services.

**Ekonomika**
- Financuje banka z vkladové marže. Program „kupuje“ zůstatek a primární vztah (účet + karta + úvěr + akceptace).
- Ilustrace: firma v tieru Platinum utratí 100 000 USD na kartě s 1,5 %. Základní odměna je 1 500 USD, bonus 50 % přidá 750 USD/rok `[EST = 100 000 × 1,5 % × 50 %]`. Bonus tak roste s útratou, vstup se ale řídí zůstatkem.

**Důkaz úspěchu**
- Za business program nejsou veřejná data o počtu členů, retenci ani vkladech `[DATA GAP: BofA 10-K, earnings]`.
- Nepřímé doklady:
  - Celý Preferred Rewards (všechny segmenty): 11,4 mil. členů, 99% retence `[CLAIM – ARS FY2025, metodika neuvedena]`.
  - Když BofA 27. 5. 2026 nahradil retailový program programem BofA Rewards, **business program ponechal beze změny** `[FACT, 02/2026]`.

**Přenositelnost do ČR: 5/5.** Nepotřebuje obchodníky ani schéma, jen data o zůstatcích, ceník a úvěrový pricing. ČS má všechny složky: účet, kartu, úvěry, akceptaci a investice.

**Co si ČS vezme**
- Architekturu pro BP5 / George Business One a BB2: tier podle zůstatku + úvěru, který odpouští poplatky, zlevňuje úvěr a násobí cashback.
- Prahy kalibrovat na distribuci zůstatků klientů ČS `[DATA GAP]`. Hodnoty v USD nepřebírat.
- Pravidlo „benefity drží rok“ snižuje frustraci při kolísání zůstatku. U OSVČ je to důležité kvůli sezónním daňovým platbám.

---

## 2. Allica Bank – Business Rewards Account (UK) · ID EU-01 · přenositelnost 4/5

**Mechanika**
- Podnikatelský účet bez měsíčního poplatku a bez úroku na běžném zůstatku.
- Cashback 1 % z plateb kartou, nad měsíčním prahem 1,5 %. K tomu pojmenovaný relationship manager a spořicí „pot“.
- Vstupní brána: firma **založená alespoň 12 měsíců** a **zůstatek 50 000 GBP+ nebo úvěr u Allica** `[FACT – Key Product Information, STALE: datum neznámé]`.
- Práh pro 1,5 %: KPI dokument uvádí 10 000 GBP měsíční útraty, tisková zpráva k FY25 4 000 GBP `[CLAIM]`. Hodnota 15 000 GBP z výchozí stopy se nepotvrdila.

**Ekonomika `[EST]`**
- Firma s útratou 20 000 GBP/měs. dostane při prahu 10 000 GBP: 10 000 × 1 % + 10 000 × 1,5 % = **250 GBP/měs.**
- Při prahu 4 000 GBP: 4 000 × 1 % + 16 000 × 1,5 % = **280 GBP/měs.**
- Financuje banka z vkladové a úvěrové marže a z interchange. Cashback tu není marketingový náklad, je to položka relationship pricingu.

**Důkaz úspěchu**
- Aktivní klienti Rewards účtu vzrostli z 6 000+ na 14 000+ (FY25).
- Vklady banky +29 % na 5,7 mld. GBP, úvěry +23 % na 3,7 mld. GBP `[CLAIM – výsledky přes tisk]`.
- Kauzalitu cashback → vklady zdroje neprokazují.

**Přenositelnost do ČR: 4/5.** Pravidlo „cashback jen pro klienty s úvěrem nebo zůstatkem nad X“ ČS replikuje bez partnerů. Snížení na 4: ekonomika stojí na commercial interchange, kterou obchodníci v EU žádají zastropovat (05/2026) `[CLAIM]`.

**Co si ČS vezme:** cashback jako **booster uvnitř vztahového tieru** (varianta V3 v reportu), ne jako plošnou nabídku. Brána „12+ měsíců a vztah“ chrání před drahými a krátkodobými klienty.

---

## 3. VÚB Money back (Mastercard Business World) vs. SLSP Moneyback (SK) · ID EU-36, EU-35 · přenositelnost 5/5

**Mechanika**
- **VÚB:** štatút platný od 1. 7. 2026 do odvolání.
  - Měsíční peněžní bonus na kartový účet za aktivní používání firemní kreditní karty Mastercard Business World.
  - Pro FO podnikatele i PO, kterým banka poskytla úvěrový limit `[FACT]`.
  - Sazba `[DATA GAP: statut-Moneyback-01072026.pdf]`.
  - Ve stejný den VÚB ruší pojištění zneužití karty a lounge benefity Zlaté Mastercard Business `[FACT – podnikajte.sk]`. Hodnota se tak přesouvá z F do A.
- **SLSP (Erste):** Moneyback zahrnuje debetní karty jen k účtům **nepodnikatelů** a kreditní karty Visa Classic/Gold `[FACT, zveřejnění k 1. 7. 2025]`.

**Ekonomika**
- VÚB váže odměnu na úvěrový produkt. Cashback platí interchange commercial kreditní karty a podporuje čerpání limitu. Nákladem jsou zrušené nefinanční benefity `[EST – interpretace]`.

**Důkaz úspěchu:** program je nový, data nejsou `[DATA GAP]`.

**Přenositelnost do ČR: 5/5.** Je to sousední trh a stejná konstelace: Erste (SLSP / ČS) proti konkurenční skupině (Intesa / VÚB).

**Co si ČS vezme**
- Konkurent cílí přesně na segment, který Erste ve svém retailovém programu vynechává.
- ČS by měla ověřit, zda ČS Moneyback také vylučuje podnikatelské karty (článek uvádí soukromou kartu `[CLAIM]`), a pokud ano, otevřít ho FOP. Vzorem je MONETA (případ 6).

---

## 4. Mastercard Business Savings / Business Bonus (UK, NL a další, HU, RS) · ID EU-13, EU-14, EU-18, EU-44–46 · přenositelnost 5/5

**Mechanika**
- Automatický cashback od obchodníka připsaný na výpis do 3–5 dní. Bez registrace a kuponů, klient je zapsán automaticky s každou způsobilou business kartou.
- NatWest/RBS/Ulster: rozšíření z kreditních na debetní karty pro cca **1 mil.** držitelů, 1 000+ nabídek (LUX, McAfee, Heathrow Express, Dropbox, Avis, Microsoft Advertising) `[FACT, STALE: 05/2024]`.
- bunq: od 15. 1. 2025 v NL, DE, FR, ES a IT (Google Workspace, Docusign, HubSpot, Sixt, Booking.com, FedEx, Fiverr) `[FACT]`.
- Dále Mettle (UK), OTP Bank (HU), Banca Intesa (RS) `[STALE]`.
- Rozšíření **Business Bonus Ultimate** (2024) přidává body (cashback, pay-with-points, nabídky) jako white-label pro emitenty `[CLAIM, STALE: 10/2024]`.

**Ekonomika**
- Nabídky financují obchodníci, program provozuje Mastercard. Pro banku je to bez vlastního rozpočtu odměn.
- Body v Ultimate nese emitent `[CLAIM]`. Podmínky pro vydavatele nejsou veřejné `[DATA GAP]`.

**Důkaz úspěchu:** data o využití ani o vlivu na retenci nejsou veřejná `[DATA GAP]`. Nasazení u velkých bank (NatWest) a v CEE (OTP, Intesa) ukazuje, že vydavatelé program považují za užitečný.

**Přenositelnost do ČR: 5/5** po technické stránce. Dostupnost pro CZ a podmínky jsou `[DATA GAP: Mastercard CEE]`. ČS už podobný model provozuje s Visou („Benefity pro firmy“: Bolt Business, EasyPark, foodora, wflow) `[FACT/STALE]`.

**Co si ČS vezme:** quick win V1. Vrstvu nabídek zapnout pro všechny podnikatelské karty ČS (Visa i Mastercard) a prezentovat ji v George Business. Nic dalšího od ní nečekat: stejnou nabídku dostane každý se stejnou kartou.

---

## 5. Commercial card rebaty – GSA SmartPay, J.P. Morgan, BofA, Citi (USA) · ID CO-01–CO-06, SC-05 · přenositelnost 2/5

**Mechanika**
- Smluvní roční revenue share z karetní útraty.
- Sazba roste s **objemem** (tiery) a s **rychlostí úhrady** (častější výpis, kratší splatnost).
- J.P. Morgan: „rebate based on your spend volume and your contractually negotiated rebate rates… typically paid annually“ `[STALE: datum neznámé]`.

**Ekonomika**
- GSA SmartPay FY2025: útrata 39,4 mld. USD, refundy 471 mil. USD `[FACT]` = **1,20 %** `[EST]`. Od vzniku programu 7,2 mld. USD refundů `[FACT]`.
- Státní kontrakty `[STALE]`:
  - JPM–New York: 180,5–43 bps podle tieru,
  - BofA–Severní Karolína: 1,99–2,18 % podle objemu a doby úhrady,
  - U.S. Bank–NASPO: 34,75 bps,
  - Citi–Texas: 1,93 % + 0,75 bp za každý den dřívější úhrady `[FACT, STALE: 07/2024]`.
- Rebate se financuje z commercial interchange: Visa USA 1,30 % + 35 USD (large ticket) až 2,95 % + 0,10 USD `[FACT 04/2026]`.

**Důkaz úspěchu**
- GSA 471 mil. USD/rok `[FACT]`.
- J.P. Morgan case Ashton Woods: +98 % útraty, +303 % rebate `[CLAIM]`.
- Rebate funguje jako „věrnost“: tiery motivují soustředit útratu u jedné banky.

**Přenositelnost do ČR: 2/5.** Commercial karty jsou z IFR stropů vyňaty `[FACT]`, takže rebate je i v EU ekonomicky možný. Český trh commercial karet je ale malý a B2B platby jdou převodem `[DATA GAP: objem commercial karet v ČR]`.

**Co si ČS vezme:** pro mid/large corporate **nestavět bodový program**. Pokud vůbec, pak objemový rebate u virtuálních a purchasing karet ve velkých AP tocích. Hlavně transparentní relationship pricing, kde zůstatek kompenzuje poplatky (obdoba ECR).

---

## 6. MONETA – Business Card 1 % + Program Odměny otevřený FOP (ČR) · ID CZ-13, CZ-14 · přenositelnost 5/5

**Mechanika**
- **MONETA Business Card:** podnikatelská kreditní karta s vedením zdarma, 1 % zpět ze všech plateb bez stropu, bezúročné období až 55 dní, sjednání online `[FACT/STALE: datum neznámé]`. K tomu časově omezené kampaně (5 % PHM, 5 % hobby markety do 1 000 Kč/měs. po 6 měsíců), evidované jako AKV.
- **Program Odměny (Smart Banka):** card-linked nabídky obchodníků po aktivaci v aplikaci. **Výslovně zahrnuje karty Business CZK a Business Premium fyzických osob podnikatelů, PO jsou vyloučeny.** Podmínky účinné od 22. 6. 2025 `[FACT, STALE: 06/2025]`.

**Ekonomika**
- Cashback platí interchange podnikatelské kreditní karty `[EST – odvozeno]`, Odměny platí obchodníci.
- V kontextu v2: MONETA je nejrychleji rostoucí banka v úvěrech segmentu (+27,5 %, 1H 2026 `[FACT v2]`) a karta s cashbackem je součást úvěrové propozice.

**Důkaz úspěchu:** samostatná data o programu nejsou `[DATA GAP]`.

**Přenositelnost do ČR: 5/5.** Domácí benchmark, stejný trh a regulace.

**Co si ČS vezme:** jediná česká banka, která retailový card-linked program **ověřeně otevírá podnikatelům**. ČS může totéž udělat s Moneybackem (nízký náklad, nabídky platí obchodníci) a podnikatele tak nepostrkovat k osobní kartě.

---

## 7. Air Bank – ukončení cashbacku 1 % pro podnikatele (ČR, negativní případ) · ID CZ-18

**Mechanika:** 1 % zpět z každé platby podnikatelskou kartou (držitel i disponent), výplata na podnikatelský účet do 10. dne následujícího měsíce. **Ukončeno k 30. 6. 2026**, od 1. 7. 2026 nárok nevzniká `[FACT – e15.cz, banky.cz]`. Rovnocenná náhrada nenalezena.

**Ekonomika:** strop programu a důvod ukončení `[DATA GAP]`. Air Bank nemá podnikatelský úvěr `[v2: DATA GAP]`, takže cashback nebyl spojený s úvěrovým výnosem. Rešerše nenašla úvěr ani vztahovou podmínku, která by náklad vyvažovala `[EST – interpretace]`.

**Důkaz:** v době programu získala Air Bank > 65 tis. podnikatelských účtů za < 2 roky (1/2026) a 17 % FO ve Fakturoidu (9/2026) `[FACT v2]`. Podíl cashbacku na tomto růstu není známý.

**Co si ČS vezme**
- Plošný cashback bez vztahové brány zvedne akvizici, ale nemusí se zaplatit. Proto variantu V3 vázat na tier (zůstatek, úvěr).
- Konkurenční okno: podnikatelé Air Bank od 7/2026 přišli o odměnu. Pro akviziční sezónu 2027 (BP4) je to argument pro „0 Kč + nabídky obchodníků + tier“.
