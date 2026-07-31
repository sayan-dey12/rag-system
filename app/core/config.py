from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "RAG System"

    VALKEY_HOST: str
    VALKEY_PORT: int

    QDRANT_HOST: str
    QDRANT_PORT: int
    
    QDRANT_COLLECTION: str = "rag_system"

    RQ_QUEUE: str
    
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    
    EMBEDDING_DIMENSION: int = 384

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()