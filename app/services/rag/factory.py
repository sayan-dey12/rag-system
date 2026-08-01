from app.services.rag.base import BaseRAGService
from app.services.rag.rag import RAGService


class RAGFactory:

    _service: BaseRAGService | None = None

    @classmethod
    def get_service(cls) -> BaseRAGService:

        if cls._service is None:
            cls._service = RAGService()

        return cls._service