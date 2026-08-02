from abc import ABC, abstractmethod
from app.events.models import EventCallback
from typing import Iterator
from app.services.prompts.message import PromptMessage
class BaseRAGService(ABC):

    @abstractmethod
    def ask(
        self,
        question: str,
        history: list[PromptMessage],
        on_event: EventCallback | None = None,
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
        question: str,
        history: list[PromptMessage],
        on_event: EventCallback | None = None,
    ) -> Iterator[str]:
        ...