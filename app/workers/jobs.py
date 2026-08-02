from math import ceil
from pathlib import Path

from app.core.config import settings
from app.events.models import EventType, RAGEvent
from app.events.printer import print_event
from app.services.batching.factory import BatcherFactory
from app.services.chunking.chunker import DocumentChunker
from app.services.embeddings.factory import EmbeddingFactory
from app.services.loaders.factory import LoaderFactory
from app.services.vectorstore.factory import VectorStoreFactory
from app.services.vectorstore.point_factory import PointBuilderFactory


def index_document(
    document_id: str,
    file_path: str,
    original_filename: str,
) -> None:

    try:

        print_event(
            RAGEvent(
                type=EventType.LOADER,
                message="Loading document...",
            )
        )

        loader = LoaderFactory.get_loader(file_path)
        documents = loader.load(file_path)

        print_event(
            RAGEvent(
                type=EventType.LOADER,
                message=f"Loaded {len(documents)} page(s).",
            )
        )

        if not documents:
            raise ValueError("No content found in the document.")

        chunker = DocumentChunker()

        chunks = chunker.split(
            documents,
            on_event=print_event,
        )

        if not chunks:
            raise ValueError("No chunks were generated.")

        #
        # Attach metadata
        #
        for index, chunk in enumerate(chunks):

            chunk.metadata["document_id"] = document_id

            chunk.metadata["file_name"] = original_filename

            chunk.metadata["storage_path"] = file_path

            chunk.metadata["chunk_index"] = index

            chunk.metadata["file_type"] = (
                Path(original_filename)
                .suffix
                .lower()
            )

        #
        # Initialize services
        #
        embedding_provider = EmbeddingFactory.get_langchain_embedding()

        point_builder = PointBuilderFactory.get_builder()

        vector_store = VectorStoreFactory.get_store()

        batcher = BatcherFactory.get_batcher()

        vector_store.create_collection()

        batch_size = settings.EMBEDDING_BATCH_SIZE

        total_batches = ceil(
            len(chunks) / batch_size
        )

        total_vectors = 0

        #
        # Process batches
        #
        for batch_number, chunk_batch in enumerate(
            batcher.batch(
                chunks,
                batch_size,
            ),
            start=1,
        ):

            print_event(
                RAGEvent(
                    type=EventType.EMBEDDING,
                    message=(
                        f"Embedding batch "
                        f"{batch_number}/{total_batches} "
                        f"({len(chunk_batch)} chunks)..."
                    ),
                )
            )

            texts = [
                chunk.page_content
                for chunk in chunk_batch
            ]

            vectors = embedding_provider.embed_documents(
                texts
            )

            total_vectors += len(vectors)

            print_event(
                RAGEvent(
                    type=EventType.EMBEDDING,
                    message=(
                        f"Embeddings generated "
                        f"for batch {batch_number}."
                    ),
                )
            )

            points = point_builder.build(
                chunk_batch,
                vectors,
            )

            vector_store.upsert(
                points,
                on_event=print_event,
            )

        print("=" * 60)
        print("Indexing Completed")
        print(f"Document ID   : {document_id}")
        print(f"Pages Loaded  : {len(documents)}")
        print(f"Chunks Created: {len(chunks)}")
        print(f"Vectors       : {total_vectors}")
        print(f"Batches       : {total_batches}")
        print("Stored successfully in Qdrant.")
        print("=" * 60)

    except Exception as e:
        print(f"Failed to index document {document_id}: {e}")
        raise