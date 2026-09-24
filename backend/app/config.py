from functools import lru_cache
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str = "PrivAI Guard"
    environment: str = "development"
    api_v1_prefix: str = "/api/v1"
    cors_origins: str = "http://localhost:5173"
    log_level: str = "INFO"
    mongodb_uri: str = "mongodb://localhost:27017"
    mongodb_db: str = "privai_guard"
    jwt_secret: str = "CHANGE_ME_IN_ENV"
    jwt_algorithm: str = "HS256"
    access_token_minutes: int = 60
    max_input_chars: int = 12000
    rate_limit_per_minute: int = 60
    llm_provider: str = "mock"
    llm_model: str = "gpt-4o-mini"
    llm_api_key: str = ""
    transformer_model: str = "dslim/bert-base-NER"
    transformer_enabled: bool = False
    transformer_threshold: float = 0.80

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

    @property
    def cors_origin_list(self):
        return [x.strip() for x in self.cors_origins.split(",") if x.strip()]

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()
