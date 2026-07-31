from app.services.vectorstore.base import BaseVectoreStore
from app.services.vectorstore.qdrant import QdrantVectorStore


class VectorStoreFactory:

    _store: BaseVectoreStore | None = None

    @classmethod
    def get_store(cls) -> BaseVectoreStore:

        if cls._store is None:
            cls._store = QdrantVectorStore()

        return cls._store