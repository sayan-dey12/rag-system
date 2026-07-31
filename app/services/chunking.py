from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


class DocumentChunker:
    """
    Splits LangChain Documents into smaller chunks.
    """

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self._splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            add_start_index=True,
        )

    def split(
        self,
        documents: list[Document],
    ) -> list[Document]:
        return self._splitter.split_documents(documents)