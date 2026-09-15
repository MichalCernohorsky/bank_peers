"""Tracker MGM programu: stahne zdroje, ulozi snapshot, porovna, zapise zmeny.

    python3 tracker/run.py                 # ostry beh
    python3 tracker/run.py --only air-bank__pozvete-pratele
    python3 tracker/run.py --dry-run       # nic nezapise

Navrhove pravidlo (viz docs/data-model.md, D6): tracker NIKDY neprepisuje
kuratorovana data v mgm-programs.json. Navrzene zmeny jdou do changelogu
s priznakem needs_review; automaticky se meni jedine pole last_checked.
"""
from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import re
import sys
import time
import urllib.robotparser
from dataclasses import dataclass, field
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

sys.path.insert(0, str(Path(__file__).resolve().parent))

from extractors import extract  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "config" / "sources.yaml"
SNAPSHOTS = ROOT / "snapshots"
DATA_JSON = ROOT / "data" / "mgm-programs.json"
HISTORY = ROOT / "data" / "history"
CHANGELOG_JSON = ROOT / "data" / "changelog.json"
CHANGELOG_MD = ROOT / "data" / "changelog.md"

# Castky: cislo (i s mezerami jako oddelovacem tisicu) nasledovane menou/procentem.
AMOUNT_RE = re.compile(
    r"(\d[\d\s\u00a0]{0,12}(?:[.,]\d+)?)\s*(Kč|Kc|CZK|EUR|€|GBP|£|%)", re.IGNORECASE
)
# Data ve tvaru 1. 1. 2026 nebo 2026-01-01.
# Kanonizace meny: prepis "500 Kč" -> "500 CZK" na strance nesmi vypadat
# jako zmena vyse odmeny.
CURRENCY_CANON = {
    "KČ": "CZK", "KC": "CZK", "CZK": "CZK",
    "EUR": "EUR", "€": "EUR",
    "GBP": "GBP", "£": "GBP",
    "%": "%",
}
DATE_RE = re.compile(r"\b(\d{1,2}\.\s?\d{1,2}\.\s?\d{4}|\d{4}-\d{2}-\d{2})\b")


@dataclass
class FetchResult:
    ok: bool
    content: bytes = b""
    error: str | None = None
    status: int | None = None


@dataclass
class SourceOutcome:
    record_id: str
    subject: str
    url: str
    source_type: str
    status: str                      # first_snapshot | unchanged | changed | error | skipped
    detail: str = ""
    diff: str = ""
    warnings: list[str] = field(default_factory=list)
    proposed: dict = field(default_factory=dict)
    needs_review: bool = True
    snapshot_path: str | None = None


# --------------------------------------------------------------------------- fetch


class Fetcher:
    """HTTP klient s robots.txt, throttlingem a retry.

    Throttluje se PER HOST, ne globalne - dva ruzne subjekty se nemaji cim
    zdrzovat navzajem, ale na jeden web nechceme pálit requesty za sebou.
    """

    def __init__(self, defaults: dict):
        self.ua = defaults.get("user_agent", "mgm-cz-tracker/1.0")
        self.timeout = float(defaults.get("timeout_seconds", 30))
        self.delay = float(defaults.get("delay_seconds", 3.0))
        self.max_retries = int(defaults.get("max_retries", 2))
        self.backoff = float(defaults.get("backoff_seconds", 2.0))
        self.respect_robots = bool(defaults.get("respect_robots", True))
        self._last_hit: dict[str, float] = {}
        self._robots: dict[str, urllib.robotparser.RobotFileParser | None] = {}

    def _throttle(self, host: str) -> None:
        last = self._last_hit.get(host)
        if last is not None:
            wait = self.delay - (time.monotonic() - last)
            if wait > 0:
                time.sleep(wait)
        self._last_hit[host] = time.monotonic()

    def _load_robots(self, origin: str):
        """Nacte robots.txt S TIMEOUTEM.

        Zamerne se nepouziva RobotFileParser.read() - ta vola urlopen() bez
        timeoutu, takze jediny zaseknuty server dokaze zablokovat cely beh.
        """
        try:
            import requests
        except ImportError:
            return None
        try:
            resp = requests.get(
                f"{origin}/robots.txt",
                timeout=min(self.timeout, 10),
                headers={"User-Agent": self.ua},
            )
        except Exception:
            # Nedostupny robots.txt se povazuje za "zadna omezeni" - stejne se
            # chova bezny crawler. Vypadek robots.txt nesmi shodit beh.
            return None
        if resp.status_code != 200:
            return None
        parser = urllib.robotparser.RobotFileParser()
        parser.parse(resp.text.splitlines())
        return parser

    def _allowed(self, url: str) -> tuple[bool, str]:
        if not self.respect_robots:
            return True, ""
        parsed = urlparse(url)
        origin = f"{parsed.scheme}://{parsed.netloc}"
        if origin not in self._robots:
            self._robots[origin] = self._load_robots(origin)
        parser = self._robots[origin]
        if parser is None:
            return True, ""
        if parser.can_fetch(self.ua, url):
            return True, ""
        return False, "zakazano v robots.txt"

    def fetch(self, url: str) -> FetchResult:
        allowed, why = self._allowed(url)
        if not allowed:
            return FetchResult(False, error=why)

        try:
            import requests
        except ImportError:
            return FetchResult(False, error="chybi requests - `pip install -r requirements.txt`")

        host = urlparse(url).netloc
        last_error = "neznama chyba"
        for attempt in range(self.max_retries + 1):
            self._throttle(host)
            try:
                resp = requests.get(
                    url,
                    timeout=self.timeout,
                    headers={"User-Agent": self.ua, "Accept-Language": "cs,en;q=0.8"},
                )
            except Exception as exc:
                last_error = f"{type(exc).__name__}: {exc}"
            else:
                if resp.status_code == 200:
                    return FetchResult(True, resp.content, status=200)
                last_error = f"HTTP {resp.status_code}"
                # 4xx krome 429 nema smysl opakovat - odpoved se nezmeni.
                if 400 <= resp.status_code < 500 and resp.status_code != 429:
                    return FetchResult(False, error=last_error, status=resp.status_code)
            if attempt < self.max_retries:
                time.sleep(self.backoff * (2 ** attempt))
        return FetchResult(False, error=last_error)


# ---------------------------------------------------------------- snapshots & diff


def _display_path(path: Path) -> str:
    """Cesta relativne ke koreni projektu, kdyz to jde.

    Snapshoty muzou lezet i mimo repozitar (--snapshots, docasny adresar v testech),
    a tam by relative_to() spadlo na ValueError.
    """
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def slug_for(url: str) -> str:
    """Stabilni nazev souboru pro URL - citelny zacatek + hash proti kolizim."""
    parsed = urlparse(url)
    tail = (parsed.path.rstrip("/").rsplit("/", 1) or [""])[-1] or "index"
    tail = re.sub(r"[^A-Za-z0-9._-]", "-", tail)[:50].strip("-") or "index"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:8]
    return f"{tail}-{digest}"


def previous_text(record_id: str, slug: str, today: str, snapshots: Path) -> str | None:
    """Baseline, proti kteremu se porovnava aktualne stazeny text.

    Poradi je podstatne:

    1. DNESNI snapshot, pokud uz existuje. Diky tomu druhy beh tehoz dne nad
       nezmenenym obsahem vrati "unchanged" (zadna falesna zmena), ale zaroven
       se ZACHYTI zmena, ktera nastala mezi dvema behy tehoz dne. Kdyby se
       dnesek preskakoval, prepsal by se snapshot novym obsahem a rozdil proti
       predchozimu stavu by se nenavratne ztratil.
    2. Jinak nejnovejsi snapshot ze starsiho dne.
    """
    today_file = snapshots / today / record_id / f"{slug}.txt"
    if today_file.exists():
        return today_file.read_text(encoding="utf-8")

    if not snapshots.exists():
        return None
    for day in sorted((p for p in snapshots.iterdir() if p.is_dir()), reverse=True):
        if day.name >= today:
            continue
        candidate = day / record_id / f"{slug}.txt"
        if candidate.exists():
            return candidate.read_text(encoding="utf-8")
    return None


def _tokens(text: str, pattern: re.Pattern) -> set[str]:
    out = set()
    for match in pattern.finditer(text):
        if pattern is AMOUNT_RE:
            number = re.sub(r"[\s\u00a0]", "", match.group(1))
            unit = match.group(2).upper()
            out.add(f"{number} {CURRENCY_CANON.get(unit, unit)}")
        else:
            out.add(re.sub(r"\s", "", match.group(1)))
    return out


def analyse(old: str, new: str, warnings: list[str]) -> tuple[str, dict, bool]:
    """Vrati (diff, navrzene strukturovane zmeny, needs_review)."""
    diff = "\n".join(
        difflib.unified_diff(
            old.splitlines(), new.splitlines(),
            fromfile="predchozi", tofile="aktualni", lineterm="", n=2,
        )
    )
    old_amounts, new_amounts = _tokens(old, AMOUNT_RE), _tokens(new, AMOUNT_RE)
    old_dates, new_dates = _tokens(old, DATE_RE), _tokens(new, DATE_RE)

    proposed = {
        "amounts_added": sorted(new_amounts - old_amounts),
        "amounts_removed": sorted(old_amounts - new_amounts),
        "dates_added": sorted(new_dates - old_dates),
        "dates_removed": sorted(old_dates - new_dates),
    }

    changed_lines = [
        line for line in diff.splitlines()
        if line.startswith(("+", "-")) and not line.startswith(("+++", "---"))
    ]
    # needs_review=False jen u jednoznacne prohozene jedne castky na par radcich
    # a bez varovani o zmene struktury. Vse ostatni je na cloveka (rozhodnuti D6).
    clean_amount_swap = (
        len(proposed["amounts_added"]) == 1
        and len(proposed["amounts_removed"]) == 1
        and not proposed["dates_added"]
        and not proposed["dates_removed"]
        and len(changed_lines) <= 4
        and not warnings
    )
    return diff, proposed, not clean_amount_swap


# ------------------------------------------------------------------------ changelog


def load_changelog() -> dict:
    if CHANGELOG_JSON.exists():
        return json.loads(CHANGELOG_JSON.read_text(encoding="utf-8"))
    return {"entries": []}


def entry_hash(today: str, record_id: str, url: str, diff: str) -> str:
    return hashlib.sha1(f"{today}|{record_id}|{url}|{diff}".encode("utf-8")).hexdigest()[:12]


def render_changelog_md(log: dict) -> str:
    by_date: dict[str, list[dict]] = {}
    for entry in log["entries"]:
        by_date.setdefault(entry["date"], []).append(entry)

    out = [
        "# Changelog změn MGM programů\n",
        "Generováno `tracker/run.py`. Nejnovější nahoře. "
        "`needs_review: true` znamená, že heuristika si změnou není jistá "
        "a data se **nesmí** aktualizovat bez ručního posouzení.\n",
    ]
    for day in sorted(by_date, reverse=True):
        out.append(f"\n## {day}\n")
        for entry in sorted(by_date[day], key=lambda e: e["subject"]):
            if entry["change_type"] == "first_snapshot":
                flag = " 🆕 první snapshot (není s čím porovnat)"
            elif entry.get("needs_review"):
                flag = " ⚠️ **needs_review**"
            else:
                flag = " ✅ jednoznačná změna"
            out.append(f"### {entry['subject']}{flag}\n")
            out.append(f"- **Zdroj:** <{entry['source_url']}>")
            out.append(f"- **Typ události:** `{entry['change_type']}`")
            if entry.get("snapshot_path"):
                out.append(f"- **Snapshot:** `{entry['snapshot_path']}`")
            prop = entry.get("proposed") or {}
            for key, label in (
                ("amounts_added", "Nové částky"),
                ("amounts_removed", "Zmizelé částky"),
                ("dates_added", "Nová data"),
                ("dates_removed", "Zmizelá data"),
            ):
                if prop.get(key):
                    out.append(f"- **{label}:** {', '.join(prop[key])}")
            for warning in entry.get("warnings") or []:
                out.append(f"- ⚠️ {warning}")
            if entry.get("diff"):
                shortened = entry["diff"]
                if len(shortened) > 3000:
                    shortened = shortened[:3000] + "\n… (zkráceno, celý diff v changelog.json)"
                out.append(f"\n```diff\n{shortened}\n```\n")
    return "\n".join(out) + "\n"


# ----------------------------------------------------------------------------- run


def process_source(
    subject: dict, source: dict, fetch_fn, today: str, snapshots: Path, write: bool
) -> SourceOutcome:
    record_id, subject_name = subject["record_id"], subject["subject"]
    url, stype = source["url"], source.get("type", "html")
    outcome = SourceOutcome(record_id, subject_name, url, stype, "error")

    result = fetch_fn(url)
    if not result.ok:
        outcome.detail = result.error or "stazeni selhalo"
        return outcome

    try:
        extracted = extract(result.content, stype, selector=source.get("selector"))
    except Exception as exc:
        outcome.detail = f"extrakce selhala: {type(exc).__name__}: {exc}"
        return outcome

    outcome.warnings = list(extracted.warnings)

    # Textove kotvy overuji, ze jsme na spravne strance a ne na chybovce/cookie zdi.
    missing = [a for a in (source.get("anchors") or []) if a.lower() not in extracted.text.lower()]
    if missing:
        outcome.warnings.append(
            f"na strance chybi ocekavane kotvy {missing} - zdroj mozna zmenil obsah nebo presmeroval"
        )

    slug = slug_for(url)
    old = previous_text(record_id, slug, today, snapshots)

    if write:
        target = snapshots / today / record_id
        target.mkdir(parents=True, exist_ok=True)
        suffix = "pdf" if stype == "pdf" else "html"
        (target / f"{slug}.{suffix}").write_bytes(result.content)
        (target / f"{slug}.txt").write_text(extracted.text, encoding="utf-8")
        outcome.snapshot_path = _display_path(target / f"{slug}.txt")

    if old is None:
        outcome.status = "first_snapshot"
        outcome.detail = "první snapshot, není s čím porovnat"
        outcome.needs_review = False
        return outcome

    if old == extracted.text:
        outcome.status = "unchanged"
        outcome.needs_review = False
        return outcome

    diff, proposed, needs_review = analyse(old, extracted.text, outcome.warnings)
    outcome.status = "changed"
    outcome.diff = diff
    outcome.proposed = proposed
    outcome.needs_review = needs_review
    return outcome


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="Tracker MGM programů")
    parser.add_argument("--config", default=str(CONFIG))
    parser.add_argument("--only", help="zpracovat jen jeden record_id")
    parser.add_argument("--dry-run", action="store_true", help="nic nezapisovat")
    parser.add_argument("--snapshots", default=str(SNAPSHOTS))
    args = parser.parse_args(argv[1:])

    try:
        import yaml
    except ImportError:
        print("CHYBA: chybi pyyaml - `pip install -r requirements.txt`", file=sys.stderr)
        return 2

    cfg = yaml.safe_load(Path(args.config).read_text(encoding="utf-8"))
    fetcher = Fetcher(cfg.get("defaults") or {})
    snapshots = Path(args.snapshots)
    today = date.today().isoformat()
    write = not args.dry_run

    subjects = cfg.get("subjects") or []
    if args.only:
        subjects = [s for s in subjects if s["record_id"] == args.only]
        if not subjects:
            print(f"CHYBA: record_id {args.only!r} není v konfiguraci", file=sys.stderr)
            return 2

    outcomes: list[SourceOutcome] = []
    for subject in subjects:
        sources = subject.get("sources") or []
        if not sources:
            outcomes.append(
                SourceOutcome(subject["record_id"], subject["subject"], "", "", "skipped",
                              detail=subject.get("note", "žádný nakonfigurovaný zdroj"),
                              needs_review=False)
            )
            continue
        for source in sources:
            outcomes.append(
                process_source(subject, source, fetcher.fetch, today, snapshots, write)
            )

    return finish(outcomes, today, write)


def finish(outcomes: list[SourceOutcome], today: str, write: bool) -> int:
    log = load_changelog()
    known = {e["diff_hash"] for e in log["entries"]}
    new_entries = []

    for outcome in outcomes:
        if outcome.status not in ("changed", "first_snapshot"):
            continue
        digest = entry_hash(today, outcome.record_id, outcome.url, outcome.diff)
        if digest in known:
            continue  # idempotence: stejny beh tyz den nezaloguje podruhe
        known.add(digest)
        new_entries.append({
            "date": today,
            "record_id": outcome.record_id,
            "subject": outcome.subject,
            "source_url": outcome.url,
            "change_type": outcome.status,
            "needs_review": outcome.needs_review,
            "proposed": outcome.proposed,
            "warnings": outcome.warnings,
            "diff": outcome.diff,
            "snapshot_path": outcome.snapshot_path,
            "diff_hash": digest,
        })

    changed = [o for o in outcomes if o.status == "changed"]
    errors = [o for o in outcomes if o.status == "error"]

    if write and new_entries:
        log["entries"].extend(new_entries)
        CHANGELOG_JSON.parent.mkdir(parents=True, exist_ok=True)
        CHANGELOG_JSON.write_text(
            json.dumps(log, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        CHANGELOG_MD.write_text(render_changelog_md(log), encoding="utf-8")

    if write and changed and DATA_JSON.exists():
        # Historie: plny snapshot dat se odklada JEN kdyz se neco zmenilo (D7).
        snapshot_dir = HISTORY / today
        snapshot_dir.mkdir(parents=True, exist_ok=True)
        (snapshot_dir / "mgm-programs.json").write_text(
            DATA_JSON.read_text(encoding="utf-8"), encoding="utf-8")

    if write and DATA_JSON.exists():
        # Jedine pole, ktere tracker meni automaticky (D6).
        payload = json.loads(DATA_JSON.read_text(encoding="utf-8"))
        fetched_ok = {
            o.record_id for o in outcomes if o.status in ("changed", "unchanged", "first_snapshot")
        }
        for record in payload["records"]:
            if record["record_id"] in fetched_ok:
                record["last_checked"] = today
        DATA_JSON.write_text(
            json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    counts: dict[str, int] = {}
    for outcome in outcomes:
        counts[outcome.status] = counts.get(outcome.status, 0) + 1
    print(f"Běh {today}: " + ", ".join(f"{k}={v}" for k, v in sorted(counts.items())))
    print(f"Nových záznamů v changelogu: {len(new_entries)}" + ("  (dry-run)" if not write else ""))
    for outcome in changed:
        flag = "needs_review" if outcome.needs_review else "ověřitelná"
        print(f"  ZMĚNA [{flag}] {outcome.subject}: {outcome.url}")
    for outcome in errors:
        print(f"  CHYBA {outcome.subject}: {outcome.url} — {outcome.detail}", file=sys.stderr)

    # Chyby stahovani nejsou duvod k nenulovemu exit kodu - vypadek jednoho webu
    # nesmi shodit cely tydenni beh v CI.
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
