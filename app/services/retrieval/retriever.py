from langchain_core.documents import Document
from app.services.vectorstore.factory import VectorStoreFactory
from app.services.retrieval.base import BaseRetriever

class Retriever(BaseRetriever):
    
    def __init__(self):
        self.vector_store = VectorStoreFactory.get_store()
        
    def retriever(
        self,
        query: str,
        limit: int = 5
    ) -> list[Document]:
        return self.vector_store.similarity_search(
            query=query,
            limit=limit,
        )