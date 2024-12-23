from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    database_hostname: str
    database_port: int
    database_password: str
    database_name: str
    database_username: str

    model_config = SettingsConfigDict(
        env_file="../.env",
        case_sensitive=False
    )


settings = Settings()