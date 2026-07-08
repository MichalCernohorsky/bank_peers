"""Shared logging setup: readable console output + optional file log."""
from __future__ import annotations

import logging
import sys
from pathlib import Path

LOGS_DIR = Path(__file__).resolve().parent.parent / "logs"


def setup_logging(log_file: str | None = None, level: int = logging.INFO) -> None:
    handlers: list[logging.Handler] = [logging.StreamHandler(sys.stdout)]
    if log_file:
        LOGS_DIR.mkdir(parents=True, exist_ok=True)
        handlers.append(logging.FileHandler(LOGS_DIR / log_file, encoding="utf-8"))
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)-7s %(name)s: %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=handlers,
        force=True,
    )
