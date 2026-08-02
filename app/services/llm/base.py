from abc import ABC, abstractmethod
from typing import Iterator
from app.services.prompts.message import PromptMessage



class BaseLLM(ABC):

    @abstractmethod
    def generate(
        self,
         prompt: list[PromptMessage],
    ) -> str:
        ...

    @abstractmethod
    def stream(
        self,
         prompt: list[PromptMessage],
    ) -> Iterator[str]:
        ...