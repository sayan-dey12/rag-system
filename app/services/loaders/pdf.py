from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document

from app.services.loaders.base import BaseDocumentLoader


class PDFDocumentLoader(BaseDocumentLoader):

    def load(self, file_path: str) -> list[Document]:
        loader = PyPDFLoader(file_path)
        return loader.load()