# Společný brief pro research agenty (čti celý)
Kontext: Diagnostika segmentu small business v ČR (FOP = OSVČ/živnostníci + PO = s.r.o., a.s., družstva, spolky-podnikatelé; roční obrat do 25 mil. Kč), období 2021–2026 (2026 = YTD), perspektiva konkurenční benchmark Česká spořitelna vs. trh. Publikum: CEO-level, styl McKinsey. Jazyk výstupu: čeština (EN termíny OK).

PRAVIDLA (porušení = kritická chyba):
1. Každé číslo = zdroj + rok/datum + metodika inline: `1 174 tis. OSVČ (ČSSZ, 12/2025, evidované OSVČ vč. vedlejší činnosti)`. Uváděj URL zdroje v poznámce nebo v seznamu zdrojů na konci souboru s datem přístupu 2026-09-08.
2. Nikdy nevymýšlej čísla. Když nenajdeš, napiš `[DATA GAP]` + kde by se dalo dohledat. Radši méně čísel, všechna ověřená.
3. Označ jistotu: `[FACT]` (ověřeno ve zdroji), `[EST]` (tvůj odhad – uveď postup), `[EXTRAP]` (extrapolace), `[CLAIM]` (marketingový výrok banky, nepřebírat jako fakt).
4. Nemíchej definice: registrovaní vs. aktivní FOP; hlavní vs. vedlejší OSVČ; obratové vs. zaměstnanecké vymezení; hrubé vs. čisté úvěry; ČNB „živnostníci" (sektor domácností) vs. „malé podniky" (nefinanční podniky). Vždy uveď, jak se definice zdroje liší od naší (obrat do 25 mil. Kč).
5. Časové řady: 2021–2025 roční + 2026 poslední bod; kde jde, 2019/2020 jako covid baseline. Tabulky v Markdownu.
6. Klíčové metriky trianguluj ze 2 nezávislých zdrojů; rozdíly vysvětli.
7. Preferuj primární zdroje (ČSÚ, ČNB ARAD, ČSSZ, MPO, MSp, weby bank, výroční zprávy, investor prezentace) > odborné organizace (ČBA, AMSP, CRIF, Creditreform, Coface, Intrum) > poradenské studie > média (jen kvalitativně / výroky managementu).
8. Používej WebSearch (česky i anglicky) a WebFetch na konkrétní stránky (ceníky bank, PDF výroční zprávy, ČSSZ otevřená data, ČNB ARAD). Proveď mnoho vyhledávání (min. 25–40 dotazů), dokud nemáš pokryté všechny body zadání. Zkoušej i alternativní formulace a různé roky (2021, 2022, 2023, 2024, 2025, 2026).
9. Struktura souboru: (a) hypotézy, (b) datové tabulky s poznámkami, (c) analýza / zjištění (action titles = závěr, ne popis), (d) „So what pro ČS" (3–5 odrážek), (e) seznam zdrojů s URL a datem přístupu, (f) log odhadů/mezer.
10. Piš rovnou do zadaného souboru (Bash heredoc / Write). Průběžně ukládej (soubor přepiš rozšířenou verzí). Cílová délka: 2 500–5 000 slov na soubor. Na konci vrať krátké shrnutí (10 řádků) hlavních čísel a kde jsou největší mezery.
