from langchain_community.document_loaders import TextLoader
from langchain_core.documents import Document

from app.services.loaders.base import BaseDocumentLoader


class TextDocumentLoader(BaseDocumentLoader):

    def load(self, file_path: str) -> list[Document]:
        loader = TextLoader(file_path)
        return loader.load()