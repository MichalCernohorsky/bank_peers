### Jak data vznikla

Research proběhl **15. 9. 2026** pomocí cílených webových vyhledávání na 21 subjektů ze zadání,
s doplňujícím kolem **30. 9. 2026** zaměřeným na tři tehdy neověřené subjekty (ČSOB, Moneta, Twisto);
s křížovou kontrolou přes české srovnávače (Měšec.cz, Peníze.cz, Finparáda, e15/FinExpert) a tiskové
zprávy. Data jsou v `data/mgm-programs.json`, validovaná proti `schema/mgm-program.schema.json`
skriptem `tracker/validate.py`.

### Zásadní omezení tohoto běhu

**Na oficiální stránky subjektů se v tomto prostředí nedá dosáhnout.** Egress proxy blokuje veškeré
relevantní domény — ověřeno na `airbank.cz`, `revolut.com`, `mesec.cz`, `penize.cz` i `cs.wikipedia.org`.
Z toho plynou tři konkrétní důsledky, které je nutné číst spolu s každým číslem v reportu:

1. **Žádný záznam nemá `confidence: high`.** Definice ze zadání zní „high = oficiální T&C". Adresy T&C
   dokumentů jsou u řady subjektů známé a uložené v poli `sources[]` (Air Bank, Raiffeisenbank, mBank,
   Partners Banka, Revolut, N26, Curve), ale **jejich obsah nebyl přečten**. Údaje pocházejí z toho, co
   o nich referovaly vyhledávací výsledky a sekundární zdroje. Validátor tuto hranici hlídá strojově:
   `confidence: high` bez zdroje typu `tc` neprojde, takže degradaci nelze omylem zamaskovat.
2. **Historii nelze postavit na snímcích.** `web.archive.org` je blokovaný, takže časová osa
   požadovaná v zadání (snímky po ~3 měsících za 3 roky) v tomto běhu nevznikla. Sekce 4 obsahuje jen
   změny doložené konkrétním datem a zdrojem.
3. **Tracker nelze v tomto prostředí ověřit proti živým zdrojům.** Je plně otestovaný na offline
   fixtures; jeho ostrý běh proti internetu je nutné spustit z prostředí bez těchto omezení.

### Riziko, které se projevilo v datech

Vyhledávací souhrny **prokazatelně přenášejí čísla mezi subjekty**. V jednom výsledku byly Komerční
bance přiřazeny parametry Air Bank („500 Kč, max. 10 doporučených ročně, celkem 5 000 Kč") — přitom KB
žádný MGM program nemá. Každý údaj byl proto ověřován proti více nezávislým dotazům a čísla, která se
nepodařilo potvrdit, jsou v datech `null` s vysvětlením v `notes`, ne dopočítaný odhad.

Druhým systematickým rizikem je **záměna akvizičního bonusu za MGM**. České srovnávače je běžně mísí
v jednom článku i v jedné větě. Akviziční bonus (odměna novému klientovi za založení účtu) do rozsahu
tohoto reportu **nepatří** a je z dat vyloučen — týká se to zejména KB (4 000 Kč), ČSOB (Plus konto),
Monety (5 % cashback do 3 000 Kč od 1. 9. 2026), Twista (registrační promokódy za 500 Kč, které
šíří slevové weby s vlastním affiliate zájmem),
UniCredit (10 000 Kč) a zářijové akce Air Bank (500 Kč „na vyzkoušení", kód SVET500).

### Co se konkrétně nepodařilo ověřit

| Subjekt | Co chybí | Proč to vadí |
|---|---|---|
| **ČSOB** | ~~existence a výše odměny~~ **dořešeno 30. 9. 2026** | Nalezeny oficiální podmínky akce „500 za doporučení“: 500 Kč, Plus Konto, ale doba trvání **1. 4. – 12. 5. 2020**. Spor 500 vs. 1 000 Kč tím padá. Otevřené zůstává jen to, zda banka od té doby spustila jiný program — žádná stopa po něm není. |
| **Moneta** | zda program vůbec běží | Všechny nalezené verze podmínek jsou z let 2018–2020, novější nic, žádná stránka programu ani položka v FAQ. Opakované hledání 30. 9. 2026 nepřineslo nic nového. Nejpravděpodobněji doběhlý program, ale bez dokladu o ukončení. |
| **Oberbank** | cokoli | Nulový výskyt v českých přehledech. Vedeno jako `unknown`, ne `none` — absence zmínky není důkaz neexistence. |
| **Twisto** | výše odměny | **Dořešeno 30. 9. 2026:** program existuje, má oficiální mechaniku (promokód v sekci „Pozvěte své přátele“, kredity pro obě strany, zpětně nelze). Výše ale ne — zdroje uvádějí 50, 150, 300 i 500 Kč. |
| **Wise** | varianta platná pro ČR | Nalezená T&C jsou britská; v některých zemích je místo bonusu jen sleva na poplatku. Nejnižší jistota v přehledu. |
| **Curve** | která mechanika platí | Dva neslučitelné modely ve zdrojích (prodloužení cashbacku vs. 50 GBP). Sekundární zdroje jsou affiliate weby motivované odměnu nadsazovat. |
| **UniCredit** | z čeho se skládá 1 700 Kč | Doložené položky dávají 300 + 700 = 1 000 Kč. Zbytek do deklarovaných 1 700 Kč se nepodařilo identifikovat. |
| **Raiffeisenbank** | vztah tří různých PDF | Banka vydává tři dokumenty s pravidly; jde patrně o paralelní varianty kampaně, ale bez přečtení to nelze rozhodnout. |

### Jak číst pole `confidence`

- **`high`** — ověřeno v oficiálních T&C. **V tomto běhu nedosaženo u žádného záznamu.**
- **`medium`** — oficiální marketing, tisková zpráva nebo konzistentní shoda více nezávislých zdrojů.
- **`low`** — jediný sekundární zdroj, fórum, affiliate web, nebo rozpor mezi zdroji.

Pole `field_confidence` snižuje jistotu u konkrétních polí tam, kde se liší od záznamové — typicky
`campaign_period` a `limits`, které se mění nejčastěji a dohledávají nejhůř.

### Co udělat pro vyšší kvalitu

Spustit tracker z prostředí s přístupem k internetu. Konfigurace v `config/sources.yaml` už obsahuje
všechny známé adresy T&C, takže první ostrý běh povýší většinu záznamů na `confidence: high`
a založí základ pro sledování změn v čase.
