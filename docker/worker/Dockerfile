FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml .

RUN pip install uv

RUN uv pip install --system \
    redis \
    rq \
    qdrant-client

COPY . .

CMD [
    "python",
    "-m",
    "app.workers.worker"
]