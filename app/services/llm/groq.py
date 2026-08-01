from groq import Groq

from app.core.config import settings
from app.services.llm.base import BaseLLM


class GroqLLM(BaseLLM):

    _client: Groq | None = None

    def __init__(self):

        if self.__class__._client is None:
            self.__class__._client = Groq(
                api_key=settings.GROQ_API_KEY,
            )

        self.client = self.__class__._client

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = self.client.chat.completions.create(
            model=settings.GROQ_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0,
        )

        return response.choices[0].message.content