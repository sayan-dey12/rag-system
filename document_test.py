from app.services.documents.factory import (
    DocumentManagerFactory,
)

manager = DocumentManagerFactory.get_manager()

documents = manager.list_documents()

for document in documents:

    print(document)