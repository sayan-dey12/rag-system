from abc import ABC, abstractmethod
from collections.abc import Callable
from typing import Iterator


class BaseRAGService(ABC):

    @abstractmethod
    def ask(
        self,
        question: str,
        on_event: Callable[[str], None] | None = None,
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
        question: str,
        on_event: Callable[[str], None] | None = None,
    ) -> Iterator[str]:
        ...