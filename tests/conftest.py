"""Sdílené fixtures: postav testovací DB z malého xlsx vzorku (tests/fixtures)."""
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from pipeline.build_db import run_build  # noqa: E402

FIXTURE_XLSX = ROOT / "tests" / "fixtures" / "key_figures_sample.xlsx"


@pytest.fixture(scope="session")
def built_db(tmp_path_factory):
    """Postaví SQLite DB z fixture xlsx; vrátí {url, result}."""
    db = tmp_path_factory.mktemp("db") / "test.db"
    url = f"sqlite:///{db}"
    result = run_build(ROOT / "config", FIXTURE_XLSX, url)
    return {"url": url, "result": result, "db_path": db}
