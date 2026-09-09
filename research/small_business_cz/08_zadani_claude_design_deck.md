# ZADÁNÍ PRO CLAUDE DESIGN: Comprehensive deck v Harvard Business Review stylu
## „Small business v ČR 2021–2026: Kde Česká spořitelna vyhrává, kde prohrává a co má CEO rozhodnout"

> Toto zadání je samostatné: obsahuje strukturu, styl, texty a všechna data pro každý slide. Podkladový dokument (`FINAL_small_business_CZ_deep_dive.md`, 17 400 slov) je k dispozici pro kontext, ale deck musí být sestavitelný jen z tohoto souboru. Čísla NEMĚŇ a NEDOPLŇUJ – kde je uvedeno `[DATA GAP]`, zobraz to jako explicitní prázdné místo (viz styl), nikdy nevymýšlej hodnotu.

---

## 1. Formát a rozsah
- **Typ:** prezentační deck, 16:9 (1920 × 1080 px), každý slide = jeden artboard na canvasu, seřazené zleva doprava po sekcích (řádky = sekce).
- **Rozsah:** 32 slidů + 3 slidy přílohy (35 celkem). Nepřidávej slidy; pokud se obsah nevejde, zmenši text, ne počet zpráv.
- **Jazyk:** čeština; odborné zkratky EN (NIM, CoR, NPL, ARPU, NPS, RM) bez překladu. Čísla: tisícové mezery (1 178 tis.), desetinná čárka, jednotky vždy (mld. Kč, tis., %, pb).
- **Publikum:** CEO a představenstvo banky. Každý slide musí být čitelný samostatně (headline = závěr, ne popis).
- **Export:** PNG i PDF, tisknutelné černobíle (kontrast bez spoléhání na barvu).

## 2. Vizuální styl: Harvard Business Review (editorial, ne corporate)
**Princip:** vypadá jako článek v HBR převedený do slidů – hodně bílého prostoru, jedna silná myšlenka na slide, typografická hierarchie místo ozdob, grafy „Economist/HBR" střihu.

**Typografie**
- Headline: serif s vysokým kontrastem (např. *Tiempos*, *Playfair Display*, *Source Serif 4*), 44–54 px, max 2 řádky, tvar „tvrzení s číslem".
- Deck (podnadpis pod headlinem): sans (např. *Inter*, *IBM Plex Sans*), 20–22 px, šedá, 1–2 věty „so what".
- Tělo / popisky: sans 16–18 px; poznámky pod grafem 12–13 px šedé.
- Číselné „callouty": serif 96–140 px, jedno číslo na slide, s krátkým labelem pod ním.
- Žádné odrážky delší než 2 řádky; žádné odstavce delší než 4 řádky.

**Barvy (brand‑neutral, HBR paleta)**
- Papír: #FFFFFF; text: #111111; sekundární text: #6B6B6B; linky/mřížka: #D9D9D9.
- Akcent 1 (ČS / hlavní série): sytá tmavě červená #B5121B.
- Akcent 2 (konkurence / srovnání): tmavě modrošedá #1F3A5F.
- Akcent 3 (neutrální série): #8A8A8A. Světlé plochy: #F4F1EC (teplý krém pro „pull‑quote" bloky).
- Jistota dat: `[FACT]` plná barva; `[FACT‑S]` plná barva s tenkým obrysem; `[EST]` šrafování / 50 % opacity; `[DATA GAP]` prázdný obdélník s čárkovaným obrysem a nápisem „chybí – ČNB ARAD" apod. Legenda značek jednou na slide 3 a v zápatí každého grafu.

**Layouty (opakuj konzistentně)**
- L1 „Headline + jeden graf": headline nahoře (2/3 šířky), graf vlevo 60 %, vpravo 3 klíčové body.
- L2 „Big number": jedno obří číslo vlevo, vpravo 3–4 řádky vysvětlení, dole zdroj.
- L3 „Tabulka HBR střihu": bez svislých linek, jen tenké vodorovné, zvýrazněný řádek ČS (světle krémový podklad #F4F1EC), zebra ne.
- L4 „Dvě karty proti sobě" (ČS vs. konkurent).
- L5 „Matice 2×2 / heat‑map".
- L6 „Pull quote" – krémový blok přes celou šířku s jednou větou závěru (serif italic 36 px).
- Každý slide: tenká horní linka s názvem sekce vlevo (malé kapitálky, 12 px) a číslem slidu vpravo; zápatí: „Zdroj: …; značka jistoty" 12 px šedě.

**Grafy (HBR/Economist styl)**
- Bez 3D, bez stínů, bez rámečků, bez legendy, pokud jde popsat přímo u série. Osa Y začíná na nule u sloupců; u čar může být zkrácená s viditelným zlomem. Gridlines jen vodorovné, světle šedé. Popisky hodnot přímo u datových bodů, ne v tabulce pod grafem.
- Jedna barva na sérii ČS (červená), konkurence modrošedá, ostatní šedé; nikdy více než 4 barvy v grafu.
- Chybějící data = šedý čárkovaný obdélník s textem „[DATA GAP]" – neinterpolovat.

---

## 3. Struktura decku (35 slidů) s texty a daty

### SEKCE 0 – Otevření (slidy 1–4)

**Slide 1 – Titulní (L6 varianta)**
- Titul (serif 64 px): „Segment small business v České republice 2021–2026"
- Podtitul: „Konkurenční benchmark: Česká spořitelna vs. trh. Diagnostika pro CEO."
- Řádek: „FOP + PO s ročním obratem do 25 mil. Kč · září 2026 · pracovní verze pro strategickou diskusi"
- Spodní lišta: malé kapitálky „Hypothesis‑driven · Fact‑based · Action‑oriented"

**Slide 2 – Executive summary (L3, 7 řádků)**
Headline: „Sedm zjištění: segment roste, ekonomika segmentu se přesouvá do vkladů a rychlého úvěru – a ČS je v obou cenově nejméně konkurenceschopná"
Tabulka: číslo | zjištění | podpůrné číslo | značka
1. Segment roste, ne stagnuje | 1 203 tis. OSVČ (6/2026), 594,5 tis. firem (1/2026); hlavní OSVČ +16 % 2019→2025 | FACT‑S
2. Adresovatelný trh ≈ 1,2 mil. subjektů; přítok ~90 tis. FO + ~35 tis. s.r.o. ročně | akvizice se odehrává v přítoku | EST/FACT‑S
3. Revenue pool ≈ 15 mld. Kč/rok (8–25); třetina = depozitní marže | Moneta: úročené komerční vklady 42,6 % → 51,4 % za 3 roky | EST/FACT
4. Úvěrový tok nemá „vlastníka" | KB 47,9 → 47,9 mld. Kč (2021–24); Moneta nové SB úvěry 4,0 → 8,4 mld. Kč (2023→25) | FACT
5. ČS jediná v pětce se 149 Kč účtem a jediná, kdo v 2026 zdražil | Moneta, RB, ČSOB, Air Bank, Fio, Creditas: 0 Kč | FACT‑S
6. Konkurence soutěží úročením zůstatku a rychlostí úvěru | Air Bank 2,6 %, UCB 2,50 %, Creditas 1,40 %; Moneta 600 tis. Kč online do 15 min | FACT‑S
7. Datová stopa segmentu se zúžila | 125 tis. OSVČ v paušálu bez přiznání; EET zrušena 2023; e‑fakturace až 2030+ | FACT‑S

**Slide 3 – Jak číst čísla v tomto decku (L3 malá + legenda)**
Headline: „Jen 45 čísel v této analýze je plně ověřených z investorských výkazů; zbytek nese značku jistoty – a dvě klíčové řady chybí úplně"
Legenda značek: FACT (45) · FACT‑S (195) · FACT‑KB (8) · EST (72) · EXTRAP (4) · CLAIM (12) · DATA GAP (90). Vysvětlení jedním řádkem ke každé. Poznámka: „Rešerše 8.–9. 9. 2026; přímý přístup k ČNB, ČSÚ, ČSSZ a webům bank byl blokován; údaje FACT‑S pocházejí z indexovaných výtahů citovaných zdrojů."

**Slide 4 – Rozhodnutí pro CEO (L6 pull quote + 2 karty)**
Pull quote: „Otázka nezní, zda investovat do živnostníků. Otázka zní, zda přestat monetizovat viditelný poplatek a přesunout ekonomiku segmentu do depozitní marže, balíčků a předschváleného úvěru."
Karta A „Program small business 2027–28": vlastní P&L, cenová architektura, BB1–BB4. Karta B „Status quo": segment v retailu, dnešní ceník → přítok nových FOP a mikro‑s.r.o. dál k Air Bank, Monetě, Revolutu.

### SEKCE 1 – Definice (slidy 5–6)

**Slide 5 – (L3)** Headline: „„Small business" nemá v ČR úřední definici – banky si ji stanovují obratem a jejich prahy (50–60 mil. Kč) jsou 2–2,4× nad naší hranicí 25 mil. Kč"
Tabulka (rámec | kritérium | hranice | slabina): EU MSP – zaměstnanci + obrat – mikro < 10 zam., ≤ 2 mil. EUR (~50 mil. Kč) – 2× širší; Zákon o účetnictví – mikro ≤ 22 mil. Kč obratu (od 9/2025) – jen PO, bez výsledovky; ČNB – S.14 živnostníci vs. S.11 podniky – PO bez velikosti; Paušální daň – ≤ 2 mil. Kč – jen 11 % OSVČ; ČSSZ – hlavní/vedlejší – bez obratu; KB < 60 mil.; RB, UCB < 50 mil.; ČS ~1 mil. EUR (inzerát); ČSOB, Moneta DATA GAP; **naše: ≤ 25 mil. Kč, FOP + PO**.

**Slide 6 – (L1 sloupcový graf, 3 sloupce)** Headline: „Registrace ≠ aktivita: tři „velikosti trhu" se liší 3× – jediný obhajitelný jmenovatel pro penetraci je ČSSZ hlavní činnost"
Graf: RŽP registrované FO 2 029 tis. (12/2025) · ČSSZ evidované OSVČ 1 179 tis. (12/2025) · ČSSZ hlavní činnost 692 tis. (12/2025). Vpravo: „Marketingové výroky bank („každá čtvrtá nová OSVČ") pracují s registracemi a nadhodnocují." Zdroj: D&B via Kurzy.cz; ČSSZ via Podnikatel.cz [FACT‑S].

### SEKCE 2 – Velikost a struktura (slidy 7–11)

**Slide 7 – (L1 skládaný sloupcový graf 2019–6/2026)** Headline: „Počet OSVČ poprvé překročil 1,2 milionu; hlavní činnost roste +2,5 % ročně, ale zpomaluje – vedlejší zrychluje"
Data (celkem | hlavní | vedlejší): 12/2019 1 031 | 598 | 433 · 12/2021 1 078 | 634 | 444 · 12/2022 1 104 | 649 | 455 · 12/2023 1 127 | 669 | 458 · 12/2024 1 154 | 681 | 473 · 12/2025 1 179 | 692 | 486 · 6/2026 1 203 | >700 | >500 (tis.). Označ 2021 a 2024 složky jako EST (šrafování). Callout: „přírůstek hlavních: >20 tis./rok (2020–23) → +11 tis. (2025)". Zdroj: ČSSZ via Podnikatel.cz, Forbes, ČTK [FACT‑S].

**Slide 8 – (L2 big number)** Číslo: **125 449**. Label: „OSVČ v paušálním režimu k 1/2026 (+10 % ročně; ~18 % hlavních OSVČ)". Headline: „Paušální daň se stala výchozím režimem nových hlavních OSVČ – 125 tis. podnikatelů bez daňového přiznání, které lze scórovat jen z účtu"
Mini‑řada vpravo: 2021 >70 tis. · 2022 ~80 · 2023 ~100 · 2024 ~99 (EST) · 2025 ~114 · 2026 125,4 tis.; záloha I. pásmo 5 469 → 9 984 Kč. Zdroj: Finanční správa, MF [FACT‑S].

**Slide 9 – (L1 sloupce vznik vs. zánik firem 2023–2025 + linka stock)** Headline: „Firemní báze roste +3,1 % ročně a rekordní churn oběma směry čistí trh – každá pátá registrovaná firma je spící"
Data: vznik (D&B) 2024 ~30,6 tis. (EST) · 2025 34 621; zánik (CRIF) 2024 17 099 · 2025 16 853; stock 576 642 (2024) → 594 520 (2025; s.r.o. 567 228). Callout: „~20 % neaktivních (Bisnode) → ~475 tis. aktivních PO [EST]". Zdroj: D&B, CRIF, Bisnode [FACT‑S].

**Slide 10 – (L4 dvě karty + mini mapa jako 3 sloupce)** Headline: „Přítok, ne stock: ročně ~90 tis. nových FO a ~35 tis. s.r.o.; třetina OSVČ sedí v Praze a Středních Čechách, kde je tvorba nejrychlejší"
Karta 1 „Tok FO (CRIF)": 2024 +82 893 / −71 875; 2025 ~91,6 tis. nových (cit. Air Bank) / ~48 tis. ukončených; 1H 2026 nejvyšší čistý přírůstek za 6 let (19 nových na 10 zaniklých). Karta 2 „Regiony (ČSSZ 12/2021)": Praha 196 tis. (18 %), Středočeský 152 tis. (14 %), Jihomoravský 120 tis. (11 %); Praha ~150 OSVČ/1 000 obyv. vs. ČR ~103 [EST]. Poznámka: pobočky ČS 400 → 324 (2021→3/2026), KB 241 → 172, Moneta 153 → 123 [FACT].

**Slide 11 – (L1 sloupce podíl cizinců na nových FO + koláč stock)** Headline: „Cizinci jsou ~10 % stocku FOP, ale 10–30 % přítoku – nejrychleji rostoucí kohorta, dominují Ukrajinci"
Data: stock 131 738 (MPO 12/2024; UA 33 %, SK 20 %, VN 16 %) vs. >195 tis. (D&B 12/2025; UA 37,8 %) – zobraz obě s poznámkou „nesoulad metodik"; podíl na nových FO 10 % (CRIF 2024) → 30 % (D&B 2025). Zdroj: MPO, D&B, CRIF [FACT‑S].

### SEKCE 3 – Kondice segmentu (slidy 12–15)

**Slide 12 – (L1 dvě čáry 2019–2025 + 1H 2026, dvě osy nebo dva panely)** Headline: „Vlna úpadků je „mikro" a „mladá": bankroty FOP +26 % za dva roky, 28 % z nich podniká méně než 6 let; firemní bankroty nejvyšší od 2017"
Data FOP: 2019 7 822 · 2020 7 284 · 2021 6 311–6 362 · 2022 5 135 · 2023 4 943 · 2024 5 331 · 2025 6 213 · 1H 2026 3 260. PO: 680 · 609 · 730–741 · 700 · 651 · 686 · ≥697 · 418 (1H 2026). Callout: míra selhání FOP ~0,5 %, PO ~0,12 % [EST]. Zdroj: CRIF, InsolCentrum [FACT‑S].

**Slide 13 – (L3 malá tabulka + 1 big number 40 %)** Headline: „Platební morálka je chronicky mírně špatná: ~40 % faktur po splatnosti, 73 % firem přistoupilo na delší splatnost – dodavatelský úvěr supluje bankovní"
Data: faktury včas 59,2 % (2023) → 61,8 % (2024, D&B); splatnost 36 dní + čekání ≤ 21 dní (EOS 2025); 61 % hodnoty B2B faktur po splatnosti (Atradius 2025); 8 z 10 firem požádáno o delší splatnost, 73 % vyhovělo (Intrum); factoring 2025: postoupené pohledávky 330 mld. Kč (+11 %), poskytnuté prostředky 44 mld. Kč (+18 %, ČLFA). [FACT‑S]

**Slide 14 – (L3 timeline 6 sloupců 2021–2026)** Headline: „Dva šoky a jedno oživení: energie/inflace 2022–23 a odvody 2024–26 zdražily „vstupenku do podnikání" o 81 % nominálně"
Řádky: repo (konec roku) 3,75 % · 7,00 % · 6,75 % · 4,00 % · 3,50 % · 3,75 % (od 19. 6. 2026); inflace 3,8 · 15,1 · 10,7 · 2,4 · ~2,5 · ~2 %; min. odvody OSVČ (Kč/měs.) 4 981 · 5 468 · 5 666 · 6 820 · 7 902 · 9 026 (→ 8 311 od 7/2026); paušál I. pásmo 5 469 · 5 994 · 6 208 · 7 498 · 8 716 · 9 984; událost: kompenzační bonus / energie / zrušení EET / konsolidační balíček / oživení / min. VZ 40 %. Značky: repo 2021–25 FACT‑KB, zbytek FACT‑S.

**Slide 15 – (L2 big number 25 % + 3 body)** Číslo: **25 %**. Label: „mikro a malých firem se za 3 roky vůbec pokusilo získat externí financování (AMSP 2024)". Headline: „Bariérou penetrace úvěru není nabídka, ale postoj majitelů – a nebankovní zdroje rostou"
Body: >1/3 majitelů úvěr odmítá principiálně; ~20 % firem bez provozní rezervy; firmy půjčující si mimo banky <10 % (2019) → ~15 % (2022); nové úvěry podnikům 9,1 % HDP (1Q 2026); NRB záruky 16–24 mld. Kč/rok 2021–22 vs. Národní záruka >2 mld. Kč. [FACT‑S]

### SEKCE 4 – Bankovní trh (slidy 16–25)

**Slide 16 – (L1 indexovaný čárový graf, 2021 = 100, plus absolutní hodnoty)** Headline: „Úvěry small business rostou dvouciferně tam, kde se banka na segment zaměřila; KB čtyři roky stagnovala – segment je „contestable""
Série: KB „Loans to small businesses" 47,9 (2021) · 46,8 · 47,5 · 47,9 · 50,3 (2025) · 51,2 (3/2026) mld. Kč; Moneta nezajištěné SB úvěry + KTK 12,1 (2022) · 13,5 · 16,2 · 20,5 (2025) · 21,5; ČSOB SME 105,2 (2024) · 115,4 (2025) · 120,1 (3/2026); ČS: prázdný čárkovaný obdélník „segment nereportován". Zdroj: KB F&F, Moneta IR, ČSOB fact sheet [FACT].

**Slide 17 – (L1 sloupce ročních nových objemů)** Headline: „Moneta zdvojnásobila nové small‑business úvěry za dva roky při nákladech rizika blízko nuly – důkaz, že poptávka existuje"
Data: nové Small Business Instalment Loans 2023 3,99 · 2024 6,36 · 2025 8,36 mld. Kč · 1Q 2026 2,14 (y/y +20 %); NPL Commercial 1,2 % → 0,9 %; impairment Commercial FY 2024 −16 mil. Kč, 1Q 2026 +22 mil. Kč (rozpuštění). Zdroj: Moneta IR [FACT].

**Slide 18 – (L3 cenový benchmark, řádek ČS zvýrazněn)** Headline: „ČS je jediná v pětce se 149 Kč základním účtem a jediná, kdo v roce 2026 zdražil; trh se rozdělil na „0 Kč základ" a „placený balíček""
Řádky (banka | základní účet | podmínky 0 Kč | vyšší varianty | úročení zůstatku): ČS 149; 75 (příjem ≥10 tis. + úvěr); 0 jen start‑upy | 599/899 od 3/2026 (+100) | žádné veřejné · ČSOB 0 | 129 | DATA GAP · KB 99; 0 v Profi programu | Gold | DATA GAP · RB 0 | 99/299 | DATA GAP · Moneta 0 | – | DATA GAP · UCB 0 START; TOP 350 s odpuštěním | – | bonus 2,50 % · Air Bank 0 | – | 2,6 % do 300 tis. · Fio 0 | – | DATA GAP · Creditas 0 | – | 1,40 % bez stropu. Zdroj: weby bank, Finmag 2026 [FACT‑S]. Poznámka: „historie 2021/2023 DATA GAP".

**Slide 19 – (L4 dvě karty ČS vs. Moneta, + KB jako třetí menší)** Headline: „V rychlém nezajištěném úvěru definují standard Moneta a KB; ČS má nižší limit a nezveřejňuje sazbu ani rychlost"
ČS: standard 500 tis. Kč bez zajištění; sazba DATA GAP; rychlost DATA GAP; start‑up 1,2 mil. Kč na 7 let bez historie (nejvyšší v pětce). Moneta: 2,5 mil. Kč bez zajištění; online do 600 tis. Kč, rozhodnutí do 15 min, podpis online; „garance nejnižšího úroku" od 16. 3. 2026; 12 měsíců podnikání, bez výkazů. KB: 5 mil. Kč, 1 mil. Kč bez dokládání příjmů, od 5,9 %, online pro klienty s účtem 6–12 měsíců. ČSOB: 150 tis. Kč ihned, limit 1,5 mil. [FACT‑S]

**Slide 20 – (L3 matice banka × dimenze, barevná škála 1–5, hvězdičky pro chybějící data)** Headline: „Benchmark v sedmi dimenzích: Moneta 30 bodů, KB 25, ČSOB 23, ČS 20, RB 18 – ČS vítězí jen v distribuci"
Dimenze × ČS/ČSOB/KB/RB/Moneta: definice 3/3/4/3/4; cena účtu 1/4/3/5/5; nezajištěný úvěr 3/3/4/?/5; digitál 3*/3*/4/2*/4; distribuce 5/3*/4/2*/2; finanční síla 3*/4/3/2*/5; priorita 2*/3*/3/2*/5. Poznámka: „* neúplná data; skóre = expertní syntéza [EST]".

**Slide 21 – (L1 horizontální sloupce čitatelů + prázdné obdélníky)** Headline: „Jediné tvrdé čitatele podílů jsou KB, Moneta a Air Bank; ČS je v segmentu statisticky neviditelná"
Data: KB ≤ 242 tis. ne‑fyzických klientů (stabilně 2021–2026, EST) · Moneta 125 tis. komerčních klientů (~2022) · Air Bank >65 tis. podnikatelských klientů (1/2026); „¼ nových OSVČ 2025" (CLAIM) ≈ 23 tis./rok (EST) · ČS DATA GAP · Fio, Creditas, UCB, RB, Revolut DATA GAP. Vpravo: „KB čitatel stagnuje, počet subjektů roste → podíl velkých bank na subjektech klesá [EXTRAP]".

**Slide 22 – (L1 skládaný sloupec 3 scénáře)** Headline: „Revenue pool segmentu je řádově 15 mld. Kč ročně (8–25) – a jeho největší složka, depozitní marže, eroduje"
Data (nízký/střední/vysoký): NII z úvěrů 3,6 / 6,3 / 10,0; NII z vkladů 2,5 / 5,3 / 9,0; poplatky 1,8 / 3,9 / 6,5; celkem ≈ 8 / 15 / 25 mld. Kč. Callout: „±1 pb depozitní marže = ±3,5 mld. Kč trhu". Vstupy střed: úvěry 180 mld. × 3,5 %; vklady 350 mld. × 1,5 %; 1,1 mil. účtů × 3,5 tis. Kč. Značka: EST ±40 %; jmenovatele ČNB DATA GAP.

**Slide 23 – (L1 dvě čáry 4Q2022–1Q2026)** Headline: „Komerční klienti Monety přesunuli za tři roky 9 procentních bodů vkladů z běžných na úročené účty – to je hrozba pro třetinu poolu"
Data Moneta Commercial: běžné účty 43,4 (4Q22) · 41,6 · 53,0 · 54,0 · 52,8 (1Q26) mld. Kč; spořicí+termínované 32,5 · 43,0 · 51,8 · 54,4 · 55,8; podíl úročených 42,6 % → 50,4 % → 48,9 % → 50,1 % → 51,4 %. Kontext: challengeři úročí 1,4–2,6 %; repo 3,75 %. Zdroj: Moneta IR [FACT].

**Slide 24 – (L5 mapa strategických skupin: osa X šíře nabídky, osa Y cenová agresivita/digitální rychlost)** Headline: „Čtyři modely obsluhy: ČS mezi univerzálními incumbenty s nejširší nabídkou a nejnižší cenovou agresivitou"
Body: Univerzální incumbenti (ČS, ČSOB, KB, RB) vpravo dole; Fokusovaný růstový hráč (Moneta) vpravo nahoře; Digital‑first akvizitéři (Air Bank, Revolut, Partners 2026) vlevo nahoře; Infrastrukturní/niche (Fio, Creditas, UCB, Wise) střed. ČS zvýraznit červeně; u každé skupiny 1 řádek „co vyhrávají / co jim chybí".

**Slide 25 – (L3 profily 9 bank, 1 řádek každá)** Headline: „Devět bank v jednom pohledu: kdo segment reportuje, kdo ho má jako prioritu a kdo jen sbírá účty"
Sloupce: banka | pozice v segmentu (1 číslo) | model | silná stránka | slabina | priorita segmentu. Řádky: ČS (324 poboček, 4 565 tis. klientů; segment nereportován) · ČSOB (SME 120,1 mld., +11 % y/y) · KB (SB 51,2 mld., KB+ 93 %) · RB (účet 0 Kč, živnostníci +11,2 %) · Moneta (nové SB úvěry 8,4 mld., 37 % výnosů z Commercial) · UCB (~450 tis. klientů, bonus 2,50 %) · Air Bank (65 tis. podnikatelů, bez úvěru) · Fio (1,55 mil. klientů, API, terminály) · Creditas (>250 tis. klientů, 1,40 % bez stropu). Sekundárně jedním řádkem: Revolut 1,3 mil. uživatelů ČR, MAU firem +31 %.

### SEKCE 5 – Trendy (slidy 26–27)

**Slide 26 – (L5 heat‑map pravděpodobnost × dopad, 13 bodů)** Headline: „Do 2030 rozhodují distribuční, ne produktové disruptory: embedded finance a Revolut jako hlavní účet sedí v pravém horním kvadrantu"
Body (P/D): embedded finance V/S–V (2027–30); Revolut hlavní účet S/V (2026–29); AMLR/AMLA V/S (2027–28); IPR EUR instant V/S (2027); PSD3/PSR V/S (≈2028); konsolidační balíček jistá/S; novela účetnictví V/N–S; Bank iD pro firmy V/S; ViDA V(2030+)/N; AI scoring V/S–V (DATA GAP); generační výměna ?/V (DATA GAP); ESG N–S/N; kyber ?/S. Značka: EST (expertní úsudek).

**Slide 27 – (L3 regulační kalendář jako horizontální timeline 2026–2035)** Headline: „Regulační vlna 2027–2028 je „compliance shock" pro všechny – pro největší banku je to výhoda škály, ne hrozba"
Body: 1/2027 IPR přijímání EUR instant; 7/2027 IPR odesílání; 10. 7. 2027 AMLR/AMLD6; 1. 1. 2028 AMLA dohled; ≈2028 PSR/PSD3; 7/2030 ViDA přeshraniční e‑fakturace; 1/2035 ViDA domácí. Vedle: Bank iD 5,3 mil. uživatelů (H1 2026); datové schránky 4,3 mil. (6/2026); audit malých jednotek zrušen 1/2026. [FACT‑S]

### SEKCE 6 – SWOT, TOWS, big bets (slidy 28–32)

**Slide 28 – (L5 SWOT 2×2, každá buňka 4 body s ikonou dopadu V/S/N)** Headline: „SWOT relativně ke konkurentům: síla ČS je v bázi a fundingu, slabina v ceně, viditelnosti a rychlosti"
S: 4 565 tis. klientů, 324 poboček (vs. KB 172, Moneta 123) · NIM 2,12 % vs. KB 1,72 % · nejpoužívanější banka ve Fakturoidu 2025 · start‑up úvěr 1,2 mil. Kč (nejvyšší v pětce). W: účet 149/75 Kč, jediné zdražení 2026 · segment nereportován (KB, Moneta ano) · nezajištěný úvěr 500 tis. bez sazby/rychlosti (Moneta 2,5 mil./15 min) · bez ekosystémového kanálu (KB Lemonero 29 %, Roger) · žádné veřejné úročení zůstatku. O: přítok 90 tis. FO + 35 tis. s.r.o./rok · cizinci 10–30 % nových FOP · paušál 125 tis. bez výkazů = scoring z účtu · depozitní marže 1/3 poolu · úvěrový tok „contestable" (KB stagnace, Moneta CoR ≈ 0). T: Air Bank 65 tis. klientů, s.r.o. od 2026, 2,6 % · Moneta +31 % nové SB úvěry, garance sazby · Revolut 1,3 mil., MAU firem +31 % · eroze depozitní marže (challengeři 1,4–2,6 %) · bankroty FOP +16 %, 28 % mladých, NPL živnostníků 5,1 % vs. 1,5 % skupina.

**Slide 29 – (L5 TOWS 2×2, 3 body na buňku)** Headline: „TOWS: čtyři strategické směry – předschválený úvěr z retailu, reset ceny, embedded kanál, first account pro nové subjekty"
SO: předschválený kontokorent/úvěr z retailové báze (parita s Monetou) · start‑up balíček vč. cizinců (Bank iD, UA/VN) · tiering úročení podmíněný aktivním účtem. ST: graduační cesta (kontokorent, terminál, SME úvěr, factoring – to Air Bank/Revolut nemají) · transakční early‑warning pro mladé FOP · compliance jako produkt pro FOP‑cizince. WO: „0 Kč základ + placená hodnota + úročený zůstatek" · nativní API ve Fakturoidu, úvěr z faktur, Shoptet · segment jako řízená jednotka (P&L, KPI, IR řada). WT: zvednout a zveřejnit rychlý úvěr (1 mil. Kč online) · online s.r.o. onboarding s QSIGN · nezdražovat viditelný atribut.

**Slide 30 – (L3 big bets tabulka 5 řádků)** Headline: „Pět big bets: dva chrání ekonomiku segmentu (vklady, úvěr), dva řeší distribuci (SW, first account), pátý čeká na data"
Řádky (co | velikost [EST] | obtížnost | horizont): BB1 Reset ekonomiky účtu – chrání ~70 mld. Kč vkladů (1 pb = ~0,7 mld. Kč/rok), riziko poplatků 0,2–0,4 mld. Kč/rok – střední – 6–12 měs. · BB2 Předschválený digitální úvěr – 10–15 mld. Kč nových úvěrů/rok, kniha 20–30 mld. do 3 let, NII 0,8–1,2 mld. Kč/rok – střední–vysoká – 12–24 měs. · BB3 Embedded finance – 3–5 mld. Kč objemů/rok, 0,1–0,3 mld. Kč výnosů, 20–30 tis. digitálních FOP/rok – vysoká – 12–36 měs. · BB4 First account – 35–40 tis. nových SB klientů/rok (30 % přítoku), +0,1–0,2 mld. Kč/rok, kumulativně 0,5–1 mld. do 5 let – střední – 6–18 měs. · BB5 Nástupnictví – DATA GAP; řád ~47 tis. převodů do 2030 – vysoká – 24–60 měs.

**Slide 31 – (L4 tři karty)** Headline: „Tři no‑regret moves s nulovým nebo nízkým nákladem, které lze spustit tento kvartál"
Karta 1: Definice a reporting segmentu (SB ≤ 25 mil. Kč; P&L, klienti, úvěry, vklady běžné vs. úročené, poplatky; IR řada „micro & small business"). Karta 2: Zveřejnit sazbu a čas rozhodnutí rychlého úvěru; online limit 1 mil. Kč. Karta 3: Uzavřít datové mezery do 30 dnů (ČNB ARAD, ceníky 2021/2023/2026, VZ 2025, CRIF věk jednatelů, průzkumy SME Banking Club/Ipsos).

**Slide 32 – (L3 timeline 6 týdnů + L6 závěr)** Headline: „Dalších šest týdnů: interní datová kotva → externí řady → customer research → business case → rozhodnutí"
Týden 1–2 interní data ČS a podíl na nových registracích; 2–3 ČNB ARAD, ceníky, VZ 2025, průzkumy; 3–4 20–30 hloubkových rozhovorů + kvantitativní vlna n≈500 (cena účtu vs. úročení vs. rychlost úvěru); 4–5 business case BB1–BB4 + pilot „0 Kč + tiering"; 6 rozhodnutí program vs. status quo. Pull quote dole: „ČS drží stock. O podílu v roce 2030 se rozhoduje v přítoku – a ten dnes teče jinam."

### PŘÍLOHA (slidy 33–35)

**Slide 33 – (L3)** „Příloha A: primární IR řady bank 2019–1Q 2026" – tabulka: ČS čisté úvěry 729 → 1 206 mld. Kč, vklady 1 000 → 1 655, pobočky 463 → 324, NIM 2,12 → 2,11 %, NPL 1,8 → 1,5 %; KB SB úvěry 45,9 (2020) → 51,2; KB klienti 1 664 → 1 798 tis. (FO 1 407 → 1 556); Moneta Commercial úvěry 82,8 (2022) → 109,1; Moneta Commercial vklady 77,2 → 109,3; ČSOB SME 105,2 (2024) → 120,1. [FACT]

**Slide 34 – (L3)** „Příloha B: co chybí a kde to dohledat" – 10 řádků: interní data ČS (klienti, úvěry, vklady, poplatky segmentu); podíl ČS na nových registracích; ČNB ARAD řady; ceníky 2021/2023/2026; průzkumy podílů a NPS; hodnocení aplikací; věk majitelů (CRIF, ČSSZ); ziskovost mikrofirem dle NACE (ČSÚ SBS); počty podnikatelských klientů Fio/Creditas/UCB/RB/Revolut; výroky managementu ke small business.

**Slide 35 – (L3 malá)** „Příloha C: zdroje a metodika" – primární IR fact sheety (KB F&F 1Q 2026, ČSOB fact sheet 1Q 2026, Moneta Basic financial data 4Q 2024 / 1Q 2026, ČS Key figures Q1 2026); státní statistika (ČSSZ, ČSÚ, MPO, FS, ČNB) přes výtahy; odborné organizace (CRIF, D&B, AMSP, ČLFA, InsolCentrum, EOS, Atradius, Intrum); weby bank a Finmag 2026. Metodická výhrada jedním odstavcem (síťová blokace, 200 dotazů, FACT‑S).

---

## 4. Pravidla, která nesmíš porušit
1. **Žádné nové číslo.** Používej jen hodnoty z tohoto zadání. Chybějící = čárkovaný obdélník „[DATA GAP]".
2. **Značky jistoty na každém slide** (zápatí grafu nebo tabulky). Odhady [EST] vizuálně odliš (šrafování / 50 % opacity).
3. **Headline = závěr s číslem**, nikdy popis („Vývoj OSVČ" je špatně).
4. **Jedna myšlenka na slide.** Maximálně 1 graf + 3 body, nebo 1 tabulka, nebo 1 big number.
5. **ČS vždy červeně, konkurence modrošedě, ostatní šedě.** Nikdy víc než 4 barvy v grafu.
6. **Neuváděj Českou spořitelnu jako klienta ani nepoužívej její logo/brand** – deck je nezávislý benchmark; pouze název v textu.
7. **Zdroj na každém slide** ve formátu „Zdroj: KB Facts & Figures 1Q 2026; Moneta IR [FACT]" nebo „Zdroj: ČSSZ via Podnikatel.cz [FACT‑S]".
8. Zachovej pořadí slidů a čísla sekcí; každý slide má číslo a název sekce v horní liště.

## 5. Kontrolní seznam před odevzdáním
- [ ] 35 artboardů 1920×1080, seřazených po sekcích.
- [ ] Každý headline je tvrzení s číslem; každý slide má zdroj a značku jistoty.
- [ ] Všechna „[DATA GAP]" místa jsou viditelná, ne zamaskovaná.
- [ ] Řádek/série ČS je vždy zvýrazněn červeně; tabulka 18 má řádek ČS podbarven.
- [ ] Grafy bez legend tam, kde lze popsat série přímo; osy sloupců od nuly.
- [ ] Export PNG + PDF; kontrast ověřen v černobílém náhledu.
