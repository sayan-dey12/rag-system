from abc import ABC, abstractmethod
from typing import Iterator


class BaseLLM(ABC):

    @abstractmethod
    def generate(
        self,
        prompt: str,
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
        prompt: str,
    ) -> Iterator[str]:
        ...