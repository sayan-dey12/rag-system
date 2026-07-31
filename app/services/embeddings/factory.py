from app.services.embeddings.huggingface import (
    HuggingFaceEmbeddingProvider,
)


class EmbeddingFactory:

    @staticmethod
    def get_provider():

        return HuggingFaceEmbeddingProvider()