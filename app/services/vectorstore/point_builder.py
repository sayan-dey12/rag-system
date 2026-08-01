from uuid import uuid4

from langchain_core.documents import Document
from qdrant_client.models import PointStruct


class PointBuilder:

    def build(
        self,
        chunks: list[Document],
        vectors: list[list[float]],
    ) -> list[PointStruct]:

        if len(chunks) != len(vectors):
            raise ValueError(
                "Number of chunks and embeddings must match."
            )

        points: list[PointStruct] = []

        for chunk, vector in zip(chunks, vectors):

            points.append(
                PointStruct(
                    id=str(uuid4()),
                    vector=vector,
                    payload={
                        "text": chunk.page_content,
                        **chunk.metadata,
                    },
                )
            )

        return points