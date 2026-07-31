from langchain_huggingface import HuggingFaceEmbeddings
from app.services.embeddings.base import BaseEmbeddingProvider
from langchain_core.embeddings import Embeddings



class HuggingFaceEmbeddingProvider(BaseEmbeddingProvider):
    
    _embedding: HuggingFaceEmbeddings | None = None

    def __init__(self):
        
        if self.__class__._embedding is None: 

            self.__class__._embedding = HuggingFaceEmbeddings(
                model_name="BAAI/bge-small-en-v1.5",
                model_kwargs={
                    "device": "cpu",
                },
                encode_kwargs={
                    "normalize_embeddings": True,
                },
            )
            
        self._embedding = self.__class__._embedding

    def embed_documents(
        self,
        texts: list[str],
    ) -> list[list[float]]:

        return self._embedding.embed_documents(texts)

    def embed_query(
        self,
        text: str,
    ) -> list[float]:

        return self._embedding.embed_query(text)
    
    @property
    def langchain_embedding(self) -> Embeddings:
        return self._embedding