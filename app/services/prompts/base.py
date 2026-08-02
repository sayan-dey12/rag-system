from abc import ABC, abstractmethod

from langchain_core.documents import Document

from app.services.chat.conversation import Message


class BasePromptBuilder(ABC):

    @abstractmethod
    def build(
        self,
        query: str,
        history: list[Message],
        documents: list[tuple[Document, float]],
    ) -> str:
        ...