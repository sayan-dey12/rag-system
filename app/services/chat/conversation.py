from collections.abc import Iterator
from dataclasses import dataclass


@dataclass(slots=True)
class Message:
    role: str
    content: str


class Conversation:

    def __init__(self) -> None:
        self._messages: list[Message] = []

    def add_system(
        self,
        message: str,
    ) -> None:

        self._messages.append(
            Message(
                role="system",
                content=message,
            )
        )

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

    def remove_last(self) -> None:

        if self._messages:
            self._messages.pop()

    def clear(self) -> None:

        self._messages.clear()

    def messages(self) -> list[Message]:

        return self._messages.copy()

    def size(self) -> int:

        return len(self._messages)

    def is_empty(self) -> bool:

        return len(self._messages) == 0

    def __iter__(self) -> Iterator[Message]:

        return iter(self._messages)

    def __len__(self) -> int:

        return len(self._messages)