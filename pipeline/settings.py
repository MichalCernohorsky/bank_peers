"""
settings.py — konfigurace z prostředí (12-factor). Žádné natvrdo zadané hodnoty;
vše přes env / .env soubor (viz .env.example).

  DATABASE_URL     sqlite:///data/cs_financials.db | postgresql://...
  XLSX_PATH        cesta ke zdrojovému ČS xlsx
  ALLOWED_ORIGINS  "*" nebo CSV originů pro CORS
"""
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

ROOT = Path(__file__).resolve().parents[1]


class Settings(BaseSettings):
    database_url: str = f"sqlite:///{ROOT / 'data' / 'cs_financials.db'}"
    xlsx_path: str = str(ROOT / "key_figures_q1_2026.xlsx")
    allowed_origins: str = "*"
    log_level: str = "info"

    model_config = SettingsConfigDict(
        env_file=str(ROOT / ".env"),
        env_file_encoding="utf-8",
        extra="ignore",
    )


def get_settings() -> Settings:
    """Nová instance při každém volání -> env/.env změny se projeví (vč. testů)."""
    return Settings()


def allowed_origins_list(value: str) -> list[str]:
    value = (value or "").strip()
    if value in ("", "*"):
        return ["*"]
    return [o.strip() for o in value.split(",") if o.strip()]
