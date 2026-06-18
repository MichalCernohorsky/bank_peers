# Design krok — sloučená SPA (BankPulse)

Cíl: **jeden web** s kompletním pohledem — deep-dive nad ČS i peer srovnání nad
bankami. Vizuál se ladí v Claude Designu (claude.ai / Artifacts), data + API +
logika zůstávají v Claude Code.

## Co vzít do Designu
`web/design/app.preview.html` — **self-contained celá SPA**: renderuje se čistě
z vloženého snapshotu (žádné volání API, žádné 404). Vlož ho do Artifactu, naběhne
na první dobrou a uvidíš celý produkt (nav + oba režimy + selector banky).

> Produkční soubor je `web/app.html` (čte z živého API). Preview je jen scratchpad
> pro vzhled — v něm je fetch schválně neutralizovaný.

## Dvě klíčová rozhodnutí pro vizuál
1. **Vizuální jednota.** Dnes mají režimy odlišný styl (Přehled = IBM Plex
   „dashboard", Srovnání = HBR „editorial"). Pro jeden kohezní web sjednoť design
   systém (typografie, barvy, komponenty), nebo ty dva režimy nech vědomě odlišené.
2. **IA / navigace.** Jeden shell, dva režimy: **Přehled banky** (deep-dive) a
   **Srovnání** (peers). Selector banky se týká jen Přehledu.

## Datové pravidlo (NEMÍCHAT v jednom grafu)
- **Přehled** = `basis=reported` (deep-dive, plná historie) — má jen ČS.
- **Srovnání** = `basis=adjusted` (peer-comparable) — všechny banky, Q1 2025/2026.
- Reported a adjusted se **nikdy** nedávají do jednoho grafu. „Overview nad peers"
  = režim Srovnání; per-bank Přehled zůstává jednobankový.
- Banka bez reported dat (KB) má v Přehledu **empty-state** s odkazem na Srovnání.

## Mantinely, aby šel vizuál čistě vrátit
Měň **jen prezentaci**, ne kontrakt s JS:
- ✅ `<style>` blok, markup, typografie, rozestupy, barvy, styl SVG grafů
- ⛔️ **neměň** (nebo drž synchronně s JS): `id` elementů, do kterých JS zapisuje
  (`ov-bankname`, `ov-kpis`, `ov-qseg`, `ov-qchart`, `ov-achart`, `ov-cats`,
  `ov-empty`, `cmp-kicker`, `cmp-deck`, `cmp-legend`, `cmp-exhibits`, `bankbtns`),
  signatury render funkcí, tvar dat a fetch/fallback logiku.
- Přejmenuješ-li v markupu `id`/třídu, uprav i JS, který na ni cílí — jinak se po
  návratu nenaplní data.

## Round-trip
1. Vylaď vzhled nad `app.preview.html` v Designu.
2. Pošli sem upravené HTML/CSS (nebo popiš změny).
3. Zaintegruju do `web/app.html` (a regeneruju preview) a ověřím přes jsdom, že to
   dál jede na živá data z API.

## Regenerace preview
Preview se generuje z produkční `web/app.html` (neutralizací fetche). Po každé
úpravě `app.html` se dá preview přegenerovat stejným postupem.
