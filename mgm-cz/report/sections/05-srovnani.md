Rozdíl mezi oběma skupinami není ve výši odměny — ta se překrývá. Je v **tom, co je na odměně
závazné**, a v **tom, čím se odměna kvalifikuje**.

### Forma odměny

| | Banky s českou licencí | Neobanky a fintechy |
|---|---|---|
| Převažující forma | hotovost připsaná na účet (9 z 11 programů) | proměnlivá — hotovost, krypto, zlomky akcií, kovová karta, prodloužený cashback, bonusový úrok |
| Je částka veřejná? | **ano**, uvedená v korunách v pravidlech akce | **zpravidla ne** — výše plave podle kampaně v aplikaci (Revolut, bunq, N26) |
| Výjimky ze vzorce | Partners Banka (úroková sazba), Skip Pay (voucher) | Skip Pay a Twisto drží korunové částky jako české banky |

Nejpodstatnější zjištění: **u neobank nelze v řadě případů odměnu vůbec zapsat jako číslo.** Revolut,
bunq a Curve mají v datech `reward_*_value: null` ne proto, že by se nepodařilo dohledat zdroj, ale
proto, že žádná fixní částka neexistuje — T&C definují mechaniku a odkazují na aktuální nabídku.
Česká banka naproti tomu vydá PDF, ve kterém stojí „500 Kč".

### Symetrie odměny

Tady jsou skupiny nejostřeji rozdělené:

- **Banky odměňují obě strany, obvykle srovnatelně.** Air Bank 500/500, Česká spořitelna 1 200/1 200
  za doporučeného, Max banka 500/500. Asymetrie se objevuje, ale mírná a v neprospěch doporučeného
  (CREDITAS 500/250).
- **U neobank symetrie mizí.** Podle podmínek Revolutu dostává odměnu **pouze doporučující**.
  Skip Pay dává doporučujícímu hotovost, ale doporučenému jen **voucher použitelný od útraty 501 Kč**.
  U N26, Wise i Curve se odměnu pro doporučeného nepodařilo spolehlivě doložit.
  Výjimkou je bunq, kde obě strany dostávají výslovně **stejnou** odměnu.

### Kvalifikační podmínky

| | Banky | Neobanky |
|---|---|---|
| Typická podmínka | 4–5 plateb kartou v prvních 1–3 měsících | první platba kartou, vklad, nebo aktivace konkrétní služby |
| Vazba na objem | vzácná — jen CREDITAS (vklad 20 000 / 90 000 Kč) | častá — N26 vyžaduje platbu **alespoň ve výši bonusu**, Wise kvalifikovaný převod ~200 GBP |
| Clawback | veřejně nekomunikován | Revolut výslovně: zrušení účtu pozvaným do 14 dnů = odměna propadá |
| Ruční nárokování | ne, vyplácí se automaticky | bunq: nutné aktivně kliknout na Claim Reward |

**Nejzajímavější mechanika celého přehledu je podmínka N26**: pozvaný musí zaplatit kartou částku
alespoň rovnou výši referral bonusu. Odměna si tak sama určuje kvalifikační práh a škáluje s ním —
konstrukce, kterou nemá žádná česká banka.

### Agresivita

„Agresivnější" vychází každá skupina v jiném rozměru, takže jednoduché pořadí nedává smysl:

- **Objemem odměny** vedou banky: mBank 26 000 Kč je nejvyšší doložitelně dosažitelná částka na trhu
  s korunovým vyjádřením. N26 sice deklaruje strop 1 500 EUR, ale bez známé jednotkové odměny to není
  příslib, jen horní mez.
- **Šíří záběru** vedou neobanky: bunq odměňuje doporučení napříč pěti produkty (účet, karty, spoření,
  akcie, krypto) a limit konstruuje jako 1 pozvaný z každé záložky měsíčně — nutí uživatele používat
  celou banku, ne jen účet.
- **Rizikovostí doporučovaného produktu** vede jednoznačně **UniCredit**, a to napříč oběma skupinami:
  700 Kč za doporučení spotřebitelské půjčky od 100 000 Kč, bez jakéhokoli stropu na počet doporučení.
  Motivovat laiky k šíření úvěrových produktů bez limitu je kvalitativně jiná věc než platit za
  založení běžného účtu, a stojí za samostatnou pozornost.
- **Vázaností peněz** vede **CREDITAS**: jako jediný program si přes MGM kupuje vklady, ne transakční
  klienty, a podle toho vypadají vstupní bariéry — 90 000 Kč a 2–4 roky vázanosti u termínovaného
  vkladu proti „zaplať 5× kartou" jinde.

### Dostupnost pro české klienty

Nejde přehlédnout, že u zahraničních neobank **nejsou podmínky lokalizované**. Nalezená T&C N26 jsou
německá a italská verze, u Wise britská. U Wise zdroje samy uvádějí, že v některých zemích je místo
hotovostního bonusu jen sleva na poplatku — **co přesně platí pro klienta v ČR, se z veřejných zdrojů
zjistit nepodařilo**. Částky u Wise (GBP) a N26 (EUR) jsou proto v datech ponechány v původní měně bez
přepočtu a **nesmí se z nich vyvozovat, co dostane český klient**.
