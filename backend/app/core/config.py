from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    PYTHONPATH: str

    class Config:
        env_file = ".env"
        env_prefix="API_"
        extra="allow"

settings = Settings()