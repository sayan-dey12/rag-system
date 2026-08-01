from abc import ABC, abstractmethod

from langchain_core.documents import Document


class BasePromptBuilder(ABC):

    @abstractmethod
    def build(
        self,
        query: str,
        documents: list[Document],
    ) -> str:
        ...