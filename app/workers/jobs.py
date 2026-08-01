from pathlib import Path

from app.events.models import EventType, RAGEvent
from app.events.printer import print_event
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

            # Human readable
            chunk.metadata["file_name"] = original_filename

            # Internal storage path
            chunk.metadata["storage_path"] = file_path

            # Extra metadata
            chunk.metadata["chunk_index"] = index
            chunk.metadata["file_type"] = Path(
                original_filename
            ).suffix.lower()

        #
        # Generate embeddings
        #
        print_event(
            RAGEvent(
                type=EventType.EMBEDDING,
                message=f"Generating embeddings for {len(chunks)} chunks...",
            )
        )

        embedding_provider = EmbeddingFactory.get_langchain_embedding()

        texts = [
            chunk.page_content
            for chunk in chunks
        ]

        vectors = embedding_provider.embed_documents(texts)

        print_event(
            RAGEvent(
                type=EventType.EMBEDDING,
                message="Embeddings generated.",
            )
        )

        #
        # Build Qdrant points
        #
        builder = PointBuilderFactory.get_builder()

        points = builder.build(
            chunks,
            vectors,
        )

        #
        # Store in Qdrant
        #
        vector_store = VectorStoreFactory.get_store()

        vector_store.create_collection()

        vector_store.upsert(
            points,
            on_event=print_event,
        )

        print("=" * 60)
        print("Indexing Completed")
        print(f"Document ID   : {document_id}")
        print(f"Pages Loaded  : {len(documents)}")
        print(f"Chunks Created: {len(chunks)}")
        print(f"Vectors       : {len(vectors)}")
        print("Stored successfully in Qdrant.")
        print("=" * 60)

    except Exception as e:
        print(f"Failed to index document {document_id}: {e}")
        raise