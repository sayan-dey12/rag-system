from collections.abc import Iterator
from typing import TypeVar

from app.services.batching.base import BaseBatcher

T = TypeVar("T")


class Batcher(BaseBatcher[T]):

    def batch(
        self,
        items: list[T],
        batch_size: int,
    ) -> Iterator[list[T]]:

        if batch_size <= 0:
            raise ValueError(
                "batch_size must be greater than zero."
            )

        for start in range(0, len(items), batch_size):
            yield items[start : start + batch_size]