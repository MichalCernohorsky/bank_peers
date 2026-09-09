# 01 – Definice segmentu „small business" v ČR: mapování a porovnání rámců

Pracovní definice projektu: **small business (SB) = FOP (OSVČ/živnostníci) + PO (s.r.o., a.s., družstva, spolky-podnikatelé) s ročním obratem do 25 mil. Kč.** Období 2021–2026. Datum rešerše: 2026-09-08.

> Metodická poznámka k této rešerši: síťový proxy v prostředí blokoval přímé načtení všech primárních webů (cnb.cz, csu.gov.cz, mpo.gov.cz, financnisprava.gov.cz, cssz.gov.cz, weby bank, PDF výročních zpráv). Vše níže pochází z výsledků vyhledávání (úryvky indexovaných stránek) – kde úryvek nestačil, je uvedeno `[DATA GAP]` s URL, kde ověřit. Žádné číslo není dopočteno bez označení `[EST]`.

---

## (a) Hypotézy k definicím

- **H-D1.** Neexistuje jediná úřední definice „small business" v ČR; každý zdroj (EU/MPO, ČSÚ, ČNB, ČSSZ, FS, banky) používá jiné kritérium (zaměstnanci vs. obrat vs. právní forma vs. sektor ESA vs. daňový režim). Naše obratová hranice 25 mil. Kč nemá přímý ekvivalent v žádné veřejné statistice → každé číslo z trhu bude nutné korigovat.
- **H-D2.** Bankovní interní segmentace v ČR je obratová a hranice small business/SME leží typicky mezi 50 a 60 mil. Kč (KB 60 mil., RB 50 mil., UniCredit 50 mil.); náš práh 25 mil. Kč je tedy **užší** než „small business" většiny bank – jejich segmentová čísla náš segment nadhodnocují.
- **H-D3.** ČNB statistika je pro FOP použitelná (podsektor domácností „živnostníci"), pro PO nikoli – úvěry nefinančním podnikům ARAD nečlení podle velikosti podniku, pouze podle objemu úvěru (MIR) a odvětví (CZ-NACE).
- **H-D4.** Daňová optika (paušální daň, paušální výdaje, limit 2 mil. Kč) definuje „nejmenší" jádro FOP; hlavní vs. vedlejší činnost (ČSSZ) je nejlepší proxy pro „aktivní" FOP.
- **H-D5.** Rozdíl registrovaní vs. aktivní je řádově 40–45 % u FOP (RŽP ~2,03 mil. vs. ČSSZ ~1,17 mil.) – bez sjednocení této definice nelze porovnávat penetraci bank.

---

## (b) Datové tabulky s poznámkami

### 1. EU / MPO / NRB definice MSP (doporučení Komise 2003/361/ES)

| Kategorie | Zaměstnanci | Roční obrat | NEBO bilanční suma | Kdo v ČR používá |
|---|---|---|---|---|
| Mikropodnik | < 10 | ≤ 2 mil. EUR | ≤ 2 mil. EUR | MPO (Sdělení č. 7/2023 Sb. – české znění doporučení), NRB (záruční programy), ČSÚ (SBS – zaměstnanecké pásmo), dotační programy OP TAK |
| Malý podnik | < 50 | ≤ 10 mil. EUR | ≤ 10 mil. EUR | dtto |
| Střední podnik | < 250 | ≤ 50 mil. EUR | ≤ 43 mil. EUR | dtto |

- `[FACT]` Hodnoty dle doporučení Komise 2003/361/ES ze dne 6. 5. 2003; české znění vyhlášeno Sdělením MPO č. 7/2023 Sb. (zakonyprolidi.cz/cs/2023-7; ASPI). Kritérium počtu zaměstnanců je primární – při jeho překročení se kategorie mění bez ohledu na finanční kritéria; obrat a bilanční suma jsou alternativní (stačí splnit jedno) (NRB, „Vysvětlení a definice malých a středních podniků"; Uživatelská příručka EK k definici MSP, ec.europa.eu/docsroom/documents/42921).
- `[FACT]` Do počtu zaměstnanců se nezapočítávají učni/studenti v odborném vzdělávání ani doba mateřské/rodičovské (Uživatelská příručka EK).
- `[FACT]` Zákon č. 47/2002 Sb., o podpoře malého a středního podnikání, na tuto definici odkazuje a je právním základem pro MPO „Výroční zprávu o implementaci Strategie podpory MSP" (§ 9); zpráva za rok 2024 schválena vládou 26. 1. 2026 (mpo.gov.cz, VZ-Strategie-MSP-za-rok-2024.pdf). Z ní: `[FACT]` v roce 2024 se na vývozu ČR podílelo 17 020 MSP, vývoz 1 293,1 mld. Kč (+11,6 % y/y), podíl MSP na vývozu 32,2 % (MPO, VZ Strategie MSP za rok 2024).
- `[FACT]` NRB program Národní záruka: limit na jednoho podnikatele = do 250 zaměstnanců a obrat do 50 mil. EUR ročně, tj. EU definice MSP; ČSOB je jedním z 8 smluvních partnerů; program překonal 2 mld. Kč (MPO tisková zpráva, zpravy.kurzy.cz/857043).
- `[FACT]` ČSÚ SBS: velikost podniku dle „počtu zaměstnaných osob" = evidenční počet zaměstnanců + pracující majitelé a spolupracující členové domácnosti (pokud je to jejich hlavní činnost) + osoby na DPP/DPČ (ČSÚ, Roční strukturální statistika průmyslu – metodika). Starší publikace ČSÚ (2006) používala pásma 1–9 / 10–99 / 100–249 s odkazem na zákon 47/2002 Sb. `[DATA GAP]` aktuální pásma v SBS (Eurostat standard 0–9 / 10–49 / 50–249 dle nařízení (EU) 2019/2152) ověřit na csu.gov.cz/vykazy/podnikova_strukturalni_statistika2014.
- **Přepočet na naši definici:** 2 mil. EUR ≈ 50 mil. Kč `[EST]` (při kurzu ~25 CZK/EUR) → EU „mikropodnik" je obratově **2× širší** než náš SB (25 mil. Kč) a navíc primárně zaměstnanecký. Náš segment ≈ „mikropodniky + část malých podniků do 25 mil. Kč obratu".

### 2. ČNB – segmentace úvěrové statistiky

| Nástroj ČNB | Přesný název řady / tabulky (dle ARAD a zrcadla kurzy.cz) | Definice / jednotka | Co pokrývá z našeho SB |
|---|---|---|---|
| ARAD – Bankovní statistika – Klientské úvěry | „Klientské úvěry podle sektorového hlediska (Kč + cizí měna)" – podsektory: *Nefinanční podniky* (S.11, vč. „Nefinanční podniky soukromé národní / pod zahraniční kontrolou / veřejné"), *Domácnosti – obyvatelstvo*, *Domácnosti – živnosti* (S.14 – FOP), *Domácnosti – NISD* (S.15) | Stav ke konci měsíce, rezidenti, banky + pobočky zahr. bank; sektory dle ESA 2010 od 2014 | FOP: **plně** (podsektor „živnostníci"); PO: jen jako součást S.11 bez členění podle velikosti |
| ARAD – Nově čerpané úvěry | „Nově čerpané klientské úvěry podle sektorového a subsektorového hlediska (Kč)" | Toky za měsíc | dtto |
| ARAD – Vklady | „Domácnosti – živnosti (rezidenti) – vklady podle druhového hlediska (Kč)"; „Vklady a přijaté úvěry od klientů celkem" | Stav | FOP vklady – plně |
| ARAD – Úvěry podle odvětví | „Klientské úvěry podle odvětví (CZ-NACE) – podle sekcí (Kč / Kč + cizí měna)" a „…podrobné" | Odvětvová struktura, ne velikost | PO i FOP smíšeně, bez velikostního klíče |
| Harmonizovaná úroková statistika (MIR) | „Úrokové sazby MFI – nové obchody – úvěry nefinančním podnikům" v členění **do 7,5 mil. Kč / 7,5–30 mil. Kč / nad 30 mil. Kč** | Dle nařízení ECB (EU) č. 1072/2013 (ECB/2013/34); sektor S.11; domácnosti S.14+S.15 | Objem úvěru jako *proxy* velikosti podniku (ne obrat) |
| Šetření úvěrových podmínek bank (BLS) | Čtvrtletní dotazník, 19 bank; segmenty: nefinanční podniky (**malé a střední** vs. **velké**), domácnosti (úvěry na bydlení, spotřebitelské) | Kvalitativní (difuzní index) | SME jako celek; `[DATA GAP]` přesná definice „malé a střední podniky" ve „Slovníčku pojmů" (cnb.cz/cs/statistika/setreni-uverovych-podminek-bank/ – dokument „Dotazník, metodologie a slovníček pojmů") – nedostupné přes proxy |
| Zpráva o finanční stabilitě (ZFS) | ZFS jaro 2025 (data k 31. 12. 2024, publ. 23. 6. 2025); ZFS podzim 2025 (data k 30. 6. 2025, publ. 15. 12. 2025) | Analýza rizik sektoru nefinančních podniků a domácností; zátěžové testy | `[DATA GAP]` zda ZFS člení úvěry podnikům podle velikosti (AnaCredit / CRÚ) – ověřit v PDF zfs_jaro_2025.pdf, zfs_podzim_2025.pdf |
| Centrální registr úvěrů (CRÚ) | Registr úvěrů právnických osob a fyzických osob-podnikatelů | Neveřejný na úrovni klienta; agregáty v ZFS | PO + FOP, ale bez obratového členění ve veřejných výstupech |

Poznámky:
- `[FACT]` Metodický list ARAD k úvěrům a vkladům obyvatelstva/živností existuje (cnb.cz/docs/ARADY/MET_LIST/tuvob_cs.pdf) – `[DATA GAP]` přesné znění definice podsektoru „živnostníci" (fyzické osoby s IČO podnikající na vlastní účet, zařazené v S.14) – ověřit tamtéž.
- `[FACT]` Od roku 2014 zavedeno nové členění sektorů podle ESA 2010; vykazují banky a pobočky zahraničních bank v ČR (ČNB, Metodické poznámky – Měnová a finanční statistika).
- `[FACT]` MIR, červenec 2025: sazba nových úvěrů nefinančním podnikům (bez kontokorentů, revolvingů a kreditních karet) 4,55 %; do 7,5 mil. Kč 5,45 %; 7,5–30 mil. Kč 5,05 %; nad 30 mil. Kč 4,43 % (ČNB Komentář k úrokovým sazbám MFI, červenec 2025, via zpravy.kurzy.cz/826640). Pásmo „do 7,5 mil. Kč" je jediná ČNB veřejná řada, která se blíží úvěrům malých podniků.
- `[FACT]` Právní režim: úvěr fyzické osobě-podnikateli (na IČO) se neřídí zákonem o spotřebitelském úvěru, ale občanským zákoníkem; ČNB varuje před „zastřenými spotřebitelskými úvěry" sjednávanými na IČO (ČNB, Upozornění pro veřejnost). To je důvod, proč banky FOP vedou v odděleném produktovém i rizikovém režimu.
- **Korekce k naší definici:** ČNB „živnostníci" = *všichni* FOP bez obratového limitu (i FOP nad 25 mil. Kč – nepatrná menšina `[EST]`) → překryv vysoký. ČNB „nefinanční podniky" = všechny PO od mikro po korporace → překryv nízký bez dodatečného klíče; jediný nepřímý filtr je objem úvěru do 7,5 mil. Kč (MIR).

### 3. Bankovní interní segmentace – přehled po bankách

| Banka | Název segmentu na webu | Hranice SB vs. SME/corporate (obrat) | Obsluhový model | Odlišné produkty FOP vs. PO | Segment reporting (VZ / IR) |
|---|---|---|---|---|---|
| **Česká spořitelna** | „Firmy a podnikatelé" (csas.cz/cs/firmy); podsekce „Účty pro podnikatele a malé firmy" `[FACT]` | `[FACT – sekundární: inzerát]` role „Firemní bankéř" = komplexní obsluha malých firem a podnikatelů s ročním obratem **do 1 mil. EUR** (~25 mil. Kč `[EST]`) (jooble.org, inzerát ČS 2026). `[DATA GAP]` oficiální hranice SME/Large Corporate (ČS – Corporate Banking) – ověřit na csas.cz/cs/firmy a ve VZ 2024 | Pobočky + firemní bankéř pro malé firmy; „Česká spořitelna – Corporate Banking" pro firmy; digitál George `[FACT – web]` | Ano: Podnikatelský účet **Živnostník** / **Klasik** / **Maxi** `[FACT]`; Maxi má obratový limit `[DATA GAP]` (úryvek uvádí chybně „60 mld. Kč" – ověřit, zda 60 mil. Kč) | VZ 2024: segmenty **Retail** a **Corporates**; Corporates = „obchodní aktivity s firemními klienty různé velikosti obratu (SME a Large Corporate), komerční nemovitosti a veřejný sektor" + dceřiné (Factoring ČS, REICO, část Leasing ČS, Erste Grantika, Global Payments…); Retail obsahuje SSČS, ČSPS, Investown, část Leasing ČS `[FACT]`. Erste Group: Retail = „private individuals, micros, free professionals" v odpovědnosti retailové sítě `[FACT]`. `[FACT]` VZ 2024: firemní vklady v segmentu SME poprvé 100 mld. Kč. **Podnikatelé/mikra jsou v ČS reportováni uvnitř Retail, ne Corporates** → náš SB je rozdělen mezi dva segmenty. |
| **Komerční banka** | „Živnostníci a malé firmy" / „Podnikatelé a malé firmy" (kb.cz/cs/podnikatele-a-firmy) vs. „Střední a velké firmy, instituce" (kb.cz/cs/korporace-a-instituce) `[FACT]` | `[FACT]` korporátní sekce = „firmy s obratem **od 60 mil. Kč**" → small business < 60 mil. Kč | Pobočky, bankéř; od 2026 převod podnikatelů a malých firem do nové digitální banky **KB+** `[FACT]` (komentář k výsledkům 4Q 2025) | Ano: účty pro OSVČ v tarifech, tarif „Start Business" zdarma pro začínající, „Profi účet pro začínající podnikatele", KB Podnikatelské finance `[FACT]` | Segmenty: **Retail Banking, Corporate Banking, Investment Banking, Other** `[FACT]`. Ve výsledcích KB komentuje „small business" portfolio uvnitř retailu (opravné položky 2024 v retailu „spotřebitelské úvěry a small business") `[FACT]`. `[DATA GAP]` přesná definice Retail vs. Corporate ve VZ 2024 (KB-vyrocni-zprava-2024.pdf) |
| **ČSOB** | csob.cz „Firmy" → „Podnikatelé a malé firmy" / firemní bankovnictví `[DATA GAP – web blokován]`; obsahová platforma „Průvodce podnikáním" pro malé a střední firmy `[FACT]` | `[DATA GAP]` – sekundární úryvky se rozcházejí: KBC segment „Retail/SME" údajně do 300 mil. Kč (citfin.cz), Corporate/SME od 200 mil. Kč a mid-cap od 300 mil. Kč (LinkedIn profil) – **neověřeno**. Slovenská ČSOB: „Podnikatelia a malé firmy" = obrat do 2,5 mil. EUR `[FACT – csob.sk]` (indikace skupinové logiky KBC) | Firemní bankéři („budovat vztahy… menších i středních firem") `[FACT – csob.jobs.cz]`; pobočky ČSOB + Poštovní spořitelna | `[DATA GAP]` | KBC reporting: Retail/SME je největší segment skupiny ČSOB (42,7 % aktiv, 65,8 % pasiv) `[FACT – sekundární, rok neuveden]`; `[FACT – sekundární]` úvěry pro malé a střední firmy 99,7 mld. Kč (rok ověřit – tz250213.pdf). VZ 2024: vz-csob-2024.pdf `[DATA GAP]` |
| **Raiffeisenbank** | „Podnikatelé a malé firmy" (rb.cz/podnikatele) vs. „Firmy" (rb.cz/firmy) `[FACT]` | `[FACT]` „Účty pro malé a střední firmy" (tarify od 1. 2. 2025) = firmy s obratem **50–250 mil. Kč**; multiměnové účty pro firmy s obratem od 100 mil. Kč (TZ 10/2020) → small business < 50 mil. Kč | FOP: účet online; PO: založení na pobočce `[FACT]`; internetové bankovnictví pro podnikatele odděleno od firemního | Ano (podnikatelský účet bez poplatků za základní služby vs. firemní účty až 19 měn) `[FACT]` | VZ 2024: podíl na úvěrech korporátního segmentu 8,88 %; portfolio úvěrů „živnostníkům" +11,2 %, tržní podíl 5,72 % `[FACT – Patria/Kurzy shrnutí VZ 2024]`. Segmentové názvy ve VZ `[DATA GAP]` (Raiffeisenbank_a_s_Vyrocni_financni_zprava_2024_CZ.pdf) |
| **Moneta Money Bank** | „Živnostníci a firmy" (moneta.cz/zivnostnici-a-firmy); samostatná sekce pro komerční segment po redesignu webu `[FACT]` | `[DATA GAP]` obratová hranice small business vs. SME (investors.moneta.cz – VZ / prezentace) | Digitální distribuce úvěrů „plně online pro retail, small business a podnikatele" `[FACT]`; pobočky | `[DATA GAP]` | Segmenty: **Commercial, Retail, Other/Treasury**; Commercial = vklady, investiční úvěry, revolving, financování nemovitostí a další služby pro **SME, korporátní klienty, finanční instituce a veřejný sektor** `[FACT]`. Podíl na výnosech 2024: Retail 62,7 %, Commercial 37 % `[FACT – MarketScreener]`. 1H 2026: strategický důraz na SME, small business a spotřebitelské úvěry; úvěry +9,1 % y/y `[FACT – Investing.com shrnutí prezentace]`. Small business je uvnitř Commercial (na rozdíl od ČS/KB, kde je v retailu). |
| **UniCredit Bank CZ&SK** | „Podnikatelé a menší firmy" (unicreditbank.cz/cs/podnikatele-a-mensi-firmy) ; sazebník „Část Small Business" `[FACT]` | `[FACT – Wikipedia/VZ]` SME definováno bankou jako obrat **50–250 mil. Kč** → Small Business < 50 mil. Kč `[EST – dovozeno]` | `[DATA GAP]` | Účty Business START (zdarma) / OPEN / TOP (350 Kč/měs.) `[FACT – Finex]`; záruční programy EIF `[FACT]` | `[DATA GAP]` segment reporting (VZ UCB CZ&SK) |
| **Air Bank** | „Podnikatelský účet" (airbank.cz/produkty/podnikatelsky-ucet) `[FACT]` | Bez obratové segmentace; cílí na OSVČ a malé s.r.o. | Plně digitální (app), bez RM; BankID onboarding plán 1H 2026 `[CLAIM]` | Účet pro OSVČ od 5/2023; pro s.r.o. s jedním jednatelem (2025), od 23. 1. 2026 i vícečlenná s.r.o. `[FACT – TZ Air Bank]`; `[CLAIM]` 65 000+ klientů účtu; „každá čtvrtá nová OSVČ (z 91 615 v r. 2025) si vybrala Air Bank" | Nereportuje segmenty (součást PPF/Home Credit) `[EST]` |
| **Fio banka** | „Podnikatelé" (fio.cz/podnikatele) – podnikatelský a firemní účet zdarma `[FACT]` | Bez obratové segmentace; účty „za stejných podmínek jako pro fyzické osoby" `[FACT – VZ 2023]` | Pobočky + internetbanking; bez RM modelu `[EST]` | Splátkový úvěr pro živnostníky (od 2023), podnikatelské úvěry vč. agroúvěru, kontokorent `[FACT]` | VZ 2023/2024 bez segmentového členění SB `[EST]`; podle chytryrejstrik.cz je Fio v top 3 u firem s obratem do 10 mil. Kč `[FACT – sekundární]` |
| **Banka Creditas** | creditas.cz `[DATA GAP – web blokován]` | Zaměření na financování firem (~70 % pohledávek za klienty), zejména české malé a střední firmy z finančnictví, energetiky a developmentu; úvěry jen podnikatelskému sektoru (hypotéky FO ukončeny) `[FACT – dluhopisar.cz]` | `[DATA GAP]` | `[DATA GAP]` | VZ 2024 publikována 4/2025 (Patria); fúze s Max bankou (ex-Expobank) `[FACT]`; segmentové členění `[DATA GAP]` |
| Revolut Business | Business účet (EU licence) | – | Digitál | FOP i PO | `[CLAIM]` aktivní firemní uživatelé v ČR +31 % y/y (2025); >1 mil. uživatelů Revolut v ČR (3/2025) `[FACT – e15]` |
| Wise Business | Business účet | – | Digitál | FOP i PO | `[DATA GAP]` počty v ČR |
| Trinity Bank | Firemní účty vč. cizoměnových `[FACT – Finmag]` | – | Pobočky/online | `[DATA GAP]` | `[DATA GAP]` |
| Partners Banka | Podnikatelský účet ve spolupráci s UniCredit Bank `[FACT – Finmag 2025]` | – | Digitál + poradci | `[DATA GAP]` | `[DATA GAP]` |
| mBank | mKonto Business – vedení a platby zdarma `[FACT]` | – | Digitál | FOP i PO | Součást mBank S.A. (PL) – bez CZ segmentu `[EST]` |

Kontextová tabulka – tržní preference podle velikosti firmy (`[FACT – sekundární]`, chytryrejstrik.cz, datum publikace neuvedeno; metodika: „malé podniky = obrat do 10 mil. Kč, střední 10–100 mil. Kč, velké > 100 mil. Kč"):

| Velikost firmy dle obratu | Top banky (pořadí) |
|---|---|
| do 10 mil. Kč | Fio, Komerční banka, ČSOB (první tři místa) |
| 10–100 mil. Kč | Komerční banka, ČSOB |

Poznámka: ČS v úryvku nefiguruje v top 3 pro firmy do 10 mil. Kč – `[DATA GAP]` ověřit celé pořadí a metodiku (zdroj pracuje se sídlem/účtem v obchodním rejstříku = jen PO).

### 4. Daňová a právní optika

**4a. OSVČ – hlavní vs. vedlejší (ČSSZ)**

| Ukazatel | Hodnota | Zdroj |
|---|---|---|
| OSVČ celkem | 1 173 951 (30. 6. 2025; +26 tis. y/y; historické maximum) | `[FACT]` ČSSZ via podnikatel.cz |
| z toho hlavní činnost | 688 824 (30. 6. 2025; +12 tis. y/y) | `[FACT]` dtto |
| z toho vedlejší činnost | 485 127 (30. 6. 2025; +14 tis. vs. polovina 2023) | `[FACT]` dtto |
| Definice | Hlavní = povinná účast na důchodovém pojištění; vedlejší (souběh se zaměstnáním, důchodem, studiem…) = účast až od dosažení rozhodného příjmu nebo dobrovolně | `[FACT]` ČSSZ „OSVČ v kostce" |
| Otevřená data | Datová sada „Přehled o celkovém počtu OSVČ v ČR" (data.cssz.cz) – měsíční, hlavní/vedlejší, dle okresů | `[FACT]` |
| Časová řada 2021–2025 | `[DATA GAP]` – data.cssz.cz/dataset/prehled-o-celkovem-poctu-osvc-v-cr (blokováno) | |

**4b. Paušální daň (zákon č. 586/1992 Sb., § 2a a § 7a; od 1. 1. 2021)**

| Rok | Limit příjmů pro vstup | Pásma | Měsíční záloha I. / II. / III. pásmo | Počet OSVČ v paušálním režimu |
|---|---|---|---|---|
| 2021 | 1 mil. Kč | 1 | 5 469 Kč | ~65 tis. `[FACT – FS]` |
| 2022 | 1 mil. Kč | 1 | 5 994 Kč | ~80 tis. (průměr roku) `[FACT – FS]` |
| 2023 | 2 mil. Kč | 3 | 6 208 / 16 000 / 26 000 Kč | ~100 tis. `[FACT – FS]` |
| 2024 | 2 mil. Kč | 3 | 7 498 / 16 745 / 27 139 Kč | 32 tis. nově přihlášených k 1/2024 `[FACT – TZ FS 1/2024]`; celkem „odhadem ~125 tis. během roku" `[FACT – FS, ale viz pozn.]` |
| 2025 | 2 mil. Kč | 3 | 8 716 / 16 745 / 27 139 Kč | `[DATA GAP]` (TZ FS „Paušální daň 2025: důležité změny") |
| 2026 | 2 mil. Kč | 3 | 9 984 (daň 100 + soc. 6 578 + zdr. 3 306) / 16 745 / 27 139 Kč | > 125 tis.; +11 tis. nových v r. 2026 `[FACT – TZ FS 2026]` |

- Poznámka k nekonzistenci: úryvek FS pro 2024 („~125 tis.") a TZ FS 2026 („přes 125 tis. po přírůstku 11 tis.") nejdou dohromady → jedno z čísel je nejspíš stav vs. kumulativní odhad. `[DATA GAP]` ověřit oficiální stavy k 31. 12. 2023/2024/2025 na financnisprava.gov.cz (TZ GFŘ 2024–2026).
- `[FACT]` Podmínky režimu: neplátce DPH, příjmy ze samostatné činnosti do 2 mil. Kč, ostatní příjmy (kapitál, nájem, ostatní) do 50 tis. Kč ročně, není zaměstnanec s příjmy zdaňovanými zálohou; přihlášení/změna pásma do 10. 1. (pro 2026 do 12. 1. 2026) (FS, Informace k institutu paušální daně 2025/2026).
- Pásma (§ 2a ZDP): I. pásmo – příjmy do 1 mil. Kč bez ohledu na obor; do 1,5 mil. Kč, pokud ≥ 75 % příjmů spadá pod 80% nebo 60% paušál; do 2 mil. Kč, pokud ≥ 75 % příjmů spadá pod 80% paušál. II. pásmo – do 1,5 mil. Kč; do 2 mil. Kč, pokud ≥ 75 % pod 80%/60% paušál. III. pásmo – do 2 mil. Kč. `[FACT – dle zákona; primární stránka FS nedostupná přes proxy, ověřit]`
- **Význam pro definici:** paušální režim = „nejmenší" FOP (obrat < 2 mil. Kč, bez DPH) → cca 11 % všech OSVČ (`[EST]` 125 tis. / 1 174 tis.), ~18 % OSVČ s hlavní činností (`[EST]` 125 / 689 tis.). Tito klienti nevedou účetnictví ani daňovou evidenci → banky pro ně nemají výkazy; scoring musí stát na transakčních datech.

**4c. Paušální výdaje procentem (§ 7 odst. 7 ZDP)** `[FACT]`

| Sazba | Činnost | Max. uplatnitelný výdaj (= strop příjmů 2 mil. Kč) |
|---|---|---|
| 80 % | zemědělství, řemeslné živnosti | 1 600 000 Kč |
| 60 % | ostatní živnosti | 1 200 000 Kč |
| 40 % | svobodná povolání, autorské příjmy, ostatní samostatná činnost | 800 000 Kč |
| 30 % | nájem | 600 000 Kč |

Limit 2 mil. Kč se v letech 2025–2026 nezměnil `[FACT – Fakturoid, Kurzy]`. Nad 2 mil. Kč příjmů je výdajový paušál „zastropován" – to je faktická daňová hranice mezi „mikro-FOP" a větším FOP.

**4d. Právnické osoby – právní formy a počty**

| Ukazatel | Hodnota | Zdroj |
|---|---|---|
| Registrované obchodní společnosti (s.r.o. + a.s.) | 594 520, z toho **567 228 s.r.o.** (95 %) a 27 291 a.s. | `[FACT – sekundární]` Dun & Bradstreet, stav začátek 2026 |
| Nově založené 2025 | 34 621 (nejvíce za 20 let), z toho 33 744 s.r.o. (97,6 %) a 847 a.s. (2,4 %); čistý přírůstek registrovaných +17 898 | `[FACT – sekundární]` D&B / BusinessInfo |
| Podnikající fyzické osoby (RŽP) | 2 029 257 registrovaných (31. 12. 2025; +40 458 y/y); dle interní metodiky D&B ~1 131 tis. aktivních (56 %) | `[FACT – sekundární]` D&B via kurzy.cz; primárně MPO „Roční přehled podnikatelů a živností" `[DATA GAP – blokováno]` |
| Družstva, spolky (podnikající) | `[DATA GAP]` – ČSÚ „Počty ekonomických subjektů podle vybraných právních forem" (csu.gov.cz/produkty/…) | |

**4e. Registrované vs. aktivní subjekty**

| Registr | Správce | Co obsahuje | Kritérium „aktivity" |
|---|---|---|---|
| RES (Registr ekonomických subjektů) | ČSÚ, § 20 zák. č. 89/1995 Sb. | Každá PO, FO s postavením podnikatele, OSS-účetní jednotka; přebírá zápisy z ROS denně | „Zjištěná aktivita" = subjekt je plátcem daně z příjmů, DPH, nebo platí pojistné na soc. zabezpečení za zaměstnance či jako OSVČ `[FACT – ČSÚ metodika]`. Konec 2024: > 2,8 mil. registrovaných subjektů (+1,3 % y/y) `[FACT]`; počet „se zjištěnou aktivitou" celkem ČR `[DATA GAP]` (csu.gov.cz/statistiky-z-registru-ekonomickych-subjektu) |
| RŽP (živnostenský rejstřík) | MPO | Podnikatelé s živnostenským oprávněním (FO i PO), vč. přerušených a nevykonávaných | Žádné – registrační; ~2,03 mil. FO `[FACT – sekundární]` |
| ČSSZ | ČSSZ | OSVČ přihlášené k pojištění (hlavní/vedlejší) | Faktický výkon činnosti (platí zálohy / podává přehled); 1,174 mil. (6/2025) `[FACT]` |
| Finanční správa | GFŘ | Poplatníci s příjmy § 7 ZDP; paušální režim | Podané přiznání / paušální záloha `[DATA GAP – počet poplatníků § 7]` |

Rozdíl RŽP (2,03 mil.) − ČSSZ (1,17 mil.) ≈ 0,86 mil. „spících" oprávnění `[EST]` – tj. ~42 % registrovaných FO nepodniká aktivně. To potvrzuje H-D5.

**4f. Kategorie účetních jednotek (§ 1b zákona č. 563/1991 Sb.) a novela 2025**

| Kategorie | Aktiva (netto) – do 2025 | Čistý obrat – do 2025 | Zaměstnanci | Nové limity dle novely 2025 (aktiva / obrat) |
|---|---|---|---|---|
| Mikro | ≤ 9 mil. Kč | ≤ 18 mil. Kč | ≤ 10 | 11 mil. / 22 mil. Kč `[FACT – TPA, KPMG]` |
| Malá | ≤ 100 mil. Kč | ≤ 200 mil. Kč | ≤ 50 | 120 mil. / 240 mil. Kč `[FACT – TPA, KPMG]` |
| Střední | ≤ 500 mil. Kč | ≤ 1 mld. Kč | ≤ 250 | `[DATA GAP]` |
| Velká | nad střední | | | |

- Pravidlo: jednotka nepřekročí alespoň 2 ze 3 kritérií k rozvahovému dni.
- `[FACT]` Novela (vyhlášena ve Sbírce 2025): změny kategorizace účinné dnem po vyhlášení, tj. **3. 9. 2025**; povinný audit od 1. 1. 2026 pouze pro střední a velké účetní jednotky (Portál POHODA, Svaz účetních). Důvod: inflace posouvala jednotky do vyšších kategorií bez reálného růstu (KPMG danovky.cz).
- `[DATA GAP]` Číslo novely ve Sbírce a přesné částky (jeden zdroj uvádí zvýšení „o 25 %" – to by odpovídalo 11,25 / 22,5 / 125 / 250 mil. Kč, jiné 11 / 22 / 120 / 240) – ověřit na zakonyprolidi.cz.
- `[FACT]` Nový (komplexní) zákon o účetnictví: účinnost nejdříve **1. 1. 2027** (Portál POHODA, Deloitte).
- **Význam pro definici:** naše hranice 25 mil. Kč obratu leží těsně nad „mikro účetní jednotkou" (22 mil. Kč obratu po novele) → mikro účetní jednotka je nejbližší veřejně dostupná právní kategorie pro PO v našem SB (+ malé jednotky do 25 mil. Kč). Mikro a malé jednotky nemají povinný audit a zveřejňují zkrácenou závěrku (ve Sbírce listin bez výkazu zisku a ztráty u mikro/malých bez auditu) → obrat PO v segmentu není z veřejných zdrojů zjistitelný; nutná proxy přes aktiva nebo data CRIF/D&B.

### 5. Mapovací tabulka: zdroj × definice × překryv s naší definicí (obrat do 25 mil. Kč)

| # | Zdroj dat | Použitá definice | Překryv s naším SB | Korekce / poznámka |
|---|---|---|---|---|
| 1 | ČSSZ (počet OSVČ) | OSVČ evidované k důch. pojištění; hlavní vs. vedlejší; bez obratu | **Vysoký** (FOP) | Zahrnuje FOP s obratem > 25 mil. Kč (zanedbatelné `[EST]`); vedlejší OSVČ = nízká bankovní hodnota → doporučeno reportovat obě řady zvlášť. Nepokrývá PO. |
| 2 | ČSÚ RES | Registrované subjekty (PO + FO podnikatelé); „zjištěná aktivita" jako filtr; velikost dle zaměstnanců | **Střední** | Registr, ne aktivita; velikostní pásma zaměstnanecká; pro PO nutno filtrovat právní formu + aktivitu; obrat chybí. |
| 3 | ČSÚ SBS (strukturální statistika) | Podniky dle „počtu zaměstnaných osob" (vč. majitelů), nařízení EU o podnikových statistikách; zahrnuje FO i PO ve vybraných NACE | **Střední** | Pásmo 0–9 zaměstnanců ≈ mikro; obrat dostupný agregovaně → lze odhadnout podíl subjektů < 25 mil. Kč `[EST]`; vylučuje část služeb/zemědělství; roční, zpoždění ~18 měs. |
| 4 | MPO / NRB – definice MSP (2003/361/ES) | < 10 zam. a ≤ 2 mil. EUR (mikro); < 50 a ≤ 10 mil. EUR (malý) | **Střední** | Mikro = obratově ~2× širší než náš SB; zaměstnanecké kritérium je primární; propojené podniky se sčítají (náš SB nikoli). |
| 5 | ČNB ARAD – „Domácnosti – živnosti" (S.14) | FOP jako podsektor domácností; úvěry/vklady bank | **Vysoký** (FOP) | Jen bankovní bilance (ne nebankovní věřitelé, ne leasing); bez obratu; FOP podnikající přes s.r.o. spadá do S.11. |
| 6 | ČNB ARAD – nefinanční podniky (S.11) | Všechny PO bez ohledu na velikost; členění dle vlastnictví a NACE | **Nízký** | Nutný externí klíč (podíl mikro/malých na úvěrech – `[DATA GAP]` ZFS/AnaCredit); MIR pásmo „úvěry do 7,5 mil. Kč" jako proxy. |
| 7 | ČNB – Šetření úvěrových podmínek bank | „Malé a střední podniky" vs. „velké podniky" (kvalitativní; definice ve slovníčku `[DATA GAP]`) | **Nízký–střední** | SME zahrnuje firmy až do 50 mil. EUR obratu; jen směr změny standardů/poptávky, ne objemy. |
| 8 | ČNB – Zpráva o finanční stabilitě | Sektor nefinančních podniků; zátěžové testy; případné boxy k MSP | **Nízký** | `[DATA GAP]` ověřit členění dle velikosti (AnaCredit). |
| 9 | Česká spořitelna – VZ (Retail / Corporates) | Podnikatelé a mikra v Retail; SME + Large Corporate v Corporates (obratové pásmo `[DATA GAP]`) | **Střední** | Náš SB = Retail-mikra + spodní část SME; interní hranice firemního bankéře „do 1 mil. EUR" `[sekundární]` ≈ náš práh → ČS interní data lze pravděpodobně mapovat nejlépe ze všech bank `[EST]`. |
| 10 | Komerční banka – VZ / výsledky | Retail Banking (vč. „small business", obrat < 60 mil. Kč) vs. Corporate (od 60 mil. Kč) | **Střední–vysoký** | Small business KB je ~2,4× širší obratově (60 vs. 25 mil. Kč); FOP i PO společně; nutno škálovat. |
| 11 | ČSOB – VZ / KBC | Retail/SME vs. Corporate; hranice `[DATA GAP]` (indikace 200–300 mil. Kč; SK 2,5 mil. EUR) | **Nízký–střední** | Pokud SME v Retail/SME sahá do 300 mil. Kč, segment je řádově širší než náš SB – nelze přímo použít. |
| 12 | Raiffeisenbank – VZ | „Podnikatelé a malé firmy" (< 50 mil. Kč) vs. „malé a střední firmy" (50–250 mil.) vs. korporace; samostatně vykazuje úvěry „živnostníkům" (podíl 5,72 %) | **Střední–vysoký** | Hranice 50 mil. Kč = 2× náš práh; řada „živnostníci" je přímo srovnatelná s ČNB S.14. |
| 13 | Moneta – VZ / IR | Commercial (SME + korporace + veřejný sektor) vs. Retail; small business uvnitř Commercial; hranice `[DATA GAP]` | **Střední** | Moneta jako jediná nedává podnikatele do retailu → její „Commercial" není srovnatelný s ČS/KB retail small business. |
| 14 | UniCredit – VZ | Small Business (< 50 mil. Kč `[EST]`), SME 50–250 mil. Kč, Corporate | **Střední–vysoký** | Hranice 50 mil. Kč; jednotka CZ+SK – nutno oddělit SK. |
| 15 | Air Bank / Fio / Creditas / mBank / Revolut / Wise | Bez obratové segmentace; produktová definice (podnikatelský účet pro OSVČ / s.r.o.) | **Vysoký** (klientská báze je fakticky SB) | Pouze počty účtů/klientů z tiskových zpráv `[CLAIM]`; žádné finanční segmentové výkazy. |
| 16 | CRIF (Cribis) / D&B | Podnikatelé FO (registrace vs. „aktivní" dle interní metodiky – 56 % `[sekundární]`), firmy dle právní formy, obratové pásmo z účetních závěrek | **Střední–vysoký** | Obrat PO dostupný jen tam, kde je zveřejněna závěrka (mikro/malé často jen rozvaha) → obratové třídění je neúplné; definice „aktivní" je proprietární. |
| 17 | Creditreform (insolvence) | Insolvenční návrhy: právnické osoby vs. fyzické osoby-podnikatelé vs. spotřebitelé (ISIR) | **Střední** | Rok 2024: 23 243 insolvenčních návrhů celkem (vše vč. spotřebitelů) `[FACT – sekundární]`; podíl FOP a PO do 25 mil. Kč `[DATA GAP]`. |
| 18 | AMSP ČR – průzkumy (Ipsos) | „Živnostníci a MSP do 250 zaměstnanců", CATI/CASI, online panel | **Střední** | Výběrové šetření (n ~ stovky), zaměstnanecké vymezení; vhodné na postoje, ne na velikost trhu. |

### 6. Porovnání definic

| Rámec | Kritérium | Hranice | Kdo používá | Slabina pro naši analýzu |
|---|---|---|---|---|
| EU MSP (2003/361/ES) | Zaměstnanci (primární) + obrat/bilance | mikro < 10 zam., ≤ 2 mil. EUR; malý < 50, ≤ 10 mil. EUR | MPO, NRB, ČSÚ, OP TAK, CRR (SME faktor: obrat ≤ 50 mil. EUR; retail expozice ≤ 1 mil. EUR `[FACT – EBA/CRR čl. 501]`) | Obratově příliš široká (mikro ≈ 50 mil. Kč); propojené podniky se sčítají; zaměstnanecké kritérium neodpovídá bankovní obsluze |
| Zákon o účetnictví (§ 1b) | Aktiva + obrat + zaměstnanci (2 ze 3) | mikro ≤ 11 mil. aktiva / 22 mil. obrat / 10 zam. (po novele 2025) | Účetní jednotky, auditoři, Sbírka listin | Jen PO (a FO vedoucí účetnictví); změna limitů 2025 láme časovou řadu; mikro zveřejňují jen rozvahu |
| ČNB sektorová (ESA 2010) | Institucionální sektor | S.14 živnostníci vs. S.11 nefinanční podniky | ČNB ARAD, MIR, BLS | Bez velikosti u PO; FOP bez obratu; jen bankovní bilance |
| ČNB MIR – objem úvěru | Velikost obchodu | do 7,5 / 7,5–30 / nad 30 mil. Kč | ČNB, ECB | Objem úvěru ≠ velikost firmy (malá firma může mít velký investiční úvěr a naopak) |
| Daňová – paušální režim | Příjmy, DPH | ≤ 2 mil. Kč, neplátce DPH, 3 pásma | FS, MF, ČSSZ | Jen dobrovolně přihlášení FOP (~11 % OSVČ `[EST]`); vylučuje plátce DPH |
| Daňová – paušální výdaje | Příjmy | strop 2 mil. Kč | FS | Nezachycuje FOP s daňovou evidencí/účetnictvím |
| ČSSZ – hlavní/vedlejší | Status pojištění | povinná vs. podmíněná účast | ČSSZ, MPSV | Bez obratu; vedlejší OSVČ zahrnují i marginální činnosti |
| Registrační (RŽP, RES) | Existence oprávnění/zápisu | – | MPO, ČSÚ | ~42 % FO neaktivních `[EST]`; PO „spící" bez závěrek |
| Bankovní – obratová | Roční obrat klienta (deklarovaný / z výkazů) | KB 60 mil.; RB 50 mil.; UCB 50 mil.; ČS ~1 mil. EUR (`[sekundární]`); ČSOB `[DATA GAP]`; Moneta `[DATA GAP]` | Banky – interní segmentace a obsluha | Nejednotné prahy (25–300 mil. Kč), FOP i PO společně, u ČS/KB v retailu, u Monety v Commercial; obrat u FOP často neověřený |
| Bankovní – produktová | Typ účtu (podnikatelský vs. firemní) | – | Air Bank, Fio, mBank, Revolut, Wise, Creditas | Bez finančního reportingu; počty klientů = `[CLAIM]` |
| Naše pracovní (projekt) | Roční obrat | ≤ 25 mil. Kč, FOP + PO | Tento projekt | Nemá přímý statistický protějšek; nejblíže: mikro účetní jednotka (22 mil.), ČNB S.14 (FOP), ČS „firemní bankéř do 1 mil. EUR" |

---

## (c) Analýza / zjištění (action titles)

**1. „Small business" v ČR nemá úřední definici – banky si ji stanovují obratem a jejich prahy (50–60 mil. Kč) jsou 2–2,4× nad naší hranicí.** KB (korporát od 60 mil. Kč `[FACT]`), Raiffeisenbank (malé a střední firmy 50–250 mil. Kč `[FACT]`) a UniCredit (SME 50–250 mil. Kč `[FACT – sekundární]`) shodně řadí firmy do ~50–60 mil. Kč obratu pod „podnikatele a malé firmy". Jakékoli srovnání segmentových objemů bank s naším SB proto vyžaduje škálovací klíč (podíl klientů/objemů pod 25 mil. Kč uvnitř bankovního „small business"), který z veřejných zdrojů nevyplývá → `[DATA GAP]`, řešit interními daty ČS.

**2. ČS je jediná velká banka, kde se veřejně dostupná obsluhová hranice (firemní bankéř „do 1 mil. EUR") kryje s naší definicí – ale v reportingu je náš segment rozřezán mezi Retail (mikra) a Corporates (SME).** Erste segmentová logika řadí „micros a free professionals" do Retail `[FACT]`, SME do Corporates `[FACT]`; VZ 2024 zmiňuje 100 mld. Kč firemních vkladů v SME `[FACT]`, ale nikoli objemy za podnikatele. Pro benchmark to znamená: ČS retailová čísla podnikatelů nejsou veřejná; peer srovnání bude možné jen na úrovni (i) ČNB S.14 živnostníci (tržní podíly úvěrů/vkladů FOP) a (ii) interních dat ČS.

**3. Pro FOP je ČNB podsektor „živnostníci" (S.14) jediná konzistentní tržní řada; pro PO do 25 mil. Kč veřejná bankovní statistika neexistuje.** ARAD člení úvěry nefinančním podnikům pouze podle vlastnictví a NACE; MIR nabízí objemové pásmo „do 7,5 mil. Kč" `[FACT]` jako jedinou proxy. Velikostní členění PO existuje v AnaCredit/CRÚ, ale veřejně `[DATA GAP]`. Důsledek: tržní podíl ČS v „PO do 25 mil. Kč" bude nutné odhadnout `[EST]` kombinací RES/SBS (počet subjektů) a interních dat, nikoli z ČNB.

**4. Registrace ≠ aktivita: ~2,03 mil. registrovaných FO (RŽP) vs. ~1,17 mil. OSVČ u ČSSZ vs. ~0,69 mil. s hlavní činností – tři různé „velikosti trhu" lišící se 3×.** Pro bankovní penetraci (podíl FOP s podnikatelským účtem) je jediný obhajitelný jmenovatel ČSSZ (aktivní) a ideálně jen hlavní činnost; marketingové výroky bank („každá čtvrtá nová OSVČ" – Air Bank `[CLAIM]`) pracují s registracemi RŽP a nadhodnocují.

**5. Daňové režimy vytvářejí uvnitř FOP tři vrstvy s odlišnou datovou stopou: paušální režim (< 2 mil. Kč, > 125 tis. OSVČ, bez evidence), paušální výdaje (< 2 mil. Kč, daňová evidence příjmů), skutečné výdaje/účetnictví (bez limitu).** Pro banku to znamená, že u > 10 % OSVČ neexistují žádné finanční výkazy a jediným zdrojem pro scoring je transakční historie účtu – konkurenční výhoda banky s hlavním účtem klienta.

**6. Novela zákona o účetnictví (účinnost 3. 9. 2025; audit jen střední/velké od 2026; nový zákon nejdříve 2027) zvyšuje práh mikro účetní jednotky na ~22 mil. Kč obratu, tj. téměř přesně na naši hranici – ale současně snižuje dostupnost obratových dat o PO ve Sbírce listin.** Mikro a malé jednotky bez auditu nezveřejňují výkaz zisku a ztráty, takže CRIF/D&B obratová pásma budou u PO v našem segmentu systematicky neúplná; časová řada 2021–2025 je navíc zlomená změnou limitů.

**7. Digitální hráči (Air Bank, Fio, Revolut, Wise, mBank, Partners) segment nedefinují obratem, ale produktem – a jejich čísla jsou výhradně `[CLAIM]`.** Air Bank (účet pro OSVČ od 5/2023, s.r.o. od 2025/2026, „65 000+ klientů") a Revolut („+31 % aktivních firemních uživatelů v ČR") nereportují objemy; jediný nezávislý test jejich podílu je ČNB S.14 (vklady/úvěry živnostníků podle bank nejsou veřejné → `[DATA GAP]`, dostupné jen ČS interně z ČNB výkazů pro banky).

---

## (d) So what pro ČS

1. **Zafixovat interní definici SB = obrat ≤ 25 mil. Kč, FOP + PO, a zveřejnit ji v IR materiálech jako „Micro & Small Business" pod Retail** – dnes je segment rozdělen mezi Retail (mikra) a Corporates (SME) a trh (KB 60 mil., RB/UCB 50 mil.) měří jinak; kdo definici nastaví, řídí benchmark.
2. **Pro tržní podíl v FOP používat výhradně ČNB S.14 „živnostníci" (úvěry i vklady) a jako jmenovatel penetrace ČSSZ hlavní činnost (~689 tis.)**, ne RŽP (2,03 mil.); tím se eliminuje nadhodnocování challengerů, kteří citují registrace.
3. **Pro PO do 25 mil. Kč vybudovat vlastní tržní odhad (RES × zjištěná aktivita × mikro/malé účetní jednotky × CRIF obrat) – veřejná ČNB data to neumí**; požádat interně o AnaCredit/CRÚ agregáty podle velikosti (ČNB je bankám poskytuje pro benchmarking), jinak zůstane `[DATA GAP]`.
4. **Paušální režim (> 125 tis. OSVČ, bez výkazů) je scoringová příležitost hlavního účtu** – navrhnout produkt/limit odvozený z transakční historie George Business; konkurence s obratovými prahy 50–60 mil. Kč tento mikro-konec obsluhuje standardizovaně.
5. **Sjednotit interní číselníky s novou kategorizací účetních jednotek (mikro ≤ 22 mil. Kč obratu od 2025) a připravit se na nový zákon o účetnictví 2027** – umožní automatické mapování PO klientů na náš SB a srovnatelnost 2025+ vs. 2021–2024 (zlom v řadě).

---

## (e) Limitace

- **Přístup ke zdrojům:** všechny primární domény (cnb.cz, csu.gov.cz, mpo.gov.cz, financnisprava.gov.cz, cssz.gov.cz, csas.cz, kb.cz, csob.cz, rb.cz, moneta.cz, unicreditbank.cz, airbank.cz, fio.cz, creditas.cz, patria.cz, kurzy.cz) byly proxy blokovány; údaje pocházejí z úryvků vyhledávače – jsou označeny `[FACT]` jen tam, kde úryvek obsahoval konkrétní hodnotu se zdrojem. Doporučení: před finální syntézou ověřit 10 položek označených `[DATA GAP]` s URL níže.
- **Bankovní hranice:** u ČSOB a Monety nebyla obratová hranice nalezena; u ČS pochází z inzerátu (sekundární); u UniCredit dovozena z definice SME (50–250 mil. Kč).
- **Paušální daň – počty:** řada 2021–2026 kombinuje průměry, odhady a stavy z různých tiskových zpráv FS; nekonzistence 2024 vs. 2026 je zdokumentována.
- **Účetní limity:** dva sekundární zdroje se liší (+20 % vs. +25 %); číslo novely nebylo ověřeno.
- **ČSÚ „zjištěná aktivita"** – celostátní počet aktivních FO a PO nebyl získán; RES časová řada 2021–2025 `[DATA GAP]`.
- **Kurzové přepočty** (1 mil. EUR ≈ 25 mil. Kč; 2 mil. EUR ≈ 50 mil. Kč) jsou `[EST]` při kurzu ~25 CZK/EUR.

---

## (f) Seznam zdrojů (přístup 2026-09-08, přes výsledky vyhledávání; přímé načtení blokováno)

**EU / MPO / NRB / ČSÚ**
- Sdělení MPO č. 7/2023 Sb. – české znění doporučení Komise 2003/361/ES: https://www.zakonyprolidi.cz/cs/2023-7
- Uživatelská příručka k definici MSP (EK): https://ec.europa.eu/docsroom/documents/42921/attachments/1/translations/cs/renditions/pdf
- MPO – Definice malého a středního podnikatele (PDF): https://mpo.gov.cz/assets/cz/podnikani/zivnostenske-podnikani/2020/3/Definice-maleho-a-stredniho-podnikatele-osetrovneOSVC.pdf
- NRB – Vysvětlení a definice malých a středních podniků: https://www.nrb.cz/podnikatele/dalsi-informace-pro-podnikatele/mali-a-stredni-podnikatele/
- Zákon č. 47/2002 Sb.: https://www.zakonyprolidi.cz/cs/2002-47
- MPO – VZ o implementaci Strategie podpory MSP za rok 2024: https://mpo.gov.cz/assets/cz/podnikani/male-a-stredni-podnikani/studie-a-strategicke-dokumenty/2026/1/VZ-Strategie-MSP-za-rok-2024.pdf
- MPO – Strategie podpory MSP 2021–2027 (aktualizace 2025): https://mpo.gov.cz/assets/cz/podnikani/male-a-stredni-podnikani/studie-a-strategicke-dokumenty/2026/2/Strategie-podpory-MSP-v-CR-2021-2027_aktualizace-2025__po-RKV_.pdf
- MPO – Národní záruka překonala 2 mld. Kč (TZ): https://zpravy.kurzy.cz/857043-program-narodni-zaruka-prekonal-milnik-2-mld-kc/
- MPO – Statistické údaje o podnikatelích (RŽP): https://mpo.gov.cz/cz/podnikani/zivnostenske-podnikani/statisticke-udaje-o-podnikatelich/ ; Roční přehled: https://mpo.gov.cz/cz/podnikani/zivnostenske-podnikani/statisticke-udaje-o-podnikatelich/rocni-prehled-podnikatelu-a-zivnosti--222295/
- ČSÚ – Metodika statistiky registrací ekonomických subjektů: https://csu.gov.cz/metodika-statistiky-registraci-ekonomickych-subjektu
- ČSÚ – Statistiky z RES – metodika: https://csu.gov.cz/statistiky-z-registru-ekonomickych-subjektu-metodika ; data: https://csu.gov.cz/statistiky-z-registru-ekonomickych-subjektu
- ČSÚ – Roční strukturální statistika průmyslu – metodika: https://csu.gov.cz/rocni-strukturalni-statistika-prumyslu-metodika ; Podniková strukturální statistika (výkazy): https://csu.gov.cz/vykazy/podnikova_strukturalni_statistika2014
- ČSÚ – 3.1.2 Rozvoj malého a středního podnikání (2006): https://csu.gov.cz/produkty/13-1134-07-2006-3_1_2_rozvoj_maleho_a_stredniho_podnikani
- ČSÚ – Ekonomické subjekty podle právních forem: https://csu.gov.cz/produkty/ekonomicke-subjekty-podle-vybranych-pravnich-forem-za-spravni-obvody-prahy-a-obci-s-rozsirenou-pusobnosti

**ČNB**
- ARAD: https://www.cnb.cz/cs/statistika/arad-system-casovych-rad/
- Metodický list – úvěry a vklady obyvatelstva/živnosti: https://www.cnb.cz/docs/ARADY/MET_LIST/tuvob_cs.pdf
- Metodické poznámky – měnová a finanční statistika: https://www.cnb.cz/cs/statistika/menova_bankovni_stat/metodicke-poznamky/
- Harmonizovaná úroková statistika (MIR): https://www.cnb.cz/cs/statistika/menova_bankovni_stat/harm_stat_data/mir_cs.htm ; Komentář k sazbám MFI: https://www.cnb.cz/cs/statistika/menova_bankovni_stat/harm_stat_data/komentar-k-urokovym-sazbam-menovych-financnich-instituci/index.html ; červenec 2025 (via Kurzy): https://zpravy.kurzy.cz/826640-urokove-sazby-menovych-financnich-instituci-v-cr-cervenec-2025/
- Šetření úvěrových podmínek bank: https://www.cnb.cz/cs/statistika/setreni-uverovych-podminek-bank/
- ZFS jaro 2025: https://www.cnb.cz/export/sites/cnb/cs/financni-stabilita/.galleries/zpravy_fs/fs_2025_jaro/zfs_jaro_2025.pdf ; ZFS podzim 2025: https://www.cnb.cz/export/sites/cnb/cs/financni-stabilita/.galleries/zpravy_fs/fs_2025_podzim/zfs_podzim_2025.pdf
- ČNB – Centrální registr úvěrů: https://www.cnb.cz/cs/dohled-financni-trh/centralni-registr-uveru/
- ČNB – Varování: úvěry na IČO: https://www.cnb.cz/cs/dohled-financni-trh/vykon-dohledu/upozorneni-pro-verejnost/Varovani-pro-spotrebitele-mozna-rizika-uveru-sjednavanych-na-ICO-tzv.-zastrenych-spotrebitelskych-uveru/
- Zrcadlo ARAD řad (názvy tabulek): https://www.kurzy.cz/cnb/ekonomika/domacnosti-zivnosti-rezidenti-vklady-podle-druhoveho-hlediska-kc-70/vklady-a-prijate-uvery-od-klientu-celkem/ ; https://www.kurzy.cz/cnb/ekonomika/nove-cerpane-klientske-uvery-podle-sektoroveho-a-subsektoroveho-hlediska-kc-c-1/nefinancni-podniky-soukrome-narodni/ ; https://www.kurzy.cz/cnb/ekonomika/klientske-uvery-podle-odvetvi-cz-nace-podle-sekci-kc-751/
- EBA / CRR čl. 501 (SME supporting factor): https://www.eba.europa.eu/single-rule-book-qa/qna/view/publicId/2014_1050 ; https://www.katalysys.com/insights/crr2-sme-support-factor

**Banky**
- ČS – Firmy a podnikatelé: https://www.csas.cz/cs/firmy ; Účty pro podnikatele a malé firmy: https://www.csas.cz/cs/firmy/ucty-podnikatele-firmy ; VZ 2024 (CZ): https://www.csas.cz/static_internet/cs/Redakce/Ostatni/Ostatni_IE/Prilohy/vz-2024.pdf ; Annual Report 2024 (EN): https://www.csas.cz/static_internet/en/Redakce/Ostatni/Ostatni_IE/Prilohy/annual_report_2024.pdf ; Half-Year Report 2025: https://www.csas.cz/static_internet/cs/Redakce/EMIL/EMIL/Prilohy/half-year-report-2025.pdf ; inzerát Firemní bankéř (obrat do 1 mil. EUR): https://cz.jooble.org/pr%C3%A1ce-%C4%8Desk%C3%A1-spo%C5%99itelna
- Erste Group – Annual Report / segment definice: https://www.erstegroup.com/en/investors/reports/financial-reports
- KB – Podnikatelé a malé firmy: https://www.kb.cz/cs/podnikatele-a-firmy ; Střední a velké firmy (od 60 mil. Kč): https://www.kb.cz/cs/korporace-a-instituce ; VZ 2024: https://www.kb.cz/getmedia/a6022aa7-cc7a-42da-a9c2-900aacae9842/KB-vyrocni-zprava-2024.pdf ; Výsledky FY 2024: https://www.kb.cz/getmedia/497f6aef-38c8-4db8-8264-eb8cdecae2a2/KB-Results-4Q2024-CZ.pdf ; komentář 4Q 2025 (KB+): https://www.marketscreener.com/news/komercn-banka-comments-on-business-and-financial-results-4q-2025-ce7f5dd8dc81f626
- ČSOB – VZ 2024: https://www.csob.cz/documents/10710/444804/vz-csob-2024.pdf ; TZ výsledky 2024: https://www.csob.cz/documents/10710/26443232/tz250213.pdf ; Průvodce podnikáním: https://www.pruvodcepodnikanim.cz/ ; ČSOB SK – Podnikatelia a firmy (2,5 mil. EUR): https://www.csob.sk/podnikatelia-firmy ; sekundární: https://www.citfin.cz/slovnik-ekonomickych-pojmu/csob-a-jeji-sluzby-pro-sme/
- Raiffeisenbank – Podnikatelé: https://www.rb.cz/podnikatele/ucty-a-platebni-styk ; Účty pro malé a střední firmy (50–250 mil. Kč, od 1. 2. 2025): https://www.rb.cz/firmy/transakcni-bankovnictvi/firemni-ucty/ucty-pro-male-a-stredni-firmy-od-01022025 ; TZ 2020 multiměnové účty: https://www.rb.cz/informacni-servis/pro-media/tiskove-zpravy/tiskove-zpravy-2020/tiskove-zpravy-202010/15102020-multimenove-ucty-pro-male-firmy ; VZ 2024: https://www.rb.cz/attachments/vyrocni-zpravy/Raiffeisenbank_a_s_Vyrocni_financni_zprava_2024_CZ.pdf ; shrnutí VZ 2024: https://www.patria.cz/zpravodajstvi/6347278/raiffeisenbank-as-vyrocni-financni-zprava-2024.html
- Moneta – Živnostníci a firmy: https://www.moneta.cz/zivnostnici-a-firmy ; IR: https://investors.moneta.cz/financial-results ; segmenty (MarketScreener): https://www.marketscreener.com/quote/stock/MONETA-MONEY-BANK-A-S-46923249/finances-segments/ ; 1H 2026: https://www.investing.com/news/company-news/moneta-1h-2026-slides-profit-up-8-guidance-raised-on-lending-strength-93CH-4810850
- UniCredit – Podnikatelé a menší firmy: https://www.unicreditbank.cz/cs/podnikatele-a-mensi-firmy/zarucni-programy.html ; Sazebník Small Business: https://www.unicreditbank.cz/content/dam/cee2020-pws-cz/cz-dokumenty/dokumenty-produkty/sazebniky/Sazebnik_Small_Business_platny_do_30-6_2022.pdf ; Wikipedia (SME 50–250 mil. Kč): https://en.wikipedia.org/wiki/UniCredit_Bank_Czech_Republic_and_Slovakia ; Finex (Business účty): https://finex.cz/banka/unicredit-bank/business-ucty-unicredit-bank/
- Air Bank – Podnikatelský účet: https://www.airbank.cz/produkty/podnikatelsky-ucet/ ; TZ vícečlenná s.r.o. (1/2026): https://www.airbank.cz/novinky/air-bank-nove-nabizi-podnikatelsky-ucet-i-pro-viceclenne-s-r-o/ ; Měšec: https://www.mesec.cz/aktuality/air-bank-nove-nabidne-podnikatelsky-ucet-i-pro-s-r-o-s-vice-cleny-z-plateb-kartou-vraci-1-bez-omezeni-cashbacku/
- Fio – Podnikatelé: https://www.fio.cz/podnikatele ; VZ 2023: https://www.fio.cz/docs/bannery/Fio_banka_vyrocni_zprava_2023.pdf ; VZ 2024: https://www.fio.cz/docs/cz/Fio_banka_vyrocni_zprava_2024.pdf
- Creditas – VZ 2023: https://www.creditas.cz/files/vyrocni-zprava-2023-creditas-banka-nahled.pdf ; VZ 2024 (Patria): https://www.patria.cz/zpravodajstvi/6381178/banka-creditas-as-vyrocni-financni-zprava-2024.html ; analýza: https://dluhopisar.cz/analyza-dluhopisu-banka-creditas/
- Partners / Trinity / mBank – Finmag přehled 2025: https://www.finmag.cz/finance/470899-podnikatelske-ucty-2025-vyplati-se-vam-prehled-vyhod-poplatku-a-nabidek-bank ; 2026: https://www.finmag.cz/finance/485143-podnikatelske-ucty-2026-vyplati-se-vam-prehled-vyhod-poplatku-a-nabidek-bank ; Partners Banka: https://www.partnersbanka.cz/podnikatelsky-ucet ; mBank mKonto Business: https://www.penize.cz/osobni-ucty/282916-mbank-podnikatelsky-ucet-mkonto-business
- Revolut Business ČR: https://cc.cz/revolut-v-cesku-raketove-roste-prekonal-milion-uzivatelu-a-nechava-za-sebou-i-velka-bankovni-jmena/ ; https://www.e15.cz/byznys/finance-a-bankovnictvi/revolut-ma-v-cesku-pres-milion-uzivatelu-v-poctu-stazeni-aplikace-prekonal-ceskou-sporitelnu-i-air-bank-1423424
- Banky podle velikosti firem: https://www.chytryrejstrik.cz/clanky/nejoblibenejsi-banky-podle-velikosti-firmy

**Daně / právo / registry**
- FS – Informace k paušální dani 2025 a 2026: https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pausalni-dan/informace-k-institutu-pausalni-dane-pro-rok-2025 ; Obecné informace: https://financnisprava.gov.cz/cs/dane/dane/dan-z-prijmu/pausalni-dan/obecne-informace ; TZ 1/2024 (32 tis.): https://financnisprava.gov.cz/cs/financni-sprava/media-a-verejnost/tiskove-zpravy-gfr/tiskove-zpravy-2024/pausalni-dan-prilakala-na-32-tisic-osvc ; TZ 2025 (změny 2025): https://financnisprava.gov.cz/cs/financni-sprava/media-a-verejnost/tiskove-zpravy-gfr/tiskove-zpravy-2024/pausalni-dan-2025-dulezite-zmeny ; TZ 2026 novinky: https://financnisprava.gov.cz/cs/financni-sprava/media-a-verejnost/tiskove-zpravy-gfr/tiskove-zpravy-2025/pausalni-dan-2026-novinky-terminy ; TZ 2026 (125 tis.): https://financnisprava.gov.cz/cs/financni-sprava/media-a-verejnost/tiskove-zpravy-gfr/tiskove-zpravy-2026/zajem-o-pausalni-dan-roste-letos ; Podnikatel.cz (řada 2021–2024): https://www.podnikatel.cz/clanky/podnikatele-ve-velkem-opousteji-danova-priznani-pausalni-dan-lame-rekordy/ ; BusinessInfo 2026: https://www.businessinfo.cz/clanky/jak-se-v-roce-2026-zvysi-pausalni-dan-hlaste-se-k-ni-od-rijna-do-ledna/ ; historie záloh: https://www.behounek.eu/l/pausalni-dan/
- Paušální výdaje: https://www.fakturoid.cz/almanach/dane/pausalni-vydaje ; https://www.kurzy.cz/dane-danova-priznani/osvc-vydajove-pausaly.htm
- ČSSZ – OSVČ v kostce: https://www.cssz.gov.cz/osvc-v-kostce ; otevřená data Počet OSVČ: https://data.cssz.cz/web/otevrena-data/graf-pocet-osvc-v-cr ; dataset: https://data.cssz.cz/dataset/prehled-o-celkovem-poctu-osvc-v-cr ; Podnikatel.cz (1 173 951; 688 824; 485 127): https://www.podnikatel.cz/clanky/opet-padl-rekord-poctu-osvc-jak-velky-podil-na-tom-ale-ma-svarcsystem/
- D&B – Rekordní rok 2025 (594 520 firem; 567 228 s.r.o.): https://www.dnb.com/cs-cz/blog/rekordni-rok-2025-vzniklo-nejvice-firem-za-poslednich-20-let.html ; https://www.businessinfo.cz/clanky/rekordni-rok-2025-vzniklo-nejvic-firem-za-poslednich-20-let/ ; RŽP 2,03 mil. FO / 56 % aktivních: https://zpravy.kurzy.cz/848220-v-cr-je-o-70-000-zivnostniku-mene-nez-pred-deseti-lety/
- CRIF – přírůstek podnikatelů 1–10/2025 (78 203 vzniklo, 48 266 zaniklo, +29 937): https://www.crif.cz/novinky-a-tiskove-zpravy/tiskove-zpravy/crif-v-cr-za-deset-mesicu-pribylo-29-937-podnikatelu-trikrat-vice-nez-v-minulem-roce/
- Insolvence 2024 (23 243 návrhů): https://vykup-nemovitosti.online/blog/insolvencni-rejstrik.php (sekundární; primárně Creditreform / ISIR)
- AMSP ČR – průzkumy a metodika (Ipsos, CATI/CASI, do 250 zam.): https://www.amsp.cz/pruzkumy-a-analyzy/pruzkumy ; https://amsp.cz/drobny-maly-a-stredni-podnikatel/
- Zákon o účetnictví – novela 2025: https://www.tpa-group.cz/news/novela-zakona-o-ucetnictvi/ ; https://danovky.cz/cs/co-prinese-novela-zakona-o-ucetnictvi ; https://portal.pohoda.cz/dane-ucetnictvi-mzdy/ucetnictvi/zmeny-v-kategorizaci-ucetnich-jednotek-a-pravidlech-povinneho-auditu-od-roku-2026/ ; https://www.svaz-ucetnich.cz/aktuality/novela-zakona-o-ucetnictvi-vysla-ve-sbirce-zakonu ; nový zákon 2027: https://portal.pohoda.cz/dane-ucetnictvi-mzdy/ucetnictvi/aktualni-stav-noveho-zakona-o-ucetnictvi/ ; https://www.deloitte.com/cz-sk/cs/services/audit-assurance/services/novy-zakon-o-ucetnictvi.html

---

## (g) Log odhadů a mezer

| Položka | Typ | Postup / kde dohledat |
|---|---|---|
| 1 mil. EUR ≈ 25 mil. Kč; 2 mil. EUR ≈ 50 mil. Kč | `[EST]` | kurz ~25 CZK/EUR; pro přesnost použít průměrný kurz ČNB daného roku |
| Podíl OSVČ v paušálním režimu ~11 % všech / ~18 % hlavních | `[EST]` | 125 tis. / 1 174 tis.; 125 / 689 tis. – různá data (2026 vs. 6/2025) |
| „Spící" FO ≈ 0,86 mil. (42 %) | `[EST]` | RŽP 2 029 257 (31. 12. 2025) − ČSSZ 1 173 951 (30. 6. 2025); různé datumy |
| UniCredit Small Business < 50 mil. Kč | `[EST]` | dovozeno z definice SME 50–250 mil. Kč (Wikipedia/VZ) – ověřit na unicreditbank.cz |
| ČNB – definice „živnostníci" v metodickém listu | `[DATA GAP]` | cnb.cz/docs/ARADY/MET_LIST/tuvob_cs.pdf |
| ČNB BLS – definice SME/velké podniky ve slovníčku | `[DATA GAP]` | cnb.cz/cs/statistika/setreni-uverovych-podminek-bank/ (dokument „Dotazník, metodologie a slovníček pojmů") |
| ČNB ZFS – členění úvěrů podnikům podle velikosti (AnaCredit) | `[DATA GAP]` | zfs_jaro_2025.pdf, zfs_podzim_2025.pdf – kapitola nefinanční podniky |
| ČS – oficiální hranice Podnikatelé / SME / Large Corporate; limit účtu Maxi | `[DATA GAP]` | csas.cz/cs/firmy, VZ 2024 (segmentová analýza), ceník podnikatelských účtů |
| ČSOB – obratová hranice „podnikatelé a malé firmy" vs. SME vs. corporate; segmenty ve VZ 2024 | `[DATA GAP]` | csob.cz/firmy; vz-csob-2024.pdf (sekundární indikace 200/300 mil. Kč neověřeny) |
| Moneta – obratová hranice small business / SME | `[DATA GAP]` | investors.moneta.cz – Annual Financial Report 2024/2025, note „Segment reporting"; IR prezentace |
| KB – přesná definice Retail vs. Corporate ve VZ 2024 | `[DATA GAP]` | KB-vyrocni-zprava-2024.pdf (kapitola Segmenty) |
| Raiffeisenbank / UniCredit / Creditas – názvy segmentů ve VZ 2024 | `[DATA GAP]` | VZ PDF (rb.cz/attachments, unicreditbank.cz, creditas.cz) |
| Paušální daň – stavy k 31. 12. 2023/2024/2025 | `[DATA GAP]` | TZ GFŘ (financnisprava.gov.cz), případně MF – nekonzistence 2024 vs. 2026 |
| ČSSZ – roční řada OSVČ 2019–2025 (hlavní/vedlejší) | `[DATA GAP]` | data.cssz.cz/dataset/prehled-o-celkovem-poctu-osvc-v-cr |
| ČSÚ – celostátní počet subjektů „se zjištěnou aktivitou" (FO / PO), řada 2021–2025 | `[DATA GAP]` | csu.gov.cz/statistiky-z-registru-ekonomickych-subjektu |
| ČSÚ SBS – aktuální velikostní pásma a podíl podniků < 25 mil. Kč obratu | `[DATA GAP]` | csu.gov.cz – Podniková strukturální statistika, tab. dle velikostních skupin |
| Novela ZoÚ – číslo ve Sbírce a přesné nové limity (11/22/120/240 vs. +25 %) | `[DATA GAP]` | zakonyprolidi.cz (Sbírka 2025), svaz-ucetnich.cz |
| Počet družstev a spolků podnikajících | `[DATA GAP]` | ČSÚ RES dle právních forem |
| Wise Business, Trinity, Partners – počty firemních klientů | `[DATA GAP]` | tiskové zprávy, VZ Partners Banky 2024 (partnersbanka.cz/userfiles/banka-vyrocni-zprava-2024-b1588b3b.pdf) |
| Creditreform – členění insolvencí FOP vs. PO 2021–2025 | `[DATA GAP]` | creditreform.cz – „Vývoj insolvencí v ČR" (roční TZ) |
