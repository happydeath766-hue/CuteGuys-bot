from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str
    OWNER_ID: int

    DATABASE_URL: str
    REDIS_URL: str

    TIMEZONE: str = "America/Bogota"
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
