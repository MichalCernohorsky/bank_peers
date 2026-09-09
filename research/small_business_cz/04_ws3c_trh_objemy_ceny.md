# 04 – WS3c: Kvantifikace bankovního trhu small business v ČR 2019–2026 (objemy, ceny, podíly, ekonomika segmentu)
Perspektiva: konkurenční benchmark Česká spořitelna vs. trh · segment FOP + PO s obratem do 25 mil. Kč · stav k 2026-09-09.
Datové tabulky: `data/ws3_uvery_zivnostnici_male_podniky.md`, `data/ws3_sazby_vs_repo.md`, `data/ws3_npl.md`, `data/ws3_cenovy_benchmark.md`, `data/ws3_trzni_podily.md`, `data/ws3_revenue_pool.md`, `data/ws3_zakaznicka_zkusenost.md`, `data/ws3_kotvy_banky.md`, `data/ws3_local_factsheets.md`.

> **Metodická výhrada (kritická):** V této relaci byl přístup na www.cnb.cz (ARAD, měnová statistika, ZFS), cbamonitor.cz, kurzy.cz, ceníky všech bank i srovnávače (Finparáda, Měšec, Peníze.cz, Banky.cz, Finmag) a web.archive.org blokován síťovou proxy a kvóta WebSearch byla vyčerpána. Tržní řady ČNB jsou proto označeny `[DATA GAP]` s přesným umístěním sestavy. Kvantifikace stojí na (i) primárních investorských fact sheetech KB, ČSOB, Moneta a ČS uložených v repozitáři (`[FACT]`), (ii) ověřených útržcích z vyhledávání (`[FACT – snippet]`) a (iii) explicitně označených odhadech (`[EST]`). **Žádné číslo nebylo doplněno z paměti.**

---

## (a) Hypotézy a verdikt

| # | Hypotéza (z 00_plan) | Verdikt | Opora |
|---|---|---|---|
| H3.1 | ČS má nejvyšší podíl na podnikatelských účtech (~25–30 %), ale nová akvizice FOP jde k Fio, Air Bank, RB | **Neověřeno** – ČS nezveřejňuje počet podnikatelských klientů; průzkumy (SME Banking Club, Datank, Ipsos) nedostupné. Nepřímá indicie: KB drží stabilně ~242 tis. ne-fyzických klientů (2021–2026), tj. velké banky v segmentu **nerostou počtem klientů** | KB F&F `[FACT]`, dopočet `[EST]` |
| H3.2 | Účet ČS pro podnikatele je dražší než Fio/Air Bank/Creditas (0 Kč), srovnatelný s KB/ČSOB; úročení vkladů podnikatelů 2023–24 vedli challengeři | **Částečně potvrzeno strukturálně**: v r. 2026 existují u RB (Chytrý účet) a UniCredit (Business Start) podnikatelské účty za 0 Kč, zatímco plné balíčky stojí 99–350 Kč/měs.; ceny ČS/ČSOB/KB `[DATA GAP]`. Úročení vkladů `[DATA GAP]`, ale Moneta ukazuje, že komerční klienti přesunuli 51 % vkladů na úročené produkty (3/2026 vs. 43 % 4Q 2022) | Finmag 2026 `[FACT – snippet]`; Moneta `[FACT]` |
| H3.4 | KB a ČSOB mají nejsilnější pozici v úvěrech malým firmám; Moneta je relativně nejsilnější v živnostnících | **Potvrzeno pro Monetu, revidováno pro KB**: Moneta zdvojnásobila nové small-business splátkové úvěry 2023→2025 (4,0 → 8,4 mld. Kč) a nezajištěné SB úvěry rostou 19 % p.a.; KB úvěry malým firmám 2020→2025 rostly jen 1,9 % p.a. a jejich podíl na portfoliu KB klesl z 6,6 % na 5,6 %. ČSOB SME (širší definice) roste 10–11 % y/y | IR fact sheety `[FACT]` |
| Nová H3.5 | Revenue pool segmentu je řádově 10–20 mld. Kč ročně a jeho největší složkou je depozitní marže na neúročených běžných účtech | **Pracovní odhad** `[EST]`: 8–25 mld. Kč, střed ≈ 15 mld. Kč; vklady ≈ 34 %, úvěry ≈ 41 %, poplatky ≈ 25 % středního scénáře – **vysoce citlivé na ČNB jmenovatele (chybí)** | model v `ws3_revenue_pool.md` |
| Nová H3.6 | Riziko FOP je strukturálně vyšší než u firemních portfolií bank | **Potvrzeno bodově**: NPL úvěrů živnostníkům 5,10 % (9/2023) vs. NPL komerčního segmentu Moneta 1,0–1,2 % a skupinová NPL ČS/ČSOB/KB 1,3–1,9 % | ČBA Monitor `[FACT – snippet]`, IR `[FACT]` |

---

## (b) Exhibity

### Exhibit 1 – Úvěry živnostníkům a malým podnikům: trh (ČNB) vs. bankovní kotvy, stav ke konci roku, mld. Kč
| Rok | ČNB: úvěry živnostníkům (S.14) | ČNB: nové obchody NFP do 7,5 mil. Kč | KB „Loans to small businesses" | ČSOB „SME loans" | Moneta Commercial celkem | Moneta nezajištěné SB úvěry + KTK | Moneta nové SB splátkové úvěry (rok) |
|---|---|---|---|---|---|---|---|
| 2019 | `[DATA GAP]` | `[DATA GAP]` | n.a. | n.a. | n.a. | n.a. | n.a. |
| 2020 | `[DATA GAP]` | `[DATA GAP]` | 45,9 | n.a. | n.a. | n.a. | n.a. |
| 2021 | `[DATA GAP]` | `[DATA GAP]` | 47,9 | n.a. | n.a. | n.a. | n.a. |
| 2022 | `[DATA GAP]` | `[DATA GAP]` | 46,8 | n.a. | 82,8 | 12,1 | n.a. |
| 2023 | `[DATA GAP]` | `[DATA GAP]` | 47,5 | n.a. | 83,8 | 13,5 | 4,0 |
| 2024 | `[DATA GAP]` | `[DATA GAP]` | 47,9 | 105,2 | 92,6 | 16,2 | 6,4 |
| 2025 | `[DATA GAP]` | `[DATA GAP]` | 50,3 | 115,4 | 104,0 | 20,5 | 8,4 |
| 1Q 2026 | `[DATA GAP]` | `[DATA GAP]` | 51,2 | 120,1 | 109,1 | 21,5 | 2,1 (1Q) |
| CAGR / y/y | – | – | +1,9 % p.a. (2020–25); +6,9 % y/y (1Q26) | +9,7 % (2025); +11,1 % y/y (1Q26) | +12,3 % (2025) | +19,1 % p.a. (2022–25); +26,3 % (2025) | +109 % (2023→25) |
Zdroje: KB Facts & Figures 1Q 2026 (list Business), ČSOB fact sheet 1Q 2026 (Business volumes), Moneta Basic financial data 4Q 2024 a 1Q 2026 (Portfolio_Net loans, New Business Volumes) – vše `[FACT]`, lokální IR soubory. Definice: KB = podnikatelé + malé firmy vč. ESSOX; ČSOB = malé **a střední** podniky (širší než náš segment); Moneta Commercial = small business + SME + korporace; „nezajištěné SB úvěry + KTK" = nejbližší proxy čistého small business. ČNB sloupce doplnit z ARAD: „Klientské úvěry podle sektorového hlediska" (Domácnosti – živnostníci) a harmonizovaná statistika „nové obchody podle objemu úvěru" (https://www.cnb.cz/cs/statistika/arad-system-casovych-rad/). Ověřené tempo trhu `[FACT – snippet, ČNB Měnová statistika 12/2024]`: úvěry nefinančním podnikům +3,6 % y/y, domácnostem +6,1 %, soukromému sektoru +5,5 % (12/2024).

### Exhibit 2 – Sazby nových úvěrů podnikům vs. 2T repo ČNB
| Období | 2T repo (konec období) | Nové úvěry NFP 7,5–30 mil. Kč | Nové úvěry NFP do 7,5 mil. Kč | Nové úvěry živnostníkům | Spread (7,5–30 mil.) nad repo |
|---|---|---|---|---|---|
| 12/2019 | 2,00 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 12/2020 | 0,25 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 12/2021 | 3,75 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 12/2022 | 7,00 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 12/2023 | 6,75 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 12/2024 | 4,00 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 2/2025 | 3,75 % | **5,53 %** | `[DATA GAP]` | `[DATA GAP]` | ≈ +1,8 pb `[EST]` |
| 6/2025 | 3,50 %* | **5,38 %** | `[DATA GAP]` | `[DATA GAP]` | ≈ +1,9 pb |
| 8/2025 | 3,50 % | **5,12 %** | `[DATA GAP]` | `[DATA GAP]` | ≈ +1,6 pb |
| 12/2025 | 3,50 % | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
| 9/2026 | **3,75 %** (od 19. 6. 2026; 6. 8. 2026 ponecháno) | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | |
Zdroje: repo 2019–2025 – ČNB FAQ „Jak se vyvíjela 2T repo sazba" (https://www.cnb.cz/cs/casto-kladene-dotazy/Jak-se-vyvijela-dvoutydenni-repo-sazba-CNB/; fetch blokován, hodnoty dle zadání koordinátora `[FACT – neověřeno fetchem]`); repo 2026 – Fio banka zpravodajství a behounek.eu `[FACT – snippet]`; sazby 2025 – Kurzy.cz „Úrokové sazby MFI v ČR – srpen 2025" přebírající komentář ČNB `[FACT – snippet]`. *Přesný měsíc snížení repo na 3,50 % v r. 2025 ověřit. Pozn.: snippet u srpna 2025 uvádí formulaci „zvýšila na 5,12 %", což je vůči červnu pokles – ověřit v původním komentáři ČNB.

Doplňkové kotvy cen peněz `[FACT]`: Moneta cost of funds na klientských vkladech 3,55 % (4Q 2023) → 2,25 % (4Q 2024) → 1,96 % (4Q 2025) → 1,99 % (1Q 2026); NIM ČS 2,12 % / ČSOB 2,41 % / KB 1,72 % / Moneta 2,0 % (FY 2025). Moneta Commercial: NII / průměrné úvěry segmentu 4,37 % (FY 2024) → 3,89 % (1Q 2026 anualizováno) `[EST – dopočet z FACT]`.

### Exhibit 3 – Kvalita úvěrů: NPL živnostníků vs. bankovní portfolia
| Ukazatel | 12/2022 | 12/2023 | 12/2024 | 12/2025 | 3/2026 | Zdroj |
|---|---|---|---|---|---|---|
| ČNB/ČBA – NPL úvěrů živnostníkům | `[DATA GAP]` | **5,10 %** (9/2023) | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | ČBA Monitor `[FACT – snippet]` |
| ČNB – NPL nefinanční podniky | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | ARAD / ZFS |
| ČS – NPL / klientské úvěry | 1,9 % | 1,8 % | 1,8 % | 1,6 % | 1,5 % | ČS key figures `[FACT]` |
| KB – NPL skupina | n.a. | 1,85 % | 1,94 % | 1,59 % | 1,54 % | KB F&F `[FACT]` |
| ČSOB – NPL (ČNB metodika) | 1,69 % | 1,42 % | 1,35 % | 1,30 % | 1,28 % | ČSOB fact sheet `[FACT]` |
| Moneta – NPL **Commercial** | 1,1 % | 1,2 % | 1,2 % | 1,0 % | 0,9 % | Moneta KPIs `[FACT]` |
| Moneta – Cost of risk skupina (% avg. net loans) | 0,32 % | 0,20 % | 0,05 % | 0,14 % | 0,22 % | Moneta KPIs `[FACT]` |
Kde doplnit řadu ČNB: ARAD „Úvěry se selháním podle sektorů"; ZFS jaro 2025 (data 12/2024) a podzim 2025 (data 6/2025, publ. 15. 12. 2025); ČBA Monitor měsíční komentáře „Bankovní statistika za …".

### Exhibit 4 – Cenový benchmark podnikatelských účtů 2021 / 2023 / 2026 (měsíční poplatek, Kč)
| Banka | 2021 | 2023 | 2026 | Podmínky 0 Kč (2026) | Jistota |
|---|---|---|---|---|---|
| Česká spořitelna | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | ceník csas.cz blokován |
| ČSOB | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
| Komerční banka | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
| Raiffeisenbank | `[DATA GAP]` | `[DATA GAP]` | **0 / 99 / 299** (Chytrý / Aktivní / Exkluzivní) | Chytrý účet bez podmínek dle snippetu – ověřit | `[FACT – snippet Finmag 2026]` |
| Moneta | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
| UniCredit Bank | `[DATA GAP]` | `[DATA GAP]` | **0 / 1. rok 0, pak 100 nebo 200 dle kritérií / 350** (Start / Open Top / Top) | Open Top: kritéria neuvedena | `[FACT – snippet Finmag 2026]` |
| Air Bank | – (ověřit datum spuštění) | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
| Fio banka | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
| Creditas | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
| Revolut Business / Wise | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | `[DATA GAP]` | blokováno |
Odchozí platba, výběr z ATM, zahraniční platba, kontokorentní sazba, úročení podnikatelských běžných/spořicích účtů: kompletní `[DATA GAP]` – rámec a URL ceníků v `data/ws3_cenovy_benchmark.md`. Kvalitativně `[FACT – snippet Finmag 2026]`: u většiny bank je většina základních transakcí na podnikatelských účtech zdarma; poplatky za vedení jsou „výrazně nad úrovní běžných účtů"; některé banky nabízejí účty s omezenými službami zdarma.

### Exhibit 5 – Tržní podíly v segmentu: ověřené čitatele a podmíněné intervaly `[EST]`
| Banka | Podnikatelští klienti (čitatel) | Úvěry segmentu 12/2025 (čitatel, mld. Kč) | Podíl na úvěrech při trhu 150 / 200 / 250 mld. Kč | Vklady segmentu | Jistota |
|---|---|---|---|---|---|
| Česká spořitelna | `[DATA GAP]` (4 565 tis. klientů celkem, 3/2026) | `[DATA GAP]` | – | `[DATA GAP]` | ČS nereportuje segment |
| ČSOB | `[DATA GAP]` | 115,4 (SME, širší def.) | nesrovnatelné | `[DATA GAP]` | `[FACT]` čitatel |
| Komerční banka | ≤ 242 tis. ne-fyzických klientů (3/2026) | 50,3 | 34 % / 25 % / 20 % | `[DATA GAP]` | čitatel `[EST-dopočet]`/`[FACT]` |
| Moneta | 125 tis. komerčních klientů (~2022) | 20,5 (nezajištěné SB) – 104,0 (Commercial) | 14 % / 10 % / 8 % (SB proxy) | 109,3 mld. (Commercial, 3/2026) | `[FACT – snippet]`/`[FACT]` |
| RB, UCB, Air Bank, Fio, Creditas, Revolut, Wise | `[DATA GAP]` | `[DATA GAP]` | – | `[DATA GAP]` | VZ 2025 / TZ |
| **Trh (ČNB)** | výstup WS1 | `[DATA GAP]` | – | `[DATA GAP]` | ARAD |
Jmenovatele 150/200/250 mld. Kč jsou pouze citlivostní scénáře (KB + Moneta ≈ 71 mld. Kč ve srovnatelných definicích by drželo 47 / 35 / 28 %). Kondicionál na počty subjektů: při 1,0–1,4 mil. aktivních FOP + PO (rozpětí hypotéz WS1, zde neověřeno) drží KB ≤ 17–24 % a Moneta ≤ 9–13 % subjektů `[EST – horní hranice]`.

### Exhibit 6 – Revenue pool segmentu small business (roční provozní výnosy bank), mld. Kč `[EST]`
| Složka | Vstup nízký / střední / vysoký | Nízký | Střední | Vysoký |
|---|---|---|---|---|
| NII z úvěrů | úvěry 120 / 180 / 250 mld. × marže 3,0 / 3,5 / 4,0 % | 3,6 | 6,3 | 10,0 |
| NII z vkladů | vklady 250 / 350 / 450 mld. × depozitní marže 1,0 / 1,5 / 2,0 % | 2,5 | 5,3 | 9,0 |
| Poplatky | 0,9 / 1,1 / 1,3 mil. účtů × ARPU 2,0 / 3,5 / 5,0 tis. Kč | 1,8 | 3,9 | 6,5 |
| **Celkem** | | **≈ 8** | **≈ 15** | **≈ 25** |
Postup a opora vstupů: `data/ws3_revenue_pool.md`. Kotvy `[FACT]`: Moneta Commercial FY 2024 – NII 3 852 mil., poplatky 686 mil., provozní výnosy 4 778 mil. Kč (37 % výnosů banky) při průměrných úvěrech 88,2 mld. Kč → 5,4 % výnosů na úvěry, ≈ 38 tis. Kč provozních výnosů a ≈ 5,5 tis. Kč poplatků na komerčního klienta (125 tis.) `[EST – dopočet]`; KB transakční + depozitní poplatky 2025 = 2 395 mil. Kč ≈ 1,35 tis. Kč na klienta napříč všemi klienty `[EST – dopočet]`. Kontrola řádu: střední scénář = 6–7 % součtu provozních výnosů ČS + ČSOB + KB + Moneta (59,2 + 48,4 + 36,9 + 13,8 ≈ 158 mld. Kč FY 2025 `[FACT]`) a ≈ 3× celý Commercial segment Moneta. Přesnost ± 40 %; **největší citlivost: depozitní marže (±1 pb = ±3,5 mld. Kč).**

### Exhibit 7 – Zákaznická zkušenost podnikatelů
Kompletní `[DATA GAP]` (SME Banking Club, Datank „Banka roku – podnikatelé", Ipsos/ČBA, KPMG CX, finanční arbitr) – rámec v `data/ws3_zakaznicka_zkusenost.md`. Metodická poznámka `[FACT – působnost dle zákona o finančním arbitrovi]`: finanční arbitr rozhoduje spory **spotřebitelů**; podnikatelé jednající v rámci podnikání do jeho působnosti nespadají, takže „podíl stížností podnikatelů" u FA je z definice ≈ 0 – relevantním zdrojem jsou podání ČNB a ombudsmani bank.

---

## (c) Zjištění (action titles)

### 1. Úvěry small business rostou v r. 2025–26 dvouciferně u těch, kdo se na segment zaměřili (Moneta, ČSOB), zatímco KB pět let stagnovala – segment je „contestable"
Nezajištěné small-business úvěry a kontokorenty Moneta vzrostly z 12,1 mld. Kč (4Q 2022) na 20,5 mld. Kč (4Q 2025), tj. +19 % p.a., a nové small-business splátkové úvěry se zdvojnásobily (4,0 → 8,4 mld. Kč, 2023→2025) `[FACT]`. ČSOB SME úvěry rostly +9,7 % (2025) a +11,1 % y/y (3/2026), rychleji než celé portfolio (+8,3 % / +7,4 %) `[FACT]`. Naproti tomu KB držela úvěry malým firmám na 46–48 mld. Kč po celé období 2020–2024 (CAGR 1,9 %), jejich podíl na skupinovém portfoliu klesl z 6,6 % na 5,6 % a oživení (+5,0 % 2025; +6,9 % y/y 1Q 2026) přišlo až s KB+ transformací `[FACT]`. Pro kontext: trh úvěrů nefinančním podnikům rostl ke konci 2024 jen +3,6 % y/y `[FACT – snippet]`. Závěr: v segmentu není „přirozený" vlastník úvěrového toku – kdo investuje do produktu (rychlý nezajištěný úvěr, digitální onboarding), bere podíl.

### 2. Sazby nových SME úvěrů se v r. 2025 držely 1,6–1,9 pb nad repo a klesaly s ní; po zvýšení repo na 3,75 % (6/2026) se cena úvěru pro podnikatele znovu zvedá
Nové úvěry podnikům v pásmu 7,5–30 mil. Kč stály 5,53 % (2/2025), 5,38 % (6/2025) a 5,12 % (8/2025) `[FACT – snippet]` při repo 3,75 → 3,50 %. ČNB 19. 6. 2026 zvýšila repo na 3,75 % a 6. 8. 2026 ji ponechala `[FACT]`. Menší úvěry (do 7,5 mil. Kč – typický small business) a úvěry živnostníkům mají v harmonizované statistice systematicky vyšší sazbu než pásmo 7,5–30 mil. Kč, hodnoty však nebyly dostupné `[DATA GAP]`. Marže banky je přitom větší než spread nad repo, protože úvěry jsou financovány vklady levnějšími než repo (Moneta cost of funds na vkladech 1,99 % v 1Q 2026 vs. repo 3,75 % `[FACT]`); Moneta realizuje na komerčních úvěrech 3,9–4,4 % NII (vč. vkladové složky segmentu) `[EST – dopočet]`.

### 3. Riziko živnostníků je ~3× vyšší než riziko firemních portfolií bank, ale náklady rizika komerčních segmentů jsou v r. 2024–26 blízko nuly – cena rizika teď segment nebrzdí
NPL úvěrů živnostníkům dosahoval 5,10 % (9/2023) `[FACT – snippet]`, zatímco NPL komerčního segmentu Moneta bylo 1,2 % (2023–24) a 0,9 % (3/2026), NPL ČS 1,5 %, ČSOB 1,28 %, KB 1,54 % (3/2026) `[FACT]`. Moneta v komerčním segmentu vykázala za FY 2024 znehodnocení jen −16 mil. Kč a v 1Q 2026 rozpuštění +22 mil. Kč `[FACT]`. Kombinace: rizikově dražší FOP subsegment je malý absolutně (objem `[DATA GAP]`), a při dnešních nákladech rizika si banky mohou dovolit expanzi nezajištěných SB úvěrů – což Moneta dělá. Řadu NPL 2019–2026 (ČNB) je nutné doplnit, aby šlo oddělit cyklus (2020–21 moratoria, 2023 energetický šok) od trendu.

### 4. Cena účtu se rozdvojila: „0 Kč základ + placený balíček" je v r. 2026 standard i u velkých bank (RB, UniCredit), a podnikatelský účet zůstává dražší než osobní
V r. 2026 nabízí Raiffeisenbank Chytrý účet pro podnikatele za 0 Kč a placené varianty za 99/299 Kč, UniCredit Business Start za 0 Kč, Open Top 100–200 Kč po prvním roce zdarma a Business Top za 350 Kč `[FACT – snippet Finmag 2026]`. Srovnávače konstatují, že základní transakce jsou u většiny bank zdarma, ale vedení podnikatelských účtů je výrazně dražší než u osobních `[FACT – snippet]`. Ceny ČS, ČSOB, KB, Moneta, Air Bank, Fio, Creditas, Revolut, Wise pro 2021/2023/2026 jsou `[DATA GAP]` (ceníky blokovány) – hypotéza H3.2 o dražším účtu ČS zůstává neověřena. Implikace: konkurence se přesouvá z měsíčního poplatku (konverguje k nule) k tomu, co je v „balíčku" (počet plateb zdarma, karty, FX, kontokorent) a k úročení zůstatků.

### 5. Vklady podnikatelů jsou největší složkou revenue poolu a zároveň nejzranitelnější: komerční klienti Moneta přesunuli za tři roky ~9 pb vkladů z běžných na úročené účty
Podíl spořicích a termínovaných vkladů na komerčních vkladech Moneta vzrostl ze 42,6 % (4Q 2022) na 51,4 % (3/2026) `[FACT]`; běžné účty přitom rostly jen z 43,4 na 52,8 mld. Kč, zatímco úročené z 32,5 na 55,8 mld. Kč `[FACT]`. Ve středním scénáři revenue poolu tvoří depozitní marže ≈ 5 mld. Kč (34 %) a ±1 pb marže mění pool o ±3,5 mld. Kč `[EST]`. Při repo 3,75 % je neúročený běžný účet podnikatele nejvýnosnější „produkt" segmentu; každé procento zůstatků přesunuté na spořicí účet konkurence (Creditas, Trinity, Fio, Air Bank – sazby `[DATA GAP]`) tuto marži eroduje.

### 6. Revenue pool segmentu je řádově 15 mld. Kč (8–25) ročně – ekvivalent ~25 % provozních výnosů ČS – ale bez ČNB jmenovatelů je odhad ±40 %
Parametrický model (Exhibit 6) dává střední hodnotu ≈ 15 mld. Kč: úvěry 6,3 (41 %), vklady 5,3 (34 %), poplatky 3,9 (25 %) `[EST]`. Kotva Moneta: celý Commercial segment (vč. SME a korporací) generuje 4,8 mld. Kč provozních výnosů při 125 tis. klientech a 92,6 mld. Kč úvěrů (FY 2024) `[FACT]`, tj. ≈ 38 tis. Kč na klienta; KB naopak inkasuje transakční + depozitní poplatky jen ≈ 1,35 tis. Kč na průměrného klienta `[EST – dopočet]` – fee-ARPU čistého small business leží mezi tím (2–5 tis. Kč). Provozní výnosy ČS FY 2025 činily 59,2 mld. Kč `[FACT]`; pokud by ČS držela v segmentu podíl odpovídající její velikosti (~20 % aktiv sektoru `[FACT – snippet thebanks.eu]`), znamenal by segment ≈ 3 mld. Kč jejích výnosů `[EST – ilustrace, nikoli měření]`.

### 7. Velké banky v segmentu nerostou počtem klientů: KB má šest let konstantních ~242 tis. ne-fyzických klientů; ČS segment vůbec nereportuje – transparentnost je sama o sobě konkurenční signál
Počet klientů KB mimo fyzické osoby (podnikatelé, firmy, veřejný sektor) byl 257 tis. (2019), 252 tis. (2020) a poté 241–244 tis. každý rok 2021–2026 `[EST – dopočet z FACT]`, přestože celkový počet klientů KB vzrostl o 173 tis. (2021→1Q 2026) `[FACT]`. Moneta vykázala růst komerčních klientů 93,5 → 125 tis. (2016→~2022, +34 %) `[FACT – snippet]`, novější číslo `[DATA GAP]`. ČS ve fact sheetu neuvádí ani počet podnikatelů, ani objem úvěrů small business (segment je v Erste reportingu součástí Retail jako „micros") `[FACT – absence dat]`. Tržní podíly na účtech tedy nelze bez průzkumů (`[DATA GAP]`) měřit; jediný tvrdý závěr je, že u KB stagnuje čitatel, zatímco počet subjektů v ekonomice (WS1) roste – podíl velkých bank na subjektech s vysokou pravděpodobností klesá `[EXTRAP]`.

---

## (d) So what pro Českou spořitelnu
1. **Změřit vlastní pozici dřív, než ji změří trh.** ČS jako jediná z velké čtyřky nereportuje small business ani interně srovnatelně s KB („Loans to small businesses") a Monetou (Commercial/SB). Prvním krokem je interní datová kotva: počet aktivních podnikatelských klientů (FOP/PO do 25 mil. Kč), úvěry, vklady (běžné vs. úročené), poplatky – a jejich poměr k ČNB sektorovým řadám (živnostníci; nové obchody do 7,5 mil. Kč), jakmile bude ARAD dostupný.
2. **Bránit depozitní marži, ne měsíční poplatek.** Vklady jsou ~1/3 revenue poolu a Moneta ukazuje odliv ~9 pb komerčních zůstatků na úročené produkty za 3 roky. ČS by měla mít segmentovanou nabídku úročení (např. tiered spořicí účet pro podnikatele s podmínkou aktivního transakčního účtu), aby udržela primární vztah, místo aby ztrácela celé zůstatky ke challengerům.
3. **Rychlý nezajištěný úvěr jako akviziční produkt.** Moneta zdvojnásobila nové SB splátkové úvěry za dva roky při téměř nulových nákladech rizika; KB po pěti letech stagnace roste s KB+. Při sazbách 5–5,5 % nad levným vkladovým fundingem je jednotková ekonomika atraktivní. ČS s 4,6 mil. klientů má největší předschválitelnou bázi FOP (existující osobní účty živnostníků) – cross-sell z retailu je levnější než akvizice.
4. **Cenová architektura „0 Kč základ + placená hodnota".** RB a UniCredit potvrzují, že bezpoplatkový vstupní účet je standard i u velkých bank. ČS by měla ověřit vlastní ceník proti Exhibitu 4 (po doplnění) a přesunout monetizaci do balíčků (platby, FX, karty, kontokorent) a do úročení – nikoli držet vyšší fixní poplatek, který je nejviditelnější a nejsnáze srovnatelný atribut.
5. **Doplnit chybějící evidenci do 30 dnů:** ARAD řady (úvěry/vklady/NPL živnostníci a nefinanční podniky 2019–2026; sazby nových úvěrů do 7,5 mil. Kč a živnostníkům), ceníky 9 bank + Revolut/Wise (2021 přes web.archive.org, 2023, 2026), výroční zprávy 2025 (ČS, ČSOB, RB, Fio, Air Bank, Creditas – počty podnikatelských klientů), průzkumy SME Banking Club / Datank / Ipsos (NPS, hlavní banka). Bez toho zůstávají Exhibity 1, 2, 4, 5 a 7 rámcem, nikoli měřením.

---

## (e) Zdroje (přístup 2026-09-08/09)
Primární – lokální investorské soubory (repozitář `bank_peers`):
- Komerční banka, Facts & Figures 1Q 2026 (`KB-Facts-and-Figures-2026-1Q.xlsx`; listy Business, NFC structure, NIM, Ratios) – veřejně: https://www.kb.cz/cs/o-bance/vztahy-s-investory
- ČSOB, Fact sheet 1Q 2026 (`csob-fact-sheet.xlsx`; listy Business volumes, Additional information, P&L Ytd.) – veřejně: https://www.csob.cz/portal/o-csob/vztahy-s-investory
- MONETA Money Bank, Basic financial data 4Q 2024 a 1Q 2026 (`mmb-4q2024-basic-financial-data.xlsx`, `mmb-1q2026-basic-financial-data.xlsx`) – veřejně: https://investors.moneta.cz/financial-results
- Česká spořitelna, Key figures Q1 2026 (`key_figures_q1_2026.xlsx`, `data/cs_financials.db`), peer PDF (`config/manual/cs_pdf.csv`, `peer_adjusted.csv`) – veřejně: https://www.csas.cz/cs/o-nas/pro-investory
Sekundární – nalezeno pouze přes WebSearch snippety (plný text nenačten, proxy blokace):
- ČNB, Měnová statistika 12/2024 a 1/2025 (tempa růstu úvěrů): https://www.cnb.cz/export/sites/cnb/cs/statistika/.galleries/menova_bankovni_stat/menova_stat_publ/2025/menstat_2025-01_CZ.pdf ; přehled publikací: https://www.cnb.cz/cs/statistika/menova_bankovni_stat/publikace-menove-statistiky/ ; anglické verze 2026 (1/2026, 4/2026, 5/2026): https://www.cnb.cz/export/sites/cnb/en/statistics/.galleries/money_and_banking_stat/mon_bank_stat/2026/menstat_2026-05_EN.pdf
- ČNB ARAD: https://www.cnb.cz/cs/statistika/arad-system-casovych-rad/ ; Bankovní statistika: https://www.cnb.cz/cs/statistika/menova_bankovni_stat/bankovni-statistika/bankovni-statistika/ ; Komentář k úrokovým sazbám MFI: https://www.cnb.cz/cs/statistika/menova_bankovni_stat/harm_stat_data/komentar-k-urokovym-sazbam-menovych-financnich-instituci/index.html
- ČNB, Zpráva o finanční stabilitě – jaro 2025: https://www.cnb.cz/export/sites/cnb/cs/financni-stabilita/.galleries/zpravy_fs/fs_2025_jaro/zfs_jaro_2025.pdf ; podzim 2025: https://www.cnb.cz/export/sites/cnb/cs/financni-stabilita/.galleries/zpravy_fs/fs_2025_podzim/zfs_podzim_2025.pdf
- ČNB cnblog „Trendy v zadluženosti (nejen) nefinančních podniků": https://www.cnb.cz/cs/o_cnb/cnblog/Trendy-v-zadluzenosti-nejen-nefinancnich-podniku/
- ČNB FAQ „Jak se vyvíjela dvoutýdenní repo sazba ČNB?": https://www.cnb.cz/cs/casto-kladene-dotazy/Jak-se-vyvijela-dvoutydenni-repo-sazba-CNB/ ; rozhodnutí bankovní rady: https://www.cnb.cz/cs/menova-politika/br-zapisy-z-jednani/
- Fio banka, „ČNB zvýšila 2T repo sazbu o 25 bb na 3,75 %" (6/2026): https://www.fio.cz/zpravodajstvi/zpravy-z-burzy/325769-cr-cnb-zvysila-2t-repo-sazbu-o-25-bazickych-bodu-na-3-75-v-souladu-s-ocekavanim ; „ČNB ponechala 2T repo sazbu na 3,75 %" (8/2026): https://www.fio.cz/zpravodajstvi/zpravy-z-burzy/327740-cr-cnb-v-souladu-s-ocekavanim-ponechala-2t-repo-sazbu-na-3-75 ; behounek.eu: https://www.behounek.eu/l/cnb-urokove-sazby/
- Kurzy.cz, „Úrokové sazby měnových finančních institucí v ČR – srpen 2025": https://zpravy.kurzy.cz/831779-urokove-sazby-menovych-financnich-instituci-v-cr-srpen-2025/
- ČBA Monitor: „Bankovní statistika za září 2023" (NPL živnostníci 5,10 %): https://www.cbamonitor.cz/aktuality/bankovni-statistika-za-zari-2023 ; „Nové úvěry nefinančním podnikům": https://www.cbamonitor.cz/statistika/nove-uvery-nefinancnim-podnikum ; „Úroková sazba nové úvěry": https://www.cbamonitor.cz/statistika/uroky-nove-uvery
- Finmag, „Podnikatelské účty 2026: přehled výhod, poplatků a nabídek bank": https://www.finmag.cz/finance/485143-podnikatelske-ucty-2026-vyplati-se-vam-prehled-vyhod-poplatku-a-nabidek-bank
- MONETA, TZ „Od vstupu na burzu MONETA dosáhla 34% růstu v počtu komerčních klientů": https://www.moneta.cz/servis-pro-media/tiskove-zpravy/detail/od-vstupu-na-burzu-moneta-dosahla-34-rustu-v-poctu-komercnich-klientu-podil-na-tom-ma-digitalizace-produktove-nabidky-i-spoluprace-s-podpurnymi-programy
- ČTK/České noviny, „České spořitelně stoupl v 1. pololetí 2025 čistý zisk…" (4,6 mil. klientů): https://www.ceskenoviny.cz/zpravy/2704339
- thebanks.eu, profil ČSOB (podíl na aktivech 20,5 %, ČS ~19,7 %): https://thebanks.eu/banks/10959
- Peníze.cz, „Největší banky v Česku – žebříčky 2025": https://www.penize.cz/osobni-ucty/481422-nejvetsi-banky-v-cesku-zebricky-podle-klientu-i-penez-2025 (nenačteno)
K doplnění (blokováno): TOP.cz srovnání podnikatelských účtů 8/2026 (https://www.top.cz/nejlepsi-podnikatelske-ucty-srovnani), Banky.cz (https://www.banky.cz/prehled-a-porovnani/podnikatelsky-ucet/), Finex.cz, Finparáda (https://www.finparada.cz/), Měšec (https://www.mesec.cz/), ceníky bank (URL v `data/ws3_cenovy_benchmark.md`), SME Banking Club (https://www.smebanking.club/), Ipsos ČR (https://www.ipsos.com/cs-cz), HN Nejlepší banka (https://nejbanka.hn.cz/vysledky/), finanční arbitr (https://www.finarbitr.cz/), NRB definice MSP (https://www.nrb.cz/podnikatele/dalsi-informace-pro-podnikatele/mali-a-stredni-podnikatele/).

---

## (f) Log odhadů a mezer
| # | Položka | Typ | Postup / co chybí |
|---|---|---|---|
| 1 | Úvěry živnostníkům (ČNB) 2019–2026, nové úvěry, sazby | `[DATA GAP]` | ARAD sektorové členění; měnová statistika PDF tab. „úvěry domácnostem – živnostníci"; ČBA Monitor |
| 2 | Úvěry malým podnikům dle velikosti podniku | `[DATA GAP]` | ČNB standardně člení podle velikosti **úvěru** (do 7,5 / 7,5–30 / nad 30 mil. Kč) a odvětví; podle velikosti podniku jen v ZFS – ověřit |
| 3 | Vklady živnostníků a nefinančních podniků | `[DATA GAP]` | ARAD „Vklady klientů podle sektorů" |
| 4 | NPL živnostníci / NFP po letech | `[DATA GAP]` mimo 9/2023 (5,10 %) | ARAD, ZFS jaro/podzim 2025, ČBA Monitor |
| 5 | Repo sazba 2019–2025 | `[FACT – neověřeno fetchem]` | hodnoty dle zadání koordinátora; ověřit ČNB FAQ vč. přesných dat změn 2025 |
| 6 | Sazby 7,5–30 mil. Kč 2025 | `[FACT – snippet]` | formulace „v srpnu zvýšila na 5,12 %" nekonzistentní s červnem 5,38 % – ověřit v komentáři ČNB |
| 7 | Cenový benchmark 2021/2023/2026 | `[DATA GAP]` mimo RB a UCB 2026 | ceníky + web.archive.org; RB/UCB údaje jen ze snippetu Finmag – ověřit podmínky |
| 8 | Úročení podnikatelských účtů 2023–24 | `[DATA GAP]` | ceníky Creditas, Trinity, Fio, Air Bank, velké banky; Finparáda |
| 9 | Počet podnikatelských klientů ČS, ČSOB, RB, UCB, Air Bank, Fio, Creditas, Revolut, Wise | `[DATA GAP]` | výroční zprávy 2025, tiskové zprávy; Moneta 125 tis. je ~2022 – aktualizovat |
| 10 | KB ne-fyzičtí klienti 242 tis. | `[EST – dopočet]` | KB celkem − Individual clients; obsahuje korporace, municipality → horní hranice |
| 11 | Jmenovatele trhu pro podíly (150/200/250 mld. Kč úvěrů; 1,0–1,4 mil. subjektů) | `[EST – citlivostní scénáře]` | bez opory v ČNB/WS1 datech; nahradit po doplnění |
| 12 | Revenue pool 8/15/25 mld. Kč | `[EST]` | parametrický model; vstupy úvěry/vklady/účty bez ČNB opory, marže kotveny na Moneta Commercial (nadhodnocuje) a KB (podhodnocuje); ±40 % |
| 13 | Ilustrace „~3 mld. Kč výnosů ČS ze segmentu" | `[EST – ilustrace]` | 20 % × střední pool; není měření podílu ČS |
| 14 | Pokles podílu velkých bank na subjektech | `[EXTRAP]` | stagnace čitatele KB vs. růst počtu subjektů (WS1) |
| 15 | NPS / spokojenost / stížnosti podnikatelů | `[DATA GAP]` | SME Banking Club, Datank, Ipsos, KPMG; FA nepříslušný pro podnikatele |
| 16 | Definice „SME" u ČSOB a „small business" u KB (obratové hranice) | `[DATA GAP]` | výroční zprávy; viz 01_definice |
| 17 | Rozdíl ČS čistých úvěrů 2019 (720,7 vs. 729,2 mld. Kč) mezi DB a Key_figures | poznámka | různé řádky výkazu (loans at amortised cost vs. „Net loans to customers*" vč. FVPL, leasingu a obchodních pohledávek); v Exhibitech použit DB (reported) |
