from app.services.llm.base import BaseLLM
from app.services.llm.groq import GroqLLM


class LLMFactory:

    _llm: BaseLLM | None = None

    @classmethod
    def get_llm(cls) -> BaseLLM:

        if cls._llm is None:
            cls._llm = GroqLLM()

        return cls._llm