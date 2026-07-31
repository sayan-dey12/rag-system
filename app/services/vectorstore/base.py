from abc import ABC , abstractmethod
from langchain_core.documents import Document

class BaseVectoreStore(ABC):
    
    @abstractmethod
    def create_collection(self) -> None:
        ...
        
    @abstractmethod
    def delete_colection(self, document_id: str) -> None:
        ...
        
    @abstractmethod
    def upsert(
        self,
        document_id: str,
        chunks: list[Document],
        vectors: list[list[float]],
    ) -> None:
        ...
        
    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
    ):
        ...
        