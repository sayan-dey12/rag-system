from abc import ABC, abstractmethod

from app.services.documents.models import IndexedDocument


class BaseDocumentManager(ABC):

    @abstractmethod
    def list_documents(
        self,
    ) -> list[IndexedDocument]:
        ...