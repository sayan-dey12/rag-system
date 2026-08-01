from abc import ABC, abstractmethod

from langchain_core.documents import Document
from qdrant_client.models import PointStruct

from app.events.models import EventCallback


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
        limit: int = 5,
    ) -> list[Document]:
        ...

    @abstractmethod
    def similarity_search_with_score(
        self,
        query: str,
        limit: int = 5,
    ):
        ...

    @abstractmethod
    def delete_document(
        self,
        document_id: str,
    ) -> None:
        ...