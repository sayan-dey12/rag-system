from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(slots=True)
class Message:
    role: str
    content: str


class Conversation:

    def __init__(self) -> None:
        self._messages: list[Message] = []

    def add_user(
        self,
        message: str,
    ) -> None:
        self._messages.append(
            Message(
                role="user",
                content=message,
            )
        )

    def add_assistant(
        self,
        message: str,
    ) -> None:
        self._messages.append(
            Message(
                role="assistant",
                content=message,
            )
        )

    def clear(self) -> None:
        self._messages.clear()

    def messages(self) -> list[Message]:
        return self._messages.copy()

    def __iter__(self) -> Iterator[Message]:
        return iter(self._messages)

    def __len__(self) -> int:
        return len(self._messages)