from collections.abc import Iterator

from app.events.models import EventCallback
from app.services.chat.base import BaseChatService
from app.services.chat.conversation import Conversation
from app.services.rag.factory import RAGFactory


class ChatService(BaseChatService):

    def __init__(self):

        self.conversation = Conversation()

        self.rag = RAGFactory.get_service()

    def ask(
        self,
        message: str,
        on_event: EventCallback | None = None,
    ) -> str:
        ...

    def stream(
        self,
        message: str,
        on_event: EventCallback | None = None,
    ) -> Iterator[str]:
        ...

    def clear(self) -> None:

        self.conversation.clear()