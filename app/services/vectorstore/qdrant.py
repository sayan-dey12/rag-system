from langchain_core.documents import Document
from langchain_qdrant import (
    QdrantVectorStore as LangChainQdrantVectorStore,
)
from qdrant_client.models import (
    Distance,
    FieldCondition,
    Filter,
    MatchValue,
    VectorParams,
)

from app.core.config import settings
from app.db.qdrant import qdrant_client
from app.services.embeddings.factory import EmbeddingFactory
from app.services.vectorstore.base import BaseVectoreStore
from app.events.models import EventCallback, EventType, RAGEvent


class QdrantVectorStore(BaseVectoreStore):

    def __init__(self):

        self.client = qdrant_client
        self.collection = settings.QDRANT_COLLECTION

    @property
    def store(self) -> LangChainQdrantVectorStore:

        return LangChainQdrantVectorStore(
            client=self.client,
            collection_name=self.collection,
            embedding=EmbeddingFactory.get_langchain_embedding(),
        )

    def create_collection(self) -> None:

        collections = self.client.get_collections().collections

        exists = any(
            collection.name == self.collection
            for collection in collections
        )

        if exists:
            return

        self.client.create_collection(
            collection_name=self.collection,
            vectors_config=VectorParams(
                size=settings.EMBEDDING_DIMENSION,
                distance=Distance.COSINE,
            ),
        )

    def delete_collection(self) -> None:

        self.client.delete_collection(
            collection_name=self.collection,
        )

    def add_documents(
        self,
        chunks: list[Document],
        on_event: EventCallback | None = None,
    ) -> None:

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.SYSTEM,
                    message=f"Generating embeddings for {len(chunks)} chunks...",
                )
            )

        self.store.add_documents(chunks)

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.SYSTEM,
                    message="Stored vectors in Qdrant.",
                )
            )

    def similarity_search(
        self,
        query: str,
        limit: int = 5,
    ) -> list[Document]:

        return self.store.similarity_search(
            query=query,
            k=limit,
        )

    def similarity_search_with_score(
        self,
        query: str,
        limit: int = 5,
    ):

        return self.store.similarity_search_with_score(
            query=query,
            k=limit,
        )

    def delete_document(
        self,
        document_id: str,
    ) -> None:

        self.client.delete(
            collection_name=self.collection,
            points_selector=Filter(
                must=[
                    FieldCondition(
                        key="document_id",
                        match=MatchValue(
                            value=document_id,
                        ),
                    )
                ]
            ),
        )