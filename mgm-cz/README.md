# mgm-cz — Member-Get-Member programy na českém bankovním trhu

Dva výstupy: **report** o MGM / „doporuč kamaráda" programech bank a fintechů působících v ČR,
a **tracker**, který nabídky průběžně sleduje, ukládá snapshoty a hlásí změny.

- Report: [`report/mgm-cz-report.md`](report/mgm-cz-report.md)
- Data: [`data/mgm-programs.json`](data/mgm-programs.json) · [`.csv`](data/mgm-programs.csv)
- Datový model: [`docs/data-model.md`](docs/data-model.md)

## Instalace

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

Python 3.11+. Žádná databáze, žádná služba — všechno jsou soubory v repozitáři.

## Spuštění

```bash
python3 tracker/run.py                 # stáhne zdroje, uloží snapshot, zapíše změny
python3 tracker/run.py --dry-run       # nic nezapíše, jen vypíše, co by se stalo
python3 tracker/run.py --only air-bank__pozvete-pratele   # jeden subjekt
python3 tracker/report.py              # přegeneruje report a CSV z JSON
python3 tracker/validate.py data/mgm-programs.json        # validace dat
python3 -m pytest tests/ -q            # testy (offline, bez sítě)
```

Běh je **idempotentní**: opakované spuštění nad nezměněným obsahem nehlásí žádnou změnu.
Chyba stažení jednoho zdroje nezastaví ostatní a nevrací nenulový exit kód — výpadek webu
nemá shodit týdenní běh v CI.

## Co tracker dělá a co záměrně nedělá

Tracker **nikdy nepřepisuje kurátorovaná data**. Když najde rozdíl, zapíše *návrh* do changelogu
s příznakem `needs_review` a v `data/mgm-programs.json` sáhne jedině na pole `last_checked`.
Heuristika nad HTML diffem by jinak tiše degradovala ověřená čísla na šum z redesignu stránky.
Aktualizace věcných polí je vždy rozhodnutí člověka.

`needs_review: false` dostane jen jednoznačná výměna jediné částky na několika řádcích a bez
varování. Všechno ostatní — změna textu podmínek, rozpadlý CSS selektor, více změněných čísel —
je označeno k ručnímu posouzení.

## Jak číst changelog

[`data/changelog.md`](data/changelog.md) je člověkem čitelný, nejnovější nahoře.
[`data/changelog.json`](data/changelog.json) nese totéž strojově včetně plných diffů.

Každý záznam má jeden ze tří příznaků:

| Příznak | Význam | Co s tím |
|---|---|---|
| 🆕 první snapshot | zdroj se sleduje poprvé, není s čím porovnat | nic, jen se založil baseline |
| ✅ jednoznačná změna | změnila se přesně jedna částka, jinak beze změny | ověřit u zdroje a promítnout do `mgm-programs.json` |
| ⚠️ needs_review | heuristika si není jistá | **přečíst diff** — může jít o změnu podmínek i jen o redesign stránky |

Pod každým záznamem je `Nové částky` / `Zmizelé částky` / `Nová data` a samotný unified diff.
Varování typu „selektor nic nenašel — fallback na plný text" znamená, že se změnila struktura
stránky; takový diff bude velký a skoro jistě nejde o změnu programu.

## Jak přidat nový subjekt

1. Přidej záznam do `data/mgm-programs.json` podle [`docs/data-model.md`](docs/data-model.md).
   Povinné je `record_id`, `subject`, `subject_type`, `status`, `source_date` a `confidence`.
   Subjekt nalezený až během researche označ `"in_original_scope": false` — v reportu se
   vypíše jako *doplněno*.
2. Ověř: `python3 tracker/validate.py data/mgm-programs.json`
3. Přidej zdroje do `config/sources.yaml` pod **stejné** `record_id`:

```yaml
  - record_id: nova-banka__program
    subject: Nová banka
    sources:
      - url: https://example.cz/pravidla.pdf
        type: pdf                 # html | pdf
        anchors: ["doporuč"]      # kontrola, že jsme na správné stránce
        note: "Primární T&C."
      - url: https://example.cz/doporucte-nas
        type: html
        selector: "main"          # volitelný CSS selektor
        anchors: ["doporuč", "Kč"]
```

4. Přegeneruj report: `python3 tracker/report.py`

Sledují se **jen oficiální zdroje subjektu**. Zpravodajské a srovnávací weby se nesledují —
mění se denně z důvodů nesouvisejících s programem a vyrobily by jen šum.

### Na co si dát pozor u URL

Část bank verzuje pravidla přímo v názvu souboru (`...pravidla-unor2026.pdf`) nebo v něm má
hash (`...doporuc-a-ziskej-5e249b95.pdf`). Při vydání nové verze vznikne **nová URL** a ta
stará začne vracet 404 nebo zamrzne na staré verzi. Tracker to pozná podle chyby stažení nebo
chybějící kotvy, ale novou adresu musí do konfigurace doplnit člověk. Stabilnější kotvou bývá
FAQ nebo rozcestník dokumentů — proto jsou u mBank a Monety nakonfigurované obě.

## Struktura

```
config/sources.yaml     sledované URL, typ extrakce, selektory, kotvy
data/
  mgm-programs.json     aktuální stav (zdroj pravdy pro report)
  mgm-programs.csv      plochý export, generovaný
  changelog.{md,json}   zachycené změny
  history/YYYY-MM-DD/   plný snapshot dat, odkládaný jen při změně
report/
  mgm-cz-report.md      generovaný report
  sections/             autorské analytické sekce (ty se edituji ručně)
schema/                 JSON Schema záznamu
snapshots/YYYY-MM-DD/   surové HTML/PDF + extrahovaný text
tracker/
  run.py                stažení, snapshot, diff, changelog
  report.py             generování reportu a CSV
  validate.py           validace dat proti schématu
  extractors/           html_extractor.py, pdf_extractor.py
tests/                  offline testy nad fixtures
```

> Soubory v `tracker/extractors/` se jmenují `html_extractor.py` a `pdf_extractor.py` záměrně.
> Modul pojmenovaný `html.py` by stínil stdlib modul `html`, na kterém závisí beautifulsoup4,
> a bs4 by spadlo na nesrozumitelný `ImportError`.

## Automatizace

V [`automation/github-workflow-tracker.yml`](automation/github-workflow-tracker.yml) je
připravený týdenní běh. **Není aktivní a sám se neaktivuje.**

GitHub načítá workflows výhradně z `.github/workflows/` v **kořeni repozitáře**; tenhle
soubor leží v `mgm-cz/automation/`, takže pro GitHub neexistuje. Zapnutí má dva vědomé kroky:

```bash
# 1) zkopírovat do kořene repozitáře
cp mgm-cz/automation/github-workflow-tracker.yml .github/workflows/mgm-tracker.yml
# 2) v novém souboru odkomentovat blok `schedule`
```

Po kroku 1 a před krokem 2 jde workflow spustit jen ručně přes *Actions → Run workflow*.

Alternativa přes cron:

```cron
# každé pondělí v 6:00
0 6 * * 1 cd /cesta/k/mgm-cz && .venv/bin/python tracker/run.py >> tracker.log 2>&1
```

## Známá omezení

- **Report nemá žádný záznam s `confidence: high`.** Data vznikla z webového vyhledávání;
  na oficiální T&C se v prostředí, kde report vznikl, nedalo dosáhnout. Adresy T&C jsou
  v `sources[]` a v `config/sources.yaml`, takže první ostrý běh trackeru je stáhne.
- **Historie není postavená na Wayback Machine** — `web.archive.org` byl nedostupný.
  Sekce 4 reportu obsahuje jen změny doložené konkrétním datem.
- **Stránky renderované JavaScriptem** se zatím neřeší. Pokud se u některého zdroje ukáže,
  že `requests` vrátí prázdnou kostru, je potřeba pro něj doplnit Playwright; proto je
  `type` v konfiguraci rozšiřitelný.
- **Množinový diff částek nemá pozici.** Když stránka nese dvakrát stejnou částku
  (odměna pro doporučujícího i doporučeného) a změní se jen jedna, nejde strojově určit
  která — taková změna proto vždy dostane `needs_review: true`.
