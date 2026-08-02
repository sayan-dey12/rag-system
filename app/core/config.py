from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_NAME: str = "RAG System"
    
    API_HOST: str = "0.0.0.0"
    API_PORT: int = 8000

    VALKEY_HOST: str
    VALKEY_PORT: int

    QDRANT_HOST: str
    QDRANT_PORT: int
    
    QDRANT_COLLECTION: str = "rag_system"

    RQ_QUEUE: str
    
    CHUNK_SIZE: int = 1000
    CHUNK_OVERLAP: int = 200
    
    EMBEDDING_DIMENSION: int = 384
    
    
    GROQ_API_KEY: str
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    
    EMBEDDING_BATCH_SIZE: int = 128
    
    RETRIEVAL_TOP_K: int = 20
    
    RETRIEVAL_SCORE_THRESHOLD: float = 0.65

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()