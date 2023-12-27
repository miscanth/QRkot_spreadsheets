from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Кошачий благотворительный фонд'
    app_description: str = 'Приложение для Благотворительного фонда поддержки котиков QRKot'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'
    INVESTED_DEFAULT_VALUE = 0
    LIFETIME_SECONDS = 3600
    MIN_LEN_PASSWORD = 3
    FORMAT = '%Y/%m/%d %H:%M:%S'
    SHEET_ID = 0
    TITLE = 'Лист1'
    ROW_COUNT = 50
    COLUMN_COUNT = 5
    SHEET_RANGE = 'A1:E50'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
