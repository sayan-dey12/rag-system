from abc import ABC , abstractmethod
from langchain_core.embeddings import Embeddings


class BaseEmbeddingProvider(ABC):
    @abstractmethod
    def embed_documents(
        self, texts: list[str]
    ) -> list[list[float]]:
        ...
    
    
    @property
    @abstractmethod
    def langchain_embedding(self) -> Embeddings:
        ...

    @abstractmethod
    def embed_query(
        self , text: str
    ) -> list[float]:
        ...
        