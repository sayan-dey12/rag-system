from app.services.loaders.factory import LoaderFactory
from app.services.chunking.chunker import DocumentChunker
from app.services.embeddings.factory import EmbeddingFactory

def index_document(document_id: str, file_path: str):

    loader = LoaderFactory.get_loader(file_path)
    documents = loader.load(file_path)
    
    chunker = DocumentChunker()
    chunks = chunker.split(documents)
    
    embedding_providers = EmbeddingFactory.get_provider()
    texts = [chunk.page_content for chunk in chunks]
    vectors = embedding_providers.embed_documents(texts)

    print("=" * 60)
    print(f"Document ID : {document_id}")
    print(f"Pages Loaded : {len(documents)}")
    print(f"Chunks Created : {len(chunks)}")
    print(f"Vectors : {len(vectors)}")
    print(f"Dimentions : {len(vectors[0])}")
    


    for index, chunk in enumerate(chunks[:5]):
        print(f"\nChunk {index + 1}")
        print(chunk.page_content[:200])
        print(f"Metadata : {chunk.metadata}")
        print("-" * 40)