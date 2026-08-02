from app.services.retrieval.factory import RetrieverFactory
from app.services.prompts.rag import RAGPromptBuilder
from app.services.llm.factory import LLMFactory

from app.services.rag.base import BaseRAGService
from app.events.models import (
    EventType,
    RAGEvent,
    EventCallback,
)

from app.services.prompts.message import PromptMessage

class RAGService(BaseRAGService):

    def __init__(self):

        self.retriever = RetrieverFactory.get_retriever()

        self.prompt_builder = RAGPromptBuilder()

        self.llm = LLMFactory.get_llm()

    def ask(
        self,
        question: str,
        history: list[PromptMessage],
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
        
        # print("=" * 80)
        # print(f"Retrieved {len(documents)} documents")
        # print("=" * 80)

        # for i, (doc, score) in enumerate(documents, start=1):
        #     print(f"\nResult {i}")
        #     print(f"Score: {score:.4f}")
        #     print("Metadata:", doc.metadata)
        #     print(doc.page_content[:500])
        #     print("-" * 80)

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
            history=history,
            documents=documents,
        )
        
        # print(prompt)

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
        history: list[PromptMessage],
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
        
        # print("=" * 80)
        # print(f"Retrieved {len(documents)} documents")
        # print("=" * 80)

        # for i, (doc, score) in enumerate(documents, start=1):
        #     print(f"\nResult {i}")
        #     print(f"Score: {score:.4f}")
        #     print("Metadata:", doc.metadata)
        #     print(doc.page_content[:500])
        #     print("-" * 80)

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
            history=history,
            documents=documents,
        )

        # print("=" * 80)
        # print(prompt)
        # print("=" * 80)
        
        
        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.LLM,
                    message="Generating answer...",
                )
            )

        yield from self.llm.stream(prompt)
        
        if on_event:
            on_event(
                RAGEvent(
                    type=EventType.DONE,
                    message="Finished...",
                )
            )