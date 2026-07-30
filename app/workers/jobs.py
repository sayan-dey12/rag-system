from app.services.loaders.factory import LoaderFactory


def index_document(document_id: str, file_path: str):

    loader = LoaderFactory.get_loader(file_path)

    documents = loader.load(file_path)

    print("=" * 60)
    print(f"Document ID : {document_id}")
    print(f"Pages Loaded : {len(documents)}")

    for index, document in enumerate(documents):
        print(f"Page {index + 1}")
        print(document.page_content[:200])
        print("-" * 40)