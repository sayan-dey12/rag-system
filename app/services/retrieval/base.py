from abc import ABC, abstractmethod

from langchain_core.documents import Document
from app.core.config import settings

class BaseRetriever(ABC):

    @abstractmethod
    def retrieve(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
    ) -> list[tuple[Document, float]]:
        ...