# WS5 část B — Benchmark trhy small business banking: Polsko, Rakousko, Slovensko

Datum práce: 2026-10-02 · Rozpočet: 35 dotazů WebSearch (využito 35: PL 13, AT 11, SK 11 vč. 1 dotazu na kurz ČNB) · WebFetch nepoužit · Cut-off nabídky bank 06/2026.
Segment: sole traders (PL JDG, AT EPU, SK živnostníci/SZČO) + mikrofirmy s obratem do ~2 mil. EUR (≈ 50 mil. Kč ≈ 8,9 mil. PLN při kurzech níže).
Kurzy pro přepočet: **1 EUR = 24,465 CZK; 1 PLN = 5,592 CZK** (ČNB, kurz devizového trhu k 1. 10. 2026 – kurz k 2. 10. 2026 v době práce nebyl v úryvku k dispozici; přístup 2026-10-02) [FACT]. Všechny CZK hodnoty níže jsou [EST] = původní měna × tento kurz.

---

## (a) Hypotézy a verdikt

| # | Hypotéza | Verdikt | Opora |
|---|---|---|---|
| H1 | Všechny tři trhy mají řádově větší/srovnatelnou základnu sole traders než ČR a jsou proto relevantní benchmark. | **Potvrzeno** | PL 3,84 mil. aktivních JDG (09/2026), AT 376 tis. EPU (12/2025), SK 377 tis. aktivních živností (2024) – viz tab. B1 |
| H2 | Benchmark banky nabízejí sole traderům účet za 0 € / 0 PLN trvale nebo podmíněně a prodávají na add-onech (fakturace, úvěr, karty). | **Potvrzeno** | SLSP „navždy zadarmo" pro živnostníky; ING/Pekao/Santander 0 PLN při aktivitě (ZUS); N26 Business Standard 0 € – tab. B2–B4 |
| H3 | George Business je v AT a SK dál než ČS (plně digitální onboarding s.r.o., integrace účetnictví, business karty) – existuje interní transfer. | **Částečně potvrzeno** | AT: samostatná aplikace George Business, správa rolí/uživatelů, export do účetnictví, co-vývoj s klienty; SK: online založení účtu bez výpisu z ŽR, George API pro ERP, add-on pro SuperFaktúru. Kvantifikace podnikatelských klientů SLSP/EBOe nenalezena [DATA GAP] |
| H4 | Regulatorní e-fakturace (PL KSeF 2026, SK 2027) je hlavní trigger pro integraci banka–fakturace–daně; AT bez národní B2B povinnosti zůstává pozadu. | **Potvrzeno** | KSeF 1. 2. / 1. 4. 2026 / 1. 1. 2027; SK zákon 385/2025 Z. z. od 1. 1. 2027; AT: žádná národní B2B povinnost, jen EU ViDA 2030 – tab. B5 |
| H5 | Fintechy (Revolut Business) rostou v segmentu rychleji než banky. | **Částečně potvrzeno** | Revolut SK: firemní klienti +33 %, objemy Business +56 % (2025); Revolut globálně 767 tis. firemních klientů. Srovnatelná růstová čísla bank chybí [DATA GAP] |

---

## (b) Datové tabulky

### B1 — Velikost a struktura segmentu

| Trh | Ukazatel | Hodnota | Zdroj / datum zdroje / metodika | Značka |
|---|---|---|---|---|
| PL | JDG v registru CEIDG celkem | 6 260 030 | outreachpilot.pl (agregátor dat CEIDG), stav 09/2026; vč. pozastavených a vymazaných | [FACT] – sekundární zdroj, ověřit na dane.biznes.gov.pl |
| PL | JDG aktivní | 3 836 780 | tamtéž, stav 09/2026 | [FACT] – sekundární zdroj |
| PL | Nové JDG 2025 | 288,8 tis. (+64 ks vs. 2024) | CEIDG via portalspozywczy.pl/poradnikhandlowca.com.pl, rok 2025 | [FACT] |
| PL | Obnovené JDG 2025 | 191,1 tis. | tamtéž | [FACT] |
| PL | Nové JDG 1H 2026 | 139,4 tis. (−6,5 % y/y) | CEIDG via Infor.pl / miedzyrzecz.biz, 1H 2026 | [FACT] |
| PL | Obnovené JDG 1H 2026 | 104,9 tis. (+2,6 % y/y) | tamtéž | [FACT] |
| PL | Nové JDG 9M 2025 | 220,1 tis. (−0,6 % y/y) | CEIDG via slaskibiznes.pl | [FACT] |
| PL | Mikropodniky (GUS/PARP, <10 zaměstnanců) | 2 307 838 (+3,0 %), 97,1 % firem | PARP „Raport o stanie sektora MŚP 2025" (ROSS 2025; verze ROSS 2026 ze dne 22. 4. 2026 existuje – neotevřena) | [FACT] |
| PL | Malé / střední / velké podniky | 48,7 tis. (2,1 %) / 14,4 tis. (0,6 %) / 3,8 tis. (0,2 %) | tamtéž | [FACT] |
| PL | Pracující v MŚP / v mikro | 6,9 mil. / 4,3 mil. | tamtéž | [FACT] |
| AT | Ein-Personen-Unternehmen (EPU) | 376 112 (+3,9 % y/y), 62,1 % všech členů WKO | WKO Statistik, stav 12/2025 (via ORF, WKO EPU-Factsheet 2025) | [FACT] |
| AT | Podíl žen mezi EPU | 51,6 % | WKO 2025 | [FACT] |
| AT | Největší skupiny EPU | Personenberatung/-betreuung ~65 900; UBIT ~40 400; persönliche Dienstleister ~29 000 | WKO 2025 | [FACT] |
| AT | KMU celkem (počet) | — | „KMU im Fokus 2025" (BMWET, 16. 3. 2026) nalezen, číslo v úryvku chybí | [DATA GAP: KMU im Fokus 2025, kap. 2; WKO Statistik „Unternehmen nach Größenklassen"] |
| AT | Digitální intenzita KMU | 73 % alespoň základní; 23 % prodává online; 29 % používá AI (2025) vs. 19 % (2024) | WKO / marie.wko.at, 2025 | [FACT] |
| AT | KMU.DIGITAL – podpořené firmy 2025 | > 6 500 | WKO, 2025 | [FACT] |
| SK | Vznik / zánik firem (PO) 2025 | > 24 000 vznik (téměr 25 tis.) / 7 708 zánik; 2024: 20 576 / 5 923 | FinStat „Analýza vzniku a zániku firiem 2025" (via teraz.sk, openiazoch.sk), rok 2025 | [FACT] |
| SK | Vznik / zánik živností 2025 | > 42 000 vznik (min. za 6 let) / > 66 000 zánik (historické max.); saldo < −20 000; první záporné saldo od 2016 | FinStat 2025 | [FACT] |
| SK | Aktivní živnosti (stock) | 377 324 (2024), z toho stavebnictví 104 148 | transparex.sk „Prehľad živností 2024" | [FACT] – rok 2024, novější stock nenalezen |
| SK | SZČO platící důchodové pojištění | 204 000 (−40 000) | Sociálna poisťovňa via techbyte.sk, 02/2026 | [FACT] – definice: pouze pojištění SZČO, ne všichni živnostníci |
| SK | Ukončené živnosti 1–8/2026 | téměř 50 000 | techbyte.sk, 08/2026 | [FACT] |
| SK | Databáze FinStat (kumulativně vč. zaniklých) | 655 902 firem a organizací; 1 515 517 živnostníků | finstat.sk/premium, 2026 | [FACT] – kumulativní, NE aktivní |

**Poznámka k definicím:** PL CEIDG = registr fyzických osob podnikatelů (aktivní vs. pozastavené); GUS/PARP mikro = < 10 zaměstnanců (ne obrat). AT EPU = členové WKO bez zaměstnanců (ne obrat). SK FinStat = vznik/zánik dle OR a ŽR; SP = pouze pojištění SZČO. Naše vymezení (obrat ≤ 50 mil. Kč ≈ 2,04 mil. EUR ≈ 8,9 mil. PLN) je širší než sole trader a užší než „mikro dle zaměstnanců" – dopad: čísla B1 jsou spodní odhad populace cílového segmentu (chybí s.r.o. s obratem 2–50 mil. Kč, které mají ≥ 10 zaměstnanců jen zřídka) [EST: kvalitativně, bez výpočtu].

**Penetrace business účtů:** [DATA GAP – PL: NBP/ZBP „Bankowość firm" nebo MGBI „Klienci biznesowi banków 2025"; AT: OeNB/WKO; SK: NBS statistika účtů].

### B2 — Polsko: klíčoví hráči (nabídka pro JDG/mikro)

| Hráč | Produkt | Cena (původní / CZK) | Onboarding, obsluha | Integrace, ekosystém | Úvěr | Ekonomika / klienti | Datum zdroje | Značka |
|---|---|---|---|---|---|---|---|---|
| mBank | Konto firmowe (segment retail – firmy), mKsięgowość | — | — | mKsięgowość (účetnictví v bance) – počet uživatelů nenalezen | — | Retail klienti 5,9 mil. PL+CZ+SK vč. mikrofirem (31. 12. 2025); 5 850 tis. (Q3 2025); korporátní klienti K1–K3: 37 375 (Q3 2025), 37,6 tis. (31. 12. 2025) – **ne** small business | mBank IR prezentace Q3 2025 (30. 10. 2025), Q4 2025 (10. 2. 2026) | [FACT] klienti; [DATA GAP: počet mikrofirem – mBank „Sprawozdanie Zarządu 2025", sekce Bankowość Detaliczna – firmy] |
| PKO BP | PKO Konto Firmowe (start-upy a MŚP s příjmy ≤ 15 mil. PLN ≈ 83,9 mil. Kč) | Taryfa změněna od 1. 12. 2025; konkrétní sazba v úryvku chybí | — | iPKO biznes, e-služby (neověřeno) | — | Promo do 3 600 PLN (≈ 20 131 Kč) od 19. 8. 2025; „blisko 40 % MŚP vybírá PKO" = průzkum 2017 | pkobp.pl 2025; bankomania 2017 | [FACT] promo; [STALE: 2017] podíl; [DATA GAP: počet firemních klientů – PKO BP Raport roczny 2025, segment „firmy i przedsiębiorstwa"] |
| Santander Bank Polska | Konto Firmowe Godne Polecenia (pro JDG v CEIDG s NIP+REGON) | 25 PLN/měs. (≈ 140 Kč), 0 PLN při platbě ZUS ≥ 200 PLN; karta 7 PLN (≈ 39 Kč), 0 při bezhot. ≥ 400 PLN; 15 tuzemských převodů zdarma | — | — | — | Promo 1. 2.–30. 4. 2026, bonus do 2 400 PLN (≈ 13 421 Kč) | bankier.pl / wise.com, datum zdroje neznámé; promo 02–04/2026 | [STALE: nejnovější datovaný zdroj 04/2026] |
| ING Bank Śląski | Konto Direct dla Firmy (JDG se zjednodušeným účetnictvím) | 0 PLN při aktivitě (1 převod ZUS/US nebo příchozí ≥ 2 000 PLN ≈ 11 184 Kč), jinak 19 PLN (≈ 106 Kč); promo „Konto za 0 zł" do 31. 3. 2026 | — | — | — | Premie do 3 600 PLN | rankingkont.org „opłaty 2026", totalmoney.pl – datum zdroje neznámé | [STALE: nejnovější datovaný zdroj 03/2026] |
| Bank Pekao | Konto Biznes z Żubrem (nahradilo Konto Przekorzystne Biznes) | PB: 15 PLN/měs. (≈ 84 Kč), 0 při příchozích ≥ 2 000 PLN nebo převodu ZUS; karta 12 PLN (≈ 67 Kč), 0 při bezhot. ≥ 500 PLN; zdražení od 1. 7. (cashless.pl) | — | — | — | Promo do 4 200 PLN (≈ 23 486 Kč), žádosti do 30. 6. 2026 | rankingkont.org „2026", cashless.pl – datum zdroje neznámé | [STALE: nejnovější datovaný zdroj 06/2026 – hraniční] |
| Revolut Business PL | Konto firmowe, plány Basic/Grow/Scale/Enterprise | Basic od 50 PLN (≈ 280 Kč), Grow od 100 PLN (≈ 559 Kč), Scale od 400 PLN (≈ 2 237 Kč)/měs. | plně digitální (CLAIM) | — | — | Revolut PL ~5 mil. uživatelů (převážně retail); globálně 500 tis. firemních klientů a „20 tis. firem měsíčně" | rankingkont.org „analiza 2026", rankomat.pl – datum neznámé | [CLAIM] růst; [STALE?: datum neznámé] cena |
| Finom PL, Qonto PL | — | — | — | — | — | — | nenalezeno | [DATA GAP: finom.co/pl, qonto.com/pl ceníky; KNF registr EMI] |

### B3 — Rakousko: klíčoví hráči

| Hráč | Produkt | Cena (původní / CZK) | Onboarding, obsluha | Integrace, ekosystém | Úvěr | Ekonomika / klienti | Datum zdroje | Značka |
|---|---|---|---|---|---|---|---|---|
| Erste Bank Oesterreich + Sparkassen | s Geschäftskonto (Einzelverrechnung), EPU Smart (paušál pro EPU), s Gründer Konto; George (1 uživatel) / George Business One (více uživatelů) | s Geschäftskonto od 10,41 €/měs. (≈ 255 Kč); EPU Smart 13,61 €/měs. (≈ 333 Kč); George 7,43 €/měs./účet (≈ 182 Kč); George Business One 18,00 €/měs. (≈ 440 Kč); Gründer 1. rok 4,95 €/měs. (≈ 121 Kč, −50 %) | s Gründer Konto „einfach online eröffnen"; samostatná aplikace George Business (iOS App Store AT) | George Business: přehled, převody, hromadné příkazy, správa business karet, správa uživatelů a rolí/oprávnění, rozhraní a export pro účetnictví, import datových nosičů; BMD software: přímé bankovní napojení pro platby | — [DATA GAP: s Betriebsmittelkredit online] | Erste Bank + Sparkassen: 4,3 mil. klientů, 48 institucí, 732 poboček (12/2025); svobodná povolání, OSVČ a menší podniky = 10,3 % úvěrového objemu; Erste Group: George 11,4 mil. uživatelů, z toho 2,6 mil. na George Business (12/2025 – viz pozn.); George Business „plně v provozu v AT, RO, CZ s > 75 000 firemními klienty" | capitalo.at / bankkonditionen.at 06–08/2026 (ceny); Erste Group Geschäftsbericht 2025; Sparkassenverband „Zahlen und Fakten" | [FACT] ceny (06–08/2026); [FACT] klienti; [FACT – ověřit] 2,6 mil. George Business (úryvek bez kontextu, patrně Erste Group celkem; interní ověření doporučeno); 75 tis. – datum výroku neznámé |
| Raiffeisen (RBG, ~300 samostatných bank) | Geschäftskonto/Gewerbekonto + Mein ELBA Business; „Willkommenspaket für Einzelunternehmen" (RLB OÖ) | ELBA-Business 7,40 €/měs. (≈ 181 Kč); Mein ELBA Basis 0 €, Premium 3,74 €, Premium Plus 7,51 €/měs.; vedení účtu např. 18,43 €/čtvrtletí u některých RB | — | — | — | — | Raiffeisen „Konditionen 2026" (PDF, regionální) | [FACT] ceny 2026 – datum účinnosti v úryvku neuvedeno → [STALE-risk]; ceny se liší dle banky |
| BAWAG | BusinessBox Dynamic; BusinessBox Starter (zakladatelé) | Dynamic 9,90 €/měs. (≈ 242 Kč) vč. 20 el. transakcí; Starter 0 € 12 měs., 0,54 €/transakce (20 zdarma) | — | hotovostní vklady přes síť Pošty | — | — | capitalo.at 09/2026 | [FACT] |
| bank99 | Geschäftskonto99 (EPU, obce, OSVČ) | ~4,99 €/měs. (≈ 122 Kč); indexace CPI +3,51 % od 1. 5. 2026; debetní karta zdarma | — | AT-IBAN, vklady hotovosti na ~1 700 místech (pošty) | — | — | capitalo.at 09/2026 | [FACT] |
| N26 Business | Business Standard / Smart / Go / Metal (pouze OSVČ pod vlastním jménem) | 0 € / 4,90 € (≈ 120 Kč) / 9,90 € (≈ 242 Kč) / 16,90 € (≈ 414 Kč)/měs.; 0,1 % cashback | plně digitální (CLAIM) | — | — | — | capitalo.at (04/2026), gratis-konto.at 09/2026 | [FACT] ceny; Smart 4,90 € datováno 04/2026 → [STALE-risk], 09/2026 srovnání potvrzuje existenci tarifu |
| Finom AT | — | úryvek „249,00 €/měs." – nevěrohodné, pravděpodobně chyba srovnávače | — | — | — | — | capitalo.at | [DATA GAP: finom.co/de-at ceník] |

### B4 — Slovensko: klíčoví hráči

| Hráč | Produkt | Cena (původní / CZK) | Onboarding, obsluha | Integrace, ekosystém | Úvěr | Ekonomika / klienti | Datum zdroje | Značka |
|---|---|---|---|---|---|---|---|---|
| Slovenská sporiteľňa (Erste) | Business účet pre živnostníkov (SZČO) „s Georgeom navždy zadarmo"; Business účet pre firmy (PO) 1 rok zdarma vč. online založení | 0 €/měs. trvale (SZČO); SEPA platba 0,22 € (≈ 5,4 Kč); 1 VISA Business + 1 vkladová karta; bonus 1 % z plateb kartou | Založení online v aplikaci George bez výpisu ze ŽR a bez návštěvy pobočky; PO: online založení (slsp.sk) | George API pro ERP; add-on pro import výpisů do SuperFaktúry; automatické párování úhrad dle VS a QR PAY; George AI (spuštěno 9. 9. 2026 pro první tisíce klientů) | Spotřební úvěr s online schválením „do minut" od 4,99 % (retail, 05/2026); splátkové úvěry pro začínající podnikatele – online schvalování business úvěru neověřeno | > 2 mil. klientů, > 400 obchodních míst, téměř 6 mil. účtů (2026); George 1,33 mil. uživatelů, 1,17 mil. v mobilu (09/2026) | slsp.sk „Začíname podnikať" (2026), podnikajte.sk 2025, techbyte.sk 02/2025 (oznámení), slsp.sk 9. 9. 2026 | [FACT] 0 € (potvrzeno slsp.sk 2026); [DATA GAP: počet podnikatelských klientů / George Business SK – SLSP Výročná správa 2025, Erste Group AR 2025 segment SK] |
| Tatra banka (RBI) | Tatra Business TB; Tatra Business Premium; PodnikAI (s Expl0) | 7 €/měs. (≈ 171 Kč), 0 € prvních 12 měs. pro nové podnikatele a jednoosobové s.r.o.; Premium 19 €/měs. (≈ 465 Kč) | — | PodnikAI – AI asistent pro podnikatele (tatrabanka.sk) | — | — | tatrabanka.sk, wise.com, finfin.sk „porovnanie 2026" – datum neznámé | [STALE-risk: datum zdroje neznámé]; Tatra Pay [DATA GAP: tatrabanka.sk/tatrapay] |
| VÚB (Intesa) | Biznis účet Štandard / Aktiv / Premium | 8 € (≈ 196 Kč) / 13 € (≈ 318 Kč) / 22 € (≈ 538 Kč)/měs.; 6 měs. zdarma; 15 el. transakcí; 100 % sleva 12 měs. pro začínající | — | — | — | — | Cenník VÚB PO platný od 1. 1. 2026 | [STALE: 01/2026 – tarif účinný od 1. 1. 2026, bez potvrzení platnosti po 06/2026] |
| 365.bank | Výhodný / Komfortný / Prémiový balík | 8 € (≈ 196 Kč) / 18 € (≈ 440 Kč) / 40 € (≈ 979 Kč)/měs. | — | — | — | — | finfin.sk 2026, wise.com – datum neznámé | [STALE-risk: datum zdroje neznámé] |
| Revolut Business SK | Firemný účet Basic/Grow/Scale/Enterprise | od 10 € (≈ 245 Kč) / 30 € (≈ 734 Kč) / 90 € (≈ 2 202 Kč)/měs. | plně digitální (CLAIM) | — | — | Revolut SK > 550 tis. klientů; firemní klienti SK +33 %, objem transakcí Business +56 % (2025); globálně 767 tis. firemních klientů = 16 % výnosů | finsider.sk / digitalportal.sk (výsledky 2025, publ. 2026); revolut.com/sk ceník | [FACT] růst; [CLAIM] „množstvo výhod"; ceník datum neznámé |

### B5 — Enablery

| Trh | Enabler | Stav / termíny | Dopad na small business banking | Zdroj, datum | Značka |
|---|---|---|---|---|---|
| PL | KSeF (povinná e-fakturace) | 1. 2. 2026: vystavování pro plátce s obratem 2024 > 200 mil. PLN (≈ 1,1 mld. Kč) + povinnost **přijímat** pro všechny vč. mikro; 1. 4. 2026: ostatní; 1. 1. 2027: nejmenší (prodej ≤ 10 tis. PLN/měs. ≈ 56 tis. Kč) | Celá populace JDG musí od 2/2026 přijímat strukturované faktury → banky/fintechy integrují KSeF do účtů (mBank má vlastní KSeF stránku) | ifirma.pl, mbank.pl/artykuly/ksef-harmonogram, bizky.ai (2025–26) | [FACT] |
| PL | BLIK | 2025: 2,9 mld. transakcí, 441,5 mld. PLN (≈ 2 469 mld. Kč); 20,7 mil. aktivních uživatelů (+2 mil.); POS 704,5 mil. transakcí (+22 %), 41,9 mld. PLN; e-commerce ~½ transakcí; ~8 mil./den | Univerzální P2P/e-com/POS akceptace pro mikropodnikatele bez terminálu | blik.com, bank.pl, 01–02/2026 | [FACT] |
| PL | BGK gwarancja de minimis | 2026: krytí do 60 % jistiny, max. 5 mil. PLN (≈ 28 mil. Kč), provize 0,5 % p.a., 60 měs. provozní / 120 měs. investiční; od 16. 4. 2026 obranný průmysl 70–80 % a 0 %; strop de minimis 300 tis. EUR/3 roky | Portfoliová garance distribuovaná bankami → standardizovaný mikroúvěr | bgk.pl, onecredit.pl 2026 | [FACT] |
| PL | Profil Zaufany / mObywatel | — | e-identita pro onboarding JDG | nenalezeno | [DATA GAP: gov.pl statistiky mObywatel 2026] |
| AT | e-Rechnung | B2G vůči federaci povinné od 1. 1. 2014; **žádná národní B2B povinnost**; EU ViDA (směrnice 2025/516, transpozice od 31. 12. 2026): od 1. 7. 2030 přeshraniční B2B jen strukturovaně; národní B2B otevřené | Slabší regulatorní tah na integraci banka–fakturace než PL/SK | wko.at (AUSTRIAPRO), selbststaendig-machen.at, EY AT, 2026 | [FACT] |
| AT | ID Austria | — | e-identita pro onboarding | nenalezeno | [DATA GAP: oesterreich.gv.at / BMF statistika ID Austria] |
| AT | KMU.DIGITAL (dotace) | 2025 > 6 500 podpořených firem | Dotované poradenství/implementace digitalizace | WKO 2025 | [FACT] |
| SK | Povinná e-fakturace | Zákon 385/2025 Z. z. (novela 222/2004 o DPH): od **1. 1. 2027** plátci DPH vystavují, posílají i přijímají tuzemské B2B a B2G faktury jen strukturovaně (XML); dobrovolně od 05/2026; pokuty 10–100 tis. EUR | Trigger pro integraci banka–fakturace (Tatra banka už publikuje návod) | tatrabanka.sk blog, forum-media.sk, KPMG SK, 2026 | [FACT] |
| SK | Okamžité platby SEPA Inst | Příjem všemi bankami od 9. 1. 2025, odesílání od 9. 10. 2025 + Verification of Payee; podíl na SEPA převodech 14,3 % (Q4 2023), 14,92 % (zač. 2024); první 4 banky (SLSP, VÚB, Tatra, Raiffeisen) > 50 % trhu plateb | Okamžité inkaso pro podnikatele, párování v reálném čase | SBA (sbaonline.sk), teraz.sk, financnykompas.sk 2025 | [FACT] |
| SK | BankID SK | — | — | nenalezeno | [DATA GAP: sbaonline.sk / bankid.sk] |
| SK | Konsolidační balíček (daně, odvody) | Rekordní zánik živností 2025 (66 tis.), pokles SZČO v SP o 40 tis. | Zmenšuje trh sole traders, posun do s.r.o. (vznik PO +~17 % y/y) | FinStat, SP via techbyte 2026 | [FACT] |

---

## (c) Zjištění s action titles

### 1. Polsko: 3,84 mil. aktivních JDG a 2,3 mil. mikrofirem – trh ~3,5× větší než ČR, ale v 1H 2026 s poklesem nových registrací o 6,5 %
Aktivních JDG je 3 836 780 (CEIDG via outreachpilot.pl, 09/2026 [FACT, sekundární]); za rok 2025 vzniklo 288,8 tis. a 191,1 tis. bylo obnoveno [FACT]. V 1H 2026 klesly nové registrace na 139,4 tis. (−6,5 %), obnovení rostou (+2,6 %) [FACT] – trh dospívá, akvizice banky musí cílit na „restart" a přechod z pozastavení, nikoli jen na start-upy. Mikropodniků dle GUS je 2 307 838 (97,1 %) a zaměstnávají 4,3 mil. osob (PARP ROSS 2025) [FACT].

### 2. Polské banky soutěží o JDG „nulou podmíněnou ZUS platbou" + welcome bonusy 2 400–4 200 PLN, nikoli trvalou nulou
Santander 25 PLN → 0 při platbě ZUS ≥ 200 PLN; ING 19 PLN → 0 při převodu na ZUS/US nebo příchozích ≥ 2 000 PLN; Pekao 15 PLN → 0 při ≥ 2 000 PLN nebo ZUS [vše STALE 03–06/2026]. Bonusy: Santander do 2 400 PLN, ING/PKO do 3 600 PLN, Pekao do 4 200 PLN (≈ 13–23 tis. Kč) [FACT/STALE]. Mechanika „ZUS jako aktivitní podmínka" zároveň nutí podnikatele koncentrovat odvody v jedné bance = primární účet. Revolut Business je naproti tomu placený od 50 PLN/měs. [datum neznámé].

### 3. KSeF od 1. 2. 2026 nutí každou JDG přijímat strukturované faktury – polské banky mají 12–18 měsíců náskok v integraci banka × e-fakturace × daně
Harmonogram: 1. 2. 2026 velcí + příjem pro všechny; 1. 4. 2026 ostatní; 1. 1. 2027 nejmenší ≤ 10 tis. PLN/měs. [FACT]. mBank provozuje vlastní KSeF obsahovou stránku a mKsięgowość (účetnictví v bance), počet uživatelů nenalezen [DATA GAP]. Pro ČS je to předobraz situace po zavedení e-fakturace v ČR.

### 4. BLIK s 2,9 mld. transakcí a 20,7 mil. aktivních uživatelů je akceptační infrastruktura mikropodnikatelů bez terminálu
2025: 2,9 mld. transakcí za 441,5 mld. PLN, POS +22 % na 704,5 mil., e-commerce ~polovina [FACT]. Pro small business je BLIK „terminál v telefonu" – ekvivalent v ČR (QR platby/okamžité platby) nemá srovnatelnou penetraci.

### 5. mBank reportuje 37,6 tis. korporátních klientů, ale mikrofirmy skrývá v 5,9 mil. retailu – benchmark „počet small business klientů" v PL není veřejný
mBank: 37 375 (Q3 2025) → 37,6 tis. (31. 12. 2025) korporátních klientů K1–K3; retail 5 850 tis. (Q3 2025) „individuálních klientů a mikropodniků" bez rozpadu [FACT]. PKO: produkt pro firmy s příjmy ≤ 15 mil. PLN, podíl „blisko 40 % MŚP" je z 2017 [STALE]. Závěr: polské banky small business segment v IR nekvantifikují → [DATA GAP] na úrovni výročních zpráv 2025 (mBank „Sprawozdanie Zarządu", PKO „Raport roczny").

### 6. Rakousko: 376 tis. EPU (+3,9 %) = 62 % všech firem; segment roste navzdory stagnaci, ženy tvoří 51,6 %
WKO 12/2025 [FACT]. Dominují osobní služby (65,9 tis.) a UBIT (40,4 tis.) – znalostní OSVČ s nízkou transakčností, vhodní pro paušální účet (EPU Smart 13,61 €).

### 7. Erste Bank/Sparkassen: George Business je samostatná aplikace s rolemi, business kartami a účetním exportem; cena 7,43 € (George) / 18 € (George Business One) měsíčně
Funkce potvrzené na sparkasse.at (2026): přehled, převody, hromadné příkazy, správa business karet, správa uživatelů a oprávnění, rozhraní/export pro účetnictví, import datových nosičů [FACT]; aplikace George Business Österreich v App Store [FACT]; vývoj „společně s firemními klienty" (brutkasten, Kickinger) [CLAIM]. Ceny 06–08/2026: s Geschäftskonto od 10,41 €/měs., EPU Smart 13,61 €, zakladatelé 4,95 €/měs. 1. rok [FACT]. Erste Group AR 2025: George 11,4 mil. uživatelů, z toho 2,6 mil. George Business (12/2025) [FACT – úryvek bez kontextu, interně ověřit]; dřívější výrok „> 75 000 firemních klientů na George Business v AT, RO, CZ" [datum neznámé]. Podíl OSVČ/svobodných povolání/menších podniků na úvěrech Sparkassen 10,3 % [FACT].

### 8. Rakouský trh účtů pro EPU je cenově stlačen na 4,99–9,90 €/měs. (bank99, BAWAG, N26) s hotovostí přes poštu jako diferenciátorem
bank99 Geschäftskonto99 ~4,99 €/měs. (CPI indexace +3,51 % od 1. 5. 2026), vklady na ~1 700 poštách; BAWAG BusinessBox Dynamic 9,90 € vč. 20 transakcí, Starter 0 € 12 měs.; N26 Business Standard 0 €/Smart 4,90 € (jen OSVČ pod vlastním jménem) [FACT 09/2026]. Erste je s 10,41–18 € prémiový; prodává na ekosystému (George Business, Gründer) – stejně jako ČS.

### 9. Rakousko bez národní B2B e-fakturace: integrace banka–účetnictví běží přes software (BMD) a export, ne přes regulatorní hub
Žádná národní B2B povinnost; B2G od 2014; ViDA 2030 [FACT]. BMD nabízí přímé bankovní napojení pro závazky/pohledávky [FACT]. George Business poskytuje export/import datových nosičů [FACT]. Z pohledu ČS: AT model = „bank-to-ERP export", SK/PL model = „regulatorní e-faktura v bance".

### 10. Slovensko: rekordní zánik 66 tis. živností v 2025 a −40 tis. SZČO v SP – segment se smršťuje a přesouvá do s.r.o. (+~17 % vzniků PO)
FinStat 2025: živnosti 42 tis. vznik / 66 tis. zánik (první záporné saldo od 2016), firmy 24 tis.+ vznik (2024: 20 576) / 7 708 zánik [FACT]; SP: 204 tis. SZČO platících důchodové pojištění (−40 tis.) [FACT]; do 8/2026 dalších ~50 tis. ukončených živností [FACT]. Důvod: konsolidační balíček (odvody, kontroly). Pro banky: růst poptávky po účtu pro jednoosobové s.r.o. – SLSP (PO 1 rok zdarma, online) i Tatra (0 € 12 měs. pro jednoosobové s.r.o.) na to už reagovaly.

### 11. SLSP: účet pro živnostníka „navždy zadarmo" + online založení bez výpisu ze ŽR + 1 % cashback – nejagresivnější nabídka Erste trhu
0 €/měs. trvale, SEPA 0,22 €, VISA Business + vkladová karta, 1 % z plateb kartou; založení v Georgi bez dokladů ze ŽR a bez pobočky; PO 1 rok zdarma vč. online založení [FACT, slsp.sk 2026; oznámeno 02/2025]. George 1,33 mil. uživatelů (09/2026), George AI od 9. 9. 2026 [FACT]. Počet podnikatelských klientů SLSP: [DATA GAP]. Konkurence: Tatra 7 €, VÚB 8–22 € [STALE 01/2026], 365.bank 8–40 €, Revolut od 10 €.

### 12. SK e-fakturace od 1. 1. 2027 + plné SEPA Instant od 10/2025: slovenské banky mají 15 měsíců na integraci; Tatra banka už vede obsahově
Zákon 385/2025 Z. z., XML, dobrovolně od 05/2026, pokuty 10–100 tis. EUR [FACT]; okamžité platby odesílají všechny banky od 9. 10. 2025 vč. Verification of Payee [FACT]; SLSP má George API pro ERP a add-on pro SuperFaktúru [FACT].

### 13. Revolut Business roste na SK o 33 % klientů a 56 % objemů (2025) – fintech tlak na Erste trhu je měřitelný
Revolut SK > 550 tis. klientů; firemní klienti +33 %, objem Business +56 %; globálně 767 tis. firemních klientů = 16 % výnosů [FACT, výsledky 2025]. V PL Revolut ~5 mil. uživatelů [FACT] a ceník od 50 PLN.

---

## Long-list pozorovaných praktik (PL + AT + SK) – kandidáti pro ČS

| # | Praktika | Kde | Vazba na ČR / možnost interního transferu v Erste |
|---|---|---|---|
| P1 | **Účet pro živnostníka trvale za 0 € + online založení bez výpisu z rejstříku, PO 1 rok zdarma online** | SLSP (SK) | Přímý transfer v rámci Erste: stejný George, stejný KYC stack. Pro ČS otázka marže vs. akvizice; SK ukazuje, že Erste to na jednom trhu už dělá. |
| P2 | **„Aktivitní nula" vázaná na platbu sociálního pojištění/daní (ZUS/US)** | ING, Santander, Pekao (PL) | Česká obdoba: platba ČSSZ/FÚ z účtu jako podmínka 0 Kč – levnější než trvalá nula, zároveň identifikuje primární účet. |
| P3 | **Samostatná aplikace George Business s rolemi/oprávněními, business kartami a účetním exportem, tarifovaná zvlášť (George 7,43 € / Business One 18 €)** | Erste Bank Oesterreich (AT) | Interní transfer: ČS může převzít model „jedno-uživatelský George vs. multi-user George Business One" vč. cenové diferenciace pro s.r.o. |
| P4 | **Regulatorní e-fakturace integrovaná do banky (KSeF content + mKsięgowość; SK příprava na 2027)** | mBank (PL), Tatra banka (SK) | ČR zatím bez povinné B2B e-fakturace, ale ViDA 2030 přijde; ČS může připravit „e-faktura v Georgi" s předstihem a využít SK pilot 2027 jako testbed. |
| P5 | **Bank API pro ERP + add-on pro import výpisů do fakturačního SaaS (SuperFaktúra), automatické párování dle VS/QR** | SLSP (SK) | Český ekvivalent: iDoklad/Fakturoid/Pohoda. Interní transfer API vrstvy George. |
| P6 | **Portfoliová státní garance mikroúvěrů distribuovaná bankou (BGK de minimis 60 %, 0,5 % p.a., do 5 mil. PLN)** | PL (BGK) | ČR: NRB záruky – srovnat parametry a míru automatizace schvalování v bance (mBank/PKO). |
| P7 | **Paušální účet pro EPU (EPU Smart 13,61 €) + zakladatelský tarif −50 % 1. rok (4,95 €)** | Erste Bank Oesterreich (AT) | Jednoduchá segmentace sole trader vs. firma a „Gründer" lifecycle pricing – přenositelné bez IT změn. |
| P8 | **Hotovost přes partnerskou síť (pošta ~1 700 míst) jako diferenciátor levného business účtu** | bank99, BAWAG (AT) | ČS: síť poboček + Česká pošta partnerství – relevance pro řemeslníky a gastro s hotovostí. |
| P9 | **Mobilní P2P/POS akceptace bez terminálu (BLIK 2,9 mld. transakcí)** | PL | ČR: QR/okamžité platby; ČS může cílit „terminál v telefonu" pro mikropodnikatele. |
| P10 | **AI asistent pro podnikatele (PodnikAI; George AI)** | Tatra banka, SLSP (SK) | George AI spuštěn 9/2026 na SK – interní transfer do ČS včetně business use-cases (cash-flow, daně). [CLAIM] – bez metrik. |

---

## (d) So what pro ČS

1. **SK ukazuje, že Erste umí „0 € navždy pro živnostníka + plně online onboarding bez dokladů"** – ČS nemusí nic vynalézat, jen rozhodnout o ekonomice (SLSP kompenzuje přes SEPA 0,22 €, karty, úvěry). Nejrychlejší interní transfer: KYC flow z George SK a PO online založení.
2. **AT ukazuje produktovou architekturu pro s.r.o.: George (1 uživatel) vs. George Business One (multi-user, role, business karty, účetní export) za 18 €/měs.** – ČS může převzít segmentaci a cenovou diferenciaci; relevantní zvlášť při přesunu živnostníků do jednoosobových s.r.o. (trend viditelný na SK).
3. **PL je 12–18 měsíců před ČR v e-fakturaci (KSeF) a SK ji zavádí 1. 1. 2027** – ČS by měla postavit „e-faktura + účetnictví v Georgi" tak, aby ji bylo možné pilotovat se SLSP v 2027 a přenést do ČR před ViDA 2030; mBank mKsięgowość je referenční bank-embedded accounting, jeho adopci je třeba dohledat.
4. **Fintech tlak je měřitelný (Revolut Business SK +33 % klientů / +56 % objemů 2025; globálně 767 tis. firem)** – argument pro cenovou obranu základního účtu (viz P1/P2) a pro rychlost onboardingu, nikoli pro feature parity.
5. **Datová mezera: ani jedna banka (mBank, PKO, Erste AT, SLSP) veřejně neuvádí počet small business klientů** – pro CEO benchmark „podíl na trhu small business" je nutný interní Erste datový pull (George Business uživatelé AT/SK/CZ, Erste Group AR 2025 segmentové tabulky) místo externího researche.

**Co lze převzít z Erste AT/SK (shrnutí):** P1 (SK: 0 € + online onboarding bez ŽR), P3 (AT: George Business One multi-user, role, karty, export), P5 (SK: George API + SuperFaktúra add-on), P7 (AT: EPU Smart paušál + Gründer −50 %), P10 (SK: George AI). Všechny běží na sdílené platformě George → nízké IT náklady transferu; chybějící jsou adopční metriky (DATA GAP).

---

## (e) Zdroje (URL · datum zdroje · přístup 2026-10-02)

**Kurz**
- https://www.cnb.cz/cs/financni-trhy/devizovy-trh/kurzy-devizoveho-trhu/kurzy-devizoveho-trhu/ · 1. 10. 2026 (EUR 24,465; PLN 5,592)

**Polsko**
- https://outreachpilot.pl/firmy · stav 09/2026 (CEIDG 6 260 030 / 3 836 780 aktivních) – sekundární agregátor
- https://www.portalspozywczy.pl/technologie/wiadomosci/w-2025-roku-na-rynku-powstalo-prawie-289-tys-firm-ponad-191-tys-odwiesilo-dzialalnosc,285835.html · 01/2026 (CEIDG 2025)
- https://mojafirma.infor.pl/jak-zalozyc-firme/podejmowanie-dzialanosci/7021682,w-pol-roku-otwarto-ponad-149-tys-jednoosobowych-firm-do-tego-wznowio.html · 07/2026 (1H 2026)
- https://miedzyrzecz.biz/aktualnosci/spada-liczba-nowych-jednoosobowych-firm/ · 2026 (1H 2026: 139,4 tis., −6,5 %)
- https://www.slaskibiznes.pl/wiadomosci,ceidg-podsumowuje-9-miesiecy-rynek-mikrofirm-w-2025-roku-stabilny-dojrzaly-odporny,wia5-1-12519.html · 10/2025
- https://fepw.parp.gov.pl/storage/publications/pdf/ROSS_2025.pdf · 2025 (PARP ROSS 2025); https://feng.parp.gov.pl/storage/publications/pdf/ROSS_2026_22-04-2026.pdf · 22. 4. 2026 (neotevřeno)
- https://bank.pl/raport-parp-mikrofirmy-z-najwiekszym-wkladem-do-polskiego-pkb/ · 2025
- https://www.mbank.pl/pdf/msp-korporacje/relacje-inwestorskie/wyniki-finansowe/2025/presentation-q3-pol.pdf · 30. 10. 2025
- https://www.mbank.pl/pdf/msp-korporacje/relacje-inwestorskie/wyniki-finansowe/2025/presentation-q4-pol.pdf · 10. 2. 2026
- https://www.mbank.pl/pdf/relacje-inwestorskie/introduction-to-mbank-pol.pdf · 31. 12. 2025
- https://www.mbank.pl/artykuly/ksef-harmonogram/ · 2025–26
- https://www.pkobp.pl/firmy/konta/konto-firmowe · 2025; https://www.pkobp.pl/aktualnosci/zmieniamy-taryfe-prowizji-i-oplat-dla-firm-i-przedsiebiorstw · 2025 (od 1. 12. 2025); https://www.pkobp.pl/media/aktualnosci/promocja-i-csr/pko-bank-polski-wystartowal-z-nowa-promocja-dla-firm-nawet-do-3600-zl-premii · 19. 8. 2025
- https://bankomania.pkobp.pl/bankofirma/blisko-40-malych-firm-wybiera-pko-bank-polski/ · 2017 [STALE]
- https://www.bankier.pl/smart/Konto-Firmowe-Godne-Polecenia-w-Santander-Bank-Polska-warunki · datum neznámé; https://wise.com/pl/blog/santander-konto-firmowe-godne-polecenia · datum neznámé
- https://rankingkont.org/konto-firmowe-ing-bank-slaski-konto-direct-dla-firmy/ · 2026; https://www.ing.pl/male-firmy/konta-firmowe · datum neznámé
- https://rankingkont.org/analizy/konto-firmowe-pekao-bank-konto-biznes-z-zubrem/ · 2026; https://www.cashless.pl/13733-pekao-biznes-podwyzki · datum neznámé; https://www.tanie-konto.pl/pekao/konto-firmowe-przekorzystne-biznes/ · 2026
- https://rankingkont.org/analizy/konto-firmowe-revolut-business-polska/ · 2026; https://rankomat.pl/finanse/poradniki/konto-firmowe-revolut/ · datum neznámé
- https://onecredit.pl/informacje/gwarancja-de-minimis-bgk-2026/ · 2026; https://www.bgk.pl/produkty/gwarancja-de-minimis/strefa-banku/ · 2026
- https://www.ifirma.pl/blog/ksef-a-obowiazki-przedsiebiorcow-kto-i-kiedy-musi-korzystac-z-systemu/ · 2025–26; https://bizky.ai/blog/ksef-od-kiedy-obowiazkowy-harmonogram/ · 2026
- https://www.blik.com/blisko-3-mld-transakcji-blikiem-w-2025-r-i-ponad-2-mln-nowych-uzytkownikow · 01/2026; https://bank.pl/blik-ma-juz-207-mln-aktywnych-uzytkownikow/ · 01/2026

**Rakousko**
- https://orf.at/stories/3428571/ · 2026 (EPU 376 112, 12/2025); https://www.wko.at/oe/epu/epu-factsheet.pdf · 2025; https://www.wko.at/epu/zahlen-daten-fakten · 2025–26
- https://www.bmwet.gv.at/dam/jcr:a69785e9-6b33-4b65-ba70-c34c37c58dc3/KMU-FOKUS_2025_barrierefrei%2016032026.pdf · 16. 3. 2026 (neotevřeno)
- https://marie.wko.at/digitalisierung/wie-oesterreich-die-kmu-digitalisierung-vorantreiben-kann.html · 2025–26; https://www.wko.at/oe/oe-news/wkoe-erfolge-2025/investitionsanreize-innovation--digitalisierung · 2025
- https://www.capitalo.at/anbieter/erste-bank/produkte/s-geschaeftskonto · 2026; https://www.bankkonditionen.at/girokonto/firmenkonto/ · 08/2026
- https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/konto-karten/business-konto/pauschalkonto-epu · 2026; https://www.sparkasse.at/erstebank/gruender/konto-und-karten/s-gruender-konto · 2026
- https://www.sparkasse.at/erstebank/unternehmen/produkte-firmenkunden/digitales-banking/george-business/funktionen · 2026; https://apps.apple.com/at/app/george-business-%C3%B6sterreich/id6443934239 · 2026
- https://brutkasten.com/artikel/george-business-kickinger · datum neznámé [CLAIM]
- https://m.bvb.ro/infocont/infocont26/EBS_RA_2025_de.pdf · Erste Group Geschäftsbericht 2025 (publ. 2026)
- https://www.sparkassenverband.at/de/ueber-uns/zahlen-fakten · 12/2025; https://www.sparkasse.at/erstebank/wir-ueber-uns · 2026
- https://www.bmd.com/at/software/buchhaltungssoftware · 2026
- https://wise.com/at/blog/raiffeisenbank-geschaeftskonto-oesterreich · datum neznámé; https://www.raiffeisen.at/noew/region-st-poelten/... Konditionen 2026 (PDF) · 2026; https://www.raiba.at/others/Schalteraushang/37482/Giroentgelte/Preise%20u%20Sendezeiten%20ELBA.pdf · datum neznámé
- https://www.capitalo.at/geschaeftskonto · 09/2026; https://kontovergleich.at/bank/bawag/business/ · 2026; https://www.gratis-konto.at/vergleich/firmenkonto/ · 09/2026
- https://www.capitalo.at/anbieter/n26/produkte/business-smart · 04/2026
- https://www.wko.at/netzwerke/einigung-bei-digitalisierung-des-umsatzsteuerrechts · 2025–26; https://www.selbststaendig-machen.at/e-rechnungspflicht-b2b-oesterreich/ · 2026; https://www.ey.com/de_at/insights/tax/e-rechnungspflicht · 2026

**Slovensko**
- https://finstat.sk/nase-clanky/analyzy/Analyza-vzniku-a-zaniku-firiem-v-roku-2025 · 01/2026; https://www.teraz.sk/ekonomika/finstat-v-2025-zaniklo-najviac-spolocn/933430-clanok.html · 01/2026; https://openiazoch.zoznam.sk/financie/rekordny-zanik-firiem-a-zivnosti-v-roku-2025-finstat-zverejnil-alarmujuce-statistiky/ · 01/2026
- https://www.finstat.sk/premium · 2026 (655 902 firem; 1 515 517 živnostníků – kumulativně)
- https://www.transparex.sk/blog/2142 · 2025 (377 324 aktivních živností 2024)
- https://www.techbyte.sk/2026/02/zanik-zivnosti-slovensko-2025/ · 02/2026 (SP 204 tis.); https://www.techbyte.sk/2026/08/o-tomto-stat-nehovori-do-augusta-skoncilo-takmer-50-tisic-zivnosti/ · 08/2026
- https://www.slsp.sk/sk/biznis/zaciname-podnikat · 2026; https://www.slsp.sk/sk/biznis/ucty/business-ucet-pre-firmy · 2026; https://www.podnikajte.sk/financny-manazment/podnikatelsky-ucet-pre-zivnostnikov-2025 · 2025; https://www.techbyte.sk/2025/02/velka-banka-laka-na-mimoriadnu-akciu-podnikatelsky-ucet-zadarmo/ · 02/2025
- https://www.slsp.sk/sk/aktuality/2026/9/9/prichadza-george-ai · 9. 9. 2026; https://kryptomagazin.sk/slovenska-sporitelna-meni-georgea-zmena-caka-133-miliona-klientov/ · 09/2026; https://www.slsp.sk/sk/aktuality/2026/2/26/slovenska-sporitelna-uzavrela-rok-2025-s-vyraznym-rastom-zisku-a-uverov · 26. 2. 2026
- https://www.slsp.sk/sk/aktuality/2026/5/19/slovenska-sporitelna-prinasa-spotrebny-uver-s-online-schvalenim-a-urokom-od-499 · 19. 5. 2026
- https://pomoc.superfaktura.sk/ako-naimportovat-vypis-z-banky-slovenska-sporitelna-george/ · datum neznámé; https://www.superfaktura.sk/integracia/ · 2026; https://www.modulario.com/blog/integracie-uctovnych-softverov/ · 2026
- https://www.tatrabanka.sk/sk/business/slobodu-napadom/ · 2026; https://www.tatrabanka.sk/sk/business/slobodu-napadom/podnikai/ · 2026; https://wise.com/sk/blog/tatrabanka-podnikatelsky-ucet · datum neznámé; https://finfin.sk/podnikatelsky-ucet-porovnanie/ · 2026
- https://www.vub.sk/document/documents/VUB/cennik/pre-podnikatelov-a-pravnicke-osoby/Cennik_PO_20260101-FINAL.pdf · platný od 1. 1. 2026
- https://wise.com/sk/blog/podnikatelsky-ucet-porovnanie · datum neznámé (365.bank)
- https://www.finsider.sk/spravy/revolut-vlani-zvysil-zisk-na-dve-miliardy-eur-na-slovensku-ma-vyse-550-000-klientov/ · 2026; https://digitalportal.sk/revolut-uzavrel-rok-2025-s-rekordnym-ziskom/ · 2026; https://www.revolut.com/sk-SK/business/business-account-plans/ · 2026
- https://www.tatrabanka.sk/sk/business/navigacia-podnikatela/zaciatok-podnikania/blog/e-faktura/ · 2026; https://forum-media.sk/povinna-elektronicka-fakturacia-2027-slovensko/ · 2026; https://kpmg.com/sk/sk/sluzby/danove-poradenstvo/elektronicka-fakturacia.html · 2026
- https://www.sbaonline.sk/novinka/rychle-platby-bez-cakania-po-novom-aj-s-overenim-prijemcu/ · 10/2025; https://www.teraz.sk/najnovsie/sba-okamzite-platby-medzi-bankami-bud/782365-clanok.html · 2025; https://www.podnikajte.sk/technologie/okamzite-platby-povinne-od-2025 · 2024–25

---

## (f) Log značek

**[EST]**
- Všechny CZK přepočty: hodnota × 24,465 (EUR) resp. × 5,592 (PLN), kurz ČNB 1. 10. 2026. Např. 18 € × 24,465 = 440,4 Kč; 25 PLN × 5,592 = 139,8 Kč; 441,5 mld. PLN × 5,592 = 2 469 mld. Kč; segmentová hranice 50 mil. Kč / 24,465 = 2,04 mil. EUR; / 5,592 = 8,94 mil. PLN.
- Vznik PO SK „+~17 % y/y": 24 000 / 20 576 − 1 = 16,6 % (spodní odhad, FinStat uvádí „> 24 000").
- Kvalitativní odhad dopadu definic (B1): bez výpočtu.

**[DATA GAP]** (kde hledat)
- PL počet small business klientů mBank/PKO/Santander/ING/Pekao → výroční zprávy 2025 (segment Bankowość Detaliczna – firmy / MŚP), MGBI „Klienci biznesowi banków. Raport 2025".
- PL mKsięgowość počet uživatelů → mBank Sprawozdanie Zarządu 2025; tiskové zprávy mBank.
- PL Finom / Qonto ceník a klienti → finom.co/pl, qonto.com/pl, KNF registr.
- PL integrace bank × wFirma/iFirma/Fakturownia → weby těchto SaaS, sekce „banki".
- PL Profil Zaufany / mObywatel statistiky → gov.pl/web/mobywatel.
- PL PKO Konto Firmowe aktuální sazba → pkobp.pl taryfa od 1. 12. 2025.
- AT počet KMU celkem → KMU im Fokus 2025 (BMWET 16. 3. 2026), WKO Statistik.
- AT Erste Bank Oesterreich počet KMU/EPU klientů, George Business uživatelé AT → Erste Group AR 2025 (segment Austria/EBOe), Sparkassenverband.
- AT ID Austria počet uživatelů → oesterreich.gv.at, BMF.
- AT penetrace business účtů; Finom AT ceník → OeNB; finom.co/de-at.
- AT Erste online business úvěr (s Betriebsmittelkredit) → sparkasse.at/erstebank/unternehmen/finanzierung.
- SK počet podnikatelských klientů SLSP, George Business SK → SLSP Výročná správa 2025, Erste Group AR 2025.
- SK aktivní živnosti stock 2025 → ŠÚ SR (Register organizácií), MV SR živnostenský register.
- SK Tatra Pay, BankID SK → tatrabanka.sk, sbaonline.sk.
- SK KROS × banka integrace, eKasa × banka → kros.sk, financnasprava.sk.
- Penetrace business účtů PL/AT/SK → NBP/ZBP, OeNB, NBS.

**[STALE]**
- PKO „blisko 40 % MŚP" – 2017.
- Santander Konto Firmowe Godne Polecenia ceny – nejnovější datovaný zdroj 04/2026 (promo).
- ING Konto Direct dla Firmy ceny – nejnovější datovaný zdroj 03/2026 (promo), stránka rankingkont „2026" bez měsíce.
- Pekao Konto Przekorzystne Biznes ceny – do 06/2026 (promo), hraniční.
- VÚB Biznis účet – cenník platný od 1. 1. 2026 (před cut-off).
- Raiffeisen „Konditionen 2026" – rok bez měsíce; N26 Business Smart 4,90 € – 04/2026 (09/2026 srovnání tarif potvrzuje).
- Tatra banka, 365.bank, Revolut (PL/SK ceníky) – datum zdroje neznámé → nelze vydávat za stav 10/2026.
- Erste „> 75 000 firemních klientů George Business AT/RO/CZ" – datum výroku neznámé.

**[CLAIM]**
- Revolut „20 tis. firem měsíčně", „množstvo výhod pre slovenských podnikateľov".
- Erste George Business „vyvinuto společně s firemními klienty" (brutkasten).
- SLSP George AI „největší inovace od vzniku Georgea".
- Tatra banka PodnikAI – bez metrik.
- Plně digitální onboarding Revolut/N26 – z marketingových stránek.

**[FACT – k internímu ověření]**
- Erste Group AR 2025: „11,4 mil. uživatelů George, z toho 2,6 mil. na George Business" – úryvek bez kontextu; číslo se jeví vysoké vůči 75 tis. firemním klientům, možná jde o jinou definici (např. uživatelé George napříč skupinou s business profilem). Ověřit v Erste Group AR 2025, kapitola Digital.

---

## Shrnutí (10 řádků)
1. PL: 3,84 mil. aktivních JDG (09/2026), 2,31 mil. mikrofirem (PARP 2025); nové JDG 1H 2026 −6,5 %.
2. AT: 376 112 EPU (+3,9 %, 12/2025) = 62,1 % firem; KMU digitální intenzita 73 %.
3. SK: rekordní zánik 66 tis. živností 2025, saldo −20 tis., SZČO v SP 204 tis. (−40 tis.); vznik PO > 24 tis. (+~17 %).
4. Erste AT: s Geschäftskonto od 10,41 €, EPU Smart 13,61 €, George 7,43 € / George Business One 18 €/měs. (06–08/2026); 4,3 mil. klientů, 732 poboček.
5. SLSP: živnostník 0 € navždy, online založení bez výpisu ze ŽR, PO 1 rok zdarma; George 1,33 mil. uživatelů, George AI od 9/2026.
6. PL banky: 0 PLN podmíněné platbou ZUS (ING 19, Santander 25, Pekao 15 PLN), bonusy 2 400–4 200 PLN – vše [STALE 03–06/2026].
7. Enablery: KSeF 1. 2./1. 4. 2026 + 1. 1. 2027; SK e-faktura 1. 1. 2027 (zákon 385/2025); SEPA Inst SK plně od 10/2025; AT bez národní B2B e-fakturace; BLIK 2,9 mld. transakcí 2025.
8. Fintech: Revolut Business SK +33 % klientů / +56 % objemů (2025), globálně 767 tis. firem; PL ceník od 50 PLN.
9. Použito 35/35 dotazů WebSearch (PL 13, AT 11, SK 10 + 1 kurz ČNB); WebFetch nepoužit.
10. Největší mezery: počet small business klientů u všech bank (mBank, PKO, Erste AT, SLSP), mKsięgowość adopce, Finom/Qonto PL+AT, ID Austria/BankID SK/Profil Zaufany statistiky, penetrace business účtů; řada SK/PL ceníků bez data → nelze potvrdit stav po 06/2026.
