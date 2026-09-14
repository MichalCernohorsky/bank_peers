# Datový model — MGM programy ČR

Jeden záznam = jeden program / varianta programu.
Strojová definice: [`schema/mgm-program.schema.json`](../schema/mgm-program.schema.json).
Validace: `python3 tracker/validate.py data/mgm-programs.json`.

## Pole ze zadání (závazný kontrakt)

| Pole | Typ | Poznámka |
|---|---|---|
| `subject` | string | Název instituce |
| `subject_type` | `bank` / `neobank` | `bank` = česká licence nebo pobočka zahraniční banky |
| `program_name` | string \| null | `null`, když program neexistuje nebo nemá vlastní název |
| `status` | `active`/`paused`/`ended`/`unknown`/**`none`** | viz rozhodnutí D4 |
| `product_scope` | string[] | běžný účet, spořicí, hypotéka, karta, investice… |
| `reward_referrer` | string \| null | čitelný text včetně formy |
| `reward_referee` | string \| null | čitelný text včetně formy |
| `reward_type` | `cash`/`voucher`/`points`/`fee_waiver`/`other` \| null | `null` když program neexistuje |
| `conditions` | string \| null | kvalifikační podmínky |
| `channel` | enum[] | `code`/`link`/`app`/`branch`/`web`/`other` |
| `limits` | string \| null | max. počet doporučení, max. odměna |
| `timing` | string \| null | lhůta splnění, lhůta výplaty |
| `campaign_period` | object \| null | `{from, to, note}` |
| `eligibility` | string \| null | kdo může doporučovat / být doporučen |
| `source_url` | uri \| null | primární zdroj, preferenčně T&C |
| `source_date` | date | datum ověření |
| `confidence` | `high`/`medium`/`low` | `high` = oficiální T&C |
| `notes` | string | zvláštnosti, gamifikace, rozpory mezi zdroji |

## Rozhodnutí Fáze 0

**D1 — `record_id` jako explicitní stabilní klíč.**
Formát `subjekt__program` (`air-bank__pozvete-pratele`). Není odvozený z `program_name`:
banky programy přejmenovávají a odvozený klíč by při přejmenování osiřel historii.

**D2 — strukturované částky vedle textových.**
`reward_referrer` zůstává čitelný text dle zadání. Navíc `reward_referrer_value` +
`reward_referrer_currency` (a totéž pro referee). Bez čísel nejde strojově zodpovědět
„kdo je nejštědřejší" a „typické rozpětí odměn", což exec summary explicitně žádá.
U tiered odměn je `value` nejvyšší dosažitelná částka a `reward_tiered: true`.

**D3 — žádný automatický přepočet měn.**
U Revolutu, Wise, N26, bunq a Curve je pravdou původní měna. CZK uvádím jen tam, kde ji
publikuje sám subjekt. Přepočet kurzem k datu ověření by vyrobil falešnou přesnost,
která druhý den neplatí, a tiše by se propagoval do srovnávacích tabulek.

**D4 — `status` rozšířen o `none`.**
Zadání říká, že „nenalezeno" je platná informace, a exec summary chce sekci „kdo MGM nemá",
ale v zadaném enumu pro to není hodnota. `unknown` znamená něco jiného — program možná
existuje, jen se nepodařilo určit stav. Rozlišení je nutné, aby šlo oddělit prokázanou
nepřítomnost od neúspěšného researche. **Odchylka od zadaného enumu.**

**D5 — `sources[]` vedle `source_url`.**
Jeden program má typicky marketingovou stránku *i* PDF s podmínkami. `source_url` zůstává
primární (preferuji T&C), `sources[]` nese všechny včetně typu, data a confidence.
Příloha reportu se generuje z `sources[]`.

**D6 — tracker nikdy nepřepíše kurátorovaná data.**
Při nalezení diffu zapíše *návrh* do changelogu s `needs_review: true`. Automaticky sahá
jediné na `last_checked`. Heuristika nad HTML diffem by jinak tiše degradovala ověřená
čísla na šum z redesignu stránky.

**D7 — historie = datované plné snapshoty.**
`data/mgm-programs.json` nese aktuální stav. Při změně se odkládá plný snapshot do
`data/history/YYYY-MM-DD/mgm-programs.json` a field-level before/after jde do changelogu.
Ne `versions[]` uvnitř hlavního souboru — ten by nabobtnal a diffy by přestaly být čitelné.

## Semantické kontroly nad rámec schématu

`tracker/validate.py` vynucuje pravidla kvality ze zadání, která JSON Schema nevyjádří:

- `status: none` ⇒ žádné pole s odměnou nesmí být vyplněné
- `status != none` ⇒ musí existovat aspoň jedna odměna (jinak patří `none`)
- `confidence: high` ⇒ musí existovat zdroj s `type: "tc"` (ne marketing)
- číselná odměna ⇒ musí mít `source_url` nebo `sources[]`
- `reward_*_value` ⇒ musí mít `reward_*_currency`
- `source_date` / `last_checked` nesmí být v budoucnosti
- `campaign_period.from` ≤ `.to`
- `record_id` musí být unikátní napříč datasetem

## CSV

`data/mgm-programs.csv` je plochý: `record_id` + přesně 18 polí ze zadání, v pořadí ze
zadání. Rozšíření (D2, D5) žijí jen v JSON, aby CSV zůstalo otevíratelné v Excelu
a porovnatelné se zadáním.
