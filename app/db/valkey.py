import redis

from app.core.config import settings

redis_client = redis.Redis(
    host=settings.VALKEY_HOST,
    port=settings.VALKEY_PORT,
    decode_responses=False,
)