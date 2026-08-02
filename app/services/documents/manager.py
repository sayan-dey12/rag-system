from app.services.documents.base import BaseDocumentManager
from app.services.documents.models import IndexedDocument
from app.services.vectorstore.factory import VectorStoreFactory


class DocumentManager(BaseDocumentManager):

    def __init__(self):

        self.vector_store = VectorStoreFactory.get_store()

    def list_documents(
        self,
    ) -> list[IndexedDocument]:

        return self.vector_store.list_documents()