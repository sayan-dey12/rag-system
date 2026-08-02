from abc import ABC, abstractmethod

from langchain_core.documents import Document
from qdrant_client.models import PointStruct

from app.events.models import EventCallback
from app.core.config import settings

class BaseVectoreStore(ABC):

    @abstractmethod
    def create_collection(self) -> None:
        ...

    @abstractmethod
    def delete_collection(self) -> None:
        ...

    @abstractmethod
    def add_documents(
        self,
        chunks: list[Document],
        on_event: EventCallback | None = None,
    ) -> None:
        ...

    @abstractmethod
    def upsert(
        self,
        points: list[PointStruct],
        on_event: EventCallback | None = None,
    ) -> None:
        ...

    @abstractmethod
    def similarity_search(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
    ) -> list[Document]:
        ...

    @abstractmethod
    def similarity_search_with_score(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
    ):
        ...

    @abstractmethod
    def delete_document(
        self,
        document_id: str,
    ) -> None:
        ...