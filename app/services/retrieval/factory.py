from app.services.retrieval.base import BaseRetriever
from app.services.retrieval.retriever import Retriever

class RetriverFactory:
    _retriever: BaseRetriever | None = None

    @classmethod
    def get_retriever(cls) -> BaseRetriever:

        if cls._retriever is None:
            cls._retriever = Retriever()

        return cls._retriever