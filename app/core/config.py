import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    SERVER_NAME: str = 'proj serv name'
    SERVER_HOST: AnyHttpUrl = None
    PROJECT_NAME: str = 'iman proj'
    POSTGRES_SERVER: str = 'localhost'
    POSTGRES_USER: str = 'user'
    POSTGRES_PASSWORD: str = 'password'
    POSTGRES_DB: str = 'postgres'
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = "postgresql://user:password@localhost:5432/project-db"
    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    FIRST_SUPERUSER: str = 'admin@domain.com'
    FIRST_SUPERUSER_PASSWORD: str = 'admin_pass'
    
    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     if isinstance(v, str):
    #         return v
    #     return PostgresDsn.build(
    #         scheme="postgresql",
    #         user='user',
    #         password='password',
    #         host='localhost',
    #         path='project-db',
    #     )


    class Config:
        case_sensitive = True


settings = Settings()
