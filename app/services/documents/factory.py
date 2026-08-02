from app.services.documents.base import BaseDocumentManager
from app.services.documents.manager import DocumentManager


class DocumentManagerFactory:

    _manager: BaseDocumentManager | None = None

    @classmethod
    def get_manager(
        cls,
    ) -> BaseDocumentManager:

        if cls._manager is None:
            cls._manager = DocumentManager()

        return cls._manager