from langchain_huggingface import HuggingFaceEmbeddings

from app.services.embeddings.base import BaseEmbeddingProvider


class HuggingFaceEmbeddingProvider(BaseEmbeddingProvider):

    def __init__(self):

        self._embedding = HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5",
            model_kwargs={
                "device": "cpu",
            },
            encode_kwargs={
                "normalize_embeddings": True,
            },
        )

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