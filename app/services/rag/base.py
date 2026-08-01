from abc import ABC, abstractmethod
from app.events.models import EventCallback
from typing import Iterator


class BaseRAGService(ABC):

    @abstractmethod
    def ask(
        self,
        question: str,
        on_event: EventCallback | None = None,
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
        question: str,
        on_event: EventCallback | None = None,
    ) -> Iterator[str]:
        ...