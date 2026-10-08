const pptxgen = require("pptxgenjs");
const { applyTheme } = require("/root/.claude/skills/synced/b9db6ca4-99b0-4ace-aa3e-32b13975ee3c_8a8958f2-2783-4068-a9b8-b5f00799a607/pptx/scripts/apply_theme.js");

const OUT = process.argv[2] || "deck.pptx";

// ---------- THEME (HBR style, same as v2 brief) ----------
const THEME = {
  name: "HBR SB Loyalty",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "111111", lt1: "FFFFFF", dk2: "6B6B6B", lt2: "F4F1EC",
    accent1: "B5121B", // ČS red
    accent2: "1F3A5F", // CZ competitors
    accent3: "4F6F5A", // EU benchmarks
    accent4: "8A8A8A", // other
    accent5: "D9D9D9", // lines
    accent6: "9A6B2F", // world benchmarks (bronze)
    hlink: "B5121B", folHlink: "6B6B6B",
  },
};
const H = THEME.colors;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.33 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.author = "Research SB v2";
pres.title = "Věrnostní programy pro podnikatele a firmy";
const C = pres.SchemeColor;

const W = 13.33, M = 0.6, CW = W - 2 * M;

// ---------- LAYOUTS ----------
pres.defineSlideMaster({
  title: "TITLE", background: { color: H.lt1 },
  objects: [
    { rect: { x: 0, y: 0, w: 0.35, h: 7.5, fill: { color: H.lt2 } } },
    { placeholder: { options: { name: "kicker", type: "body", x: M + 0.2, y: 1.1, w: CW, h: 0.4, fontSize: 12, color: C.accent1, charSpacing: 3, bold: true, margin: 0 }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: M + 0.2, y: 1.6, w: CW - 0.5, h: 2.4, fontSize: 40, bold: true, color: C.text1, valign: "top", margin: 0, align: "left" }, text: "" } },
    { placeholder: { options: { name: "sub", type: "body", x: M + 0.2, y: 4.2, w: CW - 1, h: 1.2, fontSize: 18, color: C.text2, valign: "top", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "meta", type: "body", x: M + 0.2, y: 6.3, w: CW - 1, h: 0.6, fontSize: 12, color: C.text2, valign: "top", margin: 0 }, text: "" } },
  ],
});
pres.defineSlideMaster({
  title: "SECTION", background: { color: H.lt2 },
  objects: [
    { placeholder: { options: { name: "kicker", type: "body", x: M, y: 2.3, w: CW, h: 0.4, fontSize: 12, color: C.accent1, charSpacing: 3, bold: true, margin: 0 }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 2.8, w: CW - 1, h: 1.6, fontSize: 30, bold: true, color: C.text1, valign: "top", margin: 0, align: "left" }, text: "" } },
    { placeholder: { options: { name: "sub", type: "body", x: M, y: 4.6, w: CW - 2, h: 1.4, fontSize: 16, color: C.text2, valign: "top", margin: 0 }, text: "" } },
    { slideNumber: { x: 12.3, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: C.text2, align: "right" } },
  ],
});
pres.defineSlideMaster({
  title: "CONTENT", background: { color: H.lt1 },
  objects: [
    { placeholder: { options: { name: "kicker", type: "body", x: M, y: 0.3, w: 9, h: 0.3, fontSize: 10, color: C.text2, charSpacing: 2, bold: true, margin: 0 }, text: "" } },
    { placeholder: { options: { name: "title", type: "title", x: M, y: 0.62, w: CW, h: 1.0, fontSize: 22, bold: true, color: C.text1, valign: "top", margin: 0, align: "left" }, text: "" } },
    { placeholder: { options: { name: "sub", type: "body", x: M, y: 1.62, w: CW, h: 0.45, fontSize: 13, color: C.text2, valign: "top", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "source", type: "body", x: M, y: 7.0, w: 11.4, h: 0.3, fontSize: 9, color: C.text2, valign: "middle", margin: 0 }, text: "" } },
    { slideNumber: { x: 12.3, y: 7.0, w: 0.6, h: 0.3, fontSize: 10, color: C.text2, align: "right" } },
  ],
});

// ---------- helpers ----------
const LINE = { type: "solid", pt: 0.5, color: H.accent5 };
const NONE = { type: "none" };
const HB = [LINE, NONE, LINE, NONE]; // horizontal lines only
let n = 0;
function content(kicker, title, sub, source, section) {
  const s = pres.addSlide({ masterName: "CONTENT", sectionTitle: section });
  s.addText(kicker, { placeholder: "kicker" });
  s.addText(title, { placeholder: "title" });
  if (sub) s.addText(sub, { placeholder: "sub" });
  if (source) s.addText("Zdroj: " + source, { placeholder: "source" });
  return s;
}
function tag(s, x, y, label, w) {
  // certainty chip
  const styles = {
    FACT: { fill: H.dk1, color: H.lt1, line: H.dk1, dash: "solid" },
    EST: { fill: H.lt1, color: H.dk1, line: H.dk1, dash: "dash" },
    STALE: { fill: H.lt2, color: H.dk1, line: H.dk2, dash: "sysDot" },
    CLAIM: { fill: H.lt1, color: H.dk2, line: H.accent5, dash: "solid" },
    "DATA GAP": { fill: H.lt1, color: H.accent1, line: H.accent1, dash: "dash" },
  };
  const key = Object.keys(styles).find(k => label.startsWith(k)) || "CLAIM";
  const st = styles[key];
  s.addText(label, { x, y, w: w || 0.95, h: 0.26, fontSize: 8, bold: true, color: st.color, align: "center", valign: "middle",
    fill: { color: st.fill }, line: { color: st.line, width: 0.75, dashType: st.dash }, margin: 0, isTextBox: true, objectName: "tag " + label, italic: key === "CLAIM" });
}
function legend(s, x, y) {
  const labels = ["FACT", "EST", "STALE", "CLAIM", "DATA GAP"];
  labels.forEach((l, i) => tag(s, x + i * 1.05, y, l));
}
function card(s, x, y, w, h, head, body, opts = {}) {
  const fill = opts.fill || H.lt2;
  s.addShape(pres.ShapeType.rect, { x, y, w, h, fill: { color: fill }, line: { color: fill, width: 0 }, objectName: "card " + head });
  const two = head.length > (w - 0.4) * 10;
  const off = two ? 0.98 : 0.62;
  s.addText(head, { x: x + 0.2, y: y + 0.15, w: w - 0.4, h: two ? 0.8 : 0.45, fontSize: opts.headSize || 14, bold: true, color: opts.headColor || C.text1, margin: 0, isTextBox: true, valign: "top", fontFace: "Cambria" });
  s.addText(body, { x: x + 0.2, y: y + off, w: w - 0.4, h: h - off - 0.13, fontSize: opts.bodySize || 11.5, color: C.text1, margin: 0, isTextBox: true, valign: "top", paraSpaceAfter: 4 });
}
function bullets(items, size) {
  return items.map((t, i) => ({ text: t, options: { bullet: { indent: 12 }, breakLine: i < items.length - 1, fontSize: size || 12, paraSpaceAfter: 5 } }));
}
function big(s, x, y, w, num, label, color) {
  s.addText(num, { x, y, w, h: 1.3, fontSize: 60, bold: true, color: color || C.accent1, margin: 0, isTextBox: true, fontFace: "Cambria", valign: "bottom" });
  s.addText(label, { x, y: y + 1.35, w, h: 0.7, fontSize: 11.5, color: C.text2, margin: 0, isTextBox: true, valign: "top" });
}
function table(s, rows, opts) {
  const o = Object.assign({ x: M, y: 2.2, w: CW, fontSize: 11, border: HB, fontFace: "Calibri", color: H.dk1, valign: "middle", margin: [3, 5, 3, 5], autoPage: false }, opts);
  s.addTable(rows, o);
}
function hdr(cells) { return cells.map(t => ({ text: t, options: { bold: true, color: H.dk2, fontSize: 10 } })); }
function csRow(cells, size) { return cells.map(t => (typeof t === "string" ? { text: t, options: { fill: { color: H.lt2 }, bold: true, fontSize: size } } : Object.assign({ options: {} }, t, { options: Object.assign({ fill: { color: H.lt2 }, bold: true, fontSize: size }, t.options) }))); }
const chartBase = {
  chartColors: [H.accent2], showLegend: false, showValue: true, dataLabelPosition: "outEnd", dataLabelFontSize: 10, dataLabelColor: H.dk1, dataLabelFontFace: "+mn-lt",
  catAxisLabelColor: H.dk1, catAxisLabelFontSize: 10, catAxisLabelFontFace: "+mn-lt", valAxisLabelColor: H.dk2, valAxisLabelFontSize: 9, valAxisLabelFontFace: "+mn-lt",
  valGridLine: { color: H.accent5, size: 0.5 }, catGridLine: { style: "none" }, catAxisLineShow: false, valAxisLineShow: false, showTitle: false,
};

// =====================================================================
// ČÁST A – EXECUTIVE SUMMARY
// =====================================================================
pres.addSection({ title: "A · Executive summary" });

// A01 Title
{
  const s = pres.addSlide({ masterName: "TITLE", sectionTitle: "A · Executive summary" });
  s.addText("VĚRNOSTNÍ PROGRAMY PRO PODNIKATELE A FIRMY · ČR · EVROPA · SVĚT", { placeholder: "kicker" });
  s.addText("Existují věrnostní programy i pro firemní svět – a co z toho plyne pro Českou spořitelnu?", { placeholder: "title" });
  s.addText("Část A: executive summary (A01–A08) · Část B: detail (B01–B22) · Navazuje na deep dive v2 (2. 10. 2026) a na BP3, BP4, BP5 a BB2", { placeholder: "sub" });
  s.addText("Praha, 8. října 2026 · 125 programů v databázi · 151 vyhledávání · každé číslo nese značku jistoty (FACT / EST / STALE / CLAIM / DATA GAP) · nabídka bank jen ze zdrojů 06/2026+, starší = STALE", { placeholder: "meta" });
}

// A02 Answer by segment
{
  const s = content("A02 · ODPOVĚĎ", "Ano, věrnostní programy existují i pro firmy – ale jen dole na velikostní škále. S velikostí firmy se mění v rebate, tier a pricing", "Jedna odpověď pro tři segmenty. Vzorek: 125 záznamů ze 4 workstreamů (ČR, Evropa, svět, corporate).", "DB 10_vernostni_programy_db.csv · Allica KPI, BofA FAQ 2026, VÚB štatút 1. 7. 2026, GSA SmartPay FY2025 · FACT / EST / STALE", "A · Executive summary");
  const w = (CW - 0.6) / 3, y = 2.3, h = 4.3;
  card(s, M, y, w, h, "FOP / mikro – ANO", bullets([
    "Retailové mechaniky na podnikatelské kartě nebo účtu: cashback 0,1–1,5 % v EU, 1,5–2 % flat v USA, body, nabídky obchodníků v aplikaci",
    "N26 Business 0,1 % / 0,5 % [STALE], bunq 0,5–1 % [STALE], Chase Ink Unlimited 1,5 % [FACT]",
    "U neobank roste cashback s placeným tarifem – financuje ho poplatek klienta",
    "26 programů v Evropě a 27 ve světě otevřených podnikatelům",
  ]), { headColor: C.accent3 });
  card(s, M + w + 0.3, y, w, h, "SME – ČÁSTEČNĚ", bullets([
    "Cashback a body zůstávají, ale podmiňuje je vztah: zůstatek, úvěr, stáří firmy",
    "Allica (UK): 1 % / 1,5 % jen pro firmy 12+ měsíců se zůstatkem 50 000 GBP+ nebo úvěrem [FACT, STALE]",
    "BofA Preferred Rewards for Business: tiery 20 / 50 / 100 tis. USD [FACT 2026]",
    "VÚB (SK): Money back jen ke kreditní kartě s úvěrovým limitem, od 1. 7. 2026 [FACT]",
  ]), { headColor: C.accent2 });
  card(s, M + 2 * (w + 0.3), y, w, h, "CORPORATE – NE", bullets([
    "Bodový program pro velké korporace se v rešerši nenašel",
    "Loajalitu nese smluvní rebate z firemních karet podle objemu a rychlosti úhrady, earnings credit na zůstatky, relationship pricing a RM",
    "GSA SmartPay FY2025: 471 mil. USD refundů z útraty 39,4 mld. USD [FACT] = 1,20 % [EST]",
    "Emirates Business Rewards míří výslovně na firmy bez korporátní cestovní smlouvy [STALE]",
  ]), { headColor: C.accent6 });
}

// A03 Five findings
{
  const s = content("A03 · PĚT HLAVNÍCH ZJIŠTĚNÍ", "ČR nemá žádný ucelený program pro podnikatele, podnikatelská karta nese až 10× vyšší interchange a kauzální důkaz o retenci chybí", null, "L2–L5 rešerše 6. 10. 2026 · IFR 2015/751 čl. 1 odst. 3 písm. a) · Mastercard ČR intracountry 03/2022 · J.D. Power 12/2025", "A · Executive summary");
  const rows = [hdr(["#", "Zjištění", "Číslo", "Značka"])];
  const data = [
    ["1", "Česká banka s uceleným programem pro podnikatele neexistuje; trh se v 2026 stahuje", "1 % cashback jen KB a MONETA; mBank na pozvání; Air Bank ukončila k 30. 6. 2026", "FACT / STALE"],
    ["2", "Retailové programy podnikatelské karty vylučují a tlačí FOP k osobní kartě", "SLSP Moneyback vylučuje podnikatelské debetní karty; ČS Moneyback „soukromá karta“; výjimka MONETA Odměny (FOP ano)", "FACT / CLAIM / DATA GAP"],
    ["3", "Ekonomika je silná: firemní karty nepodléhají stropům IFR", "Mastercard Corporate ČR 2,10 % vs. strop 0,20 % = 10,5×; obchodníci 05/2026 žádají zastropování", "FACT / STALE / EST"],
    ["4", "Vrstva financovaná obchodníky je hotová a běží i v CEE", "Mastercard Business Savings/Bonus: NatWest ~1 mil. karet, bunq 5 zemí, OTP HU, Intesa RS; dostupnost v ČR nejasná", "FACT / STALE / DATA GAP"],
    ["5", "Kauzální důkaz, že program zvyšuje retenci SME, chybí", "J.D. Power: „rewards earning“ 6. ze 7 dimenzí (N = 3 728); McKinsey: důvody změny banky jsou digitál, servis, úvěr", "FACT"],
  ];
  data.forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { bold: i === 1, fontSize: 11.5 } }))));
  table(s, rows, { y: 1.85, colW: [0.4, 4.6, 5.6, 1.53], rowH: 0.78 });
  legend(s, M, 6.55);
}

// A04 ČR position
{
  const s = content("A04 · ČESKÁ REPUBLIKA", "Z 12 českých bank dává podnikatelům trvalou odměnu pět a žádná nemá tier; Česká spořitelna má jen slevy financované Visou", "Inventura 12 bank + 8 nebankovních B2B programů (DB CZ-01 až CZ-37).", "kb.cz, moneta.cz (podmínky Odměn 22. 6. 2025), mbank.cz (03/2026), e15.cz (Air Bank), csas.cz, makro.cz · FACT / STALE / DATA GAP", "A · Executive summary");
  big(s, M, 2.15, 3.2, "0", "bank v ČR s tierovým nebo vztahovým programem pro podnikatele [FACT – nenalezeno u 12 bank]");
  big(s, M, 4.3, 3.2, "1 %", "typický cashback na podnikatelské kreditní kartě (KB do 31. 12. 2026, MONETA bez stropu) [FACT / STALE]", C.accent2);
  const rows = [hdr(["Banka", "Program pro podnikatele", "Retail program otevřený podnikatelům?", "Stav"])];
  const d = [
    ["Česká spořitelna", "Jen „Benefity pro firmy“ – slevy Visa Business (Bolt, EasyPark, foodora, wflow)", "Odměny / Moneyback: podnikatelská karta nezmíněna; článek uvádí soukromou kartu", "nemá vlastní"],
    ["KB", "Kreditní karta Business 1 % zpět, garance do 31. 12. 2026", "„Klub věrnosti“ jen v článku", "cashback"],
    ["ČSOB", "Pojištění k podnikatelským kartám", "Svět odměn ukončen 12/2024; Kate Coins nejasné", "nemá"],
    ["MONETA", "Business Card 1 % bez stropu + kampaně", "Program Odměny otevřený FOP vč. karet Business (PO ne)", "nejširší"],
    ["Air Bank", "1 % zpět ukončeno k 30. 6. 2026", "„Odměny za placení“ nejasné", "zrušeno"],
    ["mBank", "1 % zpět 3–12/2026, jen na pozvání", "–", "cílené"],
    ["RB, UCB, Fio, Creditas, Revolut, Wise", "Nenalezeno (Revolut cashback jen USA, Wise jen UK)", "RB a UCB programy jen retail / nejasné", "nemá"],
  ];
  d.forEach((r, i) => rows.push(i === 0 ? csRow(r, 10.5) : r.map(t => ({ text: t, options: { fontSize: 10.5 } }))));
  table(s, rows, { x: 4.3, y: 2.15, w: 8.43, colW: [1.7, 2.6, 2.8, 1.33], rowH: 0.52 });
}

// A05 Economics big number + chart
{
  const s = content("A05 · EKONOMIKA", "Podnikatelská karta nese 10,5× vyšší interchange než osobní debetní karta – proto se 1 % cashback vyplatí jen na ní", "IFR 2015/751 vyjímá commercial karty ze stropů; definice zahrnuje i OSVČ s kartou účtovanou na podnikatelský účet [FACT].", "legislation.gov.uk (IFR čl. 1 a 2), Mastercard ČR intracountry 1. 3. 2022 [STALE], Visa USA IRF 18. 4. 2026, EuroCommerce 22. 5. 2026 [CLAIM] · poměr = EST", "A · Executive summary");
  s.addChart(pres.ChartType.bar, [{ name: "Interchange (%)", labels: ["Spotřebitelská debetní (strop IFR)", "Spotřebitelská kreditní (strop IFR)", "Mastercard BusinessCard intra-EEA [STALE 01/2021]", "Mastercard Corporate ČR [STALE 03/2022]", "Visa USA commercial – spodní [FACT 04/2026]", "Visa USA commercial – horní [FACT 04/2026]"], values: [0.20, 0.30, 1.65, 2.10, 1.75, 2.95] }],
    Object.assign({}, chartBase, { x: M, y: 2.2, w: 7.6, h: 4.5, barDir: "bar", chartColors: [H.accent4, H.accent4, H.accent3, H.accent1, H.accent6, H.accent6], invertedColors: [H.accent4], valAxisMaxVal: 3.5, valAxisMinVal: 0, dataLabelFormatCode: "0.00\" %\"", catAxisLabelFontSize: 9 }));
  big(s, 8.6, 2.2, 4.1, "10,5×", "Mastercard Corporate ČR 2,10 % / strop spotřebitelské debetní karty 0,20 % [EST; vstup STALE 03/2022]");
  s.addText(bullets([
    "Na 10 000 Kč útraty: osobní debetní karta 20 Kč, podnikatelská karta 210 Kč interchange; po 1 % cashbacku (100 Kč) zbývá bance ~110 Kč [EST, před schémovými poplatky]",
    "Převést výdaje FOP z osobní na podnikatelskou kartu má hodnotu samo o sobě – program, který FOP vylučuje, působí proti tomu",
    "Riziko: obchodníci (EuroCommerce 22. 5. 2026) žádají vypuštění výjimky; „přeplatek“ 2025 ≥ 4 mld. EUR [CLAIM]",
  ], 11.5), { x: 8.6, y: 4.4, w: 4.1, h: 2.4, margin: 0, isTextBox: true, valign: "top" });
}

// A06 Benchmarks
{
  const s = content("A06 · EVROPA A SVĚT", "Čtyři přenositelné vzory: vztahový tier (BofA), cashback za vztah (Allica), firemní cashback u VÚB a schémová vrstva (Mastercard)", "Přenositelnost do ČR 1–5. Detail v části B (B07–B13) a v 10_vernostni_programy_cases.md.", "bankofamerica.com FAQ 2026, allica.bank KPI, vub.sk štatút 1. 7. 2026, slsp.sk zveřejnění 1. 7. 2025, natwestgroup.com 05/2024, mastercard.com 01/2025", "A · Executive summary");
  const w = (CW - 0.9) / 4, y = 2.25, h = 4.4;
  card(s, M, y, w, h, "BofA Preferred Rewards for Business · 5/5", bullets(["Tiery podle 3měsíčního zůstatku: 20 / 50 / 100 tis. USD [FACT 2026]", "+25 / 50 / 75 % ke kartovým odměnám, odpuštění poplatků, −0,25 p.b. z úvěru [STALE]", "Zachován i po nahrazení retailového programu (27. 5. 2026) [FACT]", "Financuje vkladová marže"], 11), { headColor: C.accent6, headSize: 12.5 });
  card(s, M + (w + 0.3), y, w, h, "Allica Business Rewards (UK) · 4/5", bullets(["1 % / 1,5 % cashback z karty jen pro firmy 12+ měsíců se zůstatkem 50 000 GBP+ nebo úvěrem [FACT, STALE]", "Klienti účtu 6 000+ → 14 000+ za FY25 [CLAIM]", "Práh 1,5 %: 10 000 GBP (KPI) vs. 4 000 GBP (tisk) – 15 000 GBP nepotvrzeno"], 11), { headColor: C.accent3, headSize: 12.5 });
  card(s, M + 2 * (w + 0.3), y, w, h, "VÚB vs. SLSP (SK) · 5/5", bullets(["VÚB od 1. 7. 2026: Money back pro firemní kreditku Mastercard Business World, FO i PO s úvěrovým limitem [FACT]; ruší pojištění a lounge", "SLSP Moneyback podnikatelské debetní karty vylučuje [FACT 07/2025]", "Konkurent Erste cílí přesně na segment, který Erste vynechává"], 11), { headColor: C.accent3, headSize: 12.5 });
  card(s, M + 3 * (w + 0.3), y, w, h, "Mastercard Business Savings / Bonus · 5/5", bullets(["Automatický cashback od obchodníků, bez registrace; NatWest ~1 mil. debetních karet, 1 000+ nabídek [FACT, STALE 05/2024]", "bunq v NL/DE/FR/ES/IT od 15. 1. 2025 [FACT]; OTP HU, Intesa RS [STALE]", "Rozpočet banky ≈ 0; dostupnost v ČR [DATA GAP]"], 11), { headColor: C.accent3, headSize: 12.5 });
}

// A07 Options
{
  const s = content("A07 · IMPLIKACE PRO ČS", "Pět variant – doporučená architektura je „0 Kč základ → placený tier → vztahový tier“ s cashbackem jen uvnitř tieru", "Vazba na BP3 (daňový pot + tier), BP4 (first account), BP5 (segmentace FOP/PO) a BB2 (0 Kč + pot + tier). Všechny odhady EST se vzorcem v reportu kap. 9.", "Report kap. 9; čísla z v2 (BB2 40–85 mil. Kč/rok, tier 149–299 Kč/měs.) převzata beze změny · EST", "A · Executive summary");
  const rows = [hdr(["#", "Varianta", "Mechanika", "Vazba", "Hrubá ekonomika [EST]", "Doporučení"])];
  const d = [
    ["V1", "Schémová vrstva nabídek pro podnikatelské karty (Visa benefity + Mastercard Business Bonus / Easy Savings pro CZ)", "D (+F)", "BP4, BB2", "Rozpočet odměn ≈ 0 (platí obchodníci); náklad = integrace do George Business", "ANO – quick win 0–6 m"],
    ["V2", "„George Business Preferred“: vztahový tier podle zůstatku + úvěru (BofA / Allica)", "C → booster A, B, F", "BP5, BB2, BB1", "Odpuštěné poplatky + sleva z úvěru (0,25 p.b. z 1 mil. Kč = 2 500 Kč/rok) vs. vkladová marže; prahy z interních dat", "ANO – jádro, 6–18 m"],
    ["V3", "Cashback na podnikatelské kartě podmíněný vztahem (Allica / VÚB)", "A/B s branou C", "BB2, BP3, BP4", "20 tis. klientů × 30 tis. Kč/měs. × 12 × 1 % = 72 mil. Kč nákladu vs. ≈ 151 mil. Kč interchange (2,10 % STALE)", "ANO – jen jako booster uvnitř V2"],
    ["V4", "Placený tier s benefity místo bodů (daňový pot, SaaS, pojištění, vyšší cashback)", "F + A", "BP3, BB2", "Výnos BB2 40–85 mil. Kč/rok; cashback +0,5 p.b. = 20–42 mil. Kč nákladu krytého interchange", "ANO – sloučit s V2"],
    ["V5", "Partnerství s nebankovním B2B programem (letecký, palivový, velkoobchod)", "H co-brand", "BP5", "Náklad bodů nese banka; ekonomika DATA GAP; riziko disintermediace (SAS)", "MONITOROVAT"],
  ];
  d.forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10.5, bold: i === 5, color: i === 5 && t.startsWith("ANO") ? H.accent1 : H.dk1 } }))));
  table(s, rows, { y: 2.2, colW: [0.45, 3.6, 1.3, 1.2, 3.6, 1.98], rowH: 0.74 });
}

// A08 CEO decision
{
  const s = content("A08 · ROZHODNUTÍ PRO CEO", "Tři doporučení a jedno rozhodnutí: zda podnikatelský tier ponese program BB2/BP5 jako jednu cenovou architekturu", null, "Shrnutí pro CEO, report kap. 11", "A · Executive summary");
  s.addShape(pres.ShapeType.rect, { x: M, y: 1.75, w: CW, h: 1.3, fill: { color: H.lt2 }, line: { color: H.lt2, width: 0 }, objectName: "pull quote" });
  s.addText("„Má ČS odměňovat podnikatele za vztah – zůstatek, úvěr, primární účet – místo aby je retailový Moneyback posílal k osobní kartě?“", { x: M + 0.3, y: 1.85, w: CW - 0.6, h: 1.1, fontSize: 20, italic: true, fontFace: "Cambria", color: C.text1, margin: 0, isTextBox: true, valign: "middle" });
  const w = (CW - 0.6) / 3, y = 3.35, h = 2.5;
  card(s, M, y, w, h, "1 · Hned (0–6 m)", bullets(["Otevřít podnikatelským kartám nabídky obchodníků (Visa / Mastercard) a ověřit zapojení do Moneybacku", "Rozpočet odměn ≈ 0 – platí obchodníci", "Ověřit u Mastercardu dostupnost Business Bonus pro CZ"], 11.5), { headColor: C.accent1 });
  card(s, M + w + 0.3, y, w, h, "2 · Do 18 měsíců", bullets(["Vztahový tier George Business podle zůstatku a úvěru (BofA model): odpuštění poplatků, sleva z úvěru, cashback jen v tieru", "Spojit s placeným tierem BB2 (daňový pot + SaaS)", "Kalibrovat prahy na interních datech (Q7 v2)"], 11.5), { headColor: C.accent2 });
  card(s, M + 2 * (w + 0.3), y, w, h, "3 · Nedělat", bullets(["Plošný cashback bez vztahové brány (Air Bank ho zrušila k 30. 6. 2026)", "Bodový program pro korporace – místo něj transparentní relationship pricing (zůstatek kompenzuje poplatky)", "Program postavený jen na commercial interchange (regulační riziko 05/2026)"], 11.5), { headColor: C.accent4 });
  s.addText([{ text: "Co rozhodnout: ", options: { bold: true } }, { text: "(1) zda small business tier bude součástí architektury „0 Kč základ → placený tier → vztahový tier“ (BB2 + BP5); (2) zda ČS přijme regulační riziko interchange u firemních karet. Vstupy: interní data o zůstatcích a útratě FOP na osobních vs. podnikatelských kartách." }], { x: M, y: 6.05, w: CW, h: 0.8, fontSize: 12, color: C.text1, margin: 0, isTextBox: true, valign: "top" });
}

// =====================================================================
// ČÁST B – DETAIL
// =====================================================================
pres.addSection({ title: "B · Detail" });
{
  const s = pres.addSlide({ masterName: "SECTION", sectionTitle: "B · Detail" });
  s.addText("ČÁST B · DETAIL", { placeholder: "kicker" });
  s.addText("Metodika, hypotézy, inventury, ekonomika, corporate, varianty pro ČS a QA", { placeholder: "title" });
  s.addText("B01 metodika a taxonomie · B02 hypotézy · B03–B05 ČR · B06–B10 Evropa · B11–B13 svět · B14–B16 ekonomika · B17 corporate · B18 domácí případy · B19–B20 varianty · B21 otázky · B22 QA", { placeholder: "sub" });
}

// B01 Methodology + taxonomy
{
  const s = content("B01 · METODIKA A TAXONOMIE", "Osm mechanik A–H pokrývá praxi beze zbytku; v databázi převažují karetní odměny (42) a nabídky obchodníků (24)", "Věrnostní program = opakovaná mechanika za setrvání, aktivitu nebo rozsah vztahu. Jednorázové akviziční bonusy (13 záznamů) se evidují zvlášť a nepočítají se.", "DB 10_vernostni_programy_db.csv (125 záznamů, hlavní mechanika bez AKV a DATA GAP) · přehledové zdroje L1: Mastercard Europe 10/2024, Visa, BofA, McKinsey, A&M", "B · Detail");
  s.addChart(pres.ChartType.bar, [{ name: "Záznamů", labels: ["A karetní odměny", "D nabídky obchodníků", "H nebankovní B2B", "G rebaty korp. karet", "F nefinanční benefity", "C vztahový tier", "B cashback na účtu", "E cena 0 za aktivitu"], values: [42, 24, 14, 9, 7, 6, 4, 1] }],
    Object.assign({}, chartBase, { x: M, y: 2.2, w: 6.2, h: 4.6, barDir: "bar", chartColors: [H.accent2], valAxisMinVal: 0, valAxisMaxVal: 50, catAxisLabelFontSize: 10 }));
  s.addText(bullets([
    "Pravidla: FACT = ověřeno ve výtahu zdroje s URL a datem (plný text stránek byl blokovaný); EST se vzorcem; STALE = zdroj starší než 06/2026 nebo bez data; CLAIM = tvrzení firmy; DATA GAP = nenalezeno + kde hledat",
    "Cut-off 06/2026 pro popis nabídky; měny v originále (kurz ČNB neověřen)",
    "Upřesnění taxonomie: atribut „booster C → A/B“ (tier sám nic nevyplácí, jen násobí); atribut „provozovatel ≠ vydavatel“ (schémové programy); podtypy G1 objem / G2 rychlost úhrady / G3 large ticket; F1 služby vs. F2 status",
    "Kategorie I (odměny v acquiringu) jen podmíněně – doložený příklad se nenašel [DATA GAP]",
  ], 11.5), { x: 7.1, y: 2.2, w: 5.6, h: 4.6, margin: 0, isTextBox: true, valign: "top" });
}

// B02 Hypotheses
{
  const s = content("B02 · HYPOTÉZY H1–H7", "Dvě hypotézy platí plně (H2, H3), čtyři částečně, jedna převážně – nejvíc se musela upravit H4 o rozdílu EU vs. USA", null, "Report kap. 3; důkazy v částech B03–B17", "B · Detail");
  const rows = [hdr(["#", "Hypotéza", "Verdikt", "Klíčový důkaz"])];
  const d = [
    ["H1", "U FOP a mikro fungují programy jako v retailu", "Částečně", "Forma ano (cashback, body, nabídky obchodníků); u neobank cashback roste s tarifem; účinnost nedoložena [DATA GAP]; Air Bank program ukončila"],
    ["H2", "S velikostí mizí body a nastupuje vztahový pricing, rebaty, balíčky", "Potvrzeno", "Allica, VÚB (cashback za vztah); BofA tiery 20/50/100 tis. USD; corporate rebaty v bps (GSA 1,20 %), ECR, relationship pricing; výhrada Brex/Ramp"],
    ["H3", "U velkých korporací klasický program téměř není", "Potvrzeno", "Žádný bodový program nenalezen; rebate, ECR, pricing, RM; Emirates cílí na firmy bez korporátní smlouvy"],
    ["H4", "Motor = vyšší interchange; IFR commercial karty nekryje; proto USA velkorysejší", "Částečně", "Výjimka IFR [FACT]; EU commercial 1,3–2,4 % [CLAIM] ≈ USA 1,75–2,95 % [FACT] – rozdíl dělá hlavně neregulovaný spotřebitelský kredit v USA (Reg II jen debet)"],
    ["H5", "Vrstva financovaná obchodníky, banka bez rozpočtu", "Částečně", "SavingsEdge, Easy Savings, Business Savings/Bonus, Revolut Rewards, Amex Offers; „bez rozpočtu“ jen pro nabídky, body nese emitent; vztah u SavingsEdge drží schéma"],
    ["H6", "Podnikatelé používají osobní produkty mj. kvůli odměnám", "Částečně", "Mastercard: 80 % z >10 000 SME, ~1/3 kvůli odměnám [CLAIM 10/2024]; USA 26 % firem platí osobní kartou [CLAIM]; ČR striktně odděluje ~1/4 [CLAIM]; mechanismus vyloučení doložen (SLSP, ČS)"],
    ["H7", "V ČR nikdo nemá ucelený program, jen cashback", "Převážně", "0 tierů u 12 bank; 1 % cashback KB, MONETA, mBank; výhrady: MONETA Odměny pro FOP (D), ČS/ČSOB nefinanční benefity (F)"],
  ];
  const vc = { "Potvrzeno": H.accent3, "Částečně": H.accent6, "Převážně": H.accent2 };
  d.forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10.5, bold: i === 2, color: i === 2 ? vc[t] : H.dk1 } }))));
  table(s, rows, { y: 1.8, colW: [0.5, 3.4, 1.1, 7.13], rowH: 0.6 });
}

// B03 ČR inventory
{
  const s = content("B03 · ČR – INVENTURA BANK", "Český trh zná jen dva vzorce: 1 % na podnikatelské kreditní kartě a slevy financované schématem – tierová logika chybí", "12 bank posouzeno; Partners, Trinity a Oberbank nehodnoceno [DATA GAP].", "kb.cz, moneta.cz, csob.cz (11/2025), rb.cz (1. 5. 2026), airbank.cz + e15.cz, mbank.cz (03/2026), revolut.com, wise.com, csas.cz · FACT / STALE / CLAIM / DATA GAP", "B · Detail");
  const rows = [hdr(["Banka", "Program pro podnikatele", "Retail program otevřený podnikatelům?", "Hodnocení", "Značka"])];
  const d = [
    ["Česká spořitelna", "Benefity pro firmy: Visa Business slevy (Bolt, EasyPark, foodora, wflow); business kreditky bez odměn", "Odměny: podnikatelská karta nezmíněna; Moneyback dle článku jen soukromá karta", "Nemá vlastní program", "FACT/STALE, CLAIM, DATA GAP"],
    ["KB", "Kreditní karta Business: 1 % zpět, garance do 31. 12. 2026; strop „29 000 Kč měs.“ nejasný", "„Klub věrnosti“ jen v článku", "Cashback na kreditní kartě", "FACT, CLAIM"],
    ["ČSOB", "Pojištění k podnikatelským kartám (11/2025)", "Svět odměn ukončen 31. 12. 2024; Kate Coins pro podnikatele nejasné", "Nemá", "STALE, DATA GAP"],
    ["Raiffeisenbank", "Nenalezeno", "Program výhod KK (1. 5. 2026) jen retailové karty", "Nemá", "STALE"],
    ["MONETA", "Business Card 1 % bez stropu; kampaně 5 % PHM / hobby (AKV)", "Program Odměny otevřený FOP vč. karet Business CZK/Premium, PO vyloučeny (22. 6. 2025)", "Nejširší nabídka, bez tierů", "FACT/STALE"],
    ["UniCredit", "„Benefitní program k platebním kartám“", "U-šetřete – zapojení podnikatelských karet nejasné", "Nejasné", "CLAIM, DATA GAP"],
    ["Air Bank", "1 % zpět z podnikatelské karty ukončeno k 30. 6. 2026", "„Odměny za placení“ nejasné", "Program zrušen", "FACT, DATA GAP"],
    ["Fio / Creditas", "Nenalezeno (nulové poplatky / jen úrok)", "Nenalezeno", "Nemá", "STALE"],
    ["mBank", "1 % zpět, 2. 3.–31. 12. 2026, jen na telefonickou pozvánku", "–", "Cílená retence", "STALE 03/2026"],
    ["Revolut / Wise", "V ČR jen akviziční odměny (Revolut Pro); Revolut cashback jen USA, Wise 0,5 % jen UK", "–", "Nemá (v ČR)", "FACT/STALE"],
  ];
  d.forEach((r, i) => rows.push(i === 0 ? csRow(r, 9.5) : r.map(t => ({ text: t, options: { fontSize: 9.5 } }))));
  table(s, rows, { y: 2.05, colW: [1.5, 4.0, 3.5, 1.6, 1.53], rowH: 0.41 });
}

// B04 ČR non-bank + reading
{
  const s = content("B04 · ČR – NEBANKOVNÍ B2B A ČTENÍ", "Tierovou logiku podle obratu mají v ČR jen nebankovní hráči – MAKRO Gold od 33 333 Kč měsíčního obratu, Qatar 5 tierů", "Prostor pro vztahový program podnikatelů je v bankách volný.", "makro.cz, lufthansagroup.com/cz, qatarairways.com (10/2021), finance.cz, edenred.cz (03/2021), echo24.cz · FACT / CLAIM / STALE", "B · Detail");
  const rows = [hdr(["Program", "Kategorie", "Dostupnost v ČR", "Mechanika", "Značka"])];
  const d = [
    ["PartnerPlusBenefit (Lufthansa Group)", "H letecký", "Ano (česká verze webu)", "Body za firemní lety, Cash & Points", "FACT / STALE"],
    ["BlueBiz (AF-KLM)", "H letecký", "Nejasné", "Blue Credits, registrace zdarma", "CLAIM"],
    ["Qatar Beyond Business", "H letecký", "Nejasné", "5 tierů, vyšší tiery s minimálním obratem", "STALE 10/2021"],
    ["MAKRO Blue / Silver / Gold", "H velkoobchod", "Ano (jen s IČO)", "Gold = měsíční obrat nad 33 333 Kč; nefinanční výhody", "FACT / STALE"],
    ["CCS, Shell Card + ClubSmart, Benzina Tankarta", "H palivo", "Ano", "Sleva 0,40–1,50 Kč/l (CCS), body (Shell), až 1 Kč/l (Benzina)", "CLAIM / STALE"],
    ["T-Mobile Bonus (firemní)", "H telco", "Ukončen 2013", "Body", "STALE 12/2013"],
    ["Mastercard Business Bonus / Ultimate", "D schéma", "Nejasné (NL/DE/FR/ES/IT, RO 02/2025)", "Slevy u partnerů; u Ultimate body", "STALE / DATA GAP"],
    ["American Express firemní karty", "G", "Ukončeno (článek)", "Membership Rewards", "STALE"],
  ];
  d.forEach(r => rows.push(r.map(t => ({ text: t, options: { fontSize: 10.5 } }))));
  table(s, rows, { y: 2.15, w: 8.3, colW: [2.6, 1.2, 1.7, 2.0, 0.8], rowH: 0.46 });
  card(s, 9.2, 2.15, 3.53, 4.3, "Co z inventury plyne", bullets([
    "(a) Plošný 1 % cashback (KB, MONETA, mBank) nemá vztahovou podmínku; Air Bank ho zrušila, mBank dává jen vybraným",
    "(b) Slevy financované schématem (ČS Visa Business, MONETA Odměny) – rozpočet ≈ 0",
    "Žádná banka neodměňuje zůstatek, úvěr ani primární účet",
    "MONETA je jediná, která retailový card-linked program otevřela FOP",
  ], 11));
}

// B05 updates to v2
{
  const s = content("B05 · ČR – CO SE ZMĚNILO OPROTI V2", "Dva údaje z v2 je nutné opravit: Air Bank cashback 1 % skončil 30. 6. 2026 a 1 % pro podnikatele u SLSP se nepotvrdilo", "Dopad na deck v2: slidy B27 (ceny účtů) a B37 (profily Air Bank, Fio, Creditas); dokument v2 kap. 4 a kap. 6.2 / BP4.", "e15.cz (Air Bank po 30. 6. 2026), banky.cz, airbank.cz pravidla; cdn0.erstegroup.com zveřejnění Moneyback 1. 7. 2025; skrblik.cz (ČS Moneyback) · FACT / CLAIM", "B · Detail");
  const w = (CW - 0.6) / 3, y = 2.25, h = 4.3;
  card(s, M, y, w, h, "Air Bank: cashback zrušen", bullets(["1 % zpět z plateb podnikatelskou kartou ukončeno k 30. 6. 2026; od 1. 7. 2026 nárok nevzniká [FACT]", "Rovnocenná náhrada nenalezena", "v2 uvádělo „0 Kč + 1 % cashback“ [STALE 03/2026] → opravit", "Konkurenční okno pro akviziční sezónu 2027 (BP4): podnikatelé Air Bank přišli o odměnu"], 11.5), { headColor: C.accent2 });
  card(s, M + w + 0.3, y, w, h, "SLSP: 1 % pro podnikatele nepotvrzeno", bullets(["Moneyback SLSP zahrnuje debetní karty jen k účtům nepodnikatelů + kreditní Visa Classic/Gold [FACT, zveřejnění 1. 7. 2025]", "v2 uvádí u SLSP „1 % cashback“ (kap. 6.2, BP4) → ověřit ve skupině Erste", "VÚB (Intesa) naopak od 1. 7. 2026 spouští Money back pro firemní kreditní kartu [FACT]"], 11.5), { headColor: C.accent3 });
  card(s, M + 2 * (w + 0.3), y, w, h, "ČS: otevřenost Moneybacku neověřena", bullets(["Podmínky Odměn: „klient ČS, používá George, 18+“; účinnost dle výtahu 1. 8. 2025 (zadání uvádělo 8. 1. 2026 – možná záměna formátu) [FACT]", "Podnikatelský účet ani karta nezmíněny [DATA GAP]", "Článek: Moneyback vyžaduje soukromou kartu ČS [CLAIM]", "Krok bez lítosti: ověřit interně a případně otevřít FOP (model MONETA)"], 11.5), { headColor: C.accent1 });
}

// B06 Europe inventory
{
  const s = content("B06 · EVROPA – INVENTURA", "26 programů pro podnikatele z 8 zemí, téměř všechny pro FOP a malé SME; Španělsko a Polsko soutěží jen akvizičními bonusy", "47 záznamů EU-01 až EU-47: 26 věrnostních otevřených podnikatelům, 8 AKV, 5 retailových (H6), 4 DATA GAP.", "allica.bank, tide.co, natwest.co.uk, mastercard.com 01/2025, finom.co, n26.com, bbva.es, caixabank.com, moneteo.com, vub.sk, slsp.sk, sasgroup.net 27. 5. 2026 · FACT / STALE / CLAIM", "B · Detail");
  const rows = [hdr(["Země", "Věrnostní programy pro podnikatele", "Akviziční (zvlášť)", "Poznámka"])];
  const d = [
    ["UK", "Allica (B+C), Tide Rewards (D), Capital on Tap 1 %, Amex Gold/Platinum, Barclaycard, NatWest Business Plus (0,5–3 %), Mastercard Business Savings, Mettle, Wise 0,5 %", "Tide 1 % 60 dní + 250 GBP", "Starling a Monzo bez vlastního programu; HSBC DATA GAP"],
    ["NL", "bunq cashback 0,5–1 % dle tarifu; bunq + Mastercard Business Bonus (5 zemí od 15. 1. 2025)", "–", "Rabobank, ING, ABN AMRO: nic nenalezeno"],
    ["DE", "Finom 1–3 % (strop 10–90 EUR/měs.), Commerzbank Business Card Premium 0,55 % p.a. (79,90 EUR/rok), N26 Business 0,1 % / 0,5 %, Amex Gold DE", "Qonto 250 EUR", "Sparkasse + Payback (07/2025) jen retail"],
    ["FR", "Amex Business Gold", "–", "Shine, BNP Hello Pro bez odměn"],
    ["ES", "–", "BBVA až 1 200 EUR v 1. roce; CaixaBank refund daní až 600 EUR (do 16. 6. 2026)", "Soutěž o domiciliaci cuota a daní"],
    ["PL", "–", "PKO až 3 600 zł; Santander 3 % max. 150 zł/měs. (do 11/2025); mBank/LeaseLink", "PKO přihlásilo známku „PKO Punkty“ [CLAIM]"],
    ["AT", "–", "–", "George Business bez bonusu; Raiffeisen Bonus Premium retail"],
    ["SK", "VÚB Money back pro Mastercard Business World (od 1. 7. 2026)", "Tatra 5 % max. 50 EUR", "SLSP Moneyback podnikatelům uzavřen"],
    ["Sever", "SAS EuroBonus Executive Business Card (start podzim 2026, 25 bodů/100 SEK)", "–", "DNB, Danske Reward jen retail; Nordea bez odměn"],
    ["HU, RS, pan-EU", "OTP, Banca Intesa: Mastercard Business Bonus; Revolut Business Rewards; Business Bonus Ultimate (white-label)", "–", "Visa obdoba SavingsEdge nenalezena"],
  ];
  d.forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 9.5, bold: i === 0 } }))));
  table(s, rows, { y: 2.0, colW: [1.1, 6.2, 2.9, 1.93], rowH: 0.38 });
}

// B07 Allica case
{
  const s = content("B07 · PŘÍPAD: ALLICA BANK (UK)", "Allica platí cashback 1 % / 1,5 % jen firmám, které už přinesly vklady nebo úvěr – cashback jako položka relationship pricingu", "Business Rewards Account · typ B + C · segment zavedené SME · přenositelnost do ČR 4/5", "allica.bank Key Product Information (V1.3 a hlavní verze, datum neznámé) [FACT/STALE]; internationalaccountingbulletin.com FY25 [CLAIM]", "B · Detail");
  card(s, M, 2.25, 5.9, 4.4, "Mechanika a vstupní brána", bullets([
    "Účet bez měsíčního poplatku, bez úroku na běžném zůstatku; 1 % cashback z plateb kartou, 1,5 % nad měsíčním prahem; pojmenovaný RM a spořicí „pot“ [FACT, STALE]",
    "Brána: firma založená min. 12 měsíců A zůstatek 50 000 GBP+ NEBO úvěr u Allica [FACT]; dle KPI V1.3 jen stávající klienti na pozvání",
    "Práh pro 1,5 %: 10 000 GBP (KPI) vs. 4 000 GBP (tisk FY25) – hodnota 15 000 GBP z výchozí stopy nepotvrzena",
  ], 11.5));
  card(s, 6.8, 2.25, 5.93, 2.0, "Ekonomika [EST]", bullets([
    "Útrata 20 000 GBP/měs. při prahu 10 000 GBP: 10 000 × 1 % + 10 000 × 1,5 % = 250 GBP/měs.; při prahu 4 000 GBP = 280 GBP/měs.",
    "Financuje banka z vkladové a úvěrové marže a interchange",
  ], 11));
  card(s, 6.8, 4.45, 5.93, 2.2, "Důkaz a co si ČS vezme", bullets([
    "Klienti Rewards účtu 6 000+ → 14 000+ (FY25); vklady banky +29 % na 5,7 mld. GBP [CLAIM]; kauzalita neprokázána",
    "Vzít: cashback jako booster uvnitř vztahového tieru (V3), brána „12+ měsíců a vztah“ chrání před krátkodobými klienty; riziko = revize IFR",
  ], 11));
}

// B08 VÚB vs SLSP
{
  const s = content("B08 · PŘÍPAD: VÚB vs. SLSP (SK)", "Konkurent Intesa (VÚB) od 1. 7. 2026 odměňuje firemní kreditku, zatímco Erste (SLSP) podnikatele z Moneybacku vylučuje", "Money back pro Mastercard Business World vs. Moneyback SLSP · typ A · přenositelnost 5/5 (sousední trh, stejná konstelace Erste vs. konkurent)", "vub.sk štatút Moneyback 1. 7. 2026 [FACT]; podnikajte.sk [FACT]; cdn0.erstegroup.com zveřejnění Moneyback 1. 7. 2025 [FACT]", "B · Detail");
  const w = (CW - 0.3) / 2;
  card(s, M, 2.25, w, 3.1, "VÚB (Intesa Sanpaolo)", bullets([
    "Štatút od 1. 7. 2026 do odvolání; měsíční peněžní bonus na kartový účet za aktivní používání firemní kreditní karty",
    "Pro FO podnikatele i PO, kterým banka poskytla úvěrový limit [FACT]; sazba bonusu [DATA GAP]",
    "Ve stejný den ruší pojištění zneužití karty pro PO a lounge benefity Zlaté Mastercard Business → hodnota se přesouvá z F (benefity) do A (cashback)",
  ], 11.5), { headColor: C.accent3 });
  card(s, M + w + 0.3, 2.25, w, 3.1, "SLSP (Erste)", bullets([
    "Moneyback zahrnuje debetní karty jen k účtům nepodnikatelů a kreditní karty Visa Classic/Gold; vyžaduje aktivaci [FACT 07/2025]",
    "Podnikatelé jsou z debetní části vyloučeni; cashback 1 % pro podnikatele (stopa z v2) nepotvrzen",
    "Stejná platforma George jako ČS – nastavení programu je skupinové rozhodnutí, ne vývoj",
  ], 11.5), { headColor: C.accent1 });
  s.addShape(pres.ShapeType.rect, { x: M, y: 5.6, w: CW, h: 1.1, fill: { color: H.lt1 }, line: { color: H.accent5, width: 0.75 }, objectName: "takeaway" });
  s.addText([{ text: "Co si ČS vezme: ", options: { bold: true } }, { text: "ověřit, zda ČS Moneyback vylučuje podnikatelské karty stejně jako SLSP (článek: soukromá karta [CLAIM]); pokud ano, otevřít ho FOP po vzoru MONETA. Odměna vázaná na úvěrový limit (model VÚB) podporuje čerpání a platí ji commercial interchange." }], { x: M + 0.2, y: 5.7, w: CW - 0.4, h: 0.9, fontSize: 12, margin: 0, isTextBox: true, valign: "middle", color: C.text1 });
}

// B09 Mastercard Business Savings
{
  const s = content("B09 · PŘÍPAD: MASTERCARD BUSINESS SAVINGS / BONUS", "Vrstva nabídek financovaných obchodníky už běží u NatWest, bunq, Mettle, OTP a Intesa – bez rozpočtu banky, ale bez diferenciace", "Typ D · segment FOP/mikro + SME · přenositelnost 5/5 technicky, dostupnost pro ČR [DATA GAP]", "natwestgroup.com 05/2024 [FACT, STALE]; mastercard.com/news bunq 15. 1. 2025 [FACT]; mettle.co.uk, otpbank.hu, bancaintesa.rs [STALE]; mastercard.com Business Bonus Ultimate 2024 [CLAIM]", "B · Detail");
  big(s, M, 2.2, 3.4, "1 mil.", "držitelů business debetních karet NatWest/RBS/Ulster zapojených automaticky (05/2024) [FACT, STALE]", C.accent3);
  big(s, M, 4.4, 3.4, "1 000+", "nabídek obchodníků (LUX, McAfee, Heathrow Express, Dropbox, Avis, Microsoft Advertising) [FACT, STALE]", C.accent3);
  card(s, 4.5, 2.2, 8.23, 4.5, "Mechanika, ekonomika, přenos", bullets([
    "Automatický cashback od obchodníka na výpis do 3–5 dní, bez registrace a kuponů; klient je zapsán s každou způsobilou business kartou",
    "bunq od 15. 1. 2025 v NL, DE, FR, ES, IT (Google Workspace, Docusign, HubSpot, Sixt, Booking.com, FedEx, Fiverr) [FACT]; OTP HU, Banca Intesa RS [STALE]",
    "Business Bonus Ultimate (2024) přidává body (cashback, pay-with-points, nabídky) jako white-label pro emitenty – body už nese emitent [CLAIM]; konkrétní emitent nenalezen [DATA GAP]",
    "Nabídky financují obchodníci, program provozuje Mastercard → rozpočet banky ≈ 0; podmínky pro vydavatele neveřejné [DATA GAP]",
    "Data o využití a vlivu na retenci nejsou veřejná [DATA GAP]",
    "ČS už podobný model má s Visou („Benefity pro firmy“) → V1 = zapnout pro všechny podnikatelské karty a ukázat v George Business; nic dalšího od vrstvy nečekat – stejnou nabídku dostane každý se stejnou kartou",
  ], 11.5));
}

// B10 Acquisition vs loyalty + SAS
{
  const s = content("B10 · EVROPA – AKVIZICE V KABÁTU LOYALTY A DISINTERMEDIACE", "Ve Španělsku a Polsku se „aktivitní“ odměna vyplácí jen 6–12 měsíců novým klientům; SAS si staví firemní kartu bez banky", null, "bbva.es, caixabank.com (16. 6. 2026), moneteo.com (PKO, Santander PL), leaselink.pl (08/2025), tatrabanka.sk (2024), sasgroup.net + nordiska.com 27. 5. 2026 · FACT / STALE / CLAIM", "B · Detail");
  const rows = [hdr(["Program (AKV)", "Mechanika", "Značka"])];
  const d = [
    ["BBVA Cuenta Negocios Bienvenida (ES)", "33,33 EUR/měs. za domiciliaci cuota + 10 + 10 + 10 EUR/měs. + 2 % palivo, až 1 200 EUR v 1. roce; do 31. 12. 2026", "FACT"],
    ["CaixaBank Cuenta Pymes Online (ES)", "Refund daní do 100 EUR/měs., max. 600 EUR, prvních 400 klientů; ukončeno 16. 6. 2026", "FACT"],
    ["PKO BP (PL)", "Do 10 % výdajů, max. 3 600 zł ve 3 obdobích", "STALE / CLAIM"],
    ["Santander Bank Polska (PL)", "3 % cashback max. 150 zł/měs., do 30. 11. 2025", "STALE 11/2025"],
    ["mBank / LeaseLink (PL), Tatra banka (SK), Tide (UK), Qonto (DE)", "Cashback za otevření účtu; 5 % max. 50 EUR k nové kreditce; 1 % 60 dní + 250 GBP; 250 EUR", "STALE"],
  ];
  d.forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10.5, bold: i === 0 } }))));
  table(s, rows, { y: 1.85, w: 7.9, colW: [2.6, 4.3, 1.0], rowH: 0.6 });
  card(s, 8.8, 1.85, 3.93, 4.9, "SAS EuroBonus Executive Business Card", bullets([
    "Oznámena 27. 5. 2026, start podzim 2026 (SE/NO/DK); 25 bodů za 100 SEK/DKK/NOK, 20 000 level bodů ročně, lounge, Priority Pass [FACT + CLAIM]",
    "Emitent Nordiska (card-as-a-service), aplikaci dodává Cardlay; dříve co-brand se SEB Kort, Amex Nordics a Lunar",
    "Aerolinka přebírá vztah se SME klientem od bank → hrozba disintermediace",
    "Přenositelnost do ČR 2/5 (chybí silný domácí letecký program); poučení: embedded partner umí postavit firemní kartu nebankovní značce",
  ], 11), { headColor: C.accent3, headSize: 12.5 });
  s.addText("Čtení: akviziční bonus ≠ věrnostní program. Pro ČR je to alternativní nástroj k BP4 (first account), ne náhrada vztahového programu.", { x: M, y: 5.75, w: 7.9, h: 0.6, fontSize: 11.5, italic: true, color: C.text2, margin: 0, isTextBox: true });
}

// B11 World inventory with chart
{
  const s = content("B11 · SVĚT – INVENTURA", "V USA je 1,5–2 % flat cashback na business kartě standard; Kanada, Austrálie a Singapur jedou na bodech aerolinek", "27 programů mimo Evropu otevřených podnikatelům (WD-01 až WD-28) + 10 corporate záznamů (CO-01 až CO-10).", "chase.com, capitalone.com, wellsfargo.com, usbank.com, americanexpress.com, brex.com (08/2026), rbcroyalbank.com, td.com, commbank.com.au (T&C 28. 9. 2026), nab.com.au, qantas.com, singaporeair.com, emirates.com, dbs.com.sg, ocbc.com · FACT / STALE / CLAIM", "B · Detail");
  s.addChart(pres.ChartType.bar, [{ name: "Základní cashback / ekvivalent (%)", labels: ["Chase Ink Unlimited [FACT]", "Capital One Spark Cash Plus [STALE]", "Wells Fargo Signify [STALE]", "Chase Ink Premier (ostatní) [STALE]", "Commerzbank Premium (DE) [STALE]", "bunq Free (NL) [STALE]", "N26 Business Smart (DE) [STALE]", "OCBC SGD útrata (SG) [STALE]"], values: [1.5, 2.0, 2.0, 2.0, 0.55, 0.5, 0.1, 0.2] }],
    Object.assign({}, chartBase, { x: M, y: 2.2, w: 6.6, h: 4.6, barDir: "bar", chartColors: [H.accent6, H.accent6, H.accent6, H.accent6, H.accent3, H.accent3, H.accent3, H.accent6], invertedColors: [H.accent6], valAxisMinVal: 0, valAxisMaxVal: 2.5, dataLabelFormatCode: "0.0#\" %\"", catAxisLabelFontSize: 9 }));
  s.addText(bullets([
    "USA kategorie 3–5 % se stropy: Ink Business Cash 5 % do 25 000 USD/rok [FACT]; Ink Preferred 3x do 150 000 USD [CLAIM]; U.S. Bank 3 % / 1 % [STALE]; Amex Business Gold kredit až 240 USD/rok [FACT 2026]",
    "Fintechy: Brex body 7x/4x/3x/2x/1x vyplácené na Brex účet [FACT 08/2026]; Ramp cashback na Ramp účet, sazba [DATA GAP] – karta jako háček pro celou platformu",
    "Kanada: RBC Avion Business 1 / 1,25 bodu za CAD, slučování s osobní kartou (H6) [STALE]; TD 9/6/2 body [STALE]",
    "Austrálie: Qantas Business Rewards (firma 20/30/40 bodů na 100 bodů cestujících, vstup 89,50 AUD) + co-brand CommBank, NAB (+50 000 bodů za 15 měsíců), Westpac, ANZ [STALE]",
    "Asie: SIA HighFlyer 5 bodů/SGD, Emirates Business Rewards 1 bod/USD („30 000+ MSME“ [CLAIM]), DBS 1 % při ≥ 2 000 SGD/měs. [STALE]",
  ], 10.5), { x: 7.4, y: 2.2, w: 5.33, h: 4.6, margin: 0, isTextBox: true, valign: "top" });
}

// B12 BofA case
{
  const s = content("B12 · PŘÍPAD: BANK OF AMERICA – PREFERRED REWARDS FOR BUSINESS", "Tier podle zůstatku sám nic nevyplácí – odpouští poplatky, zlevňuje úvěr a násobí kartové odměny; banka kupuje zůstatek a vztah", "Typ C (booster → A, B, F) · segment FOP/mikro + SME · přenositelnost 5/5 · nejbližší vzor pro BP5 / George Business One a BB2", "bankofamerica.com FAQ 2026 (tiery, pokračování programu) [FACT]; business.bankofamerica.com (benefity, datum neznámé) [STALE]; BofA ARS FY2025 [CLAIM]; newsroom 02/2026, 07/2026 [FACT]", "B · Detail");
  const rows = [hdr(["Tier", "3měsíční průměrný zůstatek", "Bonus ke kartovým odměnám", "Další benefity (všechny tiery, odstupňované)"])];
  [["Gold", "≥ 20 000 USD", "+25 %", "bez poplatků až na 4 + 4 účtech; booster úroku na spoření"],
   ["Platinum", "≥ 50 000 USD", "+50 %", "−0,25 p.b. z úrokové sazby nových úvěrů a linek"],
   ["Platinum Honors", "≥ 100 000 USD", "+75 %", "−0,05 % merchant services; benefity drží min. 1 rok"]].forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 11.5, bold: i === 0 } }))));
  table(s, rows, { y: 2.2, w: 7.9, colW: [1.5, 1.9, 1.5, 3.0], rowH: 0.5 });
  s.addText(bullets([
    "Kvalifikuje kombinovaný zůstatek na business vkladech a investicích Merrill; upgrade automatický; program zdarma [FACT]",
    "Ilustrace [EST]: útrata 100 000 USD na kartě s 1,5 % = 1 500 USD; v tieru Platinum bonus 50 % = +750 USD/rok – bonus roste s útratou, vstup řídí zůstatek",
    "Když BofA 27. 5. 2026 nahradil retailový program programem BofA Rewards, business program ponechal beze změny [FACT 02/2026]",
    "Veřejná data o členech a retenci business programu chybí [DATA GAP]; celý Preferred Rewards: 11,4 mil. členů, 99% retence [CLAIM]",
  ], 10.5), { x: M, y: 4.6, w: 7.9, h: 2.3, margin: 0, isTextBox: true, valign: "top" });
  card(s, 8.8, 2.2, 3.93, 4.55, "Co si ČS vezme", bullets([
    "Architekturu pro BP5 / George Business One a BB2: tier podle zůstatku + úvěru → odpuštění poplatků, sleva z úvěru, booster cashbacku",
    "Prahy kalibrovat na distribuci zůstatků SB klientů ČS [DATA GAP]; hodnoty v USD nepřebírat",
    "Pravidlo „benefity drží rok“ – u OSVČ důležité kvůli sezónním daňovým platbám",
    "Nepotřebuje obchodníky ani schéma: jen data o zůstatcích, ceník a úvěrový pricing",
  ], 11.5), { headColor: C.accent1 });
}

// B13 Schemes + fintechs
{
  const s = content("B13 · PŘÍPAD: VISA SAVINGSEDGE, MASTERCARD EASY SAVINGS, BREX / RAMP", "Schémata nabízejí vrstvu bez rozpočtu banky, fintechy vážou odměnu na vlastní účet – obě cesty mění kartu v akviziční kanál", "Typ D (schémata) a A s výplatou na účet (fintechy) · přenositelnost 4/5 (schémata), princip 5/5 (výplata na účet)", "usa.visa.com press 12.–13. 6. 2024 [FACT]; mastercard.com Easy Savings [STALE/CLAIM]; novo.co 06/2026 [FACT]; brex.com 08/2026 [FACT]; ramp.com [CLAIM]", "B · Detail");
  const w = (CW - 0.6) / 3, y = 2.25, h = 4.4;
  card(s, M, y, w, h, "Visa SavingsEdge (USA + Kanada)", bullets(["Relaunch 12.–13. 6. 2024 pro Visa Business kreditní, debetní i prepaid karty [FACT]", "Dvě cesty: Instant Coupons (kód u pokladny) a Cashback Offers (kredit na výpisu po registraci karty)", "Financují obchodníci, provozuje Visa – vztah s držitelem drží schéma, ne banka", "Evropská obdoba nenalezena [DATA GAP]"], 11), { headColor: C.accent6 });
  card(s, M + w + 0.3, y, w, h, "Mastercard Easy Savings (globálně)", bullets(["Automatické rebaty bez kuponů, bez ročního poplatku, sledované v aplikaci a na výpisu [STALE]", "„Až 20 %“, „50 000+ lokací“ [CLAIM]", "Aktivní u neobanky Novo (06/2026) [FACT]; stránky pro SG, IN, MY, MT, MEA; spuštění Ukrajina 2024", "Dostupnost pro CZ BIN range a model pro vydavatele [DATA GAP: Mastercard CEE]"], 11), { headColor: C.accent6 });
  card(s, M + 2 * (w + 0.3), y, w, h, "Brex a Ramp (USA fintechy)", bullets(["Brex: 7x rideshare, 4x lety a hotely, 3x restaurace, 2x software, 1x ostatní; bez stropu, výplata na Brex účet [FACT 08/2026]", "Ramp: flat cashback bez poplatku, převoditelný na Ramp Checking; sazba [DATA GAP]", "Odměna napojená na vlastní účet nebo spend platformu – karta je háček pro celou AP/expense platformu", "Stejný princip jako vztahový balíček banky"], 11), { headColor: C.accent6 });
}

// B14 Who funds
{
  const s = content("B14 · EKONOMIKA – KDO PROGRAMY FINANCUJE", "Čtyři zdroje peněz: interchange, obchodníci, marže z vkladů a úvěrů a poplatek za tarif – každý nese jinou mechaniku", null, "EuroCommerce 22. 5. 2026 [CLAIM]; Mastercard intra-EEA 22. 1. 2021 a ČR 1. 3. 2022 [STALE]; Visa USA IRF 18. 4. 2026 [FACT]; Cardlytics 20. 5. 2025 [CLAIM]; Curinos 01/2024 [STALE]; bunq, N26, Finom, Commerzbank [STALE]", "B · Detail");
  const rows = [hdr(["Zdroj financování", "Doklad", "Které mechaniky nese", "Značka"])];
  [["Interchange (vydavatel)", "EU commercial 1,3–2,4 %; Mastercard intra-EEA Corporate 1,90 %, BusinessCard 1,65 %; ČR Corporate 2,10 % / bezkontaktně 1,70 %; sazebník ČR k 1. 1. 2026 existuje, hodnoty neověřeny; USA Visa commercial 1,75–2,95 % + 0,10 USD", "A karetní odměny, G rebaty", "CLAIM / STALE / FACT / DATA GAP"],
   ["Obchodníci (merchant-funded)", "Visa SavingsEdge, Mastercard Business Savings/Bonus a Easy Savings, Amex Offers, Cardlytics (~400 bank; od 05/2025 i mimo banky), Tide Rewards (Valuedynamx), Revolut Business Rewards", "D nabídky", "FACT / STALE / CLAIM"],
   ["Marže z vkladů a úvěrů", "BofA: vstup od 20 000 USD zůstatku; Allica: 50 000 GBP+ nebo úvěr; ECR v USA: průměr 76–79 bps vs. 300+ bps u úročených účtů", "C tier, B cashback za vztah", "FACT / STALE / CLAIM"],
   ["Poplatek za tarif", "bunq 0,5 % → 1 %, N26 0,1 % → 0,5 %, Finom 1 % → 3 % s placeným tarifem; Commerzbank 79,90 EUR/rok za 0,55 %", "A u neobank, placené tiery (F)", "STALE / CLAIM"],
   ["Vlastní rozpočet schématu / emitenta", "SavingsEdge provozuje Visa přímo vůči držiteli; body v Business Bonus Ultimate nese emitent", "D, A (white-label)", "CLAIM / DATA GAP"]].forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10.5, bold: i === 0 } }))));
  table(s, rows, { y: 1.8, colW: [2.2, 6.3, 2.2, 1.43], rowH: 0.68 });
  s.addText("Amex (celá firma): rewards expense 4 378 / 4 430 / 4 168 mil. USD za Q1–Q3 2025 [FACT, STALE]; rozpad na Commercial Services [DATA GAP]. Náklady na Membership Rewards a cashback +1 234 mil. USD „primarily driven by higher billed business“ [FACT, 10-K FY2025].", { x: M, y: 6.1, w: CW, h: 0.7, fontSize: 10.5, color: C.text2, margin: 0, isTextBox: true, valign: "top" });
}

// B15 IFR
{
  const s = content("B15 · EKONOMIKA – IFR A INTERCHANGE (H4)", "Výjimka IFR dává firemním kartám v EU interchange srovnatelnou s USA; velkorysost amerických odměn dělá neregulovaný kredit", "H4 částečně potvrzena: první dvě části ano, příčinné vysvětlení rozdílu EU–USA upraveno.", "legislation.gov.uk IFR čl. 1 a 2 [FACT]; Federal Register 14. 11. 2023 [FACT]; Consumer Finance Monitor 08/2025 [FACT]; Mastercard ČR 03/2022 [STALE]; Visa USA IRF 04/2026 [FACT]; EuroCommerce 05/2026 [CLAIM]; OCBC [STALE]", "B · Detail");
  const w = (CW - 0.3) / 2;
  card(s, M, 2.25, w, 4.45, "EU – právní rámec", bullets([
    "Kapitola II IFR (stropy 0,2 % debet / 0,3 % kredit) se nevztahuje na transakce commercial karet – čl. 1 odst. 3 písm. a) [FACT]",
    "Commercial card = karta vydaná podniku, veřejnému subjektu nebo OSVČ, omezená na podnikatelské výdaje, účtovaná přímo na jejich účet [FACT] → zřejmě i debetní karta OSVČ k podnikatelskému účtu; osobní karta OSVČ ne [interpretace]",
    "Studie Komise (EY, Copenhagen Economics) 2020: bez známek přesunu k neregulovaným kartám [FACT, STALE 06/2020]",
    "2025–26: Metro CEO a EuroCommerce žádají rozšíření stropů; přeplatek 2025 ≥ 4 mld. EUR [CLAIM]; návrh Komise nenalezen [DATA GAP]",
  ], 11));
  card(s, M + w + 0.3, 2.25, w, 4.45, "USA a závěr", bullets([
    "Reg II (Durbin): strop 21 c + 5 bp + 1 c jen pro debetní karty vydavatelů ≥ 10 mld. USD aktiv [FACT]; kredit a business karty bez stropu",
    "Soud v Severní Dakotě 6. 8. 2025 Reg II zrušil, rozhodnutí pozastaveno do odvolání [FACT]",
    "Visa USA commercial 1,75–2,95 % + 0,10 USD (od 18. 4. 2026) [FACT] ≈ EU commercial 1,3–2,4 % [CLAIM] → samotná výjimka rozdíl nevysvětluje",
    "Rozdíl dělá: (a) žádný strop ani na spotřebitelský kredit v USA [FACT], (b) úroky z kreditek a Amex, (c) kreditní kultura [hypotézy, DATA GAP]",
    "Kontrast Singapur: OCBC 0,2 % na SGD útratě [STALE]",
  ], 11));
}

// B16 Evidence
{
  const s = content("B16 · EKONOMIKA – DOLOŽENÉ DOPADY", "Žádná studie s kontrolní skupinou nedokládá, že program zvyšuje retenci SME – odměna je hygienický faktor karty", "Statistiky agregátorů bez metodiky byly vyřazeny.", "jdpower.com 12/2025 [FACT]; mckinsey.com (data 2023) [FACT, STALE]; BofA ARS FY2025 [CLAIM]; Allica FY25 přes tisk [CLAIM]; Amex Q2 2025 [FACT]; Mastercard Europe 10/2024 [CLAIM]", "B · Detail");
  const rows = [hdr(["Zdroj", "Zjištění", "Metodika", "Síla důkazu"])];
  [["J.D. Power 2025 U.S. Small Business Credit Card Study", "Index 716/1 000 (+8); „rewards earning“ 6. ze 7 dimenzí podle váhy; Amex 750, Chase 718", "N = 3 728, sběr 7–9/2025", "FACT – korelační"],
   ["McKinsey, SME banking", "13 % SME změnilo primární banku za 24 měsíců (2023 vs. 5 % v 2022); důvody: digitál, servis, úvěr; RM jako kritérium 47 %", "Průzkum, N neuvedeno", "FACT, STALE"],
   ["Bank of America ARS FY2025", "Preferred Rewards (všechny segmenty): 11,4 mil. členů, 99% retence, ~500 USD odměn/klienta/rok", "Bez kontrolní skupiny", "CLAIM"],
   ["Allica FY25", "Klienti Rewards účtu 6 000+ → 14 000+; vklady +29 % na 5,7 mld. GBP", "Výsledky přes tisk", "CLAIM, kauzalita neprokázána"],
   ["Amex Q2 2025", "SME (< 300 mil. USD tržeb) = 82 % objemů Commercial Services", "Segmentové KPI", "FACT, STALE"],
   ["Mastercard, > 10 000 SME", "80 % používá osobní bankovní produkty, ~1/3 kvůli odměnám", "Země, období, agentura nezveřejněny", "CLAIM, STALE 10/2024"],
   ["Bain, Economics of loyalty", "Promotéři +45 % vkladů, +25 % produktů (retail, ne SME)", "Poradenská firma", "CLAIM"]].forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10.5, bold: i === 0 } }))));
  table(s, rows, { y: 2.15, colW: [3.0, 5.2, 2.2, 1.73], rowH: 0.56 });
}

// B17 Corporate
{
  const s = content("B17 · CORPORATE – ČÍM SE LOAJALITA NAHRAZUJE", "U mid a large corporate kupuje loajalitu rebate v bps, earnings credit a relationship pricing – GSA SmartPay vrací 1,20 %", "H2 a H3 potvrzeny. Pro ČR přenositelnost 2/5 (rebaty) až 3/5 (ECR jako transparentní relationship pricing).", "smartpay.gsa.gov FY2025 + 3. 4. 2026 [FACT]; NYS OGS, NC DOA, WA DES kontrakty [STALE]; Texas Comptroller 3. 7. 2024 [FACT, STALE]; AFP [FACT]; Curinos 01/2024 [STALE]; McKinsey, Oliver Wyman 2023, BCG 2018 [CLAIM]", "B · Detail");
  big(s, M, 2.2, 3.3, "1,20 %", "efektivní rebate GSA SmartPay FY2025: 471 mil. USD z 39,4 mld. USD útraty [FACT] = EST", C.accent6);
  const w = (CW - 3.3 - 0.6) / 2;
  card(s, 4.2, 2.2, w, 4.5, "Rebaty u commercial karet (G)", bullets([
    "Smluvní roční revenue share podle objemu (tiery) a rychlosti úhrady",
    "JPM–New York 180,5–43 bps podle tieru; BofA–Severní Karolína 1,99–2,18 % podle objemu (350–550+ mil. USD) a doby úhrady 2–25 dní; U.S. Bank–NASPO 34,75 bps [STALE]",
    "Citi–Texas 1,93 % + 0,75 bp za každý den dřívější úhrady [FACT, STALE 07/2024]; US Commerce: týdenní výpis 157–168 bps vs. 109–120 bps [STALE]",
    "Financuje commercial interchange 1,30 % + 35 USD až 2,95 % + 0,10 USD [FACT 04/2026]",
    "J.P. Morgan case Ashton Woods: +98 % útraty, +303 % rebate [CLAIM]",
  ], 10.5), { headColor: C.accent6 });
  card(s, 4.2 + w + 0.3, 2.2, w, 4.5, "Earnings credit a relationship pricing (C, F)", bullets([
    "ECR: zůstatky na neúročeném účtu generují kredit, který se odečte od poplatků za cash management [FACT – AFP]; průměr 76–79 bps vs. 300+ bps u úročených účtů (2023–24) [STALE, CLAIM Curinos]",
    "McKinsey: ~5 % strategických klientů = polovina výnosů banky; primární vztah ROE o ~20 p.b. vyšší [CLAIM]",
    "Oliver Wyman 2023: subscription pricing; BCG 2018: špatně nastavený balíček vede ke ztrátě [CLAIM]",
    "BofA Employee Banking & Investing: benefity zaměstnancům korporátních klientů (titulek: 4 mil.) [STALE, CLAIM]",
    "Pro ČS: nestavět bodový program; transparentní „zůstatek kompenzuje poplatky“; objem commercial karet v ČR [DATA GAP]",
  ], 10.5), { headColor: C.accent2 });
}

// B18 domestic cases MONETA + Air Bank
{
  const s = content("B18 · DOMÁCÍ PŘÍPADY: MONETA A AIR BANK", "MONETA jako jediná otevřela retailový program podnikatelům; Air Bank ukazuje, že plošný cashback bez vztahové brány se nezaplatí", "Přenositelnost 5/5 (domácí trh). Air Bank jako negativní případ.", "moneta.cz (Business Card; Program Odměny podmínky 22. 6. 2025) [FACT/STALE]; e15.cz, banky.cz, airbank.cz pravidla (ukončení 30. 6. 2026) [FACT]; v2 (Air Bank > 65 tis. účtů 1/2026, 17 % FO Fakturoid 9/2026) [FACT]", "B · Detail");
  const w = (CW - 0.3) / 2;
  card(s, M, 2.25, w, 4.45, "MONETA – Business Card 1 % + Program Odměny pro FOP", bullets([
    "Business Card: podnikatelská kreditní karta s vedením zdarma, 1 % zpět bez stropu, bezúročné období až 55 dní, sjednání online [FACT/STALE]; kampaně 5 % PHM / hobby markety do 1 000 Kč/měs. po 6 měsíců = AKV",
    "Program Odměny (Smart Banka): card-linked nabídky obchodníků; výslovně zahrnuje karty Business CZK a Business Premium fyzických osob podnikatelů, PO vyloučeny [FACT, STALE 06/2025]",
    "Cashback platí interchange kreditní karty, nabídky platí obchodníci; v kontextu v2: MONETA = nejrychlejší růst úvěrů segmentu (+27,5 %) a karta je součást úvěrové propozice",
    "Vzít: totéž udělat s Moneybackem ČS – nízký náklad, podnikatele nepostrkovat k osobní kartě",
  ], 11), { headColor: C.accent2 });
  card(s, M + w + 0.3, 2.25, w, 4.45, "Air Bank – ukončení cashbacku 1 % (negativní případ)", bullets([
    "1 % zpět z každé platby podnikatelskou kartou (držitel i disponent), výplata na účet do 10. dne; ukončeno k 30. 6. 2026, náhrada nenalezena [FACT]",
    "Strop programu a důvod ukončení [DATA GAP]; Air Bank nemá podnikatelský úvěr (v2 DATA GAP) → cashback nebyl spojený s úvěrovým výnosem ani vztahovou podmínkou [EST – interpretace]",
    "V době programu > 65 tis. podnikatelských účtů za < 2 roky a 17 % FO ve Fakturoidu [FACT v2]; podíl cashbacku na růstu neznámý",
    "Vzít: V3 vázat na tier (zůstatek, úvěr); pro akviziční sezónu 2027 argument „0 Kč + nabídky obchodníků + tier“",
  ], 11), { headColor: C.accent4 });
}

// B19 Options detail
{
  const s = content("B19 · VARIANTY PRO ČS – DETAIL", "Každá varianta má vazbu na BP3/BP4/BP5/BB2, odhad se vzorcem a riziko – V2 je jádro, V1 quick win, V3 a V4 se slučují do V2", "Čísla z v2 převzata beze změny; P = předpoklad k ověření na interních datech (Q7 v2).", "Report kap. 9 · EST se vzorcem; interchange 2,10 % [STALE 03/2022]; v2 BB2 40–85 mil. Kč/rok, tier 149–299 Kč/měs., 17–35 tis. platících", "B · Detail");
  const rows = [hdr(["#", "Varianta", "Hrubá ekonomika [EST] se vzorcem", "Hlavní rizika", "Doporučení"])];
  [["V1", "Schémová vrstva nabídek pro podnikatelské karty", "Rozpočet odměn ≈ 0; náklad = integrace do George Business + komunikace; podmínky schémat pro vydavatele [DATA GAP]; přínos = hygiena a aktivita karet", "Vztah drží schéma; nízká exkluzivita", "ANO – quick win 0–6 m"],
   ["V2", "„George Business Preferred“ – vztahový tier podle zůstatku + úvěru", "Náklad = odpuštěné poplatky + sleva z úvěru × úvěr + bonus ke cashbacku (0,25 p.b. z 1 mil. Kč = 2 500 Kč/rok); přínos = vkladová marže × přírůstek zůstatků + primární vztah; prahy z distribuce zůstatků [DATA GAP]", "Kanibalizace poplatků, kalibrace prahů, governance Retail vs. Corporate", "ANO – jádro, 6–18 m (s M4 v2)"],
   ["V3", "Cashback na podnikatelské kartě podmíněný vztahem", "P 20 000 klientů × P 30 000 Kč/měs. × 12 × 1 % = 72 mil. Kč/rok cashbacku vs. ≈ 151 mil. Kč interchange (× 2,10 %) před schémovými poplatky; na 10 000 Kč: 210 − 100 = 110 Kč vs. 20 Kč na osobní kartě", "Revize IFR (05/2026); Air Bank cashback zrušila; plošně bez brány drahé", "ANO – jen jako booster uvnitř V2"],
   ["V4", "Placený tier s benefity místo bodů", "Výnos BB2 40–85 mil. Kč/rok; cashback booster +0,5 p.b.: 17–35 tis. platících × P 20 000 Kč/měs. × 12 × 0,5 % = 20–42 mil. Kč nákladu krytého interchange", "Ochota platit [DATA GAP – research]; kanibalizace Maxi", "ANO – sloučit s V2 do jedné architektury"],
   ["V5", "Partnerství s nebankovním B2B programem", "Náklad bodů nese banka při co-brandu; ekonomika [DATA GAP]", "Disintermediace (SAS); nízký dopad na mikro", "MONITOROVAT"]].forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10, bold: i === 4 || i === 0, color: i === 4 && t.startsWith("ANO") ? H.accent1 : H.dk1 } }))));
  table(s, rows, { y: 2.1, colW: [0.45, 2.6, 5.1, 2.4, 1.58], rowH: 0.72 });
}

// B20 Architecture
{
  const s = content("B20 · DOPORUČENÁ ARCHITEKTURA A KROKY BEZ LÍTOSTI", "Jedna cenová architektura ve čtyřech vrstvách – 0 Kč základ, schémové nabídky, placený tier, vztahový tier; corporate jen pricing", null, "Report kap. 9; v2 Q2 (Živnostník 0 Kč), BP3, BP5, BB2", "B · Detail");
  const steps = [
    ["1 · Základ 0 Kč", "Živnostník bez podmínek (v2 Q2). Vstupní brána pro ~120 tis. nových subjektů ročně (BP4).", C.accent4],
    ["2 · Schémové nabídky", "Visa / Mastercard nabídky obchodníků pro všechny podnikatelské karty v George Business (V1). Rozpočet ≈ 0.", C.accent3],
    ["3 · Placený tier", "Daňový pot + účetní SaaS + pojištění + vyšší cashback za 149–299 Kč/měs. (V4 = BP3, BB2).", C.accent2],
    ["4 · Vztahový tier", "Podle zůstatku a úvěru: odpuštění poplatků, sleva z úvěru, booster cashbacku na podnikatelské kartě (V2 + V3 = BP5 / BB2).", C.accent1],
  ];
  const w = (CW - 0.9) / 4;
  steps.forEach((st, i) => {
    const x = M + i * (w + 0.3);
    s.addShape(pres.ShapeType.rect, { x, y: 2.0, w, h: 2.6, fill: { color: H.lt2 }, line: { color: H.lt2, width: 0 }, objectName: "step " + (i + 1) });
    s.addText(st[0], { x: x + 0.2, y: 2.15, w: w - 0.4, h: 0.5, fontSize: 15, bold: true, fontFace: "Cambria", color: st[2], margin: 0, isTextBox: true });
    s.addText(st[1], { x: x + 0.2, y: 2.7, w: w - 0.4, h: 1.8, fontSize: 11.5, color: C.text1, margin: 0, isTextBox: true, valign: "top" });
    if (i < 3) s.addShape(pres.ShapeType.rightArrow, { x: x + w + 0.03, y: 3.1, w: 0.24, h: 0.4, fill: { color: H.accent5 }, line: { color: H.accent5, width: 0 }, objectName: "arrow " + (i + 1) });
  });
  card(s, M, 4.95, 6.0, 1.85, "Kroky bez lítosti (0–3 měsíce)", bullets(["Ověřit, zda podnikatelské karty ČS jsou v Odměnách / Moneybacku; pokud ne, otevřít je FOP (model MONETA)", "Ověřit u Mastercardu dostupnost Business Bonus / Easy Savings pro CZ", "Změřit podíl útraty FOP na osobních kartách ČS (H6) na interních datech"], 11));
  card(s, M + 6.3, 4.95, CW - 6.3, 1.85, "Pro corporate", bullets(["Bodový program nestavět", "Transparentní relationship pricing typu ECR: zůstatek kompenzuje poplatky za cash management", "Rebate jen u velkých AP toků na virtuálních / purchasing kartách, objem commercial karet v ČR [DATA GAP]"], 11));
}

// B21 Open questions
{
  const s = content("B21 · OTEVŘENÉ OTÁZKY", "Čtrnáct mezer – většinu odemknou interní data ČS a jednání se schématy, ne další externí rešerše", null, "Report kap. 10", "B · Detail");
  const rows = [hdr(["#", "Otázka", "Proč je důležitá", "Kde odemknout"])];
  [["1", "Jsou podnikatelské karty ČS v Odměnách / Moneybacku? Datum podmínek 1. 8. 2025 vs. 8. 1. 2026?", "H6, V1", "Plné PDF podmínek, interně ČS"],
   ["2", "Podíl útraty FOP na osobních vs. podnikatelských kartách ČS", "Velikost interchange páky (V3)", "Interní data ČS"],
   ["3", "Distribuce zůstatků a úvěrů SB klientů ČS", "Kalibrace prahů tieru (V2)", "Interní data (Q1/Q7 v2)"],
   ["4", "Commercial interchange ČR k 1. 1. 2026; klasifikace karet ČS jako commercial", "Ekonomika V3", "Sazebníky schémat, karetní tým ČS"],
   ["5", "Mastercard Business Bonus / Easy Savings: dostupnost v ČR, podmínky pro vydavatele", "V1", "Mastercard CEE"],
   ["6", "Visa: evropská obdoba SavingsEdge", "V1", "Visa Europe"],
   ["7", "Revize IFR: návrh Komise, antimonopolní šetření scheme fees", "Riziko V3", "EUR-Lex, DG COMP / FISMA"],
   ["8", "VÚB Money back: sazba; SLSP: cashback pro podnikatele", "Benchmark Erste / Intesa", "Štatút VÚB, slsp.sk, Erste skupina"],
   ["9", "KB Klub věrnosti, ČSOB Kate Coins, UCB U-šetřete, RB karty: otevřenost podnikatelům", "Úplnost inventury ČR", "Podmínky bank"],
   ["10", "Důvod ukončení cashbacku Air Bank", "Ekonomika plošného cashbacku", "Air Bank, rozhovory"],
   ["11", "Kauzální dopad programů na retenci a share of wallet SME", "Business case všech variant", "Interní A/B pilot, case studies schémat, J.D. Power"],
   ["12", "Počet členů a dopad BofA Preferred Rewards for Business", "Vzor V2", "BofA 10-K, earnings"],
   ["13", "Ochota českých podnikatelů platit za tier s benefity", "V4", "Customer research n ≈ 500 (Q7 v2)"],
   ["14", "Partners, Trinity, Oberbank; telco a SaaS B2B programy", "Úplnost", "Weby a podmínky"]].forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 9.5, bold: i === 0 } }))));
  table(s, rows, { y: 1.7, colW: [0.4, 6.4, 2.6, 2.73], rowH: 0.33 });
}

// B22 QA
{
  const s = content("B22 · QA A ZDROJE", "Všech sedm akceptačních kritérií je splněno; slabinou je ověření z výtahů a 78 % záznamů databáze se značkou STALE", null, "Report kap. 11; loyalty_data/ logy zdrojů (URL · datum zdroje · datum přístupu 6. 10. 2026)", "B · Detail");
  const rows = [hdr(["Kritérium", "Výsledek", "Doklad"])];
  [["Odpověď po segmentech na první stránce", "Splněno", "Kap. 1 / A02"],
   ["H1–H7 s verdiktem a důkazem", "Splněno", "Kap. 3 / B02"],
   ["≥ 12 bank ČR; ≥ 5 nebankovních", "Splněno (12; 8)", "CZ-01 až CZ-36"],
   ["≥ 25 programů v Evropě z ≥ 8 zemí", "Splněno (26 z 8 + pan-EU)", "EU-01 až EU-46"],
   ["≥ 15 programů ve světě", "Splněno (27 + 10 corporate)", "WD-01 až WD-28, CO-01 až CO-10"],
   ["Každý řádek DB má URL, datum, značku", "Splněno s výhradou", "125 × 22 polí; bez data → STALE"],
   ["Kdo financuje; IFR pro commercial karty", "Splněno", "Kap. 7 / B14–B15"],
   ["3–5 variant s vazbou na BP3/BP4/BP5/BB2, EST se vzorcem", "Splněno (5)", "Kap. 9 / A07, B19"],
   ["Rozpočet", "151 vyhledávání; 0 načtení stránek", "Ověření jen z výtahů"]].forEach(r => rows.push(r.map((t, i) => ({ text: t, options: { fontSize: 10.5, bold: i === 1 } }))));
  table(s, rows, { y: 1.75, w: 7.6, colW: [3.4, 2.2, 2.0], rowH: 0.42 });
  card(s, 8.5, 1.75, 4.23, 2.3, "Značky v databázi (125 záznamů)", bullets(["STALE 97 · FACT 38 · CLAIM 29 · DATA GAP 19 · EST 1 (řádek může nést víc značek)", "CZ 37 (31 věrnostních, 5 AKV, 1 gap) · EU 47 (35 / 8 / 4) · WORLD 41 (41 / 0 / 0)", "V textu reportu: FACT 77 · EST 19 · STALE 48 · CLAIM 33 · DATA GAP 27"], 10.5));
  card(s, 8.5, 4.25, 4.23, 2.5, "Známé slabiny (nezakrývat)", bullets(["Ověřeno z výtahů, ne z plných textů", "Dopady bez kontrolní skupiny", "Ekonomika V3 na sazbě z 03/2022", "Nejisté fakty o ČS (Moneyback, datum podmínek)", "Rozpory se stopami: Allica 15 000 GBP, SLSP 1 %, datum ČS", "ES, PL, AT jen akviziční; Indie, Brazílie, UOB, Amex Canada nehledány"], 10));
  legend(s, M, 6.35);
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("written", OUT);
})();
