from rq import Worker

from app.db.valkey import redis_client
from app.queue.rq import queue

worker = Worker(
    [queue],
    connection=redis_client,
)

if __name__ == "__main__":
    worker.work()