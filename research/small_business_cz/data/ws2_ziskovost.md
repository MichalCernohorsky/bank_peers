# WS2 – Data: Ziskovost, obrat a přidaná hodnota dle velikosti a NACE

Přístup 2026-09-08. Toto je nejslabší datová oblast WS2 – primární zdroje (ČSÚ SBS, MPO Zpráva o MSP, D&B/CRIF sektorové analýzy, ČSSZ ročenka) byly v session blokované proxy; níže jen ověřené útržky a přesný návod k doplnění.

## T19. Ověřené strukturální údaje

| Ukazatel | Hodnota | Rok | Zdroj / jistota |
|---|---|---|---|
| Služby (NACE H–N bez K, S95/96 – dle ČSÚ RSS): zaměstnanci / tržby / účetní přidaná hodnota | 1 120 448 / 3 818 018 mil. Kč / 1 433 672 mil. Kč | 2023 | ČSÚ roční strukturální statistiky služeb `[FACT*]` (https://csu.gov.cz/rocni-strukturalni-statistiky-sluzeb) |
| → Přidaná hodnota / tržby ve službách (všechny velikosti) | 37,6 % | 2023 | vlastní výpočet `[EST]` |
| → Tržby na zaměstnance ve službách | ~3,41 mil. Kč | 2023 | vlastní výpočet `[EST]` |
| Průmysl: tržby celkem | −8 % y/y | 2023 | ČSÚ `[FACT*]` (https://csu.gov.cz/rocni-strukturalni-statistiky-prumyslu) |
| Počet PO celkem / nově vzniklé | 576 642 / 30 716 | 2024 | D&B `[FACT*]` |
| CRIF index stability (12 odvětví, ~350 tis. firem) | hodnoty dle odvětví [DATA GAP] | Q4 2024 | ICC ČR/CRIF (https://www.icc-cr.cz/cs/novinky/tiskova-zprava-stabilita-ceskych-firem-ve-4-ctvrtleti-2024) |

## T20. Regulační proxy nákladovosti OSVČ (výdajové paušály – zákon č. 586/1992 Sb., § 7 odst. 7) `[FACT-KB]`

| Typ činnosti | Paušální výdaj (% příjmů) | Implikovaná „daňová marže“ | Reálná marže |
|---|---|---|---|
| Řemeslné živnosti, zemědělství | 80 % (strop 1,6 mil. Kč) | 20 % | [DATA GAP] |
| Ostatní živnosti (obchod, gastro, služby) | 60 % (strop 1,2 mil. Kč) | 40 % | [DATA GAP] |
| Svobodná povolání, autorská práva, jiné podnikání (IT, poradenství, lékaři, právníci) | 40 % (strop 0,8 mil. Kč) | 60 % | [DATA GAP] |
| Nájem | 30 % (strop 0,6 mil. Kč) | 70 % | – |

Poznámka: paušály nejsou měřením reálných marží, ale jsou důležité pro banku – u OSVČ s paušálními výdaji (většina FOP se službami) je vykázaný zisk regulatorní konstrukt, nikoli cash-flow; banky proto pro úvěrování FOP používají obrat z bankovního účtu (transakční underwriting), ne daňové přiznání.

## T21. Co doplnit (přesné zdroje)

| Potřeba (dle zadání a) | Zdroj | URL | Stav |
|---|---|---|---|
| Tržby, přidaná hodnota, náklady, zisk dle velikostní třídy (0, 1–9, 10–49) a NACE, 2021–2023 | ČSÚ – Ekonomické výsledky podniků / SBS (tab. „Ukazatele podle velikostních skupin“) | https://csu.gov.cz/prurezove-podnikove-statistiky ; Eurostat sbs_sc_ovw (https://ec.europa.eu/eurostat/databrowser/view/sbs_sc_ovw/) | proxy blok |
| Podíl MSP/mikro na přidané hodnotě a zaměstnanosti 2023–2024 | MPO Zpráva o vývoji MSP a jeho podpoře 2023 / VZ Strategie MSP 2024 | https://mpo.gov.cz/assets/dokumenty/50883/57768/614113/priloha001.pdf ; https://mpo.gov.cz/assets/cz/podnikani/male-a-stredni-podnikani/studie-a-strategicke-dokumenty/2026/1/VZ-Strategie-MSP-za-rok-2024.pdf | proxy blok |
| EU SME Performance Review – Czechia fact sheet (mikro: počet, zaměstnanost, přidaná hodnota, produktivita) | EK DG GROW | https://single-market-economy.ec.europa.eu/smes/sme-strategy/sme-performance-review_en | neotevřeno (limit vyhledávání) |
| Průměrný vyměřovací základ OSVČ (hlavní/vedlejší), podíl OSVČ na minimu | ČSSZ Statistická ročenka z oblasti důchodového pojištění 2023–2025, kap. OSVČ | https://www.cssz.gov.cz/documents/20143/99587/Statistick%C3%A1+ro%C4%8Denka+z+oblasti+d%C5%AFchodov%C3%A9ho+poji%C5%A1t%C4%9Bn%C3%AD+2025.pdf | proxy blok |
| Rozdělení základu daně OSVČ (DPFO § 7), podíl paušálních výdajů | Finanční správa – Informace o činnosti FS / analýzy daňových přiznání | https://financnisprava.gov.cz/cs/financni-sprava/financni-sprava-cr/vyrocni-zpravy-a-informace-o-cinnosti | proxy blok |
| Marže dle odvětví (EBITDA, ROS) pro mikro firmy | CRIF Cribis „Odvětvové analýzy“, D&B „Finanční zdraví“, Coface CEE Top 500 (jen velké) | https://www.crif.cz/ ; https://www.bisnode.cz/ | placené/proxy |
| Hrubá míra zisku nefinančních podniků (S.11) 2021–2025 | ČSÚ sektorové účty | https://csu.gov.cz/sektorove-ucty | proxy blok |
