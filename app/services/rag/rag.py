from app.services.retrieval.factory import RetrieverFactory
from app.services.prompts.rag import RAGPromptBuilder
from app.services.llm.factory import LLMFactory

from app.services.rag.base import BaseRAGService
from collections.abc import Callable


class RAGService(BaseRAGService):

    def __init__(self):

        self.retriever = RetrieverFactory.get_retriever()

        self.prompt_builder = RAGPromptBuilder()

        self.llm = LLMFactory.get_llm()

    def ask(
        self,
        question: str,
        on_event: Callable[[str], None] | None = None,
    ) -> str:

        documents = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            query=question,
            documents=documents,
        )

        return self.llm.generate(prompt)
    
    
    def stream(
        self,
        question: str,
        on_event: Callable[[str], None] | None = None,
    ):

        if on_event:
            on_event("🔍 Searching knowledge base...")
            
        documents = self.retriever.retrieve(question)
        
        if on_event:
            on_event(f"✓ Retrieved {len(documents)} chunks")

        if on_event:
            on_event("🧠 Building prompt...")

        prompt = self.prompt_builder.build(
            query=question,
            documents=documents,
        )
        
        if on_event:
            on_event("🤖 Generating answer...")

        yield from self.llm.stream(prompt)
        
        if on_event:
            on_event("✅ Done")