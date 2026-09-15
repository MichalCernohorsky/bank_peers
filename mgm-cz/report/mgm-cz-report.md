# Member-Get-Member programy na českém bankovním trhu

*Datová základna ověřena k 2026-09-15. Report je generovaný z `data/mgm-programs.json` skriptem `tracker/report.py` — needitovat ručně; analytické sekce se upravují v `report/sections/`.*

---

## 1. Executive summary

- **Nejštědřejší program má jednoznačně mBank** — až 26 000 Kč ročně pro doporučujícího, což je čtyřapůlnásobek druhého nejvyššího stropu na trhu (ČS, 6 000 Kč). Cena za to je nejsložitější mechanika v přehledu: odměna se nedrobí po doporučených, ale po jednotlivých platbách kartou (100 Kč za platbu, max. 10 plateb), a k tomu se přidává milníkový bonus 1 000 Kč za každého 3., 6., 9., 12., 15. a 18. doporučeného. N26 sice deklaruje vyšší strop (1 500 EUR), ale jednotkovou odměnu za doporučeného nezveřejňuje, takže ho nelze srovnávat.

- **Tržním standardem je 500 Kč za doporučeného.** Stejnou částku dává Air Bank, Banka CREDITAS i Skip Pay a dávala ji i Max banka, než program ukončila. Ověřené jednotkové odměny pro doporučujícího se pohybují v rozpětí **300–2 000 Kč**, přičemž 500 Kč je zdaleka nejčastější hodnota. Horní konec drží Raiffeisenbank (2 000 Kč za podnikatelský účet) a UniCredit (700 Kč za doporučenou půjčku).

- **Převládající model podmínek je „nový klient + zaplať kartou".** Prakticky všechny bankovní programy kombinují definici nového klienta (typicky: nesmí mít u banky účet, u RB v posledních 12 měsících, u Air Bank nikdy) s požadavkem na několik plateb kartou v prvních týdnech. **Pětkrát kartou je modální podmínka trhu.** Banky tedy neplatí za registraci, ale za prokázané transakční chování.

- **Strop 10 doporučených ročně je druhý nejčastější vzorec** (Air Bank, Skip Pay, Revolut 5 na kampaň, bunq 5 měsíčně, N26 10). Výjimkou je **UniCredit, jediný program zcela bez stropu** na počet doporučení i celkovou odměnu — a zároveň jediný, který odměňuje za doporučení **úvěru** (700 Kč za PRESTO Půjčku od 100 000 Kč), což je podstatně agresivnější než doporučování běžných účtů.

- **Tři subjekty MGM prokazatelně nemají: Komerční banka, Fio banka a Trinity Bank.** U KB je to nejnápadnější — jako jediná z velké čtyřky nahrazuje MGM čistě akvizičním bonusem (až 4 000 Kč novým klientům). Fio staví na bezpoplatkovosti místo bonusů, Trinity odměňuje jen vlastní chování klienta (Prémiový klub, Narozeninový bonus), ne přivedení nového.

- **U čtyř subjektů se program nepodařilo ověřit: ČSOB, Moneta, Oberbank a Twisto.** U ČSOB a Monety je to nejvíc frustrující — obě banky MGM zjevně provozují (Moneta k němu vydává vlastní PDF s pravidly), ale aktuální výši odměny nelze z veřejných zdrojů doložit. U ČSOB si sekundární zdroje přímo odporují (500 Kč vs. 1 000 Kč) a žádný oficiální dokument k MGM se nepodařilo najít.

- **Neobanky hrají jinou hru než české banky: neuvádějí částky.** Zatímco česká banka odměnu zveřejní v korunách v pravidlech akce, Revolut, bunq i N26 nechávají výši odměny plovoucí podle aktuální kampaně v aplikaci. Odměna tam navíc často není hotovost — bunq nabízí krypto, zlomky akcií nebo kovovou kartu, N26 může bonus vyplatit v akciích, Curve prodlužuje cashback. **Symetrie odměny, u českých bank pravidlo, u neobank mizí:** podle podmínek Revolutu dostává odměnu pouze doporučující.

- **Odměnou nemusí být peníze.** Partners Banka jako jediná nabízí místo částky **úrokovou sazbu** (4,06 % p.a. do 500 000 Kč, doporučující na 1 měsíc, doporučený na 3) a Skip Pay dává doporučenému jen **slevový voucher** použitelný od útraty 501 Kč. Hodnota takové odměny závisí na chování klienta a nelze ji postavit do jedné tabulky s hotovostí.


### Souhrnná čísla

- **Subjektů celkem:** 21 (14 bank, 7 neobank/fintechů)
- **Podle statusu:** aktivní: 13, neověřeno: 4, nemá MGM: 3, ukončen: 1
- **Podle jistoty zdroje:** střední: 13, nízká: 8


---

## 2. Přehledová tabulka

| Subjekt | Typ | Status | Odměna doporučující | Odměna doporučený | Klíčová podmínka | Limit | Conf. | Zdroj |
|---|---|---|---|---|---|---|---|---|
| **Air Bank** | banka | aktivní | 500 Kč za každého doporučeného | 500 Kč | Doporučující pošle odkaz z mobilní aplikace (Menu / Nastavení a banka / Pozvat přátele). Doporučený… | max. 10 doporučených přátel ročně (tj. max. 5 000 Kč ročně… | střední | [odkaz](https://www.airbank.cz/file-download/pravidla-akce-pozvani-pratel-doporucujici) |
| **Banka CREDITAS** | banka | aktivní | 500 Kč za doporučeného | 250 Kč | Doporučený uvede při založení produktu jméno, příjmení a členské číslo doporučujícího. U spořicího… | nepodařilo se ověřit | střední | [odkaz](https://www2020.creditas.cz/doporucte-a-ziskejte) |
| **Česká spořitelna** | banka | aktivní | až 6 000 Kč celkem (až 1 200 Kč za každého z max. 5 doporučených) | až 1 200 Kč | Doporučený si přes George sjedná účet Plus, Standard, Premier nebo Erste Private Banking a následně… | max. 5 doporučených přátel (6 000 Kč pro doporučujícího) | střední | [odkaz](https://www.e15.cz/finexpert/banky-a-ucty/ceska-sporitelna-prodlouzila-odmenovani-za-doporuceni-uctu-ziskat-muzete-az-6-000-korun-1430070) |
| **ČSOB (vč. Poštovní spořitelny)** | banka | neověřeno | nejednoznačné: sekundární zdroje uvádějí 500 Kč i 1 000 Kč za doporučeného | nejednoznačné: jeden zdroj uvádí 500 Kč pro obě strany, jiný pouze odměnu pro d… | Nepodařilo se ověřit. Nalezené oficiální PDF s pravidly ČSOB se týkají akvizičních kampaní (Plus ko… | — | nízká | [odkaz](https://www.penize.cz/osobni-ucty/487348-banky-vas-odmeni-za-doporuceni-prehled-kde-a-jak-si-prilepsite) |
| **Fio banka** | banka | nemá MGM | — | — | — | — | nízká | [odkaz](https://www.finparada.cz/3524-Banky-zkouseji-ziskat-nove-klienty-odmenou-za-doporuceni.aspx) |
| **Komerční banka** | banka | nemá MGM | — | — | — | — | střední | [odkaz](https://www.kb.cz/cs/obcane/bonus-az-4-000-kc-pro-nove-klienty) |
| **Max banka** | banka | ukončen | 500 Kč (program ukončen) | 500 Kč (program ukončen) | Nový klient musel provést 3 platby debetní kartou do 2 měsíců od založení účtu. | — | střední | [odkaz](https://www.mesec.cz/aktuality/max-banka-predcasne-ukoncila-odmeny-za-zalozeni-uctu-puvodne-mela-skoncit-az-v-breznu-2023/) |
| **mBank** | banka | aktivní | 100 Kč za každou platbu kartou doporučeného, max. 1 000 Kč za doporučeného; nav… | 100 Kč za každou vlastní platbu kartou, max. 1 000 Kč | Doporučující je stávající klient mBank starší 15 let, majitel mKonta nebo mKonta #navlastnitriko. N… | max. 20 doporučených na jednoho doporučujícího; max. 1 000… | střední | [odkaz](https://www.mbank.cz/informace-k-produktum/dokumenty-ke-stazeni/dokumenty/akce/doporucte-mbank_pravidla-unor2026.pdf) |
| **Moneta Money Bank** | banka | neověřeno | výše neověřena; banka komunikuje „tisíce korun ročně“ | existuje (obě strany dostávají odměnu), výše neověřena | Nepodařilo se ověřit. Banka odkazuje na PDF s podmínkami kampaně „Odměna za doporučení klienta“. | — | nízká | [odkaz](https://www.moneta.cz/dokumenty-ke-stazeni/osobni/ucty) |
| **Oberbank** | banka | neověřeno | — | — | — | — | nízká | [odkaz](https://www.oberbank.cz/) |
| **Partners Banka** | banka | aktivní | zvýhodněná sazba 4,06 % p.a. na spořicím účtu do 500 000 Kč na 1 kalendářní měs… | zvýhodněná sazba 4,06 % p.a. na spořicím účtu do 500 000 Kč na 3 měsíce | Doporučený zadá kód stávajícího klienta. Zvýhodněná sazba za doporučení platí i bez plnění standard… | nepodařilo se ověřit | střední | [odkaz](https://www.partnersbanka.cz/userfiles/podminky-doporuc-a-ziskej-5e249b95.pdf) |
| **Raiffeisenbank** | banka | aktivní | 1 000 Kč za osobní účet, 2 000 Kč za podnikatelský účet, 1 000 Kč za stavební s… | 6× 500 Kč za aktivní používání účtu (akviziční složka navázaná na doporučení) | Doporučený se registruje telefonním číslem přes unikátní odkaz a do 30 dnů od registrace uzavře a a… | nepodařilo se ověřit | střední | [odkaz](https://www.rb.cz/podpora/podminky-akci/odmena-za-doporuceni) |
| **Trinity Bank** | banka | nemá MGM | — | — | — | — | nízká | [odkaz](https://www.trinitybank.cz/download/391) |
| **UniCredit Bank** | banka | aktivní | až 1 700 Kč za každého doporučeného: 300 Kč za U konto / U konto Premium, 700 K… | nepodařilo se ověřit, zda doporučený dostává odměnu | Doporučující sdělí novému klientovi svůj unikátní promo kód. Nový klient si během trvání kampaně sj… | celková výše odměny není omezena, záleží pouze na počtu dop… | střední | [odkaz](https://www.investujeme.cz/tiskove-zpravy/doporucte-produkty-unicredit-bank-svym-pratelum-a-ziskejte-odmenu-az-1700-korun-za-kazdeho-doporuceneho-klienta/) |
| **bunq** | neobanka | aktivní | obě strany dostávají stejnou odměnu; forma se liší podle aktuální nabídky v apl… | stejná odměna jako doporučující (symetrická) | Pozvaný se připojí a splní kvalifikační krok navázaný na konkrétní nabídku — aktivace Switch Servic… | max. 5 pozvaných za kalendářní měsíc — 1 z každé záložky (H… | střední | [odkaz](https://www.bunq.com/personal-account/banking-features/refer-a-friend) |
| **Curve** | neobanka | aktivní | ROZPOR MEZI ZDROJI: oficiální podmínky uvádějí 1 % cashback na 30 dnů navíc za… | nepodařilo se spolehlivě ověřit; sekundární zdroje uvádějí 50 GBP v Curve Cash | Doporučený musí podat žádost, dokončit onboarding a provést alespoň 1 nákup kartou Curve. Odměny se… | dle sekundárních zdrojů max. 5 doporučených za období nabíd… | nízká | [odkaz](https://www.curve.com/legal/referral-promo-terms/) |
| **N26** | neobanka | aktivní | výše bonusu se liší podle kampaně; celkový strop 1 500 EUR na zákazníka | nepodařilo se ověřit, zda pozvaný dostává odměnu | Pozvaný musí provést první platbu kartou (nákup v obchodě nebo online, PayPal vyloučen) v hodnotě a… | max. 10 referral bonusů na uživatele; celkem max. 1 500 EUR… | střední | [odkaz](https://docs.n26.com/legal/01+DE/01+Account/en/15account-terms-and-conditions-friend-referral-3.0-en.pdf) |
| **Revolut** | neobanka | aktivní | výše se mění podle kampaně; sekundární zdroj uvádí až 1 500 Kč | dle podmínek odměnu dostává POUZE doporučující, ne pozvaný | Doporučující musí mít aktivní osobní účet po celou dobu trvání akce i v okamžiku připsání odměny. P… | max. 5 pozvaných osob v rámci jedné kampaně | střední | [odkaz](https://www.revolut.com/cs-CZ/legal/referrals-terms/) |
| **Skip Pay** | neobanka | aktivní | 500 Kč za každý nově ověřený balíček MAXI přes odkaz, celkem až 5 000 Kč | sleva 500 Kč (voucher do e-mailu) | Odkaz lze sdílet neomezeně často. Odměna 500 Kč náleží za každý nově ověřený balíček MAXI pořízený… | max. 10 doporučení, tj. až 5 000 Kč | střední | [odkaz](https://skippay.cz/doporucte-nas) |
| **Twisto** | neobanka | neověřeno | nejednoznačné: zdroje uvádějí 50 Kč za doporučeného, jinde 300–500 Kč pouze pro… | 500 Kč po registraci s promo kódem (dle sekundárních zdrojů) | Nepodařilo se ověřit. Zdroje shodně uvádějí, že nejde o plošnou kampaň — promo kódy jsou dostupné j… | nepodařilo se ověřit | nízká | [odkaz](https://www.twisto.cz/vychytavky/twistoucet/) |
| **Wise** | neobanka | aktivní | závisí na zemi; typicky cca 75 GBP po 3 pozvaných, kteří provedou kvalifikovaný… | převod zdarma na první mezinárodní platbu do stanoveného limitu (typicky cca 50… | Doporučující musí mít ověřený účet v dobrém stavu a mít za sebou alespoň jeden osobní převod. Pozva… | nepodařilo se ověřit pro ČR | nízká | [odkaz](https://wise.com/gb/legal/referral-terms) |


---

## 3. Detailní karty subjektů

### Banky

#### Air Bank

| Pole | Hodnota |
|---|---|
| Program | Pozvěte přátele |
| Status | aktivní |
| Produkty | běžný účet |
| Odměna doporučující | 500 Kč za každého doporučeného |
| Odměna doporučený | 500 Kč |
| Typ odměny | cash |
| Podmínky | Doporučující pošle odkaz z mobilní aplikace (Menu / Nastavení a banka / Pozvat přátele). Doporučený si nejpozději do 45 dnů založí účet na stejné telefonní číslo, na které byl pozván, a zaplatí alespoň 5× kartou v měsíci aktivace účtu nebo v měsíci bezprostředně následujícím. |
| Kanál | app; link |
| Limity | max. 10 doporučených přátel ročně (tj. max. 5 000 Kč ročně pro doporučujícího) |
| Lhůty | 45 dnů na založení účtu od pozvánky; 5 plateb kartou v měsíci aktivace nebo následujícím; výplata zpravidla do druhého dne po splnění podmínek, nejpozději do konce kalendářního měsíce následujícího po měsíci splnění |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučený musí být starší 15 let a nesmí být ani v minulosti být klientem Air Bank s vlastní rámcovou smlouvou (disponent nebo držitel karty k cizímu účtu doporučen být může) |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** Nejlépe zdokumentovaný program v přehledu — jediný, u kterého jsou z veřejných zdrojů známé VŠECHNY parametry včetně lhůt a výplatního cyklu. Symetrická odměna 500/500 Kč. reward_referrer_value = 5 000 Kč jako roční maximum (500 Kč × 10). Podmínka „stejné telefonní číslo“ je nezvyklá a v praxi je nejčastější příčinou nevyplacení. Air Bank v září 2026 paralelně běží akviziční bonus 500 Kč „na vyzkoušení“ a kód SVET500 — to NEJSOU MGM.

#### Banka CREDITAS

| Pole | Hodnota |
|---|---|
| Program | Doporučte a získejte |
| Status | aktivní |
| Produkty | spořicí účet; termínovaný vklad |
| Odměna doporučující | 500 Kč za doporučeného |
| Odměna doporučený | 250 Kč |
| Typ odměny | cash |
| Podmínky | Doporučený uvede při založení produktu jméno, příjmení a členské číslo doporučujícího. U spořicího účtu je nutný vklad minimálně 20 000 Kč. U termínovaného vkladu doba sjednání 24, 36 nebo 48 měsíců a vklad minimálně 90 000 Kč (pouze CZK). |
| Kanál | branch; web |
| Limity | nepodařilo se ověřit |
| Lhůty | nepodařilo se ověřit |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučující = stávající klient s členským číslem; doporučený = nový klient |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `limits`: nízká, `timing`: nízká

**Poznámky.** JEDINÝ program v přehledu vázaný na DEPOZITNÍ produkty místo běžného účtu — Creditas si přes MGM kupuje vklady, ne transakční klienty. Tomu odpovídají vstupní bariéry (20 000 Kč na spořicí účet, 90 000 Kč a 2–4 roky vázanosti na termínovaný vklad), které jsou řádově vyšší než u ostatních programů, kde stačí zaplatit kartou. Asymetrická odměna v neprospěch doporučeného (500 vs. 250 Kč). Doporučení běží přes členské číslo, ne přes odkaz nebo kód — pozůstatek družstevní záložny. Doména www2020.creditas.cz naznačuje starou stránku, riziko neaktuálnosti.

#### Česká spořitelna

| Pole | Hodnota |
|---|---|
| Program | Doporučte George |
| Status | aktivní |
| Produkty | běžný účet (Plus, Standard, Premier, Erste Private Banking) |
| Odměna doporučující | až 6 000 Kč celkem (až 1 200 Kč za každého z max. 5 doporučených) |
| Odměna doporučený | až 1 200 Kč |
| Typ odměny | cash |
| Podmínky | Doporučený si přes George sjedná účet Plus, Standard, Premier nebo Erste Private Banking a následně zaplatí alespoň 4× kartou v každém ze 3 měsíců následujících po měsíci založení účtu. Odměna 1 200 Kč se vyplácí rozděleně do 3 měsíců. |
| Kanál | app; link |
| Limity | max. 5 doporučených přátel (6 000 Kč pro doporučujícího) |
| Lhůty | podmínka aktivity ve 3 měsících po založení účtu; odměna rozdělena do 3 měsíčních plateb |
| Platnost kampaně | ? – ? (Program byl prodloužen a pokračuje i v roce 2026; konkrétní datum konce se nepodařilo ověřit.) |
| Kdo se může účastnit | doporučující = klient ČS s George; doporučený = nový klient sjednávající účet přes George |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `campaign_period`: nízká

**Poznámky.** Největší odměna pro doporučujícího mezi velkými bankami. Odměna je strukturovaná per-doporučený (1 200 Kč), ne jako jedna částka. Dřívější komunikace banky uváděla 1 200 Kč pro obě strany — viz FB post ČS. Oficiální T&C se nepodařilo dohledat (egress blokován), proto medium.

#### ČSOB (vč. Poštovní spořitelny)

| Pole | Hodnota |
|---|---|
| Program | — |
| Status | neověřeno |
| Produkty | běžný účet |
| Odměna doporučující | nejednoznačné: sekundární zdroje uvádějí 500 Kč i 1 000 Kč za doporučeného |
| Odměna doporučený | nejednoznačné: jeden zdroj uvádí 500 Kč pro obě strany, jiný pouze odměnu pro doporučujícího |
| Typ odměny | cash |
| Podmínky | Nepodařilo se ověřit. Nalezené oficiální PDF s pravidly ČSOB se týkají akvizičních kampaní (Plus konto, podnikatelský účet, Premium konto), ne MGM programu. |
| Kanál | — |
| Limity | — |
| Lhůty | — |
| Platnost kampaně | — |
| Kdo se může účastnit | — |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** ROZPOR MEZI ZDROJI, NEROZŘEŠEN. Jeden sekundární zdroj tvrdí 500 Kč na oba účty, jiný 1 000 Kč pro doporučujícího. Nepodařilo se najít žádnou oficiální stránku ani PDF s pravidly MGM programu ČSOB — všechny nalezené oficiální dokumenty jsou akviziční kampaně pro nové klienty. Dokud nebude ověřeno z T&C, částku neuvádím jako fakt. Prioritní kandidát na ověření trackerem.

#### Fio banka

| Pole | Hodnota |
|---|---|
| Program | — |
| Status | nemá MGM |
| Produkty | — |
| Odměna doporučující | — |
| Odměna doporučený | — |
| Typ odměny | — |
| Podmínky | — |
| Kanál | — |
| Limity | — |
| Lhůty | — |
| Platnost kampaně | — |
| Kdo se může účastnit | — |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** Fio dlouhodobě nenabízí akviziční bonusy ani MGM; staví na bezpoplatkovosti a kvalitě služby. Odměňuje jinak — za splácení hypotéky a cashback přes Mastercard Priceless Specials, což nejsou MGM. Status 'none' opřen pouze o sekundární zdroje a o absenci jakékoli zmínky na straně banky, proto confidence low: negativní zjištění se z veřejných zdrojů dokazuje hůř než pozitivní.

#### Komerční banka

| Pole | Hodnota |
|---|---|
| Program | — |
| Status | nemá MGM |
| Produkty | — |
| Odměna doporučující | — |
| Odměna doporučený | — |
| Typ odměny | — |
| Podmínky | — |
| Kanál | — |
| Limity | — |
| Lhůty | — |
| Platnost kampaně | — |
| Kdo se může účastnit | — |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** KB nemá MGM program. Má pouze AKVIZIČNÍ bonus až 4 000 Kč pro nové klienty (sjednání do 30. 11. 2026, 3× 1 000 Kč za 5 plateb kartou + příjem ≥ 15 000 Kč měsíčně). POZOR: agregátory tyto dvě věci opakovaně zaměňují — jeden vyhledávací souhrn přiřadil KB parametry Air Bank (500 Kč, max 10 ročně). Akviziční bonus není MGM a do rozsahu tohoto reportu nepatří.

#### Max banka

| Pole | Hodnota |
|---|---|
| Program | Odměna za doporučení (Neo účet) |
| Status | ukončen |
| Produkty | běžný účet (Neo účet) |
| Odměna doporučující | 500 Kč (program ukončen) |
| Odměna doporučený | 500 Kč (program ukončen) |
| Typ odměny | cash |
| Podmínky | Nový klient musel provést 3 platby debetní kartou do 2 měsíců od založení účtu. |
| Kanál | link |
| Limity | — |
| Lhůty | 3 platby kartou do 2 měsíců od založení účtu |
| Platnost kampaně | ? – 2022-10-27 (Akce měla původně běžet do 31. 3. 2023, banka ji ale předčasně ukončila k 27. 10. 2022 na základě výhrady v podmínkách.) |
| Kdo se může účastnit | doporučující = stávající klient Max banky; doporučený = nový klient |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** SUBJEKT JIŽ NEEXISTUJE SAMOSTATNĚ — Max banka fúzovala s Bankou CREDITAS k 1. 10. 2024 (datum fúze pouze z fórového zdroje, confidence low). Program 500 + 500 Kč byl ukončen podstatně dříve, 27. 10. 2022, ačkoli podmínky slibovaly běh do 31. 3. 2023; banka využila výhradu o možnosti předčasného ukončení. Je to jediný doložený případ v přehledu, kdy banka MGM program ukončila dřív, než sama avizovala — relevantní pro posouzení závaznosti deklarovaných campaign_period u ostatních subjektů.

#### mBank

| Pole | Hodnota |
|---|---|
| Program | Doporučte mBank (mKlub) |
| Status | aktivní |
| Produkty | běžný účet (mKonto, mKonto #navlastnitriko); dětský účet |
| Odměna doporučující | 100 Kč za každou platbu kartou doporučeného, max. 1 000 Kč za doporučeného; navíc mimořádný bonus 1 000 Kč za každého 3., 6., 9., 12., 15. a 18. doporučeného; celkem až 26 000 Kč |
| Odměna doporučený | 100 Kč za každou vlastní platbu kartou, max. 1 000 Kč |
| Typ odměny | cash |
| Podmínky | Doporučující je stávající klient mBank starší 15 let, majitel mKonta nebo mKonta #navlastnitriko. Nový i dosavadní klient dostanou 100 Kč za každou platbu kartou, nejvýše za 10 plateb během 60 dnů od založení účtu. Mimořádný bonus 1 000 Kč se vyplácí za každého 3., 6., 9., 12., 15. a 18. doporučeného, který splní alespoň 1 platbu. |
| Kanál | app; link; code |
| Limity | max. 20 doporučených na jednoho doporučujícího; max. 1 000 Kč za jednoho doporučeného; celkem až 26 000 Kč |
| Lhůty | 60 dnů od založení účtu na provedení 10 plateb kartou |
| Platnost kampaně | 2026-01-30 – 2026-03-31 (Období akce dle pravidel; k datu researche (2026-09-15) banka program stále komunikuje, takže buď byl prodloužen, nebo běží navazující kampaň — neověřeno.) |
| Kdo se může účastnit | doporučující = klient mBank 15+ s mKontem; doporučený = nový klient |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `campaign_period`: nízká

**Poznámky.** NEJŠTĚDŘEJŠÍ a zároveň NEJVÍC GAMIFIKOVANÝ program na trhu. Tři odlišné mechaniky najednou: (1) per-transakční drobení odměny (100 Kč za platbu, ne jednorázová částka), (2) milníkový bonus za každého 3. doporučeného, (3) strop 20 doporučených. Odměna tedy není lineární — doporučující je tlačen k dosažení násobků tří. Samostatná větev pro dětský účet: 500 Kč rodič + 500 Kč dítě, dítě dále 300 Kč za založení a 10× 67 Kč „kapesné“ (celkem 970 Kč). mBank v roce 2026 zvýšila strop z 10 000 Kč na 26 000 Kč. Existence dodatků č. 1 (leden) a č. 2 (únor 2026) dokládá, že pravidla se mění v řádu týdnů — silný argument pro tracker.

#### Moneta Money Bank

| Pole | Hodnota |
|---|---|
| Program | Odměna za doporučení klienta |
| Status | neověřeno |
| Produkty | běžný účet |
| Odměna doporučující | výše neověřena; banka komunikuje „tisíce korun ročně“ |
| Odměna doporučený | existuje (obě strany dostávají odměnu), výše neověřena |
| Typ odměny | cash |
| Podmínky | Nepodařilo se ověřit. Banka odkazuje na PDF s podmínkami kampaně „Odměna za doporučení klienta“. |
| Kanál | app |
| Limity | — |
| Lhůty | — |
| Platnost kampaně | — |
| Kdo se může účastnit | — |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** Program prokazatelně existuje (banka pro něj vydává vlastní PDF s pravidly a komunikuje „obě strany dostanou odměnu“), ale aktuální výši odměny se nepodařilo z veřejných zdrojů ověřit. Historicky 100 Kč, od 15. 9. 2018 zvýšeno na 300 Kč — pouze fórový zdroj, confidence low, do historie nezařazeno. Nezaměňovat s „Program Odměny“, což je cashback u obchodníků, ne MGM.

#### Oberbank

| Pole | Hodnota |
|---|---|
| Program | — |
| Status | neověřeno |
| Produkty | — |
| Odměna doporučující | — |
| Odměna doporučený | — |
| Typ odměny | — |
| Podmínky | — |
| Kanál | — |
| Limity | — |
| Lhůty | — |
| Platnost kampaně | — |
| Kdo se může účastnit | — |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** NENALEZENO. Žádný ze zdrojů — ani oficiální web, ani žádný ze srovnávačů pokrývajících český trh — o MGM programu Oberbank nic neuvádí. Oberbank se v českých přehledech bonusů a odměn za doporučení systematicky nevyskytuje, což je slabá nepřímá indicie, že program nemá; banka ale cílí na privátní a firemní klientelu, kde se MGM běžně neřeší veřejnou kampaní. Rozlišeno jako 'unknown', ne 'none': absence zmínky v médiích zaměřených na retail nedokazuje neexistenci programu. Vyžaduje ověření přímo na webu banky, až bude dostupný.

#### Partners Banka

| Pole | Hodnota |
|---|---|
| Program | Doporuč a získej |
| Status | aktivní |
| Produkty | spořicí účet |
| Odměna doporučující | zvýhodněná sazba 4,06 % p.a. na spořicím účtu do 500 000 Kč na 1 kalendářní měsíc |
| Odměna doporučený | zvýhodněná sazba 4,06 % p.a. na spořicím účtu do 500 000 Kč na 3 měsíce |
| Typ odměny | other |
| Podmínky | Doporučený zadá kód stávajícího klienta. Zvýhodněná sazba za doporučení platí i bez plnění standardních podmínek pro zvýšený úrok (5 plateb kartou měsíčně + aktivní Hlídač minimálního zůstatku nastavený na alespoň 20 000 Kč). |
| Kanál | code; app |
| Limity | nepodařilo se ověřit |
| Lhůty | doporučující 1 kalendářní měsíc, doporučený 3 měsíce |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučující = stávající klient Partners Banky; doporučený = nový klient s kódem |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `limits`: nízká

**Poznámky.** JEDINÝ program na trhu, kde odměnou NENÍ PENĚŽNÍ ČÁSTKA, ale úroková sazba — proto reward_type 'other' a reward_*_value = null. Hodnota odměny závisí na zůstatku klienta, takže není srovnatelná s hotovostními programy a nelze ji seřadit do tabulky; při plném zůstatku 500 000 Kč a rozdílu cca 0,86 p.b. proti základní sazbě 3,2 % vychází zhruba 360 Kč za měsíc pro doporučujícího — ORIENTAČNÍ ODVOZENÍ, ne údaj banky. Pozoruhodná asymetrie: doporučený dostává výhodu 3× déle než doporučující. Zároveň jediný program, kde odměna obchází standardní podmínky pro zvýšený úrok.

#### Raiffeisenbank

| Pole | Hodnota |
|---|---|
| Program | Odměna za doporučení |
| Status | aktivní |
| Produkty | osobní běžný účet; podnikatelský účet; stavební spoření |
| Odměna doporučující | 1 000 Kč za osobní účet, 2 000 Kč za podnikatelský účet, 1 000 Kč za stavební spoření |
| Odměna doporučený | 6× 500 Kč za aktivní používání účtu (akviziční složka navázaná na doporučení) |
| Typ odměny | cash |
| Podmínky | Doporučený se registruje telefonním číslem přes unikátní odkaz a do 30 dnů od registrace uzavře a aktivuje smlouvu o běžném účtu nebo stavebním spoření. Novým klientem je ten, kdo v posledních 12 měsících neměl u RB vedený žádný bankovní účet. Odměnu dostanou obě strany jen při splnění všech podmínek. |
| Kanál | app; link |
| Limity | nepodařilo se ověřit |
| Lhůty | 30 dnů od registrace na uzavření smlouvy; odměna připsána nejpozději 15. den měsíce následujícího po aktivaci produktu |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučující = stávající klient RB; doporučený = nový klient bez účtu u RB v posledních 12 měsících. Zaměstnanci RB a jejich rodinní příslušníci jsou vyloučeni. |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `limits`: nízká, `reward_referee`: nízká

**Poznámky.** Jediná banka v přehledu s odstupňováním odměny podle TYPU produktu (osobní/podnikatelský/stavební spoření) — 2 000 Kč za podnikatelský účet je nejvyšší jednorázová sazba za doporučeného na trhu. Banka pro program vydává hned tři různá PDF s pravidly, což naznačuje více paralelních variant kampaně; jejich vzájemný vztah se bez přečtení PDF nepodařilo určit. reward_referrer_value = 2000 jako nejvyšší dosažitelná sazba.

#### Trinity Bank

| Pole | Hodnota |
|---|---|
| Program | — |
| Status | nemá MGM |
| Produkty | — |
| Odměna doporučující | — |
| Odměna doporučený | — |
| Typ odměny | — |
| Podmínky | — |
| Kanál | — |
| Limity | — |
| Lhůty | — |
| Platnost kampaně | — |
| Kdo se může účastnit | — |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** MGM program nenalezen. Trinity Bank má několik jiných bonusových schémat — Prémiový klub (finanční odměna 1 500 Kč), Narozeninový bonus, Bonus+ (příplatek k sazbě až 0,40 % p.a.), Dobrý klient — žádné z nich ale není MGM, všechna odměňují vlastní chování klienta, ne přivedení nového. Absence programu doložena jen fórovým zdrojem a absencí zmínky na webu banky, proto confidence low.

#### UniCredit Bank

| Pole | Hodnota |
|---|---|
| Program | Doporuč a získej |
| Status | aktivní |
| Produkty | běžný účet (U konto, U konto Premium); spotřebitelský úvěr (PRESTO Půjčka) |
| Odměna doporučující | až 1 700 Kč za každého doporučeného: 300 Kč za U konto / U konto Premium, 700 Kč za PRESTO Půjčku ≥ 100 000 Kč |
| Odměna doporučený | nepodařilo se ověřit, zda doporučený dostává odměnu |
| Typ odměny | cash |
| Podmínky | Doporučující sdělí novému klientovi svůj unikátní promo kód. Nový klient si během trvání kampaně sjedná příslušný produkt; u PRESTO Půjčky musí být ve výši alespoň 100 000 Kč. |
| Kanál | code |
| Limity | celková výše odměny není omezena, záleží pouze na počtu doporučených |
| Lhůty | nepodařilo se ověřit |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučující = klient UniCredit Bank s promo kódem |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `reward_referee`: nízká, `campaign_period`: nízká

**Poznámky.** JEDINÝ program v přehledu BEZ STROPU na počet doporučení i celkovou odměnu. Zároveň jediný, který odměňuje za doporučení ÚVĚRU (700 Kč za PRESTO Půjčku ≥ 100 tis. Kč) — to je podstatně agresivnější než doporučování běžných účtů a vyvolává otázku vhodnosti motivovat laiky k šíření úvěrových produktů. 300 + 700 = 1 000 Kč; deklarovaných 1 700 Kč implikuje ještě další produkt, který se z dostupných zdrojů nepodařilo identifikovat — proto reward_tiered a nižší jistota. Měšec uvádí odlišnou mechaniku (až 3 % z platby kartou), zdroje si neodpovídají.

### Neobanky a fintechy

#### bunq

| Pole | Hodnota |
|---|---|
| Program | Refer a friend |
| Status | aktivní |
| Produkty | osobní účet; karty; spoření; akcie; krypto |
| Odměna doporučující | obě strany dostávají stejnou odměnu; forma se liší podle aktuální nabídky v aplikaci — hotovost, krypto, Metal Card, bonusový úrok na spoření nebo výhody pro obchodování s akciemi |
| Odměna doporučený | stejná odměna jako doporučující (symetrická) |
| Typ odměny | other |
| Podmínky | Pozvaný se připojí a splní kvalifikační krok navázaný na konkrétní nabídku — aktivace Switch Service, vložení peněz nebo provedení platby. Po splnění přijde doporučujícímu notifikace a odměnu je nutné aktivně nárokovat tlačítkem Claim Reward. |
| Kanál | app; link |
| Limity | max. 5 pozvaných za kalendářní měsíc — 1 z každé záložky (Home, Cards, Savings, Stocks, Crypto) |
| Lhůty | nepodařilo se ověřit |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučující = uživatel bunq; pozvaný = nový uživatel (zvaný přes telefonní číslo v aplikaci) |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `reward_referrer`: nízká, `reward_referee`: nízká

**Poznámky.** NEJŠIRŠÍ PALETA FOREM ODMĚNY v přehledu — jako jediný subjekt nabízí krypto a zlomky akcií vedle hotovosti, fyzické karty a bonusového úroku; proto reward_type 'other'. Limit je konstruován zcela odlišně od všech ostatních: ne „X doporučených celkem“, ale 1 pozvaný z KAŽDÉ z pěti záložek aplikace za měsíc, což uživatele tlačí k používání všech produktů banky, ne jen účtu. Odměna se nepřipisuje automaticky — je nutné ji ručně nárokovat (Claim Reward), což je mechanika, která část odměn nechá propadnout. Konkrétní částky nejsou veřejné, závisí na nabídce v aplikaci — bez přístupu do aplikace neověřitelné.

#### Curve

| Pole | Hodnota |
|---|---|
| Program | Refer a friend |
| Status | aktivní |
| Produkty | platební karta / agregátor karet |
| Odměna doporučující | ROZPOR MEZI ZDROJI: oficiální podmínky uvádějí 1 % cashback na 30 dnů navíc za každého doporučeného; sekundární zdroje uvádějí 50 GBP v Curve Cash za doporučeného |
| Odměna doporučený | nepodařilo se spolehlivě ověřit; sekundární zdroje uvádějí 50 GBP v Curve Cash |
| Typ odměny | other |
| Podmínky | Doporučený musí podat žádost, dokončit onboarding a provést alespoň 1 nákup kartou Curve. Odměny se za více doporučených sčítají (3 doporučení = 1 % cashback po 90 dnů). |
| Kanál | link; code |
| Limity | dle sekundárních zdrojů max. 5 doporučených za období nabídky (až 250 GBP v Curve Cash); dle oficiálních podmínek limit neuveden |
| Lhůty | 1 % cashback navazuje na úvodních 6 měsíců cashbacku, poté +30 dnů za každé doporučení |
| Platnost kampaně | — |
| Kdo se může účastnit | nepodařilo se ověřit dostupnost a podmínky pro české klienty |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `reward_referrer`: nízká, `reward_referee`: nízká, `limits`: nízká

**Poznámky.** ROZPOR NEROZŘEŠEN. Dvě neslučitelné mechaniky ve zdrojích: prodloužení 1% cashbacku o 30 dnů vs. 50 GBP v Curve Cash. Pravděpodobně jde o dvě různé kampaně v čase, ale bez přístupu k T&C to nelze rozhodnout, proto žádnou z nich neuvádím jako číselnou hodnotu. Odměna ve formě PRODLOUŽENÍ CASHBACKU je v přehledu unikátní — hodnota pro doporučujícího závisí na jeho vlastní útratě, takže program odměňuje nejvíc ty, kdo kartu stejně používají nejvíc. Sekundární zdroje jsou převážně affiliate weby sbírající referral kódy, tedy strana se zájmem na nadsazení odměny — zacházet s nimi opatrně. Dostupnost Curve pro české klienty a měna odměny neověřena.

#### N26

| Pole | Hodnota |
|---|---|
| Program | Refer a Friend Program |
| Status | aktivní |
| Produkty | osobní účet |
| Odměna doporučující | výše bonusu se liší podle kampaně; celkový strop 1 500 EUR na zákazníka |
| Odměna doporučený | nepodařilo se ověřit, zda pozvaný dostává odměnu |
| Typ odměny | cash |
| Podmínky | Pozvaný musí provést první platbu kartou (nákup v obchodě nebo online, PayPal vyloučen) v hodnotě alespoň rovné výši referral bonusu. Program lze používat pouze pro osobní, nekomerční účely. |
| Kanál | link; app |
| Limity | max. 10 referral bonusů na uživatele; celkem max. 1 500 EUR na zákazníka |
| Lhůty | připsání odměny může trvat až 60 dnů; zahájená, ale nedokončená doporučení se po roce mažou |
| Platnost kampaně | — |
| Kdo se může účastnit | doporučující = stávající zákazník N26; pozvaný = nový uživatel |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `reward_referrer`: nízká, `reward_referee`: nízká

**Poznámky.** NEJVYŠŠÍ STROP ODMĚNY V CELÉM PŘEHLEDU: 1 500 EUR (řádově 37 000 Kč) proti 26 000 Kč u mBank — pozor ale, že jde o strop, ne o reálně dosahovanou částku, a jednotková odměna za doporučeného je neznámá. Dvě mechaniky jinde nevídané: (1) podmínka, že pozvaný musí zaplatit kartou ALESPOŇ TOLIK, KOLIK ČINÍ BONUS — odměna si tak sama určuje kvalifikační práh, (2) bonus může být vyplacen v AKCIÍCH nebo zlomcích akcií místo v eurech, navázaný na N26 Brokerservice. Nalezené T&C jsou německá a italská verze; česká varianta neexistuje, N26 pro ČR nemá lokalizované podmínky. Částka ponechána v EUR bez přepočtu (rozhodnutí D3).

#### Revolut

| Pole | Hodnota |
|---|---|
| Program | Doporučení (Refer a friend) |
| Status | aktivní |
| Produkty | osobní účet; Revolut Pro (samostatný program); Kids & Teens (samostatný program) |
| Odměna doporučující | výše se mění podle kampaně; sekundární zdroj uvádí až 1 500 Kč |
| Odměna doporučený | dle podmínek odměnu dostává POUZE doporučující, ne pozvaný |
| Typ odměny | cash |
| Podmínky | Doporučující musí mít aktivní osobní účet po celou dobu trvání akce i v okamžiku připsání odměny. Pozvaný si musí otevřít osobní účet přes odkaz pro doporučení a provést kroky uvedené v pozvánce v určeném časovém rámci. Odměna nebude vyplacena nebo bude zrušena, pokud pozvaný zruší účet do 14 dnů od otevření. |
| Kanál | link; app |
| Limity | max. 5 pozvaných osob v rámci jedné kampaně |
| Lhůty | kroky musí být dokončeny před termínem uvedeným v pozvánce; clawback při zrušení účtu pozvaným do 14 dnů |
| Platnost kampaně | ? – 2026-03-31 (Sekundární zdroj uvádí konec aktuální akce k 31. 3. 2026; k datu researche (2026-09-15) je toto datum v minulosti, takže buď běží navazující kampaň, nebo je údaj neaktuální. Neověřeno.) |
| Kdo se může účastnit | doporučující = zákazník Revolutu s aktivním osobním účtem; pozvaný = nový uživatel |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `reward_referrer`: nízká, `campaign_period`: nízká

**Poznámky.** STRUKTURÁLNĚ ODLIŠNÝ OD ČESKÝCH BANK: podle podmínek odměnu dostává POUZE doporučující — chybí symetrie, která je u českých bank pravidlem (Air Bank 500/500, ČS 6000/1200, Creditas 500/250). Revolut jako jediný subjekt v přehledu provozuje TŘI oddělené referral programy s vlastními T&C (osobní, Pro, Kids & Teens). Výše odměny není v T&C fixovaná, mění se kampaň od kampaně a je vázaná na konkrétní pozvánku — proto reward_referrer_value = null. Explicitní clawback (zrušení účtu do 14 dnů) je v přehledu ojedinělý; české banky takovou klauzuli veřejně nekomunikují.

#### Skip Pay

| Pole | Hodnota |
|---|---|
| Program | Doporučte Skip Pay |
| Status | aktivní |
| Produkty | odložené platby (balíček MAXI) |
| Odměna doporučující | 500 Kč za každý nově ověřený balíček MAXI přes odkaz, celkem až 5 000 Kč |
| Odměna doporučený | sleva 500 Kč (voucher do e-mailu) |
| Typ odměny | voucher |
| Podmínky | Odkaz lze sdílet neomezeně často. Odměna 500 Kč náleží za každý nově ověřený balíček MAXI pořízený přes odkaz doporučujícího. Doporučený dostane slevu 500 Kč e-mailem a uplatní ji při platbě objednávky nebo měsíčního vyúčtování v minimální hodnotě 501 Kč v Zákaznické zóně. |
| Kanál | link |
| Limity | max. 10 doporučení, tj. až 5 000 Kč |
| Lhůty | nepodařilo se ověřit |
| Platnost kampaně | — |
| Kdo se může účastnit | nepodařilo se ověřit |
| Confidence | střední |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `timing`: nízká, `eligibility`: nízká

**Poznámky.** ASYMETRIE FORMY ODMĚNY: doporučující dostává 500 Kč, ale doporučený jen SLEVOVÝ VOUCHER 500 Kč použitelný na objednávku od 501 Kč — tedy nutí k další útratě a je podmíněně hodnotný, ne hotovost. Proto reward_type 'voucher', nikoli 'cash'. Skip Pay patří do skupiny ČSOB, takže jde fakticky o jediný MGM program v této skupině, který se podařilo doložit (u samotné ČSOB zůstává nejasný). Struktura 500 Kč × 10 = 5 000 Kč je totožná s Air Bank, ale mechanika je vázaná na produkt odložených plateb, ne na běžný účet.

#### Twisto

| Pole | Hodnota |
|---|---|
| Program | Promo kódy / doporučení |
| Status | neověřeno |
| Produkty | odložené platby; Twisto účet; karta |
| Odměna doporučující | nejednoznačné: zdroje uvádějí 50 Kč za doporučeného, jinde 300–500 Kč pouze pro vybrané zákazníky |
| Odměna doporučený | 500 Kč po registraci s promo kódem (dle sekundárních zdrojů) |
| Typ odměny | cash |
| Podmínky | Nepodařilo se ověřit. Zdroje shodně uvádějí, že nejde o plošnou kampaň — promo kódy jsou dostupné jen vybraným zákazníkům z portfolia. |
| Kanál | code |
| Limity | nepodařilo se ověřit |
| Lhůty | nepodařilo se ověřit |
| Platnost kampaně | — |
| Kdo se může účastnit | pouze vybraní zákazníci Twista, neplošně |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

**Poznámky.** NEJDE O STANDARDNÍ MGM PROGRAM. Zdroje se shodují jen v tom, že promo kódy nejsou plošné a dostávají je pouze vybraní zákazníci — tím se Twisto vymyká definici otevřeného MGM programu, kde může doporučovat každý klient. Uváděné částky si přímo odporují (50 Kč vs. 300–500 Kč), a část zdrojů jsou recenzní weby s vlastním affiliate kódem v textu, tedy motivované k nadsazení. Žádnou částku proto neuvádím jako fakt. Status 'unknown' místo 'active': není jisté, že program v otevřené podobě vůbec existuje.

#### Wise

| Pole | Hodnota |
|---|---|
| Program | Invite program / Referral program |
| Status | aktivní |
| Produkty | mezinárodní převody; platební karta |
| Odměna doporučující | závisí na zemi; typicky cca 75 GBP po 3 pozvaných, kteří provedou kvalifikovaný převod (obvykle ≥ 200 GBP každý) |
| Odměna doporučený | převod zdarma na první mezinárodní platbu do stanoveného limitu (typicky cca 500 GBP) nebo karta zdarma — podle země |
| Typ odměny | cash |
| Podmínky | Doporučující musí mít ověřený účet v dobrém stavu a mít za sebou alespoň jeden osobní převod. Pozvaný musí být nový uživatel, zaregistrovat se přes odkaz, projít ověřením totožnosti a splnit požadavek na objem převodu nebo útratu kartou. Odměnu lze uplatnit do jednoho roku od kvalifikace, poté propadá. |
| Kanál | link |
| Limity | nepodařilo se ověřit pro ČR |
| Lhůty | odměnu je nutné uplatnit do 1 roku od kvalifikace |
| Platnost kampaně | — |
| Kdo se může účastnit | geografická omezení — v některých zemích je místo hotovostního bonusu pouze sleva na poplatku; konkrétní varianta platná pro české klienty neověřena |
| Confidence | nízká |
| Ověřeno dne | 2026-09-15 |

*Nižší jistota u jednotlivých polí:* `reward_referrer`: nízká, `reward_referee`: nízká

**Poznámky.** NEJNIŽŠÍ JISTOTA V CELÉM PŘEHLEDU. Wise přiřazuje „invite program“ podle země a nalezené T&C jsou britská verze (wise.com/gb/) — částky v GBP se na české klienty nemusí vztahovat vůbec. Zdroje samy uvádějí, že v některých zemích je místo bonusu jen sleva na poplatku. Číselné hodnoty ponechány v GBP bez přepočtu na CZK (rozhodnutí D3); ODMĚNA PLATNÁ PRO ČESKÉ KLIENTY NENÍ OVĚŘENA a nesmí se z tohoto záznamu vyvozovat. Odměna je prahová (3 pozvaní najednou), ne per-doporučený — to je mezi sledovanými subjekty ojedinělé. Prioritní kandidát na ověření trackerem přes wise.com/cz/.


---

## 4. Historie a trendy

> **Rozsah této sekce je vědomě omezený.** Zadání žádalo časovou osu po ~3 měsících za poslední 3 roky,
> stavěnou na snímcích z Wayback Machine. Ten je v tomto běhu nedostupný (viz sekce 6), takže souvislou
> časovou řadu sestavit nelze. Níže je proto jen to, co je **doložené konkrétním datem a zdrojem** —
> podle zadání „udělej historii, kde máš jistotu dat". Nedatované a fórové zmínky jsem vynechal,
> i když by osu opticky zaplnily.

### Doložené změny

| Datum | Subjekt | Změna | Jistota |
|---|---|---|---|
| 27. 10. 2022 | Max banka | Předčasně ukončila program 500 + 500 Kč za doporučení Neo účtu. Podmínky slibovaly běh **do 31. 3. 2023**; banka využila výhradu o možnosti kdykoli akci ukončit. | střední (Měšec.cz) |
| 1. 10. 2024 | Max banka | Fúze s Bankou CREDITAS — subjekt přestal existovat samostatně. | nízká (pouze fórový zdroj) |
| 30. 1. 2026 | mBank | Začátek aktuální akce „Doporučte mBank" (dle pravidel do 31. 3. 2026). | střední (oficiální PDF) |
| leden 2026 | mBank | Dodatek č. 1 k pravidlům akce. | střední (oficiální PDF) |
| únor 2026 | mBank | Dodatek č. 2 k pravidlům akce. | střední (oficiální PDF) |
| 2026 | mBank | Zvýšení stropu odměny z **10 000 Kč na 26 000 Kč** — nejvýraznější doložený pohyb odměn na trhu. | střední (e15) |
| 2026 | Česká spořitelna | Prodloužení programu „Doporučte George" (až 6 000 Kč) do roku 2026. | střední (e15) |

### Co z toho lze a nelze vyvodit

**Doložitelné:**

1. **Pravidla se mění v řádu týdnů, ne let.** mBank vydala ke stejné kampani dva dodatky během dvou po sobě jdoucích měsíců. To je samo o sobě nejsilnější argument pro tracker — roční ani čtvrtletní kontrola takový pohyb nezachytí.
2. **Deklarovaná platnost kampaně není závazná.** Max banka je doložený případ, kdy banka ukončila program o pět měsíců dříve, než sama avizovala, na základě výhrady ve vlastních podmínkách. Údaje v poli `campaign_period` je proto u všech subjektů nutné číst jako záměr, ne jako závazek.
3. **Na horním konci trhu došlo k eskalaci.** Zvýšení stropu mBank z 10 000 na 26 000 Kč je jediná doložená změna výše odměny v datech a jde o více než zdvojnásobení.

**Nedoložitelné z tohoto běhu** — uvádím explicitně, aby se z mlčení nevyvozoval závěr:

- Zda 500 Kč bylo tržním standardem i před třemi lety, nebo jde o nedávnou konvergenci.
- Kdy přesně jednotlivé banky programy zaváděly a rušily (mimo Max banku).
- Zda gamifikace (milníkové bonusy, drobení po transakcích) je nový jev, nebo tu byla vždy. mBank je dnes jediný takový program v přehledu, ale bez historie nelze říct, jestli jde o trend, nebo o odlehlou hodnotu.
- Zda posun k nehotovostním odměnám (Partners Banka, bunq, Curve) roste, nebo je stabilní.

Tyto otázky zodpoví až tracker po několika měsících běhu — nebo jednorázový doběh přes Wayback Machine, až bude síť dostupná.


---

## 5. Srovnání: banky vs. neobanky

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


---

## 6. Metodika a limity

### Jak data vznikla

Research proběhl **15. 9. 2026** pomocí cílených webových vyhledávání na 21 subjektů ze zadání,
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
UniCredit (10 000 Kč) a zářijové akce Air Bank (500 Kč „na vyzkoušení", kód SVET500).

### Co se konkrétně nepodařilo ověřit

| Subjekt | Co chybí | Proč to vadí |
|---|---|---|
| **ČSOB** | existence a výše MGM odměny | Zdroje si odporují (500 Kč vs. 1 000 Kč) a žádný oficiální dokument k MGM se nenašel — všechna nalezená PDF ČSOB jsou akviziční kampaně. Největší nevyřešená mezera v reportu. |
| **Moneta** | aktuální výše odměny | Program prokazatelně existuje (banka k němu vydává vlastní PDF), ale částku nelze doložit. |
| **Oberbank** | cokoli | Nulový výskyt v českých přehledech. Vedeno jako `unknown`, ne `none` — absence zmínky není důkaz neexistence. |
| **Twisto** | zda jde o otevřený program | Zdroje se shodují jen na tom, že promo kódy nejsou plošné. Částky si odporují (50 Kč vs. 300–500 Kč). |
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


---

## 7. Příloha — kompletní seznam zdrojů

**Air Bank**

- [Pravidla akce Pozvání přátel — doporučující (Air Bank)](https://www.airbank.cz/file-download/pravidla-akce-pozvani-pratel-doporucujici) — T&C, jistota střední, ověřeno 2026-09-15
- [Jak doporučit Air Bank příteli](https://www.airbank.cz/co-vas-nejvic-zajima/jak-doporucit-air-bank-priteli/) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Jak se stát klientem Air Bank na doporučení přítele](https://www.airbank.cz/co-vas-nejvic-zajima/jak-se-stat-klientem-air-bank-na-doporuceni-pritele/) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Banka CREDITAS**

- [Doporučte a získejte (Banka CREDITAS)](https://www2020.creditas.cz/doporucte-a-ziskejte) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Creditas rozdává bonusy za doporučení (Měšec.cz)](https://www.mesec.cz/aktuality/zalozna-creditas-rozdava-financni-bonusy-za-doporuceni/) — sekundární, jistota střední, ověřeno 2026-09-15
- [Za doporučení spořicího účtu nabízí Creditas 500 Kč — akce má háček (e15)](https://www.e15.cz/finexpert/vydelavame/za-doporuceni-sporicicho-uctu-nabizi-creditas-500-korun-akce-ma-ale-jeden-hacek-1352981) — sekundární, jistota střední, ověřeno 2026-09-15

**Česká spořitelna**

- [ČS prodlužuje bonus za doporučení až 6 000 Kč (e15)](https://www.e15.cz/finexpert/banky-a-ucty/ceska-sporitelna-prodlouzila-odmenovani-za-doporuceni-uctu-ziskat-muzete-az-6-000-korun-1430070) — sekundární, jistota střední, ověřeno 2026-09-15
- [Spořitelna dá klientům odměnu až 6000 Kč (Peníze.cz)](https://www.penize.cz/osobni-ucty/480388-sporitelna-da-klientum-odmenu-az-6000-korun-mysli-i-na-novacky) — sekundární, jistota střední, ověřeno 2026-09-15

**ČSOB (vč. Poštovní spořitelny)**

- [Banky vás odmění za doporučení (Peníze.cz)](https://www.penize.cz/osobni-ucty/487348-banky-vas-odmeni-za-doporuceni-prehled-kde-a-jak-si-prilepsite) — sekundární, jistota nízká, ověřeno 2026-09-15
- [Pravidla akce ČSOB podnikatelský účet — AKVIZIČNÍ, ne MGM](https://www.csob.cz/documents/10710/17504789/pravidla-akce-podnikatelsky-ucet-s-odmenou-2000-kc-2026.pdf) — T&C, jistota nízká, ověřeno 2026-09-15

**Fio banka**

- [Banky zkoušejí získat nové klienty odměnou za doporučení (Finparáda)](https://www.finparada.cz/3524-Banky-zkouseji-ziskat-nove-klienty-odmenou-za-doporuceni.aspx) — sekundární, jistota nízká, ověřeno 2026-09-15
- [Fio spouští program odměn za splácení hypoték — NE MGM](https://www.fio.cz/spolecnost-fio/media/tiskove-zpravy/326669-fio-banka-spousti-program-odmen-za-splaceni-hypotek) — tisková zpráva, jistota střední, ověřeno 2026-09-15

**Komerční banka**

- [Bonus až 4 000 Kč pro nové klienty (KB) — AKVIZIČNÍ, ne MGM](https://www.kb.cz/cs/obcane/bonus-az-4-000-kc-pro-nove-klienty) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Které banky dají bonus za sjednání nebo doporučení (Měšec.cz)](https://www.mesec.cz/clanky/ktere-banky-vam-nyni-daji-financni-bonus-za-sjednani-sveho-produktu-nebo-doporuceni-klienta/) — sekundární, jistota střední, ověřeno 2026-09-15

**Max banka**

- [Max banka předčasně ukončila odměny za založení účtu (Měšec.cz)](https://www.mesec.cz/aktuality/max-banka-predcasne-ukoncila-odmeny-za-zalozeni-uctu-puvodne-mela-skoncit-az-v-breznu-2023/) — sekundární, jistota střední, ověřeno 2026-09-15
- [MaxBanka — fúze s Creditas k 1. 10. 2024 (FinExpert fórum)](https://forum.finexpert.e15.cz/viewtopic.php?f=316&p=13347117) — sekundární, jistota nízká, ověřeno 2026-09-15

**mBank**

- [Dodatek č. 2 k Pravidlům akce Doporučte mBank (únor 2026)](https://www.mbank.cz/informace-k-produktum/dokumenty-ke-stazeni/dokumenty/akce/doporucte-mbank_pravidla-unor2026.pdf) — T&C, jistota střední, ověřeno 2026-09-15
- [Dodatek č. 1 k Pravidlům akce Doporučte mBank (leden 2026)](https://www.mbank.cz/informace-k-produktum/dokumenty-ke-stazeni/dokumenty/akce/doporucte-mbank_pravidla-leden2026.pdf) — T&C, jistota střední, ověřeno 2026-09-15
- [Bankovní bonusy v září 2026: až 26 tisíc za doporučení (e15)](https://www.e15.cz/finexpert/banky-a-ucty/bankovni-bonusy-v-zari-2026-az-26-tisic-za-doporuceni-slevy-na-netflix-nebo-cashback-na-jidlo-1435389) — sekundární, jistota střední, ověřeno 2026-09-15
- [Časté dotazy: Odměny za doporučení a založení mKonta](https://www.mbank.cz/blog/post,550,caste-dotazy-odmeny-za-doporuceni-a-zalozeni-mkonta.html) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Moneta Money Bank**

- [Dokumenty ke stažení — Účty (Moneta), obsahuje PDF podmínek kampaně](https://www.moneta.cz/dokumenty-ke-stazeni/osobni/ucty) — T&C, jistota nízká, ověřeno 2026-09-15
- [Program Odměny (Moneta) — cashback u obchodníků, NE MGM](https://www.moneta.cz/ucty-a-karty/program-odmeny) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Oberbank**

- [Oberbank ČR — web banky](https://www.oberbank.cz/) — oficiální marketing, jistota nízká, ověřeno 2026-09-15

**Partners Banka**

- [Pravidla klientské akce Doporuč a získej (Partners Banka, PDF)](https://www.partnersbanka.cz/userfiles/podminky-doporuc-a-ziskej-5e249b95.pdf) — T&C, jistota střední, ověřeno 2026-09-15
- [Úroky u spořicího účtu (Partners Banka)](https://www.partnersbanka.cz/urok-sporici-ucet) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Bankovní bonusy v září 2026 (e15)](https://www.e15.cz/finexpert/banky-a-ucty/bankovni-bonusy-v-zari-2026-az-26-tisic-za-doporuceni-slevy-na-netflix-nebo-cashback-na-jidlo-1435389) — sekundární, jistota střední, ověřeno 2026-09-15

**Raiffeisenbank**

- [Podmínky akce Odměna za doporučení (Raiffeisenbank)](https://www.rb.cz/podpora/podminky-akci/odmena-za-doporuceni) — T&C, jistota střední, ověřeno 2026-09-15
- [Pravidla reklamní akce Finanční odměna za doporučení (PDF)](https://www.rb.cz/attachments/pi/pravidla-reklamni-akce/pravidla-reklamni-akce-financni-odmena-za-doporuceni.pdf) — T&C, jistota střední, ověřeno 2026-09-15
- [Pravidla reklamní akce Odměna za doporučení (PDF)](https://www.rb.cz/attachments/pi/pravidla-reklamni-akce/pravidla-reklamni-akce-odmena-za-doporuceni-final.pdf) — T&C, jistota střední, ověřeno 2026-09-15
- [Odměna za doporučení (Raiffeisenbank)](https://www.rb.cz/osobni/ucty/doporuceni/odmena-za-doporuceni) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Trinity Bank**

- [Prémiový klub — podmínky (Trinity Bank) — věrnostní, ne MGM](https://www.trinitybank.cz/download/391) — T&C, jistota nízká, ověřeno 2026-09-15
- [Pravidla akce Narozeninový bonus (Trinity Bank) — ne MGM](https://www.trinitybank.cz/file/1196) — T&C, jistota nízká, ověřeno 2026-09-15
- [Trinity Bank — dotaz na program doporučení (FinExpert fórum)](https://forum.finexpert.e15.cz/viewtopic.php?style=5&f=316&t=1296326&p=13670233) — sekundární, jistota nízká, ověřeno 2026-09-15

**UniCredit Bank**

- [Tisková zpráva UniCredit Bank — odměna až 1 700 Kč](https://www.investujeme.cz/tiskove-zpravy/doporucte-produkty-unicredit-bank-svym-pratelum-a-ziskejte-odmenu-az-1700-korun-za-kazdeho-doporuceneho-klienta/) — tisková zpráva, jistota střední, ověřeno 2026-09-15
- [Za doporučení až 3 % z platby kartou (Měšec.cz)](https://www.mesec.cz/clanky/za-doporuceni-noveho-klienta-az-3-z-platby-kartou-unicredit-bank-rozdava-bonusy/) — sekundární, jistota nízká, ověřeno 2026-09-15

**bunq**

- [Refer a friend and earn rewards (bunq)](https://www.bunq.com/personal-account/banking-features/refer-a-friend) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [How can I invite my friends to join bunq (bunq Help)](https://help.bunq.com/articles/how-can-i-invite-my-friends-to-join-bunq) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Curve**

- [Referral promo terms (Curve)](https://www.curve.com/legal/referral-promo-terms/) — T&C, jistota nízká, ověřeno 2026-09-15
- [Curve Referral Rewards 2026 (referralcodes.com)](https://referralcodes.com/shop/curve-referral-codes) — sekundární, jistota nízká, ověřeno 2026-09-15

**N26**

- [T&C of N26 Bank SE for the Refer a Friend Program (v3.0, DE)](https://docs.n26.com/legal/01+DE/01+Account/en/15account-terms-and-conditions-friend-referral-3.0-en.pdf) — T&C, jistota střední, ověřeno 2026-09-15
- [Referral Bonus Criteria (N26 Support)](https://support.n26.com/en-de/app-and-features/friend-referral/why-hasnt-my-referral-bonus-arrived) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Invite friends to join N26](https://n26.com/en-eu/invite-friends) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Revolut**

- [Podmínky pro doporučení (Revolut Česko)](https://www.revolut.com/cs-CZ/legal/referrals-terms/) — T&C, jistota střední, ověřeno 2026-09-15
- [Podmínky doporučení Revolut Pro](https://www.revolut.com/cs-CZ/legal/referrals-revpro-terms/) — T&C, jistota střední, ověřeno 2026-09-15
- [Kids & Teens Referrals Promotion (Revolut)](https://www.revolut.com/cs-CZ/legal/u18referrals/) — T&C, jistota střední, ověřeno 2026-09-15
- [Jaké jsou požadavky pro získání odměny za doporučení](https://help.revolut.com/cs-CZ/help/referrals/other/what-are-the-requirements-to-get-my-referral-reward/) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Bonus u Revolutu za doporučení (Inteligentnisvet.cz)](https://inteligentnisvet.cz/clanky/ziskejte-bonus-1250-kc-u-revolutu-jak-ziskat-odmenu-za-doporuceni) — sekundární, jistota nízká, ověřeno 2026-09-15

**Skip Pay**

- [Doporučte Skip Pay a získejte až 5 000 Kč](https://skippay.cz/doporucte-nas) — oficiální marketing, jistota střední, ověřeno 2026-09-15
- [Kolik můžu za doporučení celkem získat (Skip Pay FAQ)](https://skippay.cz/caste-dotazy/dalsi-caste-otazky/kolik-muzu-za-doporuceni-celkem-ziskat) — oficiální marketing, jistota střední, ověřeno 2026-09-15

**Twisto**

- [Twisto účet (Twisto)](https://www.twisto.cz/vychytavky/twistoucet/) — oficiální marketing, jistota nízká, ověřeno 2026-09-15
- [Twisto recenze 2026 — promo kód 500 Kč](https://www.moneyspot.cz/twisto-recenze/) — sekundární, jistota nízká, ověřeno 2026-09-15
- [Twisto recenze + bonus 500 Kč (DuoFinance)](https://www.duofinance.cz/recenze-twisto) — sekundární, jistota nízká, ověřeno 2026-09-15

**Wise**

- [Wise Referral Program terms (GB verze)](https://wise.com/gb/legal/referral-terms) — T&C, jistota nízká, ověřeno 2026-09-15
- [How do invite programs work (Wise Help)](https://wise.com/help/articles/2Q37yOkW1DmaMo1oKBWa5Z/how-do-invite-programs-work) — oficiální marketing, jistota střední, ověřeno 2026-09-15
