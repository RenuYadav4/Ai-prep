from pydantic import BaseSettings #type: ignore

class Settings(BaseSettings):
    DATABASE_URl: str

    class Config:
        env_file = ".env"

Settings = Settings()