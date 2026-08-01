from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from app.core.config import settings
from app.events.models import EventCallback, EventType, RAGEvent

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
        on_event: EventCallback | None = None,
    ) -> list[Document]:

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.SYSTEM,
                    message="Splitting document into chunks...",
                )
            )

        chunks = self._splitter.split_documents(documents)

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.SYSTEM,
                    message=f"Created {len(chunks)} chunks.",
                )
            )

        return chunks