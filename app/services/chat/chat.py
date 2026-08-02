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
        
        #save user message
        self.conversation.add_user(message)
        #ask rag
        
        try:
            
            answer = self.rag.ask(
                question=message,
                history=self.conversation.messages(),
                on_event=on_event,
            )
        except Exception:
            self.conversation.remove_last_user()
            raise
        
        #save assistant message
        self.conversation.add_assistant(answer)

        return answer

    def stream(
        self,
        message: str,
        on_event: EventCallback | None = None,
    ) -> Iterator[str]:

        #
        # Save user message
        #
        self.conversation.add_user(message)

        response_parts: list[str] = []

        try:
            
            for token in self.rag.stream(
                question=message,
                history=self.conversation.messages(),
                on_event=on_event,
            ):

                response_parts.append(token)

                yield token
        
        except Exception:
            self.conversation.remove_last_user()
            raise

        #
        # Save completed assistant response
        #
        self.conversation.add_assistant(
            "".join(response_parts)
        )
        
    
    def clear(self) -> None:
        self.conversation.clear()