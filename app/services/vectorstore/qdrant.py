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

from qdrant_client.models import PointStruct
from qdrant_client.models import Document as QdrantQuery
from langchain_core.documents import Document

from collections import defaultdict

from app.services.documents.models import IndexedDocument

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
                    type=EventType.EMBEDDING,
                    message=f"Generating embeddings for {len(chunks)} chunks...",
                )
            )

        self.store.add_documents(chunks)

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.VECTORSTORE,
                    message="Stored vectors in Qdrant.",
                )
            )

    def similarity_search(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
    ) -> list[Document]:

        return self.store.similarity_search(
            query=query,
            k=limit,
        )

    def similarity_search_with_score(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
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
        
        
    def upsert(
        self,
        points: list[PointStruct],
        on_event: EventCallback | None = None,
    ) -> None:

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.VECTORSTORE,
                    message=f"Uploading {len(points)} vectors...",
                )
            )

        self.client.upsert(
            collection_name=self.collection,
            points=points,
            wait=True,
        )

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.VECTORSTORE,
                    message="Upload complete.",
                )
            )
            
    def search(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
    ) -> list[Document]:

        embedding_provider = EmbeddingFactory.get_provider()

        query_vector = embedding_provider.embed_query(query)

        response = self.client.query_points(
            collection_name=self.collection,
            query=query_vector,
            limit=limit,
            with_payload=True,
        )

        documents: list[Document] = []

        for point in response.points:

            payload = point.payload or {}

            documents.append(
                Document(
                    page_content=payload.get("text", ""),
                    metadata={
                        key: value
                        for key, value in payload.items()
                        if key != "text"
                    },
                )
            )

        return documents
    
    def search_with_score(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
        score_threshold: float | None = None,
    ) -> list[tuple[Document, float]]:

        embedding_provider = EmbeddingFactory.get_provider()

        query_vector = embedding_provider.embed_query(query)

        response = self.client.query_points(
            collection_name=self.collection,
            query=query_vector,
            limit=limit,
            with_payload=True,
        )

        results: list[tuple[Document, float]] = []

        for point in response.points:

            #
            # Skip weak matches (optional)
            #
            if (
                score_threshold is not None
                and point.score < score_threshold
            ):
                continue

            payload = point.payload or {}

            document = Document(
                page_content=payload.get("text", ""),
                metadata={
                    key: value
                    for key, value in payload.items()
                    if key != "text"
                },
            )

            results.append(
                (
                    document,
                    point.score,
                )
            )

        return results
    
    
    def list_documents(
        self,
    ) -> list[IndexedDocument]:

        grouped: dict[str, IndexedDocument] = {}

        offset = None

        while True:

            points, offset = self.client.scroll(
                collection_name=self.collection,
                with_payload=True,
                with_vectors=False,
                limit=256,
                offset=offset,
            )

            for point in points:

                payload = point.payload or {}

                document_id = payload.get("document_id")

                if document_id is None:
                    continue

                if document_id not in grouped:

                    grouped[document_id] = IndexedDocument(
                        document_id=document_id,
                        file_name=payload.get(
                            "file_name",
                            "Unknown",
                        ),
                        chunk_count=1,
                    )

                else:

                    current = grouped[document_id]

                    grouped[document_id] = IndexedDocument(
                        document_id=current.document_id,
                        file_name=current.file_name,
                        chunk_count=current.chunk_count + 1,
                    )

            if offset is None:
                break

        return sorted(
            grouped.values(),
            key=lambda doc: doc.file_name.lower(),
        )