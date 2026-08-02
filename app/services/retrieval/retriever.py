from langchain_core.documents import Document

from app.services.retrieval.base import BaseRetriever
from app.services.vectorstore.factory import VectorStoreFactory
from app.core.config import settings

class Retriever(BaseRetriever):

    def __init__(self):
        self.vector_store = VectorStoreFactory.get_store()

    def retrieve(
        self,
        query: str,
        limit: int = settings.RETRIEVAL_TOP_K,
    ) -> list[tuple[Document, float]]:

        # return self.vector_store.similarity_search_with_score(
        #     query=query,
        #     limit=limit,
        # )
        
        return self.vector_store.search_with_score(
            query=query,
            limit=limit,
            score_threshold=settings.RETRIEVAL_SCORE_THRESHOLD
        )