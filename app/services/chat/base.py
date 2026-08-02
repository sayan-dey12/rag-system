from abc import ABC, abstractmethod
from collections.abc import Iterator

from app.events.models import EventCallback


class BaseChatService(ABC):

    @abstractmethod
    def ask(
        self,
        message: str,
        on_event: EventCallback | None = None,
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
        message: str,
        on_event: EventCallback | None = None,
    ) -> Iterator[str]:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...