# ZADÁNÍ PRO CLAUDE DESIGN (v2): deck v Harvard Business Review stylu
## „Small business v ČR 2021–2026: kde Česká spořitelna ztrácí přítok, co dělá Evropa jinak a co udělat v příštích 36 měsících"

> Zadání je samostatné: obsahuje strukturu, styl, texty a všechna data pro každý slide. Zdroj obsahu: `FINAL_small_business_CZ_deep_dive_v2.md` (2. 10. 2026). **Čísla neměň a nedoplňuj.** Kde je `[DATA GAP]`, zobraz prázdné místo (viz styl). Nahrazuje brief v1 (`../small_business_cz/08_zadani_claude_design_deck.md`, hranice 25 mil. Kč) – ten už nepoužívej.

---

## 1. Formát a rozsah
- **Typ:** prezentační deck 16:9 (1920 × 1080 px), každý slide = jeden artboard; řádky canvasu = sekce.
- **Rozsah:** 36 slidů + 3 přílohy (39). Nepřidávej slidy; když se obsah nevejde, zmenši text, ne počet zpráv.
- **Jazyk:** čeština; zkratky EN (NIM, CoR, NPL, ARPU, ARPAC, NPS, RM, KPI) bez překladu. Čísla: tisícové mezery (1 202 860), desetinná čárka, jednotky vždy.
- **Publikum:** CEO a představenstvo. Každý slide čitelný samostatně; headline = závěr s číslem.
- **Export:** PNG i PDF, čitelné černobíle.

## 2. Vizuální styl: Harvard Business Review
**Princip:** článek z HBR převedený do slidů. Hodně bílého prostoru, jedna myšlenka na slide, typografie místo ozdob, grafy v Economist/HBR střihu.

**Typografie**
- Headline: serif s vysokým kontrastem (Tiempos, Playfair Display nebo Source Serif 4), 44–54 px, max 2 řádky.
- Podnadpis: sans (Inter nebo IBM Plex Sans), 20–22 px, šedý, 1–2 věty „so what".
- Tělo 16–18 px; poznámky pod grafem 12–13 px šedě.
- Big number: serif 96–140 px, jedno číslo na slide, krátký label pod ním.

**Barvy**
- Papír #FFFFFF; text #111111; sekundární #6B6B6B; linky #D9D9D9; krémový blok #F4F1EC.
- **ČS vždy tmavě červená #B5121B**; konkurence ČR modrošedá #1F3A5F; evropské benchmarky zelenošedá #4F6F5A; ostatní #8A8A8A. Max 4 barvy v grafu.

**Vizuální kódování jistoty dat (povinné, legenda na slidu 3 a v zápatí každého grafu)**
- `[FACT]` plná barva · `[EST]` šrafování nebo 50 % opacity · `[STALE]` plná barva s tečkovaným obrysem a štítkem „zdroj 03/2026" · `[CLAIM]` kurzíva s ikonou uvozovek · `[DATA GAP]` prázdný obdélník s čárkovaným obrysem a textem „chybí – [zdroj]".

**Layouty**
- L1 headline + jeden graf (graf 60 % vlevo, 3 body vpravo) · L2 big number · L3 tabulka HBR (jen vodorovné linky, řádek ČS podbarven krémově) · L4 dvě až tři karty proti sobě · L5 matice 2×2 / heat-map · L6 pull quote (krémový pruh, serif italic 36 px) · L7 timeline / Gantt.
- Horní lišta: název sekce malými kapitálkami vlevo, číslo slidu vpravo. Zápatí: „Zdroj: … · značka" 12 px.

**Grafy:** bez 3D, stínů a rámečků; popisky přímo u dat; sloupce od nuly; jen vodorovné gridlines; chybějící data nikdy neinterpolovat.

---

## 3. Struktura (39 slidů) – texty a data

### SEKCE 0 – Otevření (1–5)

**Slide 1 – Titulní (L6).** „Segment small business v České republice 2021–2026" · podtitul „Konkurenční benchmark Česká spořitelna vs. trh · evropská gap analýza · plán na 36 měsíců" · řádek „FOP + PO s ročním obratem do 50 mil. Kč · 2. října 2026".

**Slide 2 – Executive summary (L3, 10 řádků).** Headline: „Segment roste a ekonomika se přesouvá k rychlému úvěru, nulovému účtu a integracím – ČS drží stock, přítok jde jinam."
| # | Zjištění | Číslo | Značka |
|---|---|---|---|
| 1 | Segment roste | 1 202 860 OSVČ (6/2026); 594 520 firem | FACT |
| 2 | Růst táhne vedlejší činnost a nové s.r.o. | vedlejší +16 tis. y/y; 34 621 nových s.r.o. 2025 (max za 20 let) | FACT |
| 3 | Riziko se rozpojilo | bankroty FOP 1H 2026 0 %; konkurzy PO +9 %, návrhy +22 % | FACT |
| 4 | 50 mil. Kč = EU mikropodnik | 2 mil. EUR × 24,26 = 48,5 mil. Kč | FACT/EST |
| 5 | Úvěry rostou u fokusovaných bank | Moneta +27,5 %, ČSOB SME +11,1 %, KB +6,9 %, ČS SME +5,2 % | FACT |
| 6 | ČS jediná z velké trojky s podmíněnou cenou | 75 / 45 / 0 Kč vs. 9 z 13 bank 0 Kč | FACT |
| 7 | ČS č. 1 ve Fakturoidu, ale ztrácí u PO | ČS 17 %; Fio 31 % PO; Air Bank 17 % FO | FACT |
| 8 | 2027 = regulatorní zeď | SEPA Instant 1/2027 a 7/2027; AMLR 10. 7. 2027 | FACT |
| 9 | 4 z 5 best practices už běží v Erste | SLSP, Erste AT George Business One | FACT |
| 10 | ČS segment nereportuje | KB a Moneta ano | FACT |

**Slide 3 – Jak číst čísla (L3 malá + legenda).** Headline: „Každé číslo nese značku jistoty – a 176 míst v hlavním textu zůstává prázdných, protože data nejsou veřejná." Legenda pěti značek s vizuálem. Řádek: „Ověřeno z výtahů citovaných zdrojů s URL a datem (2. 10. 2026); plnotextové jsou jen investorské fact sheety KB, ČSOB, Moneta a ČS. Nabídka bank jen ze zdrojů 06/2026+."

**Slide 4 – Pozice ČS (L2 + 3 řádky).** Big number **17 %** (podíl ČS mezi bankami uživatelů Fakturoidu, 30. 9. 2026). Headline: „ČS je nejčastější bankou podnikatelů – a zároveň nejpomaleji rostoucí v jejich úvěrech." Tři řádky: síla (4,6 mil. klientů, 324 poboček, NIM 2,11 %); slabina (podmíněná cena, SME +5,2 %, App Store 3,9); důsledek (stock drží ČS, přítok FOP jde k Air Bank, s.r.o. k Fio a KB, úvěry k Monetě).

**Slide 5 – Rozhodnutí pro CEO (L6 + 2 karty).** Pull quote: „Má být small business řízený segment s vlastní definicí, P&L a cenovou architekturou – nebo zůstane uvnitř retailu s dnešním ceníkem?" Karta A „Program 2027–2029": definice ≤ 50 mil. Kč, 0 Kč + placená hodnota + rychlý úvěr, transfer z Erste SK/AT, P&L páka 0,7–1,3 mld. Kč/rok do 3 let `[EST]`. Karta B „Status quo": přítok nových FOP a mikro-s.r.o. dál k Air Bank, Fio, Monetě.

### SEKCE 1 – Definice (6–7)

**Slide 6 (L3).** Headline: „„Small business" nemá úřední definici; naše hranice 50 mil. Kč odpovídá EU mikropodniku a leží pod bankovními prahy." Tabulka: EU mikro < 10 zam., ≤ 2 mil. EUR ≈ 48,5 mil. Kč · mikro účetní jednotka ≤ 22 mil. Kč obratu · paušální daň ≤ 2 mil. Kč příjmů · ČNB člení úvěry podle objemu (do 7,5 / 7,5–30 / nad 30 mil. Kč), ne podle klienta · KB korporát od 60 mil. Kč · RB kampaň do 100 mil. · ČS Maxi do 100 mil. `[STALE]` · ČSOB SME do 300 mil. · **naše: ≤ 50 mil. Kč, FOP + PO**.

**Slide 7 (L1, 4 horizontální sloupce).** Headline: „Registrace ≠ aktivita: „živnostníků" je 2,03 mil. na papíře a 1,18 mil. reálně." Data (12/2025): RŽP 2 029 257 · ČSÚ RES podnikající FO 2 028 363 · ČSSZ OSVČ 1 178 514 · ČSSZ hlavní 692 402 · paušál 125 449. Callout: rozdíl ~850 tis. neaktivních oprávnění `[EST]`.

### SEKCE 2 – Velikost a struktura (8–12)

**Slide 8 (L1 skládané sloupce 2019–6/2026).** Headline: „OSVČ poprvé přes 1,2 milionu; od 2024 roste hlavně vedlejší činnost." Hlavní / vedlejší (tis.): 2019 598/433 · 2021 634/444 · 2022 649/455 · 2023 669/458 · 2024 681/474 · 2025 692/486 · 6/2026 702/501. Callout: podíl hlavní činnosti na přírůstku 85 % (2021) → 45 % (1H 2026) `[EST]`. Zdroj: ČSSZ via Podnikatel.cz `[FACT]`.

**Slide 9 (L1 sloupce toků).** Headline: „Vznik akceleruje, zánik klesá: 19 nových FOP na 10 zaniklých v 1H 2026, nejvíce za 8 let." FOP 2025 ~84 tis. vznik / ~49 tis. zánik; 1H 2026 51 534 / 27 300. PO 2025 34 621 / 16 853; 1H 2026 15 498 / 7 796. Zdroj: CRIF, D&B `[FACT]`.

**Slide 10 (L2).** Big number **30 %**. Label: „podíl cizinců na nových FOP (26 535 v 2025)". Headline: „Třetina přítoku FOP jsou cizinci – Ukrajinci tvoří 38 % cizích živnostníků." Vpravo: UA 37,8 % (73 699), SK 16,8 %, VN 16,1 %; stock ~10 % OSVČ. Zdroj: D&B via BusinessInfo `[FACT]`.

**Slide 11 (L1 řada).** Headline: „Paušální daň: 125 449 OSVČ bez daňového přiznání, +10 % ročně." 1. pásmo: 2022 63 413 · 2023 77 410 · 2024 97 512 · 2025 110 854 · 2026 120 114. Platba 1. pásma 9 984 Kč → 9 162 Kč od 7/2026. Zdroj: Finanční správa `[FACT]`.

**Slide 12 (L4, 3 karty).** Headline: „Adresovatelný trh ≈ 1,18 mil. subjektů – a pro bankovní vztah má každá skupina jinou logiku." Karta „Hlavní OSVČ 701 819 – jádro pro úvěr a cash management" · „Vedlejší OSVČ 501 041 – retail s IČO, účet bez bankéře" · „Aktivní PO ≈ 475 tis. `[EST]` – podíl s obratem ≤ 50 mil. Kč `[DATA GAP: ČSÚ SBS]`".

### SEKCE 3 – Kondice (13–15)

**Slide 13 (L1 dva panely).** Headline: „Riziko se rozpojilo: bankroty živnostníků stagnují, konkurzy firem jsou na 9letém maximu." FOP: 2025 6 213 (+16 %); 1H 2026 3 260 (0 %), návrhy −2 %. PO: 2025 746 (max od 2018); 1H 2026 418 (+9 %), návrhy 678 (+22 %); 1–8/2026 538. Callout: krachují hlavně firmy s tržbami do 30 mil. Kč. Zdroj: CRIF `[FACT]`; 2024 `[EST]`.

**Slide 14 (L7 timeline 2021–2026).** Headline: „Šest let ve dvou šocích: inflace 2022–23 a odvody 2024–26; ČNB v červnu 2026 sazby znovu zvedla." HDP 4,0 / 2,8 / 0,0 / 1,3 / 2,6 % (2021–25); inflace 3,8 / 15,1 / 10,7 / 2,4 / 2,5 %; repo 3,50 % (2025) → 3,75 % (18. 6. 2026). Min. záloha soc. 5 720 → 5 005 Kč od 7/2026; zdrav. 3 306 Kč. Repo 2021–2024 `[DATA GAP]`. Zdroj: ČSÚ, ČNB, ČSSZ `[FACT]`.

**Slide 15 (L2 + body).** Big number **25 %**. Label: „podniků se za 3 roky pokusilo o externí financování (AMSP, datum neznámé)". Headline: „Bariérou úvěru je proces a postoj, ne nabídka." Body: > 1/3 úvěr odmítá; 34 % živnostníků financuje byznys osobní půjčkou; 61,8 % firem platí včas (2024); ČLFA podnikatelé 120,5 mld. Kč 1H 2026 (+9 %); factoring 172 mld. Kč (+8,5 %); NRB záruky 25,9 mld. Kč (2025). `[FACT]`

### SEKCE 4 – Bankovní trh ČR (16–23)

**Slide 16 (L1 vodorovné sloupce y/y).** Headline: „Úvěry segmentu rostou tam, kde se banka zaměřila; ČS roste pod vlastním skupinovým tempem." Moneta živnostníci + malé firmy +27,5 % (23,4 mld. Kč) · ČSOB SME +11,1 % (120,1 mld.) · KB small business +6,9 % (51,2 mld.) · ČS SME +5,2 % (objem `[DATA GAP]`) · ČS skupina celkem +9,5 % jako tečkovaná referenční linka. Poznámka: definice se liší (ČSOB do 300 mil. Kč). `[FACT]`

**Slide 17 (L1 sloupce čtvrtletí).** Headline: „Moneta zdvojnásobila nové small-business úvěry za dva roky při nulových nákladech rizika." Nové splátkové úvěry (mil. Kč): Q1 2024 1 323 · Q2 1 544 · Q3 1 394 · Q4 2 101 · Q1 2025 1 781 · Q2 2 213 · Q3 1 964 · Q4 2 399 · Q1 2026 2 138. NPL Commercial 0,9 %; impairment Commercial Q1 2026 +22 mil. Kč. Zdroj: Moneta IR `[FACT]`.

**Slide 18 (L3, řádek ČS zvýrazněn).** Headline: „9 ze 13 bank má účet za 0 Kč bez podmínek; ČS je jediná z velké trojky s podmíněnou cenou." Řádky (základní / další tarify · datum): ČS Živnostník 75 / 45 / 0 Kč podmíněně, Klasik 0 Kč s výhradou, Maxi 399 Kč · 1. 7. 2026 `[FACT]` · KB 0 / 39 / 89 / 499 Kč `[STALE 03/2026]` · ČSOB 0 Kč online / 129 Kč `[STALE]` · RB 0 / 99 / 299 Kč · 8/2026 `[FACT]` · Moneta 0 Kč + 5 % cashback `[STALE]` · UCB 0 / 150 / 350 Kč `[STALE]` · Air Bank 0 Kč + 1 % cashback `[STALE]` · Fio 0 Kč + 2,7 % úrok · 8/2026 `[FACT]` · Creditas 0 Kč · 7/2026 `[FACT]`. Ceny 2021 `[DATA GAP]`. Pozitivum ČS: 2 roky zdarma pro nové firmy + startovací KTK 20–100 tis. Kč.

**Slide 19 (L1 skládané sloupce FO / PO).** Headline: „ČS vede u živnostníků, u firem ji předbíhá Fio, KB i RB." Fakturoid 30. 9. 2026 (FO / PO): ČS 17 / 13 · Air Bank 17 / 3 · ČSOB 16 / 12 · RB 14 / 17 · Fio 10 / 31 · KB 11 / 14 · Moneta 8 / 5. Poznámka: vzorek digitálně zdatných uživatelů, ne celý trh. `[FACT]`

**Slide 20 (L4, 3 karty).** Headline: „V rychlém úvěru určuje standard Moneta; ČS nezveřejňuje sazbu ani čas rozhodnutí." Moneta: 600 tis. Kč online do 15 min, 2,5 mil. bez zajištění, garance sazby `[STALE]` · KB: 1 mil. Kč bez dokládání příjmů `[STALE]` · ČS: 500 tis. Kč, start-up 600 tis. fix 9 % `[STALE]`, sazba a čas `[DATA GAP]`. Trh: nové úvěry do 7,5 mil. Kč 6,29 % (7/2026) při repo 3,75 % `[FACT]`.

**Slide 21 (L3 skóre 1–5, barevná škála).** Headline: „Benchmark sedmi dimenzí: ČS vyhrává jen v síti." Celkem: Moneta 4,3 · ČSOB 3,9 · KB 3,7 · Air Bank 3,3 · ČS 3,1 · RB 3,0 · Fio 3,0 · UCB 2,4 · Creditas 2,3. Dimenze: cena, digitál, onboarding, úvěry, distribuce, momentum, transparentnost. ČS: 3 / 3 / 3 / 3 / 5 / 3 / 2. Poznámka: skóre = expertní syntéza `[EST]`.

**Slide 22 (L2 + srovnání).** Big number **3,9**. Label: „George Business, App Store CZ (650 hodnocení, 2. 10. 2026)". Headline: „Business aplikace ČS má nejnižší iOS hodnocení z velkých bank." Vedle: ČSOB Smart 4,8 · Smart Banka 4,8 `[CLAIM]` · George Business Google Play 4,6. `[FACT]`

**Slide 23 (L5 mapa skupin; X = šíře nabídky, Y = cenová agresivita a digitální rychlost).** Headline: „Čtyři strategické skupiny – ČS mezi univerzálními lídry s nejnižší cenovou agresivitou." A univerzální lídři (ČS, KB, ČSOB) · B challengeři s úvěrovou hranou (Moneta, RB, UCB) · C digitální transakční banky (Fio, Air Bank, Creditas, mBank, Trinity) · D fintech multi-currency (Revolut, Wise). ČS červeně.

### SEKCE 5 – Trendy (24–25)

**Slide 24 (L7 regulatorní timeline 2026–2035).** Headline: „Rok 2027 je regulatorní zeď – pro největší banku je to výhoda škály." 9. 1. 2027 SEPA Instant příjem · 9. 7. 2027 odesílání + Verification of Payee · 10. 7. 2027 AMLR (remediace portfolia do 2032) · ≈ konec 2027 PSR · 1. 1. 2027 e-fakturace SK · 7/2030 ViDA přeshraniční · 1/2035 ViDA domácí. Vedle: Bank iD 5,3 mil. uživatelů (H1 2026). SEPA Instant dnes nabízí 5 bank bez ČS `[STALE: datum neznámé]`.

**Slide 25 (L5 heat-map).** Headline: „Do 2030 rozhodují kanály, ne produkty: e-fakturace, embedded finance a AMLR jsou v pravém horním rohu." Body (pravděpodobnost / dopad): AMLR V/V · ViDA V/V · SEPA Instant V/S · PSR V/S · daně OSVČ V/S · Bank iD V/S · fintech platby V/S · embedded lending S/S · AI pro podnikatele S/S · generační výměna V/S · FIDA S/S (monitor) · ESG pro SME N/N. Fakta: Shoptet Pay 9 mld. Kč 2025 (+55 %); Flowpay ~0,5 mld. Kč kumulativně; Revolut 1,3 mil. uživatelů ČR; AI u bank jen retail (SME funkce nikde). Značka: `[EST]`.

### SEKCE 6 – Evropská gap analýza (26–30)

**Slide 26 (L3 skóring trhů).** Headline: „Pět benchmark trhů: Slovensko na prvním místě, protože kombinuje stejnou strukturu a platformu Erste." SK 19 · PL 14 · AT 14 · NL 13 · UK 12 (kritéria: hráči s úspěchem, srovnatelnost, přenositelnost, relevance pro Erste; max 20). Záložní: HU 12, RO 11, DE 11, FR 10.

**Slide 27 (L4, 5 mini-karet trhů).** Headline: „Co měřitelně funguje jinde." UK: Monzo 1 mil. business účtů, 47 % platících, ARPAC £484 · Starling 56 % SME = primární banka. NL: Rabobank úvěr z 13 měsíců transakcí za 5–20 min; Knab > 270 tis. podnikatelů. PL: KSeF e-fakturace od 2/2026; BLIK 2,9 mld. transakcí. AT: Erste George Business One 18 €/měs. s rolemi a účetním exportem. SK: SLSP 0 € navždy, onboarding bez výpisu ze ŽR, George API, George AI od 9/2026. `[FACT]`, Tide 15 % UK SME `[CLAIM]`.

**Slide 28 (L3 gap matice, škála 1–5).** Headline: „ČS má velkou mezeru v šesti z jedenácti dimenzí – žádná z nich není regulatorní." Mezera ČS 4: onboarding PO, monetizace, digitální funkce, lending, integrace, segmentace. Mezera 3: onboarding FOP, data a AI. Mezera 2: obsluha. Mezera 1: ESG. Sloupec „důvod": strategie / organizace / ekonomika.

**Slide 29 (L3 test přenositelnosti).** Headline: „Z 18 praktik prošlo pět s nejvyšším skóre přenositelnosti." Vážené skóre (max 35): úvěr z transakcí 32,0 · George API + e-fakturace 30,5 · daňový pot + placený tier 29,5 · primární banka jako KPI 29,0 · 0 Kč + onboarding bez dokladů 28,5 · George Business One 25,5 · embedded lending přes partnera 25,5 · … BLIK 17,5 · hotovost přes poštu 16,5.

**Slide 30 (L3, 5 řádků).** Headline: „Pět best practices – čtyři z nich už běží uvnitř Erste." BP1 úvěr z transakční historie (NL, Moneta) · BP2 banka v účetním a e-shop SW (SLSP, mBank, Fio) · BP3 daňový pot + placený tier (Monzo, Starling, Mettle) · BP4 first account: 0 Kč + onboarding bez dokladů + s.r.o. online (SLSP, Air Bank) · BP5 George vs. George Business One + KPI primární banka (Erste AT, Starling). Sloupce: důkaz · vazba na SWOT · dopad `[EST]` · náročnost.

### SEKCE 7 – SWOT a big bets (31–33)

**Slide 31 (L5 SWOT 2×2, ikona dopadu V/S/N).** Headline: „Síla ČS je v bázi, fundingu a platformě; slabina v ceně, viditelnosti a rychlosti." S: 4,6 mil. klientů, 324 poboček · NIM 2,11 % · č. 1 ve Fakturoidu · George s hotovými praktikami v SK/AT. W: podmíněná cena · segment nereportován · SME +5,2 % · bez ekosystému · App Store 3,9 · PO 13 %. O: přítok 120 tis. subjektů/rok · účet jako jediný zdroj dat · úvěrový tok „contestable" · cizinci 30 % · regulace 2027. T: Air Bank 65 tis. účtů · Moneta +27,5 % · Fio 31 % PO · embedded lending · konkurzy PO +22 % návrhů · eroze depozitní marže.

**Slide 32 (L5 TOWS 2×2).** Headline: „Čtyři směry: úvěr z dat, first account, faktura → platba → financování, segment jako řízená jednotka." SO / ST / WO / WT po 3 bodech (texty z dokumentu kap. 7.2).

**Slide 33 (L3 big bets + no-regret).** Headline: „Pět big bets s řádovou velikostí – a tři kroky bez lítosti na tento kvartál." BB1 předschválený úvěr: kniha +15–25 mld. Kč do 3 let, NII 0,5–1,0 mld. Kč/rok · BB2 0 Kč + daňový pot + tier: 40–85 mil. Kč/rok · BB3 banka v SW + e-fakturace: 20–30 tis. klientů/rok · BB4 first account: 30–36 tis. klientů/rok · BB5 George Business One + nástupnictví: 50–100 mil. Kč/rok. Vše `[EST]`. No-regret: definice a reporting segmentu · zveřejnit sazbu a čas úvěru, limit 1 mil. Kč online · Živnostník 0 Kč bez podmínek.

### SEKCE 8 – Plán (34–36)

**Slide 34 (L3, 3 sloupce horizontů).** Headline: „Plán ve třech horizontech: 8 rychlých kroků, 7 projektů, 4 strukturální sázky." Quick 0–6 m: reporting · 0 Kč · úvěr do 1 mil. online · daňový pot MVP · SEPA Instant · Fakturoid API · interní data + research · early-warning PO. Mid 6–18 m: předschválený úvěr · placený tier · online s.r.o. · George Business One · app ≥ 4,5 · Shoptet · Hey George pro podnikatele. Long 18–36 m: e-fakturační hub · embedded platforma · nástupnictví · AI obsluha + RM pool.

**Slide 35 (L7 Gantt Q1 2027 – 2029).** Headline: „Roadmap: první viditelné změny pro klienty v Q2 2027, plný úvěrový produkt v Q4 2027." Řádky a milníky přesně podle tabulky 8.2 v dokumentu (● milník, ■ realizace, ○ příprava).

**Slide 36 (L3 KPI dashboard).** Headline: „Devět KPI řídí program – pět z nich nemá dnes veřejný baseline." K1 přírůstek klientů · K2 podíl na nových registracích (cíl 25–30 %) · K3 primární účty (+10 p.b.) · K4 nová produkce úvěrů (+25 % y/y, ≤ 15 min, ≥ 60 % auto) · K5 digitální onboarding (FOP 85 %, PO 70 %) · K6 konverze na tier (15–25 %) · K7 App Store (3,9 → ≥ 4,6) · K8 Fakturoid (17/17/13 → 19/19/17 %) · K9 CoR ≤ 0,5 %. Baseline `[DATA GAP]` vizualizuj prázdnou buňkou.

### PŘÍLOHA (37–39)
**Slide 37 (L3).** „Příloha A: primární IR řady 2019–1Q 2026" – ČS pobočky 463 → 324, NIM 2,12 → 2,11 %, NPL 1,8 → 1,5 %; KB small business úvěry 45,9 (2020) → 51,2 mld. Kč; KB pobočky 342 → 172; Moneta Commercial úvěry 82,8 (2022) → 109,1 mld. Kč; ČSOB SME 105,2 (12/2024) → 120,1 mld. Kč. `[FACT]`
**Slide 38 (L3).** „Příloha B: co chybí a kde to dohledat" – 12 řádků z kap. 9.1.
**Slide 39 (L3 malá).** „Příloha C: zdroje a metodika" – IR fact sheety, ČSSZ, ČSÚ, ČNB, CRIF, D&B, Fakturoid, weby bank, evropské výroční zprávy; metodická výhrada jedním odstavcem.

---

## 4. Pravidla, která nesmíš porušit
1. Žádné nové ani zaokrouhlené číslo nad rámec zadání; chybějící = čárkovaný obdélník „[DATA GAP]".
2. Značka jistoty na každém slidu; `[EST]`, `[STALE]` a `[CLAIM]` vizuálně odlišené.
3. Headline = tvrzení s číslem, nikdy popis.
4. Jedna myšlenka na slide: 1 graf + 3 body, nebo 1 tabulka, nebo 1 big number.
5. ČS červeně, konkurence ČR modrošedě, evropské benchmarky zelenošedě, ostatní šedě.
6. Nepoužívej logo ani brand ČS ani jiných bank; deck je nezávislý benchmark.
7. Zdroj na každém slidu ve formátu „Zdroj: … · značka".
8. Zachovej pořadí slidů a čísla sekcí.

## 5. Kontrolní seznam před odevzdáním
- [ ] 39 artboardů 1920 × 1080, seřazených po sekcích.
- [ ] Každý headline je tvrzení s číslem; každý slide má zdroj a značku.
- [ ] Všechny `[DATA GAP]` jsou viditelné; `[STALE]` ceny mají štítek s datem.
- [ ] Řádek a série ČS vždy červeně; v tabulkách podbarven.
- [ ] Grafy bez legend tam, kde lze popsat série přímo; sloupce od nuly.
- [ ] Export PNG + PDF; kontrola v černobílém náhledu.
