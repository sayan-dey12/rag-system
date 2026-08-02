from abc import ABC, abstractmethod

from langchain_core.documents import Document

from app.services.chat.conversation import Message
from app.services.prompts.message import PromptMessage


class BasePromptBuilder(ABC):

    @abstractmethod
    def build(
        self,
        query: str,
        history: list[Message],
        documents: list[tuple[Document, float]],
    ) -> list[PromptMessage]:
        ...