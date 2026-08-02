from abc import ABC, abstractmethod

from langchain_core.documents import Document

from app.services.prompts.message import PromptMessage


class BasePromptBuilder(ABC):

    @abstractmethod
    def build(
        self,
        query: str,
        history: list[PromptMessage],
        documents: list[tuple[Document, float]],
    ) -> list[PromptMessage]:
        ...