from app.services.chat.base import BaseChatService
from app.services.chat.chat import ChatService


class ChatFactory:

    _service: BaseChatService | None = None

    @classmethod
    def get_service(cls) -> BaseChatService:

        if cls._service is None:
            cls._service = ChatService()

        return cls._service