from pathlib import Path

from app.services.loaders.base import BaseDocumentLoader
from app.services.loaders.markdown import MarkdownDocumentLoader
from app.services.loaders.pdf import PDFDocumentLoader
from app.services.loaders.text import TextDocumentLoader


class LoaderFactory:

    _loaders = {
        ".pdf": PDFDocumentLoader,
        ".txt": TextDocumentLoader,
        ".md": MarkdownDocumentLoader,
    }

    @classmethod
    def get_loader(cls, file_path: str) -> BaseDocumentLoader:
        extension = Path(file_path).suffix.lower()

        loader = cls._loaders.get(extension)

        if loader is None:
            raise ValueError(f"Unsupported file type: {extension}")

        return loader()