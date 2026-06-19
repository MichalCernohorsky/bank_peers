"""Sdílené fixtures: postav testovací DB z malého xlsx vzorku (tests/fixtures).

Hermetické: testovací banks.yaml = cs (xlsx z fixture) + kb (adjusted z manual CSV).
Peer banky se strukturovaným xlsx (kb/csob/moneta) se testují přes pipeline odděleně;
jejich velké zdrojové soubory nejsou v repu, takže by testy nebyly deterministické.
"""
import shutil
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pipeline.build_db import run_build  # noqa: E402

FIXTURE_XLSX = ROOT / "tests" / "fixtures" / "key_figures_sample.xlsx"

_TEST_BANKS = (
    "banks:\n"
    "  - {code: cs, name: Česká spořitelna, parent_group: Erste Group, source: {kind: xlsx, map: cs}}\n"
    "  - {code: kb, name: Komerční banka, parent_group: Société Générale, source: {kind: adjusted}}\n"
)


@pytest.fixture(scope="session")
def built_db(tmp_path_factory):
    """Postaví SQLite DB z fixture xlsx přes hermetický config; vrátí {url, result}."""
    cfg = tmp_path_factory.mktemp("cfg") / "config"
    shutil.copytree(ROOT / "config", cfg)
    (cfg / "banks.yaml").write_text(_TEST_BANKS, encoding="utf-8")

    db = tmp_path_factory.mktemp("db") / "test.db"
    url = f"sqlite:///{db}"
    result = run_build(cfg, FIXTURE_XLSX, url)
    return {"url": url, "result": result, "db_path": db, "config_dir": cfg}
