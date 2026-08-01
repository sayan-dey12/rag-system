from app.services.loaders.factory import LoaderFactory
from app.services.chunking.chunker import DocumentChunker
#from app.services.embeddings.factory import EmbeddingFactory
from app.services.vectorstore.factory import VectorStoreFactory
from app.events.printer import print_event
from app.events.models import EventType, RAGEvent


def index_document(document_id: str, file_path: str, original_filename: str,) -> None:
    
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
        
        for chunk in chunks:
            chunk.metadata["document_id"] = document_id
            
            # Display name
            chunk.metadata["file_name"] = original_filename

            # Internal path (optional)
            chunk.metadata["storage_path"] = file_path
        
        # embedding_providers = EmbeddingFactory.get_provider()
        # texts = [chunk.page_content for chunk in chunks]
        # vectors = embedding_providers.embed_documents(texts)
        
        vector_store = VectorStoreFactory.get_store()
        vector_store.create_collection()
        vector_store.add_documents(
            chunks,
            on_event=print_event,
        )
        
        print("=" * 60)
        print("Indexing Completed")
        print(f"Document ID   : {document_id}")
        print(f"Pages Loaded  : {len(documents)}")
        print(f"Chunks Created: {len(chunks)}")
        print("Stored successfully in Qdrant.")
        print("=" * 60)
        # print(f"Vectors : {len(vectors)}")
        # print(f"Dimentions : {len(vectors[0])}")
        


        # for index, chunk in enumerate(chunks[:5]):
        #     print(f"\nChunk {index + 1}")
        #     print(chunk.page_content[:200])
        #     print(f"Metadata : {chunk.metadata}")
        #     print("-" * 40)
    
    except Exception as e:
        print(f"Failed to index document {document_id}: {e}")
        raise