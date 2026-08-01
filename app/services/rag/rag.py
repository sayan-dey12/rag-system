from app.services.retrieval.factory import RetrieverFactory
from app.services.prompts.rag import RAGPromptBuilder
from app.services.llm.factory import LLMFactory

from app.services.rag.base import BaseRAGService


class RAGService(BaseRAGService):

    def __init__(self):

        self.retriever = RetrieverFactory.get_retriever()

        self.prompt_builder = RAGPromptBuilder()

        self.llm = LLMFactory.get_llm()

    def ask(
        self,
        question: str,
    ) -> str:

        documents = self.retriever.retrieve(question)

        prompt = self.prompt_builder.build(
            question=question,
            documents=documents,
        )

        return self.llm.generate(prompt)