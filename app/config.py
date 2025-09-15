from pydantic_settings import BaseSettings
from pydantic import computed_field


class Settings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_NAME: str
    DB_PASSWORD: str
    GH_TOKEN: str

    SECRET_KEY: str
    ALGORITHM:str

    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USER: str
    SMTP_PASS: str

    @computed_field
    def get_db_url(self) -> str:
        return f'postgresql+asyncpg://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'

    @computed_field()
    def get_jwt_key(self) -> str:
        return self.SECRET_KEY

    @computed_field()
    def get_jwt_algorithm(self) -> str:
        return self.ALGORITHM

    class Config:
        env_file = '.env'

settings = Settings()

#bd
DB_URL = settings.get_db_url

#jwt
SECRET_KEY = settings.get_jwt_key
ALGORITHM = settings.get_jwt_algorithm


