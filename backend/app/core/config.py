from pydantic import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://admin@admin.com:root@localhost:5433/postgres"

    class Config:
        env_file = ".env"


settings = Settings()