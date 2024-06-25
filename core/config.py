import os
from pathlib import Path

from dotenv import load_dotenv
from urllib.parse import quote_plus
from pydantic_settings import BaseSettings


env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)


class Settings(BaseSettings):
    """Project settings."""

    # Database
    DB_USER: str = os.getenv('DB_USER')
    DB_PASSWORD: str = os.getenv('DB_PASSWORD')
    DB_NAME: str = os.getenv('DB_NAME')
    DB_HOST: str = os.getenv('DB_HOST')
    DB_PORT: str = os.getenv('DB_PORT')
    DATABASE_URL: str = (
            f"postgresql://"
            f"{DB_USER}:%s"
            f"@{DB_HOST}:{DB_PORT}/"
            f"{DB_NAME}" % quote_plus(DB_PASSWORD))


def get_settings() -> Settings:
    return Settings()
