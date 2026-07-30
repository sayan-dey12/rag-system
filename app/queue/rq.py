from rq import Queue

from app.core.config import settings
from app.db.valkey import redis_client

queue = Queue(
    settings.RQ_QUEUE,
    connection=redis_client
)