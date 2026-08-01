from abc import ABC, abstractmethod


class BaseRAGService(ABC):

    @abstractmethod
    def ask(
        self,
        question: str,
    ) -> str:
        ...