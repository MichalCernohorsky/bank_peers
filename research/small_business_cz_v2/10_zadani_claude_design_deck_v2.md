# ZADÁNÍ PRO CLAUDE DESIGN (v2): deck v Harvard Business Review stylu – ČÁST A executive summary + ČÁST B detail
## „Small business v ČR 2021–2026: kde Česká spořitelna ztrácí přítok, co dělá Evropa jinak a co udělat v příštích 36 měsících"

> Zadání je samostatné: obsahuje strukturu, styl, texty a všechna data pro každý slide. Zdroj obsahu: `FINAL_small_business_CZ_deep_dive_v2.md` (2. 10. 2026). **Čísla neměň, nezaokrouhluj a nedoplňuj.** Kde je `[DATA GAP]`, zobraz prázdné místo (viz styl). Nahrazuje brief v1 (`../small_business_cz/08_zadani_claude_design_deck.md`, hranice 25 mil. Kč) – ten už nepoužívej; z v1 se nepřebírá žádné číslo.

---

## 1. Co máš vytvořit
Jeden projekt v Claude Design se **dvěma samostatně exportovatelnými částmi**:

| Část | Účel | Rozsah | Kdo ji čte |
|---|---|---|---|
| **A – Executive summary deck** | Stejná logika jako deck v1: příběh od segmentu přes trh a pozici ČS k rozhodnutí CEO, jedna myšlenka na slide. Navíc obsahuje nové bloky v2: Evropa, 5 best practices, plán ve třech horizontech, KPI. | **16 slidů** (A01–A16) | CEO, představenstvo; 20–25 minut |
| **B – Detailní deck** | Kompletní obsah dokumentu v2: definice a mapování, WS1–WS7, otevřené otázky, přílohy včetně QA. Každá kapitola: hypotézy → data → zjištění → „so what". | **78 slidů** (B01–B78) | management segmentu, strategie, pracovní týmy; čtení i příloha k rozhodnutí |

- Na canvasu: **řádek 1 = Část A**, další řádky = sekce Části B (jedna sekce na řádek).
- Číslování slidů: `A01…A16` a `B01…B78`. V Části A ukaž v zápatí odkaz na detail („Detail: B23–B25"), aby čtenář věděl, kde hledat podklad.
- Export: Část A a Část B zvlášť jako PDF i PNG; plus jeden spojený PDF (A + B).

## 2. Formát
- 16:9, 1920 × 1080 px, každý slide = jeden artboard.
- Čeština; zkratky EN (NIM, CoR, NPL, ARPU, ARPAC, NPS, RM, KPI, API, KYC/KYB) bez překladu. Čísla: tisícové mezery (1 202 860), desetinná čárka, jednotky vždy.
- Každý slide čitelný samostatně; headline = závěr s číslem, ne popis.
- Nepřidávej ani neubírej slidy; když se obsah nevejde, zmenši text nebo tabulku, ne počet zpráv. U tabulkových slidů Části B je v pořádku hustší sazba (tělo 14 px).
- Musí být čitelné i černobíle.

## 3. Vizuální styl: Harvard Business Review
**Princip:** článek z HBR převedený do slidů. Hodně bílého prostoru, typografie místo ozdob, grafy v Economist/HBR střihu. Část A je vzdušnější (big numbers, jeden graf), Část B je „exhibit" styl (tabulka nebo graf + 3 body + zdroj).

**Typografie**
- Headline: serif s vysokým kontrastem (Tiempos, Playfair Display nebo Source Serif 4), 44–54 px (Část B 36–44 px), max 2 řádky.
- Podnadpis: sans (Inter nebo IBM Plex Sans), 20–22 px, šedý, 1–2 věty „so what".
- Tělo 16–18 px (tabulky v Části B 13–14 px); poznámky pod grafem 12–13 px šedě.
- Big number: serif 96–140 px, jedno číslo na slide, krátký label pod ním.

**Barvy**
- Papír #FFFFFF; text #111111; sekundární #6B6B6B; linky #D9D9D9; krémový blok #F4F1EC.
- **ČS vždy tmavě červená #B5121B**; konkurence ČR modrošedá #1F3A5F; evropské benchmarky zelenošedá #4F6F5A; ostatní #8A8A8A. Max 4 barvy v grafu.
- Horizonty plánu: Quick 0–6 m #B5121B, Mid 6–18 m #1F3A5F, Long 18–36 m #4F6F5A.

**Vizuální kódování jistoty dat (povinné; legenda na A03 a B02 a v zápatí každého grafu)**
- `[FACT]` plná barva · `[EST]` šrafování nebo 50 % opacity · `[STALE]` plná barva s tečkovaným obrysem a štítkem s datem zdroje (např. „zdroj 03/2026") · `[CLAIM]` kurzíva s ikonou uvozovek · `[DATA GAP]` prázdný obdélník s čárkovaným obrysem a textem „chybí – [zdroj]" · `[TARGET TBD]` (jen KPI) prázdná buňka s tečkou.

**Layouty**
- L1 headline + jeden graf (graf 60 % vlevo, 3 body vpravo) · L2 big number · L3 tabulka HBR (jen vodorovné linky, řádek ČS podbarven krémově) · L4 dvě až pět karet vedle sebe · L5 matice 2×2 / heat-map · L6 pull quote (krémový pruh, serif italic 36 px) · L7 timeline / Gantt · **L8 profil** (Části B: levý sloupec „fakta" s ikonami, pravý sloupec „co funguje / co z toho plyne") · **L9 so-what box** (krémový panel s 3–5 číslovanými body, používá se jako poslední slide každé sekce Části B).
- Horní lišta: název části a sekce malými kapitálkami vlevo („B · 4 BANKOVNÍ TRH"), číslo slidu vpravo. Zápatí: „Zdroj: … · značka" 12 px.

**Grafy:** bez 3D, stínů a rámečků; popisky přímo u dat; sloupce od nuly; jen vodorovné gridlines; chybějící data nikdy neinterpolovat.

---

## 4. ČÁST A – Executive summary deck (16 slidů)
Logika jako v1 (otevření → segment → kondice → trh a pozice ČS → trendy → strategie → rozhodnutí), rozšířená o nové bloky v2 (Evropa, best practices, plán ve třech horizontech, KPI).

**A01 – Titulní (L6).** „Segment small business v České republice 2021–2026" · podtitul „Konkurenční benchmark Česká spořitelna vs. trh · evropská gap analýza · plán na 36 měsíců" · řádek „Executive summary · FOP + PO s ročním obratem do 50 mil. Kč · 2. října 2026".

**A02 – Executive summary (L3, 10 řádků).** Headline: „Segment roste a ekonomika se přesouvá k rychlému úvěru, nulovému účtu a integracím – ČS drží stock, přítok jde jinam."
| # | Zjištění | Číslo | Značka |
|---|---|---|---|
| 1 | Segment roste | 1 202 860 OSVČ (6/2026); 594 520 obchodních společností | FACT |
| 2 | Růst táhne vedlejší činnost a nové s.r.o. | vedlejší +16 tis. y/y; 34 621 nových s.r.o. 2025 (nejvíce za 20 let); cizinci 30 % nových FOP | FACT |
| 3 | Riziko se rozpojilo | bankroty FOP 1H 2026 3 260 (0 %); konkurzy PO 418 (+9 %), návrhy +22 % | FACT |
| 4 | 50 mil. Kč = EU mikropodnik | 2 mil. EUR × 24,26 = 48,5 mil. Kč; pod KB (korporát od 60 mil.) | FACT/EST |
| 5 | Úvěry rostou u fokusovaných bank | Moneta +27,5 %, ČSOB SME +11,1 %, KB +6,9 %, ČS SME +5,2 % (skupina +9,5 %) | FACT |
| 6 | ČS jediná z velké trojky s podmíněnou cenou | Živnostník 75 / 45 / 0 Kč vs. 9 z 13 bank 0 Kč | FACT |
| 7 | ČS č. 1 ve Fakturoidu, ale ztrácí u PO | ČS 17 %; Fio 31 % PO; Air Bank 17 % FO; George Business iOS 3,9 | FACT |
| 8 | 2027 = regulatorní zeď | SEPA Instant 9. 1. a 9. 7. 2027; AMLR 10. 7. 2027; PSR ≈ konec 2027 | FACT |
| 9 | 4 z 5 best practices už běží v Erste | SLSP 0 € navždy + George API + George AI; Erste AT George Business One 18 €/měs. | FACT |
| 10 | ČS segment nereportuje | KB a Moneta ano; žádná benchmark banka nepublikuje počet SB klientů | FACT |

**A03 – Jak číst čísla (L3 malá + legenda).** Headline: „Každé číslo nese značku jistoty – co není ověřené, zůstává prázdné." Legenda šesti značek (FACT, EST, STALE, CLAIM, DATA GAP, TARGET TBD) s vizuálem. Tři řádky pravidel: (1) „Definice: FOP + PO s ročním obratem do 50 mil. Kč." (2) „Nabídka bank jen ze zdrojů 06/2026 a novějších; starší = `[STALE]` s datem, nevydáváno za současný stav." (3) „Ověřeno z výtahů citovaných zdrojů s URL a datem (2. 10. 2026); plnotextové jsou investorské fact sheety KB, ČSOB, Moneta a ČS; nic z verze 1." Detail: B02.

**A04 – Segment v číslech (L4, 4 big numbers vedle sebe).** Headline: „Adresovatelný trh ≈ 1,18 mil. subjektů a ~120 tis. nových každý rok." Karty: **1 202 860** OSVČ (6/2026; 701 819 hlavních, 501 041 vedlejších) `[FACT]` · **≈ 475 tis.** aktivních PO z 594 520 `[EST]` · **~120 tis.** nových subjektů/rok (~84 tis. FOP + 34 621 PO, 2025) `[FACT]` · **125 449** paušalistů (1/2026, +10 %/rok) `[FACT]`. Pod tím jeden řádek: „Registrace ≠ aktivita: 2,03 mil. FO v RŽP, ale 1,18 mil. pojištěných OSVČ (12/2025)." Detail: B08–B15.

**A05 – Kondice (L1 dva mini panely).** Headline: „Riziko se rozpojilo: bankroty živnostníků stagnují, konkurzy firem jsou na 9letém maximu." FOP: 2025 6 213 (+16 %); 1H 2026 3 260 (0 %). PO: 2025 746 (max od 2018); 1H 2026 418 (+9 %), návrhy 678 (+22 %). Tři body vpravo: „krachují firmy s tržbami do 30 mil. Kč" · „25 % firem se za 3 roky pokusilo o externí financování; 34 % živnostníků financuje byznys osobní půjčkou" · „repo 3,75 % od 18. 6. 2026". Zdroj: CRIF, AMSP, ČNB `[FACT]`. Detail: B16–B22.

**A06 – Úvěry segmentu (L1 vodorovné sloupce y/y).** Headline: „Úvěry segmentu rostou tam, kde se banka zaměřila; ČS roste pod vlastním skupinovým tempem." Moneta +27,5 % (23,4 mld. Kč) · ČSOB SME +11,1 % (120,1 mld.) · KB small business +6,9 % (51,2 mld.) · ČS SME +5,2 % (objem `[DATA GAP]`) · tečkovaná linka ČS skupina +9,5 %. Poznámka: definice se liší (ČSOB SME do 300 mil. Kč). `[FACT]` Detail: B24–B26.

**A07 – Pozice ČS (L2 + 3 řádky).** Big number **17 %** (podíl ČS mezi bankami uživatelů Fakturoidu, 30. 9. 2026). Headline: „ČS je nejčastější bankou podnikatelů – a zároveň nejpomaleji rostoucí v jejich úvěrech." Síla: 4,6 mil. klientů, 324 poboček, NIM 2,11 %. Slabina: podmíněná cena, SME +5,2 %, App Store 3,9, PO jen 13 %. Důsledek: stock drží ČS, přítok FOP jde k Air Bank, s.r.o. k Fio a KB, úvěry k Monetě. Detail: B29, B34.

**A08 – Benchmark bank (L3 skóre 1–5 jako tečkový graf).** Headline: „Benchmark sedmi dimenzí: ČS vyhrává jen v síti a je pátá z devíti." Celkem: Moneta 4,3 · ČSOB 3,9 · KB 3,7 · Air Bank 3,3 · ČS 3,1 · RB 3,0 · Fio 3,0 · UCB 2,4 · Creditas 2,3. Pod grafem: „Cena: 9 z 13 bank 0 Kč bez podmínek; ČS Živnostník 75 / 45 / 0 Kč (ceník 1. 7. 2026)." Skóre = expertní syntéza `[EST]`. Detail: B27, B32.

**A09 – Trendy (L7 timeline 2026–2035, zjednodušená).** Headline: „Rok 2027 je regulatorní zeď – pro největší banku je to výhoda škály." 9. 1. 2027 SEPA Instant příjem · 9. 7. 2027 odesílání + VoP · 10. 7. 2027 AMLR (remediace do 2032) · ≈ konec 2027 PSR · 1. 1. 2027 e-fakturace SK · 7/2030 ViDA přeshraniční · 1/2035 ViDA domácí. Vpravo: „Bank iD 5,3 mil. uživatelů; AI pro podnikatele nemá žádná česká banka." Detail: B39–B44.

**A10 – Evropa: kde se učit (L4, 5 mini karet trhů se skóre).** Headline: „Pět benchmark trhů: Slovensko první, protože kombinuje stejnou strukturu a platformu Erste." SK 19 · PL 14 · AT 14 · NL 13 · UK 12 (max 20). Na každé kartě jedno číslo: SK „SLSP živnostník 0 € navždy" · PL „KSeF e-fakturace od 2/2026" · AT „George Business One 18 €/měs." · NL „úvěr z 13 měsíců transakcí za 5–20 min" · UK „Monzo 47 % platících, ARPAC £484". Pod tím: „ČS má mezeru 4 (z 5) v šesti z jedenácti dimenzí – žádná není regulatorní." Detail: B45–B53.

**A11 – Pět best practices (L3, 5 řádků).** Headline: „Pět best practices – čtyři z nich už běží uvnitř Erste."
| BP | Praktika | Vzor | Řádový dopad `[EST]` |
|---|---|---|---|
| BP1 | Předschválený úvěr z transakční historie, rozhodnutí v minutách | Rabobank/ING (NL), Moneta | kniha +15–25 mld. Kč do 3 let; NII 0,5–1,0 mld. Kč/rok |
| BP2 | Banka v účetním a e-shop SW + příprava e-fakturace | SLSP George API, mBank + KSeF, Fio | 20–30 tis. digitálních klientů/rok |
| BP3 | Daňový „pot" + placený tier s účetním SaaS | Monzo, Starling, Mettle (UK) | 40–85 mil. Kč/rok |
| BP4 | First account: 0 Kč navždy + onboarding bez dokladů + s.r.o. online | SLSP, Air Bank | 30–36 tis. klientů/rok; +60–140 mil. Kč/rok |
| BP5 | Segmentace FOP vs. PO + KPI „primární banka" | Erste AT, Starling | 50–100 mil. Kč/rok |
Detail: B54–B59.

**A12 – SWOT v jednom pohledu (L5 2×2, po 3 bodech).** Headline: „Síla ČS je v bázi, fundingu a platformě; slabina v ceně, viditelnosti a rychlosti." S: 4,6 mil. klientů a 324 poboček · NIM 2,11 % · George s hotovými praktikami v SK/AT. W: podmíněná cena · segment nereportován · SME +5,2 %. O: přítok ~120 tis. subjektů/rok · účet jako jediný zdroj příjmových dat · úvěrový tok „contestable". T: Air Bank >65 tis. účtů · Moneta +27,5 % · Fio 31 % PO. Detail: B60–B64.

**A13 – Big bets a no-regret moves (L3 + 3 karty).** Headline: „Pět big bets s řádovou velikostí – a tři kroky bez lítosti hned." Tabulka BB1–BB5 (název · velikost · horizont): BB1 předschválený úvěr · NII 0,5–1,0 mld. Kč/rok · 12–24 m · BB2 0 Kč + daňový pot + tier · 40–85 mil. Kč/rok · 6–12 m · BB3 banka v SW + e-fakturační hub · 20–30 tis. klientů/rok · 12–36 m · BB4 first account · 30–36 tis. klientů/rok · 6–18 m · BB5 George Business One + nástupnictví · 50–100 mil. Kč/rok · 3–9 m / 24–60 m. Vše `[EST]`. Tři karty no-regret: definice a reporting segmentu · zveřejnit sazbu a čas úvěru, limit 1 mil. Kč online · Živnostník 0 Kč bez podmínek. Detail: B65–B66.

**A14 – Plán ve třech horizontech (L4, 3 sloupce v barvách horizontů).** Headline: „8 rychlých kroků, 7 projektů, 4 strukturální sázky – první změny pro klienty v Q2 2027." Quick 0–6 m (Q1–Q2 2027): reporting · 0 Kč · úvěr do 1 mil. online · daňový pot MVP · SEPA Instant · Fakturoid API · interní data + research · early-warning PO. Mid 6–18 m (Q3 2027 – Q2 2028): předschválený úvěr · placený tier · online s.r.o. · George Business One · app ≥ 4,5 · Shoptet · Hey George pro podnikatele. Long 18–36 m (Q3 2028 – Q4 2029): e-fakturační hub · embedded platforma · nástupnictví · AI obsluha + RM pool. Pod sloupci: „P&L páka programu 0,7–1,3 mld. Kč/rok do 3 let `[EST]`." Detail: B67–B71.

**A15 – KPI, podle kterých se program řídí (L3, 5 vybraných KPI × 6/18/36 m).** Headline: „Devět KPI řídí program – pět z nich dnes nemá veřejný baseline." Řádky: K2 podíl na nových registracích (měřeno → 22 % → 25–30 %) · K4 nová produkce SB úvěrů (+15 % → +25 % y/y, ≤ 15 min → kniha +15–25 mld. Kč) · K5 digitální onboarding (FOP 50 % → FOP 70 % / PO 50 % → FOP 85 % / PO 70 %) · K7 App Store (4,2 → ≥ 4,5 → ≥ 4,6) · K8 Fakturoid celkem / FO / PO (17/17/13 → 18/18/15 → 19/19/17 %). Poznámka: „Baseline K1–K3, K5, K9 se stanoví do konce Q1 2027." Detail: B73.

**A16 – Rozhodnutí pro CEO (L6 + 2 karty + pruh „prvních 6 měsíců").** Pull quote: „Má být small business řízený segment s vlastní definicí, P&L a cenovou architekturou – nebo zůstane uvnitř retailu s dnešním ceníkem?" Karta A „Program 2027–2029": definice ≤ 50 mil. Kč, 0 Kč základ + placená hodnota + rychlý úvěr, transfer z Erste SK/AT, P&L páka 0,7–1,3 mld. Kč/rok do 3 let `[EST]`, obrana podílu 16–20 % u FOP a 13–17 % u PO. Karta B „Status quo": přítok nových FOP a mikro-s.r.o. dál k Air Bank, Fio a Monetě. Pruh dole: „Prvních 6 měsíců: reporting segmentu · Živnostník 0 Kč · úvěr do 1 mil. Kč online se zveřejněnou sazbou · daňový pot · parita ve Fakturoidu · SEPA Instant do 7/2027 · interní data pro business case. Rozhodnutí za 8 týdnů (B76)."

---

## 5. ČÁST B – Detailní deck (78 slidů)
Každá sekce: (1) hypotézy a verdikt, (2) exhibity s daty, (3) so-what box (L9). Čísla a značky přesně podle dokumentu.

### B · 0 OTEVŘENÍ A METODIKA (B01–B03)

**B01 – Titulní a obsah (L6 + seznam).** „Segment small business v ČR 2021–2026 – detailní report" · obsah: 1 Definice a metodika · 2 Velikost a struktura (WS1) · 3 Kondice (WS2) · 4 Bankovní trh ČR (WS3) · 5 Trendy do 2030 (WS4) · 6 Evropská gap analýza (WS5) · 7 SWOT, TOWS, big bets (WS6) · 8 Plán 0–36 měsíců (WS7) · 9 Otevřené otázky · Přílohy A–E.

**B02 – Pravidla ověření (L3 + legenda).** Headline: „Pravidla v2: jen dohledaná čísla, nabídka bank jen od 06/2026, nic z verze 1." Body: definice FOP + PO ≤ 50 mil. Kč · značky FACT / EST / EXTRAP / DATA GAP / STALE / CLAIM s definicí · cut-off 06/2026 pro popis nabídky bank · rozpočet rešerše 190 vyhledávání (2. 10. 2026) · plný text externích stránek nedostupný → FACT = ověřeno ve výtahu zdroje s URL a datem · plnotextové jsou lokální IR fact sheety KB, ČSOB, Moneta, ČS.

**B03 – Struktura práce (L4, 7 karet WS).** Headline: „Sedm workstreamů od definice k plánu." Karty: Definice · WS1 velikost · WS2 kondice · WS3 bankovní trh (9 bank + sekundární vrstva) · WS4 trendy · WS5 Evropa (UK, NL, PL, AT, SK) · WS6 SWOT/TOWS · WS7 plán. Pod každou: hlavní otázka jednou větou.

### B · 1 DEFINICE A MAPOVÁNÍ (B04–B07)

**B04 – Definice v ČR (L3).** Headline: „„Small business" nemá úřední definici; naše hranice 50 mil. Kč odpovídá EU mikropodniku (48,5 mil. Kč, rozdíl 3 %)." Tabulka: EU mikro < 10 zam., ≤ 2 mil. EUR = 48,52 mil. Kč `[EST]` · EU malý < 50 zam., ≤ 10 mil. EUR = 242,6 mil. Kč `[EST]` · EU střední < 250 zam., ≤ 50 mil. EUR · kurz ČNB 24,260 CZK/EUR (30. 6. 2026) · ČNB velký podnik: 2 ze 3 (aktiva > 0,5 mld., obrat > 1 mld., > 250 zam.) · ČNB úvěrová statistika podle objemu úvěru: do 7,5 / 7,5–30 / nad 30 mil. Kč · mikro účetní jednotka obrat ≤ 22 mil. Kč (dříve 18), aktiva ≤ 11 mil. · malá ÚJ obrat ≤ 240 mil. Kč, audit zrušen od 1. 1. 2026 · paušální daň ≤ 2 mil. Kč příjmů · rozhodná částka vedlejší činnosti 117 521 Kč/rok. `[FACT]`

**B05 – Bankovní segmentace (L3, řádek ČS zvýrazněn).** Headline: „Banky segmentují výš: KB < 60 mil., RB a ČS 100 mil., ČSOB 300 mil. Kč – a reportují jen KB, Moneta a ČSOB." Sloupce: banka · segment / produkty · hranice obratu · reporting. ČS: Podnikatelé a malé firmy; Živnostník / Klasik / Maxi; Maxi do 100 mil. Kč `[STALE]`; nereportuje · KB: korporát 60 mil. – 1,5 mld. → SB < 60 mil. `[FACT]`; reportuje Loans to small businesses 51,2 mld. · ČSOB: SME do 300 mil. Kč; reportuje SME loans · RB: kampaň do 100 mil. `[FACT 03/2026]`; nereportuje · Moneta: Small Business uvnitř Commercial, hranice `[DATA GAP]`; reportuje · UCB, Air Bank, Fio, Creditas: hranice `[DATA GAP]`; nereportují.

**B06 – Mapování zdrojů na naši definici (L3).** Headline: „Každý zdroj vymezuje segment jinak – pro sizing platí ČSSZ a KB, ne RŽP a ČSOB." Sloupce: zdroj · jak vymezuje · překryv (Vysoký / Střední / Nízký jako barevný puntík) · korekce. Řádky: ČSSZ OSVČ – vysoký u FOP – adresovatelný trh 1,20 mil., primární vztah 702 tis. · RŽP – nízký jako stock (+80 % vs. aktivní) – nepoužívat stock · ČSÚ RES – střední – oddělit FO/PO · D&B 594 520 PO – vysoký po odečtu spících – aktivní ≈ 475 tis. `[EST]` · MPO MSP 1 341 014 – střední – jen horní mez · EU mikro – vysoký – prakticky ekvivalent · EU malý – nízký (4,9× širší) – nepoužívat · KB SB < 60 mil. – vysoký – použitelné přímo (odchylka ≤ +10 % `[EST]`) · RB / ČS Maxi 100 mil. – střední – „SB + lower mid" · ČSOB SME – nízký–střední – nesrovnávat bez definice · Moneta SB instalment – vysoký · ČNB do 7,5 mil. Kč (S.11) – střední, chybí živnostníci (S.14) `[DATA GAP]` · paušál – vysoký, podmnožina (~18 % hlavních OSVČ) · mikro ÚJ – vysoký, podmnožina.

**B07 – So what: definice (L9).** 1. Přijmout ≤ 50 mil. Kč jako interní definici SB a zveřejnit ji. 2. Pro sizing používat ČSSZ (702 tis. hlavních + 501 tis. vedlejších) a ≈ 475 tis. aktivních PO `[EST]`, ne 2,03 mil. „živnostníků". 3. Segmentovat FOP podle hlavní/vedlejší a paušál/ne-paušál: 577 tis. hlavních ne-paušalistů `[EST]` = jádro pro úvěry. 4. Benchmark s KB je nejčistší (60 mil. Kč, 51,2 mld. Kč). 5. Chybějící hranice ČSOB CZ, UCB, Moneta, Air Bank, Fio, Creditas `[DATA GAP]`.

### B · 2 VELIKOST A STRUKTURA – WS1 (B08–B15)

**B08 – Hypotézy a verdikt WS1 (L3).** H1.1 ≥ 95 % aktivních PO v segmentu – pravděpodobné, neověřeno přímo (`[DATA GAP: ČSÚ SBS]`) · H1.2 OSVČ rostou, hlavní zpomaluje, vedlejší zrychluje – potvrzeno ve 2 ze 3 částí · H1.3 cizinci 10–30 % nových FOP – potvrzeno na horní hranici (30 %) · H1.4 Praha + STČ = třetina – potvrzeno na datech 2022 (32 %). Verdikt jako barevný štítek.

**B09 – Stock OSVČ (L1 skládané sloupce 2019–6/2026).** Headline: „OSVČ poprvé přes 1,2 milionu; od 2024 roste hlavně vedlejší činnost." Hlavní / vedlejší: 2019 598 086 / 433 279 · 2021 634 205 / 443 891 · 2022 649 189 / 455 069 · 2023 668 737 / 458 452 · 2024 681 351 / 473 529 · 2025 692 402 / 486 112 · 6/2026 701 819 / 501 041. 9/2026 `[DATA GAP]` jako prázdný sloupec. Callout: podíl hlavní činnosti na ročním přírůstku 73–85 % (2021–23) → 46–47 % (2024–25) → ≈ 45 % (1H 2026) `[EST]`; 2019→6/2026 +171 495 (+16,6 %) `[EST]`. Zdroj: ČSSZ via Podnikatel.cz `[FACT]`.

**B10 – Toky FOP a PO (L1 sloupce vznik/zánik).** Headline: „Vznik akceleruje, zánik klesá: 19 nových FOP na 10 zaniklých v 1H 2026, nejvíce za 8 let." FOP 2025 ~84 tis. / ~49 tis.; 1H 2026 51 534 (+10 %) / 27 300 (−11 %). PO 2025 34 621 (max za 20 let) / 16 853 (rekord); 1H 2026 15 498 / 7 796. Poznámka: v 1H 2025 přerušeno 53 779 živností. Zdroj: CRIF, D&B `[FACT]`.

**B11 – Triangulace „kolik je živnostníků" (L1 vodorovné sloupce s indexem ČSSZ = 100).** Headline: „Registrace ≠ aktivita: 2,03 mil. na papíře, 1,13–1,20 mil. reálně." RŽP 2 029 257 (172) · ČSÚ RES FO 2 028 363 (172) · ČSÚ RES FO+PO aktivní 1 780 970 (151) · ČSSZ OSVČ 1 178 514 (100) · D&B aktivní ~1 131 000 (96) · ČSSZ hlavní 692 402 (59) · paušál 125 449 (11). Callout: rozdíl RŽP − ČSSZ ≈ 851 tis. `[EST]`. Stav 31. 12. 2025 `[FACT]`.

**B12 – Právnické osoby (L4, 3 karty + mini tabulka).** Headline: „594 520 obchodních společností, pětina spí – aktivních ≈ 475 tis." Karty: 594 520 PO (D&B 2026) `[FACT]` · ~1/5 neaktivních, z toho 57 % v Praze (57 212) `[FACT, datum neznámé]` · ≈ 475 tis. aktivních `[EST = 594 520 × 0,8]`. Řádek: MSP 0–249 zam. 1 341 014 = 99,87 % subjektů (2024) `[FACT]`. Prázdný obdélník: „podíl PO s obratem ≤ 50 mil. Kč – chybí – ČSÚ SBS / MF DPPO".

**B13 – Paušál a odvody (L1 řada + tabulka vpravo).** Headline: „Paušální daň: 125 449 OSVČ bez daňového přiznání, 96 % v 1. pásmu." 1. pásmo: 2022 63 413 · 2023 77 410 · 2024 97 512 · 2025 110 854 · 2026 120 114; 2. pásmo 4 709, 3. pásmo 626; nově 11 554. Tabulka 2026: min. VZ hlavní 40 % průměrné mzdy = 19 587 Kč · záloha soc. 5 720 → 5 005 Kč od 1. 7. 2026 · vedlejší 1 574 Kč · zdravotní 3 306 Kč · paušál 1. pásmo 9 984 → 9 162 Kč od 7/2026; 2./3. pásmo 16 745 / 27 139 Kč. Zdroj: FS, ČSSZ `[FACT]`.

**B14 – Struktura: cizinci, regiony, obory (L4, 3 karty).** Headline: „Třetina přítoku FOP jsou cizinci, třetina živnostníků sedí v Praze a Středních Čechách." Cizinci: 26 535 = 30 % nových FOP (2025); stock téměř 10 %; UA 37,8 % (73 699), SK 16,8 %, VN 16,1 % `[FACT]`; ≈ 195 tis. cizích živnostníků `[EST]`. Regiony: Praha 18 % + STČ 14 % = 32 % (2022) `[FACT]`; Praha 195 146 aktivních živnostníků (2025); STČ 72,1 % živnostníků mezi subjekty. Obory: stavebnictví 11,77 % živností; obchod 13,1 % / stavebnictví 13,0 % subjektů (krajské RES). Gender: ~16 % mužů vs. < 10 % žen na vlastní účet. Věk `[DATA GAP]`.

**B15 – So what: velikost (L9).** 1. Adresovatelný trh ≈ 1,18 mil. subjektů (702 tis. hlavních OSVČ + ≈ 475 tis. aktivních PO `[EST]`); penetraci měřit proti ČSSZ/D&B, ne RŽP. 2. Růst je v přítoku: ~120 tis. onboardingů/rok, 30 % cizinci. 3. Vedlejší OSVČ (+16 tis. y/y) = „podnikatelský modul v osobním Georgi". 4. Paušalisté a mikro ÚJ = levný automatizovaný servis; úvěry pro 577 tis. hlavních ne-paušalistů `[EST]` a aktivní s.r.o. 5. Doplnit: podíl PO ≤ 50 mil. Kč, ČNB S.14 vs. S.11, krajský rozpad 2025.

### B · 3 KONDICE SEGMENTU – WS2 (B16–B22)

**B16 – Hypotézy a verdikt WS2 (L3).** H2.1a bankroty FOP 1H 2026 stagnují – potvrzeno · H2.1b PO nejvyšší od 2017 – potvrzeno s upřesněním (1H na úrovni 2017, celý rok 2025 max od 2018) · H2.2 ~60 % platí včas – potvrzeno jen na metrice „firmy" (61,8 %) · H2.3 ~25 % zkouší externí financování – potvrzeno (zdroj bez data) · H2.4 datová stopa se zúžila – směrově potvrzeno.

**B17 – Insolvence (L1 dva panely).** Headline: „Bankroty živnostníků stagnují, konkurzy firem jsou na 9letém maximu." FOP: 2024 ≈ 5 350 `[EST]` · 2025 6 213 (+16 %) · 1H 2026 3 260 (0 %), návrhy 3 294 (−2 %). PO: 2024 ≈ 678 `[EST]` · 2025 746 (max od 2018) · 1H 2026 418 (+9 %), návrhy 678 (+22 %) · 1–8/2026 538 (vs. 519). Odvětví PO 1H 2026: obchod 93, výroba 66, stavebnictví 52. Callout: 746 konkurzů ≈ 0,06 % MSP `[EST]` – relevantní je trend. 2019–2023 `[DATA GAP]`. Zdroj: CRIF `[FACT]`.

**B18 – Exekuce a platební morálka (L4, 2 panely).** Headline: „Cash-flow, ne solventnost: pětina faktur chodí pozdě, splatnost ~52 dní." Exekuce: > 4,0 mil. (2023) → 3,35 mil. (2024) → ~3,16 mil. (6/2025); nově zahájené +6,3 % (1–9/2025). Morálka: firmy platící včas 59,2 % (2022–23) → 61,8 % (2024); EOS 2025 faktury 76 % včas / 20 % pozdě / 4 % nedobytné; splatnost ~52 dní; zhoršení čeká 17 % vs. zlepšení 11 %. `[FACT]`

**B19 – Makro 2021–2026 (L7 timeline).** Headline: „Dva šoky – inflace 2022–23 a odvody 2024–26; ČNB v červnu 2026 sazby znovu zvedla." HDP 4,0 / 2,8 / 0,0 / 1,3 / 2,6 %; inflace 3,8 / 15,1 / 10,7 / 2,4 / 2,5 % (2021–25); repo 3,50 % (2025) → 3,75 % (18. 6. 2026), beze změny 6. 8. 2026. Repo 2021–2024 a HDP 2026 `[DATA GAP]`. Události: zrušení EET 1. 1. 2023; od 7/2026 záloha −715 Kč (≈ 8,6 tis. Kč/rok na minimálního plátce `[EST]`). Zdroj: ČSÚ, ČNB `[FACT]`.

**B20 – Financování (L2 big number 25 % + tabulka).** Headline: „Bariérou úvěru je proces a postoj, ne nabídka." Big number **25 %** (firem se za 3 roky pokusilo o externí financování, AMSP, datum neznámé). Tabulka: > 1/3 úvěr odmítá · ~20 % bez rezervy · živnostníci: 57 % podnikatelský úvěr / 34 % osobní půjčka · < 10 % mimo banky · ČLFA podnikatelé 120,5 mld. Kč 1H 2026 (+9 %) · factoring 172 mld. Kč (+8,5 %) · NRB záruky 25,9 mld. Kč (2025), Národní záruka 830 firem / 5,4 mld. Kč · Flowpay ~500 mil. Kč kumulativně, cíl 2 mld. `[CLAIM]`.

**B21 – Digitální stopa (L4, 3 karty).** Headline: „Data o tržbách se přesunula od státu k platformám a k bankovnímu účtu." EET zrušeno 1. 1. 2023 (201 tis. subjektů, 19,2 mld. účtenek) `[FACT]` · Shoptet > 45 tis. e-shopů, > 79 mld. Kč obratu (2024) `[CLAIM]`; 21 % podniků 10+ zam. prodává online `[FACT]` · ViDA přeshraničně 1. 7. 2030, domácí 1/2035, ČR bez mandátu `[FACT]`. Závěr: „Pro paušalisty je transakční účet jediný průběžný zdroj příjmové pravdy."

**B22 – So what: kondice (L9).** 1. Oddělit rizikovou politiku FOP a malých s.r.o. (early-warning na návrhy +22 %). 2. Produkt na 52denní splatnost: invoice financing a kontokorent navázaný na faktury. 3. Převést osobní půjčky živnostníků (34 %) do podnikatelského produktu + NRB Národní záruka. 4. Embedded lending jako obrana i útok (Shoptet, fakturační SW). 5. Data-first: scoring z účtu před ViDA.

### B · 4 BANKOVNÍ TRH ČR – WS3 (B23–B38)

**B23 – Hypotézy a verdikt WS3 (L3).** H1 „0 Kč" je standard – potvrzeno (9 z 13) · H2 digitální banky přebírají nové FOP a s.r.o. – potvrzeno s nuancí · H3 úvěry rostou rychleji u challengerů – potvrzeno · H4 cena úvěrů 2026 nad 2021 – potvrzeno (6,29 % vs. 3,65 %) · H5 ČS drží distribuci, ztrácí transparentnost – potvrzeno. Poznámka: nabídka bank jen ze zdrojů 06/2026+, starší `[STALE]`.

**B24 – Kotvy z IR fact sheetů (L3).** Headline: „Tvrdá data o segmentu publikují jen tři banky." KB Loans to small businesses 46,0 (3/2021) → 51,2 mld. Kč (1Q 2026), CAGR ~2,2 % `[EST]` · KB pobočky 242 → 172 · ČS pobočky 409 → 324 · ČS FTE 9 803 → 9 299 · Moneta pobočky 153 (4Q 2022) → 123 · Moneta SB splátkové úvěry nová produkce 918 (4Q 2022) → 2 138 mil. Kč (1Q 2026) · Moneta Commercial deposits 105,8 → 109,3 mld. · ČSOB SME 105,2 (12/2024) → 120,1 mld. Kč. `[FACT]`

**B25 – Růst úvěrů segmentu (L1 vodorovné sloupce).** Headline: „Úvěry rostou tam, kde se banka zaměřila; ČS SME +5,2 % je nejpomalejší složka jejího portfolia po CRE." Moneta +27,5 % (23,4 mld.; nová produkce 5,2 mld., +29,9 %) · ČSOB SME +11,1 % (120,1 mld.) · KB +6,9 % (51,2 mld.) · ČS SME +5,2 %. Vedle malý panel ČS složek 1H 2026: velké podniky +14,2 %, veřejný sektor +19,2 %, SME +5,2 %, CRE +1,4 %, celkem korporátní +9,1 % (466,3 mld.); skupina +9,5 %. `[FACT]`

**B26 – Moneta jako důkaz (L1 sloupce čtvrtletí).** Headline: „Moneta zdvojnásobila nové small-business úvěry za dva roky při nízkém riziku." SB splátkové úvěry, nová produkce (mil. Kč): Q1 2024 1 323 · Q2 1 544 · Q3 1 394 · Q4 2 101 · Q1 2025 1 781 · Q2 2 213 · Q3 1 964 · Q4 2 399 · Q1 2026 2 138. Callout: NPL Commercial 0,9 %; impairment Commercial Q1 2026 +22 mil. Kč (rozpuštění); KB SB za 5 let jen +11,3 % vs. korporátní +35,7 % → segment je „contestable". Zdroj: Moneta, KB IR `[FACT]`.

**B27 – Ceny účtů (L3, řádek ČS zvýrazněn).** Headline: „9 ze 13 bank má účet za 0 Kč bez podmínek; ČS je jediná z velké trojky s podmíněnou cenou." Řádky (tarify · datum zdroje · značka): ČS Živnostník 75 / 45 / 0 Kč podmíněně, Klasik 0 Kč s výhradou, Maxi 399 Kč, startovací KTK 20–100 tis. Kč, 2 roky zdarma pro nové firmy · 1. 7. 2026 `[FACT]` · KB 0 / 39 / 89 / 499 Kč `[STALE 03/2026]` · ČSOB 0 Kč online (Bank iD); firmy 0 / 129 Kč `[STALE 03/2026]` · RB 0 / 99 / 299 Kč · 8/2026 `[FACT]` · Moneta 0 Kč + 5 % cashback `[STALE 03/2026]` · UCB 0 / 150 / 350 Kč `[STALE 03–06/2026]` · Air Bank 0 Kč + 1 % cashback `[STALE 03/2026]` · Fio 0 Kč + 2,7 % úrok · 8/2026 `[FACT]` · Creditas 0 Kč · 7/2026 `[FACT]` · Revolut Business od 250 Kč, Wise 0 Kč + 1 150 Kč setup, mBank 0 Kč `[STALE: datum neznámé]`. Ceny 2021 `[DATA GAP]` jako prázdný sloupec.

**B28 – Sazby a marže (L1 dvojice sloupců 2021 vs. 2026).** Headline: „Při stejném repo 3,75 % jsou malé firemní úvěry dražší než v 2021: marže ~2,15 → ~2,54 p.b." Nové úvěry NFC do 7,5 mil. Kč: 3,65 % (10/2021, repo 1,50 %) → 6,29 % (7/2026, repo 3,75 %); 7,5–30 mil. 5,56 % (7/2026); vklady NFC termínované 3,23 %, jednodenní 1,19 % (7/2026). Úročení podnikatelských zůstatků: Fio 2,7 %, Moneta spořicí 1,85 % `[STALE]`, Creditas 0 %. Marže `[EST]`, ostatní `[FACT]`.

**B29 – Podíly na účtech (L1 skládané sloupce FO / PO).** Headline: „ČS vede u živnostníků, u firem ji předbíhá Fio, RB i KB." Fakturoid 30. 9. 2026, celkem / FO / PO: ČS 17 / 17 / 13 · ČSOB 15 / 16 / 12 · Air Bank 15 / 17 / 3 · RB 14 / 14 / 17 · Fio 13 / 10 / 31 · KB 11 / 11 / 14 · Moneta 7 / 8 / 5 · mBank 4 / 4 / — · UCB 3 / 2 / 3. Druhý zdroj (malé firmy – plátci DPH, chytryrejstrik, datum neznámé): Fio 24,4 %, KB 23,39 %, ČSOB 18,24 %, ČS 16,62 %, RB 16,53 %. Syntéza ČS 16–20 % `[EST]`. Poznámka: vzorek digitálně zdatných, ne celý trh.

**B30 – Digitál a onboarding (L2 big number 3,9 + srovnání).** Headline: „Business aplikace ČS má nejnižší iOS hodnocení z velkých bank; online onboarding s.r.o. u ČS neověřen." Big number **3,9** (George Business, App Store CZ, 650 hodnocení, 2. 10. 2026). Vedle: George Business Google Play 4,6 · ČSOB Smart 4,8 iOS (144 tis.) / 4,2 Android · Smart Banka 4,8 `[CLAIM]` · RB 4,8 Android `[STALE]`. Onboarding: RB FOP jen s IČO a 2 doklady `[STALE]` · Air Bank vícečlenné s.r.o. online od 23. 1. 2026 · KB+ > 70 tis. podnikatelů v migraci 2025–2027 · ČS s.r.o. online `[DATA GAP]`.

**B31 – Distribuce (L1 sloupce 2021 vs. 2026).** Headline: „Všichni zavírají pobočky; ČS si drží dvojnásobek sítě KB." ČS 409 → 324 (−20,8 %) · KB 242 → 172 (−28,9 %) · Moneta 153 (4Q 2022) → 123 (−19,6 %) · ČSOB 88 firemních poboček `[STALE]`. `[FACT]`, změny `[EST]`.

**B32 – Benchmarková matice (L3 heat-map 9 bank × 7 dimenzí, škála 1–5).** Headline: „Benchmark sedmi dimenzí: ČS vyhrává jen v síti." Řádky (cena / digitál / onboarding / úvěry / distribuce / momentum / transparentnost = celkem): Moneta 5/4/4/5/3/5/4 = 4,3 · ČSOB 4/4/4/4/4/4/3 = 3,9 · KB 4/4/4/3/4/3/4 = 3,7 · Air Bank 5/5/4/1/2/4/2 = 3,3 · **ČS 3/3/3/3/5/3/2 = 3,1** · RB 4/4/4/2/3/3/1 = 3,0 · Fio 5/3/3/2/3/4/1 = 3,0 · UCB 4/3/3/2/2/2/1 = 2,4 · Creditas 4/3/3/1/2/2/1 = 2,3. Poznámka: skóre = expertní syntéza `[EST]`; buňky ze STALE zdrojů označ tečkovaným rámečkem.

**B33 – Mapa strategických skupin (L5; X = šíře nabídky, Y = cenová agresivita a digitální rychlost).** Headline: „Čtyři strategické skupiny – ČS mezi univerzálními lídry s nejnižší cenovou agresivitou." A univerzální lídři (ČS, KB, ČSOB) · B challengeři s úvěrovou hranou (Moneta, RB, UCB) · C digitální transakční banky (Fio, Air Bank, Creditas, mBank, Trinity) · D fintech multi-currency (Revolut, Wise). Pod každou skupinou slabina jednou větou. ČS červeně. `[EST]`

**B34 – Profil: Česká spořitelna (L8).** Headline: „ČS: největší báze a síť, ale nejpomalejší úvěrový růst a nejslabší aplikace." Fakta: 4,6 mil. klientů (6/2026) · 324 poboček · ceník 1. 7. 2026 (Živnostník 75/45/0, Klasik, Maxi 399, KTK 20–100 tis.) · start-up úvěr do 600 tis. fix 9 %, Simple do 1,2 mil. `[STALE]` · George Business 3,9 / 4,6 · korporátní úvěry 466,3 mld. (+9,1 %), SME +5,2 % (1H 2026); FY2025 SME úvěry +7,7 %, SME depozita poprvé 100 mld. · private-markets fond v George Business od 5/2026 · Fakturoid 17 % FO / 13 % PO. Chybí: počet podnikatelských klientů, obratová hranice, s.r.o. online, výroky managementu `[DATA GAP]`.

**B35 – Profily: KB a ČSOB (L8 dvojitý).** KB: SB úvěry 51,2 mld. (+6,9 %) · KB+ Business 0/39/89/499 Kč `[STALE]` · > 70 tis. podnikatelů v KB+ · 172 poboček · skupina 2 313 000 klientů, úvěry 945,8 mld. (+10,0 %), zisk 8,5 mld. (1H 2026) · 11 % FO / 14 % PO; 23,4 % malých firem → „banka s.r.o.". ČSOB: SME do 300 mil. Kč; SME loans 120,1 mld. (+11,1 %) · účet 0 Kč online přes Bank iD `[STALE]` · ČSOB Smart 4,8 iOS · úvěry firmám a podnikatelům 441 mld. (+8 %), investiční úvěry OSVČ +8,5 %, +71 tis. aktivních klientů (1H 2026) · Euromoney 2026 nejlepší banka ČR i SME · 15–18 % podíl.

**B36 – Profily: Moneta, RB, UCB (L8 trojitý).** Moneta: živnostníci a malé firmy 23,4 mld. (+27,5 %), nová produkce 5,2 mld. (+29,9 %), nové úvěry SME 16,6 mld. (+58,2 %), ROTE 23,3 %, ~1,6 mil. klientů (1H 2026); Konto PRO 0 Kč + 5 % cashback `[STALE]`; 123 poboček; podíl na účtech jen 7–8 %. RB: CHYTRÝ 0 / AKTIVNÍ 99 / EXKLUZIVNÍ 299 Kč (8/2026); FOP online za pár minut `[STALE]`; úvěry 432 mld. (+12,5 %); 14 % FO / 17 % PO; segment nereportován. UCB: Business Start 0 / Open 150 / Top 350 Kč `[STALE]`; úvěry 655 mld. (+5,9 %), ~900 tis. klientů CZ+SK; 2–3 % Fakturoid, 8,4 % středních firem.

**B37 – Profily: Air Bank, Fio, Creditas + sekundární vrstva (L8 čtyřdílný).** Air Bank: 0 Kč + 1 % cashback, fakturace z mobilu (> 30 tis. faktur/měs.), daňové podklady `[STALE 01/2026]`; > 65 tis. účtů za < 2 roky; vícečlenné s.r.o. od 23. 1. 2026; Finparáda 2026 1. místo; 17 % FO / 3 % PO; úvěr `[DATA GAP]`. Fio: 0 Kč, 14 měn, 2,7 % úrok (8/2026); KTK od 4,9 % `[STALE]`; 1,6 mil. klientů; 31 % PO, 24,4 % malých firem → „default účet s.r.o.". Creditas: firemní účet 0 Kč, neúročen (7/2026); 400 tis. klientů; SB úvěry `[DATA GAP]`. Sekundární: Revolut Business od 250 Kč · Wise 0 Kč + 1 150 Kč · mBank 0 Kč jen FOP, 4 % FO · Trinity garance 4,08/3,30 % · Partners bez účtu (vše `[STALE]` kromě mBank podílu).

**B38 – So what: bankovní trh (L9).** 1. Živnostník na 0 Kč bez podmínek. 2. Zavřít mezeru u s.r.o. (13–17 % vs. Fio 24–31 %, KB 23 %): online s.r.o. vč. vícečlenných + 2 roky zdarma jako hlavní sdělení. 3. Úvěry SB ≥ 10 % y/y (vs. +5,2 %). 4. George Business ≥ 4,5 v App Store. 5. Reportovat segment čtvrtletně jako KB a Moneta. Přidej malý řádek: „Ocenění 2026: ČSOB (Euromoney), Air Bank (Finparáda); Zlatá koruna 2026 a NPS podnikatelů `[DATA GAP]`."

### B · 5 TRENDY A DISRUPTORY DO 2030 – WS4 (B39–B44)

**B39 – Hypotézy a verdikt WS4 (L3).** H1 regulace je hlavní vynucený program, většina 2027 – potvrzeno · H2 FIDA do 2028 nový kanál – zpochybněno (trilog pozastaven) · H3 fintech už bere primární vztah – částečně · H4 AI pro podnikatele masově – nepotvrzeno · H5 ESG povinnost do 2028 – vyvráceno · H6 generační výměna jako tichý churn – potvrzeno kvalitativně.

**B40 – Regulace (L3).** Headline: „Šest regulací mění small-business banking; čtyři termíny padají do 2027." Sloupce: oblast · fakt · pravděpodobnost · dopad · horizont · implikace ČS. IPR: příjem SEPA Instant 9. 1. 2027, odesílání + VoP 9. 7. 2027; dnes 5 bank (Oberbank, J&T, Fio, Partners, UCB) `[STALE]` · AMLR 10. 7. 2027, remediace do 2032 · PSD3/PSR ≈ konec 2027 · ViDA 7/2030 přeshraničně, 1/2035 domácí; PL 2026, SK 1/2027 · zákon o účetnictví: novela 1. 1. 2026, nový zákon nejdříve 2027/2028 · Bank iD 5,3 mil. uživatelů, 550+ firem · FIDA pozastavena `[DATA GAP: stav 10/2026]` · daně OSVČ: 9 026 Kč/měs. min. pojistné, od 7/2026 5 005 Kč soc. záloha.

**B41 – Regulatorní timeline (L7 2026–2035).** Headline: „Rok 2027 je regulatorní zeď – pro největší banku je to výhoda škály." Body na ose: 1. 1. 2026 novela účetnictví · 7/2026 nižší zálohy OSVČ · 9. 1. 2027 · 1. 1. 2027 SK e-fakturace · 9. 7. 2027 · 10. 7. 2027 · ≈ konec 2027 PSR · 2028+ FIDA · 7/2030 ViDA · 2032 konec AMLR remediace · 1/2035 ViDA domácí. `[FACT]`

**B42 – Fintech a embedded finance (L3 + 1 graf).** Headline: „Fintech zatím malý, ale distribuce přes brány a POS obchází banku." Revolut 1,3 mil. uživatelů ČR, transakce +130 % `[FACT/CLAIM]` · Shoptet Pay > 9 mld. Kč 2025 (+55 %) · Flowpay ~500 mil. Kč, linka 30 mil. EUR, cíl 2 mld. `[CLAIM]`, Teya · Lemonero 10 mld. Kč schváleno v Evropě `[CLAIM]`, × Comgate · Fakturoid integruje KB (od 2018) a Monetu (8/2025), ČS nenalezena `[DATA GAP]` · Stripe dostupný od 2023 · 215 tis. terminálů. Revolut Business klienti ČR, GoPay, Comgate, Roger `[DATA GAP]`.

**B43 – AI, ESG, generační výměna (L4, 3 karty).** Headline: „AI pro podnikatele nemá nikdo, ESG tlak nepřijde, generační výměna ano." AI: Hey George pilot ~100 tis., Kate ~0,5 mil., KB+ retail; SME use-case nikde; George AI SK od 9. 9. 2026. ESG: Omnibus vyjímá ~80 % firem, CSRD > 1 000 zam., VSME ~25 datových bodů. Generační výměna: majitelé 50+, polovina rodinných firem předání nezačala, až 2/3 bez plánu, 36 % formální plán; věk jednatelů `[DATA GAP]`.

**B44 – Heat-mapa trendů (L5, pravděpodobnost × dopad, kvadranty).** Headline: „AMLR a ViDA jsou v pravém horním rohu; AI a Bank iD jsou jediné, kde ČS může vést." Body s postojem: IPR MUST-DO · AMLR MUST-WIN · PSR MUST-DO · ViDA BUILD OPTION · daně OSVČ QUICK WIN · Bank iD QUICK WIN · fintech platby DEFEND · embedded lending DEFEND/PARTNER · AI DIFFERENTIATE · generační výměna HARVEST/RETAIN · zákon o účetnictví, FIDA, ESG MONITOR · DAC7 `[DATA GAP]`. Pod: so-what 5 bodů z kap. 5 (compliance 2027 jako produkt · faktura → platba → financování · Hey George pro podnikatele do konce 2026 · program nástupnictví · neinvestovat do FIDA a ESG před 2028). `[EST]`

### B · 6 EVROPSKÁ GAP ANALÝZA – WS5 (B45–B59)

**B45 – Výběr trhů (L3 skóring, 4 kritéria × 1–5).** Headline: „Pět benchmark trhů: SK 19, PL 14, AT 14, NL 13, UK 12 – dva trhy Erste a dva digital-first." Kritéria: hráči s měřitelným úspěchem · srovnatelnost struktury · přenositelnost regulace/infrastruktury · relevance pro Erste. UK 5/3/3/1 · NL 4/4/4/1 · PL 3/5/4/2 · AT 3/3/3/5 · SK 4/5/5/5. Záložní (předběžně `[EST]`): HU 12, RO 11, DE 11, FR 10.

**B46 – Profil UK (L8, zelenošedá).** Headline: „UK: digital-first lídři dokazují, že podnikatel zaplatí za daně a účetnictví." Trh: 5,7 mil. firem, 75 % bez zaměstnanců; 4,53 mil. self-employed (ONS 7/2026). Hráči: Monzo FY26 905 tis. business klientů (+45 %), 47 % platí, ARPAC £484 (13 870 Kč) · Starling PBT £217 mil., 56 % SME = primární banka · Tide revenue £177 mil. (+55 %, FY2024), ~900 tis. členů `[CLAIM]` · iwoca £1,5 mld. úvěrů 2025 přes > 50 partnerů · challengeři 60 % hrubých SME úvěrů. Enablery: Open Banking 18 mil. uživatelů; MTD ITSA od 4/2026 (860 tis.); Companies House IDV od 11/2025. `[FACT]`

**B47 – Profil NL (L8).** Headline: „Nizozemsko: úvěr z 13 měsíců transakcí za 5–20 minut." Trh: 2,43 mil. podniků, 2,01 mil. jednoosobových; 1,2 mil. zzp aktivních vs. 1,79 mil. registrovaných – stejný problém jako ČR. Hráči: Knab > 270 tis. podnikatelů, 1. místo srovnávačů 2026 (8,9) · bunq zisk €85,3 mil. (2024, +65 %) · Rabobank/ING úvěr z transakcí 5–20 min · ceny €0–9,90/měs. Enablery: iDEAL → Wero (10/2026), iDIN, KvK API, Peppol; e-fakturace ~2028. `[FACT]`

**B48 – Profil PL (L8).** Headline: „Polsko: 12–18 měsíců napřed v e-fakturaci." Trh: 3,84 mil. aktivních JDG (9/2026), 2,31 mil. mikrofirem (97 %), 288,8 tis. nových JDG (2025). Hráči: mBank (mKsięgowość), PKO BP, Santander, ING, Pekao; Revolut ~5 mil. uživatelů. Praxe: „aktivitní nula" při platbě ZUS/US + bonusy 2 400–4 200 PLN `[STALE 03–06/2026]`; BLIK 2,9 mld. transakcí, 20,7 mil. uživatelů (2025). Enablery: KSeF 1. 2. 2026 (příjem pro všechny), 1. 1. 2027 nejmenší; BGK de minimis 60 %, 0,5 % p.a. Počty SB klientů bank `[DATA GAP]`.

**B49 – Profil AT (L8).** Headline: „Rakousko: domácí trh Erste s hotovým George Business One." Trh: 376 112 EPU (+3,9 %, 12/2025) = 62 % firem; 51,6 % žen. Erste AT ceny 06–08/2026: Geschäftskonto od 10,41 €, EPU Smart 13,61 €, George 7,43 €, George Business One 18 €/měs. (role, business karty, účetní export), Gründer 4,95 € 1. rok; 4,3 mil. klientů, 732 poboček. Enablery: ID Austria; BMD napojení; bez národní B2B e-fakturace. Adopce `[DATA GAP]`.

**B50 – Profil SK (L8).** Headline: „Slovensko: stejný trh, stejná platforma – a SLSP už má účet za 0 € navždy." Trh: 377 tis. aktivních živností (2024); 2025: 42 tis. vznik / 66 tis. zánik (rekord), SZČO v SP 204 tis. (−40 tis.); PO vznik > 24 tis. (+~17 %). SLSP: živnostník 0 € navždy, online bez výpisu ze ŽR, PO 1 rok zdarma online, 1 % cashback, George API + SuperFaktúra, George AI od 9. 9. 2026; George 1,33 mil. uživatelů. Revolut Business SK +33 % klientů, +56 % objemů (2025). Enablery: SEPA Instant plně od 9. 10. 2025 vč. VoP; e-fakturace B2B od 1. 1. 2027. `[FACT]`

**B51 – Gap matice (L3 heat-map, 11 dimenzí, mezera 1–5).** Headline: „ČS má mezeru 4 v šesti z jedenácti dimenzí – žádná z nich není regulatorní." Sloupce: dimenze · ČR trh · ČS · nejlepší praxe · mezera ČR · mezera ČS · důvod (R/I/S/K/E). Onboarding FOP 2/3 (S, K) · Onboarding PO 3/4 (S, I) · Pricing 2 cena / 4 monetizace → ČS 4 (S, E) · Digitální funkce 3/4 (S, K) · Lending 2/4 (S, K, E) · Integrace 3/4 (S, I) · Obsluha 1/2 · Data & AI 3/3 (S, K) · Nefinanční služby 4/4 (S, R) · ESG 1/1 · Segmentace 2/4 (S, K). Do buněk „nejlepší praxe" krátce: SLSP bez ŽR, Knab 5 min · Starling, Tide, SLSP PO · Monzo 47 % platících · Monzo Tax Pots, George Business One · Rabobank 5–20 min, iwoca · SLSP George API, mBank KSeF · Erste AT 732 poboček · George AI SK · Tide payroll · VSME · Erste AT George vs. Business One, Starling 56 %.

**B52 – Long-list 18 praktik (L3 kompaktní).** Headline: „18 praktik z pěti trhů jako vstup do testu." L1 SLSP 0 € + bez ŽR · L2 aktivitní nula (PL) · L3 George Business One (AT) · L4 e-fakturace v bance (mBank, Tatra) · L5 Bank API + fakturační add-on (SLSP, Fio) · L6 portfoliová garance (BGK, NRB) · L7 EPU paušál + Gründer (AT) · L8 hotovost přes poštu (bank99, BAWAG) · L9 BLIK · L10 AI asistent (SLSP, Tatra) · L11 daňové pots (Monzo, Starling, Mettle) · L12 účetní SW v tieru (Mettle, Starling) · L13 embedded lending (Tide–iwoca) · L14 úvěr z transakcí (Rabobank, ING, Knab) · L15 registrace firmy + účet + payroll (Tide) · L16 fixní cena + bonus (Knab, PL) · L17 primární banka jako KPI (Starling) · L18 digitální s.r.o. s více jednateli (Starling, Air Bank). Značky dle dokumentu.

**B53 – Test přenositelnosti (L3 + vodorovné sloupce skóre).** Headline: „Šest kritérií s váhami: pět praktik nad hranicí 25 bodů tvoří short-list." Váhy: bolest ČR ×1,5 · proveditelnost ×1 · nikdo v ČR ×1 · vazba na SWOT ×1,5 · důkaz ×1 · ekonomika ×1 (max 35). Skóre: L14 úvěr z transakcí 32,0 · L5+L4 API + e-fakturace 30,5 · L11+L12 daňový pot + tier 29,5 · L17 primární banka KPI 29,0 · L1+L18 0 Kč + onboarding 28,5 · L3 George Business One 25,5 · L13 embedded lending 25,5 · L2 aktivitní nula 24,5 · L6 garance 22,5 · L10 AI 22,0 · L15 registrace + payroll 20,5 · L7 EPU paušál 19,5 · L16 fixní cena 18,0 · L9 BLIK 17,5 · L8 hotovost přes poštu 16,5. Pod: „Short-list (MECE): BP1 = L14 · BP2 = L5 + L4 · BP3 = L11 + L12 · BP4 = L1 + L18 · BP5 = L3 + L17."

**B54 – BP1 Předschválený úvěr z transakční historie (L8 s pevnou šablonou BP).** Šablona BP (stejná pro B54–B58): popis · kde a kdo · důkaz úspěchu · proč v ČR · vazba na SWOT · rizika · řádový dopad `[EST]` · náročnost · kdo z konkurence první. BP1: kontokorent a splátkový úvěr do ~1 mil. Kč z 12–13 měsíců transakcí, rozhodnutí v minutách v George Business · Rabobank (5–20 min), ING, Knab; iwoca £1,5 mld.; Moneta 600 tis. online do 15 min · Moneta nová produkce SB 1Q 2026 2 138 mil. Kč (+20 % y/y), NPL Commercial 0,9 %; challengeři 60 % SME úvěrů v UK · jen ~25 % firem zkouší financování, 34 % osobní půjčka; marže ~2,5 p.b. · S1, S2 / W3 / O3 / T2 · CoR u FOP, nutný early-warning, PSD2 data · kniha +15–25 mld. Kč do 3 let, NII 0,5–1,0 mld. Kč/rok (5,2 mld. × 0,5 × 2,9 = 7,5 mld./pololetí) · střední–vysoká, 12–18 m · Moneta už dělá; KB, ČSOB.

**B55 – BP2 Banka v účetním a fakturačním SW.** George API pro ERP/účetní SW, add-ony Fakturoid, iDoklad, Pohoda, Money; Shoptet; cesta „faktura → platba → financování"; pilot se SLSP při SK e-fakturaci od 1. 1. 2027 · SLSP George API + SuperFaktúra, mBank + KSeF, Tatra, Fio API, Starling Ember, Tide · Fio 31 % PO a 24,4 % malých firem; Shoptet Pay 9 mld. Kč (+55 %); adopce `[DATA GAP]` · ČS 17 % ve Fakturoidu, ale mezi partnery nenalezena; ViDA 2030 · S3 / W4 / O2 / T4, T5 · nevýlučná partnerství, nejistý termín ČR · 20–30 tis. digitálních klientů/rok; invoice financing 3–5 mld. Kč objemů, 0,1–0,2 mld. Kč výnosů; hlavní hodnota obranná · vysoká, 12–36 m · KB, Fio, Moneta.

**B56 – BP3 Daňový „pot" + placený tier.** Obálky na paušál, zálohy ČSSZ + ZP, DPH; odhad daně; tier 149–299 Kč/měs. `[EST]` s fakturačním SaaS; základ 0 Kč · Monzo Tax Pots (Pro £9), Starling Toolkit £7/£12, Mettle + FreeAgent; v ČR Air Bank daňové podklady · Monzo 47 % platících, ARPAC £484, business 14 % revenue · 125 449 paušalistů, min. zálohy 9 026 Kč/měs., změna od 7/2026; nikdo z 13 bank tier nemá · W1, W5 / O4 / S1 · ochota platit `[DATA GAP]`, kanibalizace Maxi · 17–35 tis. platících × 200 Kč × 12 ≈ 40–85 mil. Kč/rok · střední, 6–12 m · Air Bank, Moneta.

**B57 – BP4 First account.** Živnostník 0 Kč navždy, onboarding bez výpisu ze ŽR (ARES/RŽP + Bank iD), s.r.o. online vč. více jednatelů, 2 roky zdarma pro nové firmy zachovat, UA/VN/EN, AML-ready · SLSP, Air Bank (> 65 tis. účtů, vícečlenné s.r.o. od 23. 1. 2026), Starling, Knab · Air Bank 17 % FO = ČS; Finparáda 2026; SLSP adopce `[DATA GAP]` · přítok ~84 tis. FOP + 34,6 tis. PO; cizinci 30 %; Bank iD 5,3 mil. · W1, W7 / T1, T5 / O1, O5 / S6, S7 · ztráta 75 Kč × část klientů `[DATA GAP]`, AML u cizinců · 25–30 % přítoku = 30–36 tis. klientů/rok, +60–140 mil. Kč/rok · střední, 6–12 m · Air Bank, ČSOB, RB.

**B58 – BP5 Segmentace FOP vs. PO + KPI primární banka.** Živnostník (FO, 0 Kč, George) vs. Firma (PO, George Business One ~300–450 Kč/měs. `[EST]`); definice ≤ 50 mil. Kč; čtvrtletní reporting klientů, úvěrů, vkladů, podílu primárních účtů · Erste AT George 7,43 € vs. Business One 18 €; Starling 56 %; KB, Moneta reportují · KB 23,4 % malých firem, 14 % PO vs. 11 % FO; Fio 31 % PO · 34,6 tis. nových PO; ČS PO 13 % vs. FO 17 % · W2, W6, W5 / S7 / T5 · cenová citlivost, kanibalizace, governance Retail vs. Corporates · ≈ 60–80 tis. PO klientů ČS × 20–30 % × 350 Kč × 12 ≈ 50–100 mil. Kč/rok · nízká–střední, 3–9 m · KB, Fio.

**B59 – So what: Evropa (L9).** 1. Čtyři z pěti BP mají hotovou implementaci v Erste (SLSP, EBOe) – transfer je rozhodnutí, ne vývoj. 2. Jen BP3 nemá vzor v Erste – first-mover okno ~12 měsíců. 3. BP1 má největší P&L páku (NII 0,5–1,0 mld. Kč/rok `[EST]`). 4. Všechny mezery ČS jsou strategické nebo organizační. 5. Žádná evropská banka nepublikuje počet SB klientů → interní Erste pull.

### B · 7 SWOT, TOWS, BIG BETS – WS6 (B60–B66)
Pro B60–B63 jednotná tabulka: # · bod · fakt / číslo · vs. koho · dopad (V/S/N) · jistota (V/S/N) · BP. Dopad a jistotu ukaž jako dvě malé tečkové škály.

**B60 – Strengths (L3, 7 řádků).** Headline: „Sedm silných stránek – největší je báze, funding a platforma Erste." S1 4,6 mil. klientů, 324 poboček, 4,46 mil. karet · V/V · S2 NIM 2,11 %, vklady 1 655 mld., NPL 1,5 % vs. KB 1,6 %, Moneta 2,0 %, ČSOB 2,45 % · S/V · S3 č. 1 ve Fakturoidu 17 % · S/S · S4 2 roky zdarma + KTK 20–100 tis. · S/S · S5 graduační cesta: korporátní úvěry 466,3 mld., SME depozita > 100 mld., factoring, leasing · S/V · S6 Bank iD 5,3 mil., výhoda škály v regulaci · S/V · S7 George s praktikami v AT/SK · V/S.

**B61 – Weaknesses (L3, 8 řádků).** Headline: „Osm slabých stránek – všechny strategické, žádná regulatorní." W1 podmíněná cena · V/V · W2 segment neviditelný v reportingu · S/V · W3 SME +5,2 % vs. skupina +9,5 %, sazba a čas nezveřejněny · V/V · W4 bez ekosystémového kanálu · S–V/S · W5 žádná přidaná hodnota nad účet · S/S · W6 App Store 3,9 · S/V iOS · W7 s.r.o. online, hranice a RM model nezveřejněny · S/N · W8 PO 13 % vs. FO 17 % · S/S.

**B62 – Opportunities (L3, 8 řádků).** Headline: „Osm příležitostí – nejsilnější je rekordní přítok a účet jako zdroj dat." O1 přítok FOP ~84 tis., PO 34 621 · V/V · O2 datová stopa u účtu (EET, paušál, ViDA) · V/V · O3 úvěrový tok „contestable" · V/V · O4 volatilita daní OSVČ · S/V · O5 cizinci 30 % + AMLR · S/S · O6 regulatorní zeď 2027 jako produkt · S/V · O7 přesun do s.r.o. a generační výměna · S–V/N–S · O8 transfer z Erste AT/SK · V/S.

**B63 – Threats (L3, 8 řádků).** Headline: „Osm hrozeb – Air Bank bere první účet, Moneta úvěr, Fio s.r.o." T1 Air Bank > 65 tis. účtů · V/V · T2 Moneta +27,5 % · V/V · T3 Fio 31 % PO, 2,7 % úrok · S–V/S · T4 embedded lending (Shoptet Pay 9 mld., Flowpay, Lemonero × Comgate, KB 29 % v Lemonero) · S/S · T5 Revolut 1,3 mil. uživatelů, SK +33 % firemních klientů · S/S · T6 KB+ > 70 tis. podnikatelů · S/V · T7 konkurzy PO +22 % návrhů, NRB záruky 25,9 mld. · S/V · T8 eroze depozitní marže (Fio 2,7 %, Moneta úročené vklady 51 %) · V/S.

**B64 – TOWS (L5 2×2, po 3 bodech).** Headline: „Čtyři směry: úvěr z dat, first account, faktura → platba → financování, segment jako řízená jednotka." SO: předschválený úvěr (S1+S2 × O2+O3) · first account vč. cizinců (S4+S6+S7 × O1+O5) · faktura → platba → financování před ViDA (S3+S7 × O2+O6). ST: graduační cesta jako obrana (S5 × T1+T5) · transakční early-warning (S1 × T7) · compliance 2027 jako produkt (S6 × T5+O6). WO: reset ceny a monetizace (W1+W5 × O4) · ekosystémový kanál (W4 × O2) · segment jako řízená jednotka (W2+W7+W8 × O7+O8). WT: zveřejnit a zvednout rychlý úvěr (W3 × T2) · online s.r.o. vč. vícečlenných (W7+W8 × T1+T6) · George Business ≥ 4,5 (W6 × T1). U každého bodu odkaz na BP.

**B65 – Big bets (L5 bublinový graf: X = obtížnost, Y = horizont, velikost bubliny = řád přínosu; vedle tabulka).** Headline: „Pět big bets – BB1 má největší páku, BB2 a BB4 nejrychlejší start." Tabulka: BB1 předschválený digitální úvěr · kniha +15–25 mld. Kč, NII 0,5–1,0 mld. Kč/rok · střední–vysoká · 12–24 m. BB2 0 Kč navždy + daňový pot + placený tier · 40–85 mil. Kč/rok, obrana 16–20 % podílu u FO · střední · 6–12 m. BB3 banka v SW + e-fakturační hub · 20–30 tis. klientů/rok, invoice financing 3–5 mld. Kč objemů, 0,1–0,2 mld. Kč výnosů · vysoká · 12–36 m. BB4 first account pro 120 tis. nových subjektů · 30–36 tis. klientů/rok, +60–140 mil. Kč/rok · střední · 6–18 m. BB5 George Business One + nástupnictví · 50–100 mil. Kč/rok; nástupnictví `[DATA GAP]` · nízká–střední / vysoká · 3–9 m / 24–60 m. Vše `[EST]`.

**B66 – No-regret moves (L4, 3 karty).** Headline: „Tři kroky bez lítosti: nulový nebo nízký náklad, start tento kvartál." 1. Definice a reporting segmentu (≤ 50 mil. Kč; klienti, úvěry, vklady běžné vs. úročené, podíl primárních účtů; IR řada) – náklad ≈ 0, 3 měsíce. 2. Zveřejnit sazbu a čas rozhodnutí nezajištěného úvěru, online limit 1 mil. Kč – vs. Moneta 600 tis. / 15 min, KB 1 mil. bez příjmů. 3. Živnostník 0 Kč bez podmínek – SLSP na stejné platformě; náklad 75 Kč × placené účty `[DATA GAP]`.

### B · 8 PLÁN 0–36 MĚSÍCŮ – WS7 (B67–B74)
Pro B68–B70 jednotná tabulka: # · aktivita · popis · BP/SWOT · cíl a KPI · náklad (L/M/H) · přínos · vlastník · závislosti. Barva záhlaví podle horizontu.

**B67 – Přehled plánu (L4, 3 sloupce).** Headline: „Plán ve třech horizontech: 8 rychlých kroků, 7 projektů, 4 strukturální sázky." Quick 0–6 m (Q1–Q2 2027) Q1–Q8 · Mid 6–18 m (Q3 2027 – Q2 2028) M1–M7 · Long 18–36 m (Q3 2028 – Q4 2029) L1–L4. Pod: P&L páka 0,7–1,3 mld. Kč/rok do 3 let `[EST]`.

**B68 – Quick wins 0–6 m (L3, 8 řádků).** Q1 definice a reporting SB · BP5, W2 · interní dashboard Q1 2027, IR řada 1H 2027; podíl primárních účtů `[TARGET TBD]`, benchmark Starling 56 % · L · Finance / IR + Retail. Q2 Živnostník 0 Kč · BP4, W1, T1 · ceník 1. 4. 2027; Fakturoid FO ≥ 18 % · L · Retail pricing. Q3 sazba a čas úvěru, 1 mil. Kč online · BP1, W3, T2 · Q2 2027; nová produkce +15 % y/y · L–M · Retail lending. Q4 daňový pot MVP · BP3, O4, W5 · Q2 2027; aktivace u ≥ 15 % FOP `[TARGET TBD]` · M · Digital / George. Q5 SEPA Instant + VoP · O6, T5 · 1/2027 a 7/2027 · M · Payments / Compliance. Q6 Fakturoid/iDoklad API a partnerství · BP2, W4, S3 · Q2 2027; Fakturoid ≥ 18 % · L–M · Digital partnerships. Q7 interní datový pull Erste + CRIF + research n ≈ 500 · BP1–BP5 · Q1 2027; uzavřít 6 `[DATA GAP]` · L · Strategy. Q8 early-warning malá s.r.o. · T7 · Q2 2027 · L–M · Risk.

**B69 – Mid-term 6–18 m (L3, 7 řádků).** M1 předschválený úvěr z transakcí · start Q4 2027; KPI 18 m: produkce +25 % y/y, auto ≥ 60 %, ≤ 15 min, CoR ≤ 0,5 % · H · kniha +15–25 mld. Kč, NII 0,5–1,0 mld. Kč/rok. M2 placený tier + SaaS 149–299 Kč · Q3 2027; konverze 10 % do 12 m, 15–25 % do 36 m · M · 40–85 mil. Kč/rok. M3 online s.r.o. + bez výpisu ze ŽR · Q3 2027; digitální onboarding FOP ≥ 70 %, PO ≥ 50 %; ≤ 10 min FOP / ≤ 1 den PO · M–H · 30–36 tis. klientů/rok. M4 George Business One z AT · Q1 2028; PO ve Fakturoidu 13 → 16 % · M · 50–100 mil. Kč/rok. M5 George Business ≥ 4,5 iOS · do Q4 2027 · M. M6 Shoptet a embedded nabídka · podpis do Q1 2028 · M · 3–5 mld. Kč objemů/rok. M7 Hey George pro podnikatele · pilot Q4 2027 · M.

**B70 – Long-term 18–36 m (L3, 4 řádky).** L1 e-fakturační hub „faktura → platba → financování" · pilot SK 2027–28, CZ launch 2028–29 · H · 0,1–0,2 mld. Kč výnosů + obrana dat. L2 embedded finance platforma (API-first, partnerství nebo akvizice fintechu) · 2028–29; ≥ 20 % nových SB klientů z partnerských kanálů `[TARGET TBD]` · H · 20–30 tis. klientů/rok. L3 program nástupnictví (jednatelé 55+, financování odkupu, private banking) · 2028+ · M · `[DATA GAP]` po CRIF datech. L4 AI-driven obsluha + RM pool · 2029; náklad na obsluhu −20 % · H.

**B71 – Roadmap (L7 Gantt Q1 2027 – 2029).** Headline: „První viditelné změny pro klienty v Q2 2027, plný úvěrový produkt v Q4 2027, e-fakturace v ČR 2028–29." Řádky a symboly přesně podle tabulky 8.2 (■ realizace, ○ příprava/pilot, ● milník); sloupce Q1 27 … Q4 28, 2029; barva řádku podle horizontu. Klíčové milníky popiš přímo: ● IR řada Q3 27 · ● 0 Kč Q2 27 · ● SEPA příjem Q1 27, odesílání Q3 27 · ● BB1 Q4 27 · ● George Business One Q1 28 · ● e-fakturace CZ Q4 28.

**B72 – Závislosti (L5 síťový diagram).** Headline: „Bez definice a interních dat nelze řídit nic dalšího." Šipky: Q1 → všechny KPI · Q7 → M2, L3 · Q3 + Q8 → M1 · Q4 + Q6 → M2 · Q6 → M6 → L2 · M3 + M4 + M5 → podíl u PO · M1 + M6 → L1 · M5 + M7 → L4 · Q5 nezávislé, komunikačně navázané na M3. Uzly obarvit podle horizontu.

**B73 – KPI dashboard (L3, 9 řádků × baseline / 6 / 18 / 36 m / jak stanovit).** Headline: „Devět KPI řídí program – pět z nich dnes nemá veřejný baseline." K1 čistý přírůstek aktivních SB klientů · `[DATA GAP]` · baseline · +15 % · +30 %. K2 podíl na nových registracích · `[DATA GAP]` (stock 16–20 % `[EST]`) · měřeno · 22 % · 25–30 %. K3 podíl primárních účtů · `[DATA GAP]` · měřeno · +5 p.b. · +10 p.b. K4 nová produkce SB úvěrů · +5,2 % `[FACT]` · +15 % y/y, sazba zveřejněna · +25 % y/y, ≤ 15 min, ≥ 60 % auto · kniha +15–25 mld. Kč, CoR ≤ 0,5 %. K5 digitální onboarding · `[DATA GAP]` · FOP 50 % · FOP 70 % / PO 50 %, ≤ 10 min · FOP 85 % / PO 70 %. K6 konverze na tier · 0 % · – · 10 % · 15–25 %, ARPU +500 Kč/rok. K7 George Business App Store / Google Play · 3,9 / 4,6 · 4,2 / 4,6 · ≥ 4,5 / ≥ 4,6 · ≥ 4,6 / ≥ 4,7. K8 Fakturoid celkem / FO / PO · 17 / 17 / 13 % · 17 / 17 / 13 · 18 / 18 / 15 · 19 / 19 / 17. K9 CoR / NPL SB · `[DATA GAP]` (skupina NPL 1,5 %) · měřeno · ≤ 0,5 % · ≤ 0,5 %. Prázdné baseline jako `[DATA GAP]` obdélník, cíle `[TARGET TBD]` jako prázdná buňka s tečkou.

**B74 – Rizika a předpoklady (L4, 5 karet).** Headline: „Pět rizik programu a jak je tlumit." Cenová elasticita a kanibalizace (Q2, M2, M4) → research Q7, regionální pilot · risk appetite (M1) → early-warning Q8, limity dle hlavní/vedlejší činnosti a stáří firmy · skupinová koordinace (M3, M4, M7, L1) → skupinový sponzor, pilot SK 2027 · regulatorní kapacita 2027 → spojit compliance s obchodem (VoP = „ochrana proti fakturačnímu podvodu") · datové mezery → `[TARGET TBD]` stanovit do konce Q1 2027.

### B · 9 OTEVŘENÉ OTÁZKY A DALŠÍ POSTUP (B75–B76)

**B75 – Co jsme nemohli ověřit (L3, 12 řádků: otázka · proč vadí · kde odemknout).** Headline: „Dvanáct otevřených otázek – většinu odemknou interní data ČS a Erste." Klienti, úvěry, vklady, poplatky, NPS segmentu ČS · podíl ČS na nových registracích · adopce praktik v Erste SK/AT · ČNB řady S.14, objemy do 7,5 mil. Kč, NPL · ceníky 2021 a aktuální ceny KB/ČSOB/Moneta/UCB/Air Bank · hodnocení aplikací a čas onboardingu · NPS, Zlatá koruna 2026 · podíl PO ≤ 50 mil. Kč, ziskovost dle NACE · věk jednatelů · Revolut Business ČR a fintech objemy · ochota platit za tier · FIDA, DAC7, zálohy OSVČ 7/2026, termín české e-fakturace, Bank iD pro PO.

**B76 – 8 týdnů do rozhodnutí (L7 timeline 5 kroků).** Headline: „Osm týdnů: interní data → externí řady → research → business case → rozhodnutí." Týden 1–2 interní datová kotva (Q1, Q7) · týden 2–3 externí doplnění (ČNB, ceníky, aplikace, NPS, CRIF) · týden 3–5 customer research (20–30 rozhovorů + n ≈ 500) · týden 5–7 business case BB1–BB5 na interních datech + regionální pilot · týden 8 rozhodnutí: program 2027–2029 vs. status quo.

### B · PŘÍLOHY (B77–B78)

**B77 – Příloha A: primární IR řady (L3).** Headline: „Primární řady z investorských fact sheetů 2021–1Q 2026." ČS: pobočky 409 → 400 → 398 → 366 → 337 → 329 → 324 (3/2021 – 3/2026); FTE 9 803 → 9 299; čisté úvěry 773,9 → 1 206,1 mld. Kč · KB: SB úvěry 46,0 / 47,9 / 46,8 / 47,5 / 47,9 / 50,3 / 51,2 mld. Kč; korporátní 301,7 → 409,3 mld.; pobočky 242 → 172 · Moneta: Commercial úvěry 82 781 (4Q 2022) → 109 070 mil. Kč (1Q 2026); SB nová produkce 918 → 2 138 mil. Kč; Commercial vklady 105 784 → 109 289 mil. Kč · ČSOB: SME 105,2 / 108,1 / 110,7 / 113,2 / 115,4 / 120,1 mld. Kč (12/2024 – 3/2026). `[FACT]`

**B78 – Příloha B–E: zdroje, glosář, log značek, QA (L3 + L4).** Headline: „QA: každé číslo má zdroj a značku; pět známých slabin je řešitelných do 3 týdnů." Levá část – QA scorecard (kontrola · výsledek): čísla bez zdroje – splněno v rámci konvence · nabídka jen 06/2026+ – splněno s označením výjimek · velikost segmentu – ano · definice a obsluha 9 bank – ano, s mezerami · ekonomika segmentu – částečně · výběr trhů a 5 BP – ano · SWOT s faktem, dopadem, jistotou – ano · plán s KPI, vlastníkem, roadmapou – ano · CEO rozhodnutí – ano. Počty značek v hlavním textu: FACT 554 · EST 83 · EXTRAP 1 · CLAIM 25 · DATA GAP 176 · STALE 62. Pravá část – „Známé slabiny": (1) ověření z výtahů, ne plných textů; (2) ceny KB, ČSOB, Moneta, UCB, Air Bank jen `[STALE 03/2026]`; (3) podíly z Fakturoidu a registru plátců DPH; (4) chybí ČNB řady, NPS, ceníky 2021, adopce Erste SK/AT; (5) revenue pool trhu nekvantifikován. Dole: typy zdrojů (IR fact sheety, ČSSZ, ČSÚ, ČNB, MPO, FS, CRIF, D&B, AMSP, ČLFA, Fakturoid, weby bank 06/2026+, výroční zprávy evropských bank) a odkaz „úplný seznam URL, glosář a log značek: přílohy B–D dokumentu".

---

## 6. Matice pokrytí zadání v2 (kontrola, že nic nechybí)
| Požadavek zadání v2 | Část A | Část B |
|---|---|---|
| Hranice 50 mil. Kč, definice a mapování zdrojů | A03, A04 | B04–B07 |
| Cut-off 06/2026 pro nabídku bank, starší = STALE | A03, A08 | B02, B23, B27, B34–B37 |
| Jen ověřená data, značky, nic z v1 | A03 | B02, B78 |
| WS1 velikost, struktura, dynamika 2021–2026 | A04 | B08–B15 |
| WS2 kondice (insolvence, morálka, makro, financování, digitalizace) | A05 | B16–B22 |
| WS3 bankovní trh, profily bank, benchmark, ceny, podíly | A06–A08 | B23–B38 |
| WS4 trendy a disruptory do 2030 | A09 | B39–B44 |
| WS5 výběr 4–5 evropských trhů (UK, NL, PL, AT, SK) | A10 | B45 |
| WS5 profily trhů a hráčů | A10 | B46–B50 |
| WS5 gap matice | A10 | B51 |
| WS5 long-list a test přenositelnosti | – | B52–B53 |
| WS5 5 best practices v detailu | A11 | B54–B59 |
| WS6 SWOT s dopadem a jistotou | A12 | B60–B63 |
| WS6 TOWS | – | B64 |
| WS6 big bets a no-regret moves | A13 | B65–B66 |
| WS7 plán Quick 0–6 / Mid 6–18 / Long 18–36 m | A14 | B67–B70 |
| WS7 roadmap po kvartálech a závislosti | A14 | B71–B72 |
| WS7 KPI dashboard 6/18/36 m | A15 | B73 |
| WS7 rizika a předpoklady | – | B74 |
| Co má CEO rozhodnout a prvních 6 měsíců | A16 | B66, B68 |
| Kap. 9 otevřené otázky a další postup | A16 | B75–B76 |
| Přílohy A–E vč. QA | – | B77–B78 |

## 7. Pravidla, která nesmíš porušit
1. Žádné nové ani zaokrouhlené číslo nad rámec zadání; chybějící = čárkovaný obdélník „[DATA GAP]".
2. Značka jistoty na každém slidu; `[EST]`, `[STALE]`, `[CLAIM]` a `[TARGET TBD]` vizuálně odlišené.
3. Headline = tvrzení s číslem, nikdy popis.
4. Část A: jedna myšlenka na slide (1 graf + 3 body, nebo 1 tabulka, nebo 1 big number). Část B: jeden exhibit na slide + max 3 body.
5. ČS červeně, konkurence ČR modrošedě, evropské benchmarky zelenošedě, ostatní šedě; horizonty plánu dle barev v kap. 3.
6. Nepoužívej logo ani brand ČS, Erste ani jiných bank; deck je nezávislý benchmark.
7. Zdroj na každém slidu ve formátu „Zdroj: … · značka".
8. Zachovej pořadí a číslování slidů (A01–A16, B01–B78).
9. Část A musí dávat smysl bez Části B; každý slide Části A má v zápatí odkaz na detail v Části B.

## 8. Kontrolní seznam před odevzdáním
- [ ] 16 + 78 artboardů 1920 × 1080; Část A v prvním řádku canvasu, sekce Části B v dalších řádcích.
- [ ] Každý headline je tvrzení s číslem; každý slide má zdroj a značku.
- [ ] Všechny `[DATA GAP]` jsou viditelné; `[STALE]` ceny mají štítek s datem zdroje.
- [ ] Řádek a série ČS vždy červeně; v tabulkách podbarven.
- [ ] Šablona BP (B54–B58) a šablona SWOT (B60–B63) jsou jednotné.
- [ ] Gantt B71 odpovídá tabulce 8.2 symbol po symbolu.
- [ ] Grafy bez legend tam, kde lze popsat série přímo; sloupce od nuly.
- [ ] Export: Část A PDF + PNG, Část B PDF + PNG, spojený PDF; kontrola v černobílém náhledu.
