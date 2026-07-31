from app.services.embeddings.huggingface import (
    HuggingFaceEmbeddingProvider,
)
from app.services.embeddings.base import BaseEmbeddingProvider


class EmbeddingFactory:
    
    _provider: BaseEmbeddingProvider | None = None

    @classmethod
    def get_provider(cls) -> BaseEmbeddingProvider:

        if cls._provider is None:
            cls._provider = HuggingFaceEmbeddingProvider()

        return cls._provider