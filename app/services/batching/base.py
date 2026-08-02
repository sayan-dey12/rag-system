from abc import ABC, abstractmethod
from collections.abc import Iterator
from typing import Generic, TypeVar

T = TypeVar("T")


class BaseBatcher(ABC, Generic[T]):

    @abstractmethod
    def batch(
        self,
        items: list[T],
        batch_size: int,
    ) -> Iterator[list[T]]:
        ...