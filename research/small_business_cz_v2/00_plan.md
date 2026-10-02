# 00 – Research plan v2: Small business (FOP + PO do 50 mil. Kč) v ČR 2021–2026 + evropská gap analýza + plán pro ČS
Zahájeno 2026-10-02 · Engagement Manager view · navazuje na v1 (`../small_business_cz/`, hranice 25 mil. Kč, září 2026)

## 0. Co se změnilo proti v1 a co to znamená
| Změna | Důsledek pro práci |
|---|---|
| Hranice segmentu 25 → **50 mil. Kč** | Lépe sedí na bankovní segmentaci (KB < 60 mil., RB/UCB < 50 mil.) a na EU „mikropodnik" (≤ 2 mil. EUR ≈ 50 mil. Kč); překryv bankovních řad s naší definicí stoupne ze „střední" na „vysoký". Čísla v1 o FOP se nemění; u PO se rozšíří jmenovatel (více s.r.o. v segmentu) – nutno přepočítat sizing. |
| **Cut-off 06/2026+** pro nabídku bank | Každá položka nabídky musí mít datum zdroje; v1 data z Finmag 2026 / ceníků bez data je nutné znovu datovat nebo označit `[STALE]`. |
| **Pouze ověřená data** (žádná paměť modelu) | Eliminuje značku `[FACT-KB]` z v1 (8 položek – repo sazby 2019–25, zálohy OSVČ 2021–23, EET, DAC7) → buď dohledat, nebo `[DATA GAP]`. |
| Nové WS5 (Evropa) a WS7 (plán) | Nový research: 4–5 trhů, 10–15 praktik, 5 best practices s důkazem; akční plán ve 3 horizontech s KPI. |

## 1. Prostředí a limity – ověřeno 2026-10-02 (čti před schválením)
- **WebSearch funguje** (limit 200 dotazů na session; v1 jej vyčerpalo 7 agentů za ~40 minut).
- **WebFetch je blokován egress proxy na všech testovaných doménách** (csas.cz, kb.cz, finmag.cz, penize.cz, podnikatel.cz, cnb.cz, cbamonitor.cz, erstegroup.com, ecb.europa.eu, wise.com, en.wikipedia.org). Plný text žádné externí stránky nelze otevřít.
- Důsledek pro pravidlo „pouze ověřená data": ověření je možné **jen v indexovaném výtahu vyhledávače** (titulek + URL + úryvek s číslem). Navrhuji konvenci: `[FACT]` = číslo přečtené v úryvku citovaného zdroje s URL a datem; v příloze D vždy poznámka „ověřeno z výtahu, plný text nedostupný". Čísla, která úryvek neobsahuje, jsou `[DATA GAP]`. Lokální IR fact sheety (KB, ČSOB, Moneta, ČS v repozitáři) zůstávají jediným plnotextovým primárním zdrojem.
- Datování zdrojů: u výtahů je datum často jen v URL/titulku; kde chybí, zkusím dohledat druhý dotaz na datum; jinak `[STALE: datum neznámé]`.
- **Doporučení:** pokud lze v nastavení prostředí povolit domény (minimálně csas.cz, kb.cz, csob.cz, rb.cz, moneta.cz, unicreditbank.cz, airbank.cz, fio.cz, creditas.cz, cnb.cz, csu.gov.cz, cssz.gov.cz, mpo.gov.cz, erstegroup.com, finmag.cz, penize.cz, mesec.cz, web.archive.org, tide.co, starlingbank.com, qonto.com, bunq.com), kvalita ověření se skokově zvýší. Bez toho bude dokument mít řádově 60–100 `[DATA GAP]` jako v1.
- Rozpočet 200 dotazů rozdělím: WS1 20 · WS2 20 · WS3 60 (9 bank × ~5 + ceny/podíly) · WS4 15 · WS5 70 (5 trhů × ~12 + praktiky) · rezerva 15. Agenty poběží ve **dvou vlnách** (ne 7 paralelně – v1 skončilo rate-limitem).

## 2. Hypotézy per workstream
### WS1 – Velikost a struktura (hranice 50 mil. Kč)
- H1.1 Při hranici 50 mil. Kč je v segmentu ≥ 95 % všech aktivních PO (s.r.o. s obratem > 50 mil. Kč jsou řádově desítky tisíc); adresovatelný trh ≈ 692 tis. hlavních OSVČ + ~500 tis. aktivních PO.
- H1.2 Růst OSVČ pokračuje (1,2 mil. 6/2026), hlavní činnost zpomaluje, vedlejší zrychluje; konsolidační balíček 2024–26 přesunul část FOP do vedlejší činnosti nebo s.r.o.
- H1.3 Cizinci tvoří 10–30 % nových FOP; Praha + Střední Čechy třetinu stocku.
### WS2 – Kondice
- H2.1 Bankroty FOP rostly 2024–25, 1H 2026 stagnace; PO bankroty nejvyšší od 2017 – riziko koncentrované v mladých FOP.
- H2.2 Platební morálka ~60 % faktur včas; splatnost 36 + 21 dní; factoring +18 %.
- H2.3 Externí financování používá ~25 % mikrofirem; bariéra = postoj majitelů.
### WS3 – Bankovní trh ČR (zdroje 06/2026+)
- H3.1 ČS má jediný placený základní účet v pětce (149 Kč) a jako jediná zdražila 3/2026; ověřit, zda ceník s účinností 1. 7. 2026 něco změnil.
- H3.2 Konkurence soutěží úročením zůstatku (Air Bank 2,6 %, UCB 2,5 %, Creditas 1,4 %) a rychlostí nezajištěného úvěru (Moneta 600 tis. online do 15 min).
- H3.3 Jen KB a Moneta reportují small business; v pololetních zprávách 1H 2026 ověřit nové hodnoty (KB SB úvěry, Moneta nové SB úvěry, ČSOB SME).
- H3.4 Air Bank přesáhla 65 tis. podnikatelských klientů a rozšířila s.r.o.; Partners Banka spustila/nespustila podnikatele 2026.
### WS4 – Trendy
- H4.1 IPR (EUR instant 1/2027, 7/2027), AMLR 7/2027, PSR ≈ 2028 – regulační vlna zvýhodňuje škálu.
- H4.2 Embedded finance (Shoptet, Fakturoid, Lemonero/KB, Roger) je hlavní distribuční disruptor; Revolut cílí na hlavní účet.
- H4.3 Daňový režim OSVČ 2026+ (min. VZ 40 %, snížení soc. zálohy 7/2026) mění ekonomiku mikro-FOP.
### WS5 – Evropská gap analýza
- H5.1 Předběžný výběr trhů (finální skóring v WS5): **UK** (Tide, Starling, Monzo Business – digital-first lídři s publikovanými čísly), **NL** (bunq, ING, Knab – open banking + e-fakturace), **PL** (mBank, PKO BP, Pekao – CEE, nejbližší struktura a Bank iD ekvivalent mojeID; Finom/Qonto vstup), **AT** (Erste George Business, Raiffeisen – interní transfer know-how), **SK** (SLSP George Business, Tatra banka – Erste, SEPA/euro, srovnatelný segment). DE/FR jako záložní (Qonto, Penta/Finom, Holvi).
- H5.2 Nejpřenositelnější praktiky: (1) plně digitální onboarding s.r.o. v minutách (Tide, Starling, SLSP), (2) účet s integrovanou fakturací a účetnictvím (Tide, Qonto, bunq), (3) data-driven instant lending/overdraft z transakcí (Starling, Tide, iwoca partnerství), (4) tiering úročení + „0 Kč základ" (bunq, Finom), (5) marketplace/ekosystém nefinančních služeb (Tide: registrace firmy, daně; PKO BP: e-služby), (6) RM „pool" model + video bankéř (ING, Erste AT).
- H5.3 Mezera ČR vs. benchmark je největší v onboardingu PO, integracích a nefinančních službách; nejmenší v platbách (okamžité platby CZK) a Bank iD.
### WS6 – SWOT ČS (po WS1–5)
- Navazuje na v1 SWOT (S1–S7, W1–W8, O1–O9, T1–T8), doplní evropské srovnání a 50 mil. Kč sizing.
### WS7 – Plán
- Quick wins: cenový reset (0 Kč základ), zveřejnění sazby/rychlosti úvěru, reporting segmentu, Fakturoid API. Mid: předschválený úvěr z retailu, online s.r.o. onboarding, úročení tiering. Long: embedded finance platforma, RBF/faktoring partnerství, AI obsluha.

## 3. Konkrétní vyhledávání (pořadí)
1. **WS3 nejdřív** (nejcitlivější na datum): „ceník pro podnikatele účinnost 2026" pro 9 bank; „pololetní zpráva 1H 2026" ČS/KB/ČSOB/Moneta/RB/UCB/Fio/Creditas/Air Bank; „podnikatelský účet úrok 2026"; „podnikatelský úvěr online 2026"; app store „George Business" / „KB+" / „Smart Banka" hodnocení 2026; Partners Banka podnikatelé 2026; SME Banking Club Czech 2026; Zlatá koruna 2026 podnikatelský účet.
2. **WS1/WS2**: ČSSZ OSVČ 6/2026 a 9/2026; FS paušální daň 2026; CRIF 1H 2026 firmy/živnostníci; D&B 2026; bankroty 1H 2026 a 3Q 2026; ČSÚ RES 2025; MPO VZ Strategie MSP 2025; ČLFA 1H 2026; ČNB ZFS podzim 2026 / jaro 2026; repo sazba rozhodnutí 2026; ČBA Monitor úvěry živnostníkům 2026.
3. **WS4**: PSR publikace Úřední věstník 2026; AMLR transpozice ČR 2026; IPR ČNB 2027; ViDA ČR; Revolut Business ČR 2026; Shoptet 2026; Flowpay/Lemonero 2026; Bank iD firmy 2026.
4. **WS5**: pro každý trh: Tide annual report 2025/26 (members, revenue); Starling annual report 2025; Monzo Business customers 2026; bunq business 2026; ING Business NL; Knab; mBank firmy 2026; PKO BP małe firmy 2026; Finom/Qonto PL; George Business AT Erste 2026; Raiffeisen Mein ELBA Business; SLSP George Business SK 2026; Tatra banka Business; ECB SAFE 2026; Eurostat SBS mikro podniky; národní statistiky OSVČ (PL CEIDG, AT WKO EPU, SK živnostníci, NL KvK zzp, UK ONS self-employed).

## 4. Soubory a pořadí prací
`00_plan.md` → schválení → `01_definice.md` (50 mil.) → `02_ws1.md` → `03_ws2.md` → `04_ws3.md` (+ `data/ws3_*.md`, každý řádek s datem zdroje) → `05_ws4.md` → `06_ws5_gap.md` → `07_ws6_swot.md` → `08_ws7_plan.md` → `FINAL_small_business_CZ_deep_dive_v2.md` → QA (příloha E). Data z v1 přebírám jen s novým ověřením nebo s označením roku jako historie; nic z v1 označeného `[FACT-KB]` nepřebírám bez dohledání.

## 5. Rozhodnutí, která potřebuji před spuštěním (viz dotaz)
1. Konvence ověření při blokovaném WebFetch (výtah vyhledávače = `[FACT]` s poznámkou) – ano/ne; případně povolit domény v nastavení prostředí.
2. Předběžný výběr benchmark trhů UK, NL, PL, AT, SK – souhlas, nebo nahradit (DE/HU/RO/FR).
3. Převzít ověřená data z v1 jako baseline (s přeznačením a datací) – ano/ne.
