from app.db.qdrant import qdrant_client
from app.services.vectorstore.base import BaseVectoreStore
from app.core.config import settings
from qdrant_client.models import Distance , VectorParams 
from langchain_core.documents import Document
from qdrant_client.models import Filter, FieldCondition, MatchValue
from langchain_qdrant import (
    QdrantVectorStore  as LangChainQdrantVectorStore
)
from app.services.embeddings.factory import EmbeddingFactory
from app.core.config import settings

class QdrantVectorStore(BaseVectoreStore):
    
    def __init__(self):
        self.client = qdrant_client
        self.collection = settings.QDRANT_COLLECTION
        
        self.store = LangChainQdrantVectorStore(
            client = self.client,
            collection_name = self.collection,
            embedding = EmbeddingFactory.get_langchain_embedding()
        )
        
        
    def create_collection(self):
        
        collections = self.client.get_collections().collections
        if any(
            c.name == self.collection
            for c in collections
        ):
            return
        
        self.client.create_collection(
            collection_name= self.collection,
            vectors_config = VectorParams(
                size = settings.EMBEDDING_DIMENSION,
                distance = Distance.COSINE
            ),                                                                       
        )
        
        
    def delete_collection(self) -> None:

        self.client.delete_collection(
            collection_name=self.collection
        )
        
        
    def add_documents(
        self,
        chunks: list[Document],
    ):

        self.store.add_documents(chunks)
        
    def similarity_search(
        self,
        query: str,
        limit: int = 5,
    ):

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