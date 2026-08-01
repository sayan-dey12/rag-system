from app.services.retrieval.factory import RetrieverFactory
from app.services.prompts.rag import RAGPromptBuilder
from app.services.llm.factory import LLMFactory

from app.services.rag.base import BaseRAGService
from app.events.models import (
    EventType,
    RAGEvent,
    EventCallback,
)

class RAGService(BaseRAGService):

    def __init__(self):

        self.retriever = RetrieverFactory.get_retriever()

        self.prompt_builder = RAGPromptBuilder()

        self.llm = LLMFactory.get_llm()

    def ask(
        self,
        question: str,
        on_event: EventCallback | None = None,
    ) -> str:

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.RETRIEVAL,
                    message="Searching relevant documents...",
                )
            )

        documents = self.retriever.retrieve(question)

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.RETRIEVAL,
                    message=f"Retrieved {len(documents)} documents.",
                )
            )

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.PROMPT,
                    message="Building prompt...",
                )
            )

        prompt = self.prompt_builder.build(
            query=question,
            documents=documents,
        )

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.LLM,
                    message="Generating answer...",
                )
            )

        return self.llm.generate(prompt)
    
    def stream(
        self,
        question: str,
        on_event: EventCallback | None = None,
    ):

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.RETRIEVAL,
                    message="Searching relevant documents...",
                )
            )

        documents = self.retriever.retrieve(question)

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.RETRIEVAL,
                    message=f"Retrieved {len(documents)} documents.",
                )
            )

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.PROMPT,
                    message="Building prompt...",
                )
            )

        prompt = self.prompt_builder.build(
            query=question,
            documents=documents,
        )

        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.LLM,
                    message="Generating answer...",
                )
            )

        yield from self.llm.stream(prompt)