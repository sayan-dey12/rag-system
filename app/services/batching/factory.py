from app.services.batching.base import BaseBatcher
from app.services.batching.batcher import Batcher


class BatcherFactory:

    _batcher: BaseBatcher | None = None

    @classmethod
    def get_batcher(cls) -> BaseBatcher:

        if cls._batcher is None:
            cls._batcher = Batcher()

        return cls._batcher