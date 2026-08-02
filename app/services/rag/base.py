from abc import ABC, abstractmethod
from app.events.models import EventCallback
from typing import Iterator
from app.services.chat.conversation import Message

class BaseRAGService(ABC):

    @abstractmethod
    def ask(
        self,
        question: str,
        history: list[Message],
        on_event: EventCallback | None = None,
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
        question: str,
        history: list[Message],
        on_event: EventCallback | None = None,
    ) -> Iterator[str]:
        ...