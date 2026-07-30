from fastapi import FastAPI

from app.core.config import settings
from app.db.qdrant import qdrant_client
from app.db.valkey import redis_client

app = FastAPI(title=settings.APP_NAME)


@app.get("/")
def root():
    return {
        "message": settings.APP_NAME,
    }


@app.get("/health")
def health():

    redis_client.ping()

    qdrant_client.get_collections()

    return {
        "status": "healthy",
        "services": {
            "api": "ok",
            "valkey": "ok",
            "qdrant": "ok",
        },
    }