from app.services.prompts.base import BasePromptBuilder
from app.services.prompts.rag import RAGPromptBuilder


class PromptFactory:

    _builder: BasePromptBuilder | None = None

    @classmethod
    def get_builder(cls) -> BasePromptBuilder:

        if cls._builder is None:
            cls._builder = RAGPromptBuilder()

        return cls._builder