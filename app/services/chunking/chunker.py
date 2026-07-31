from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.config import settings

class DocumentChunker:
    """
    Splits LangChain Documents into smaller chunks.
    """

    def __init__(self,):
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
             separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
            length_function=len,
            add_start_index=True,
        )

    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:
        return self._splitter.split_documents(documents)