# Mini RAG

<p align="center">
  <img src="docs/images/logo.png" alt="Mini RAG Logo" width="180"/>
</p>

<p align="center">
  <strong>A production-style Retrieval-Augmented Generation (RAG) system built from scratch using FastAPI, Qdrant, HuggingFace Embeddings, Groq LLM, RQ and Docker.</strong>
</p>

<p align="center">
  Upload your own knowledge base, build a vector database, and chat with your documents through a conversation-aware RAG pipeline.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-009688?logo=fastapi)
![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-red)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![Docker](https://img.shields.io/badge/Docker-Container-blue?logo=docker)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

# ✨ Overview

Mini RAG is a modular Retrieval-Augmented Generation system that demonstrates how a modern AI-powered document assistant can be built from first principles.

Instead of relying entirely on high-level frameworks, this project implements the entire RAG pipeline as independent services—from document ingestion and chunking to embeddings, vector storage, retrieval, prompt construction, conversation management, and streaming responses.

The project focuses on **clean architecture**, **scalability**, and **extensibility**, making it an excellent starting point for building production-ready AI systems.

---

# 🚀 Features

## 📄 Document Processing

- Upload PDF documents through FastAPI
- Background indexing using RQ workers
- Automatic document loading
- Recursive document chunking
- Rich metadata generation
- Batch document processing
- Automatic collection creation
- Delete indexed documents

---

## 🧠 Embeddings

- HuggingFace embedding models
- Configurable embedding provider
- Batch embedding generation
- Embedding abstraction layer
- Easy provider replacement

---

## 🗄️ Vector Database

- Qdrant integration
- Batch vector uploads
- Manual vector construction
- Rich metadata payloads
- Similarity search
- Similarity search with scores
- Score threshold filtering
- Collection management

---

## 💬 Retrieval-Augmented Generation

- Semantic document retrieval
- Conversation-aware prompting
- Session memory
- Prompt engineering
- Streaming LLM responses
- Source citations
- Retrieval score filtering

---

## ⚙️ Architecture

- Service-oriented architecture
- Factory pattern
- Dependency inversion
- Event-driven progress reporting
- Modular components
- Replaceable providers
- Clean separation of concerns

---

## 🖥 CLI

Interactive CLI for

- Chat
- Document listing
- Future utilities

---

## 🌐 REST API

- FastAPI
- Swagger UI
- Async upload endpoint
- Background indexing
- Validation using Pydantic

---

## 🐳 DevOps

- Docker Compose
- Separate API
- Separate Worker
- Qdrant container
- Valkey container
- Environment-based configuration

---

# 🎯 Why this project?

Many RAG tutorials only show a few lines of LangChain code.

This project takes a different approach.

Every major stage has been designed as an independent service with its own responsibility.

Instead of writing:

```
Loader
↓

VectorStore.from_documents(...)
↓

Done
```

the pipeline is fully modular.

```
Upload

↓

Loader

↓

Chunker

↓

Metadata Generator

↓

Batch Processor

↓

Embedding Provider

↓

Point Builder

↓

Vector Store

↓

Retriever

↓

Prompt Builder

↓

LLM

↓

Streaming Response
```

This architecture makes every component independently replaceable, testable, and reusable.

---

# 🏗 Architecture

## High-Level Architecture

```text
                        User
                          │
             ┌────────────┴────────────┐
             │                         │
             ▼                         ▼
        FastAPI API                 CLI Chat
             │                         │
             │                         ▼
             │                  Chat Service
             │                         │
             ▼                         ▼
      Background Queue          Conversation
             │                         │
             ▼                         ▼
         RQ Worker  ─────────────► RAG Service
             │                         │
             ▼                         ▼
         Document Loader         Retriever
             │                         │
             ▼                         ▼
        Document Chunker      Prompt Builder
             │                         │
             ▼                         ▼
      Batch Processing           Groq LLM
             │                         │
             ▼                         ▼
      Embedding Provider      Streaming Response
             │
             ▼
        Point Builder
             │
             ▼
          Qdrant
```

---

## Document Indexing Pipeline

```text
PDF

↓

Loader

↓

Documents

↓

Chunker

↓

Chunks

↓

Metadata

↓

Batcher

↓

Embeddings

↓

Point Builder

↓

Qdrant
```

---

## Retrieval Pipeline

```text
Question

↓

Query Embedding

↓

Vector Search

↓

Score Filtering

↓

Retrieved Documents

↓

Prompt Builder

↓

Groq LLM

↓

Streaming Answer
```

---

## Conversation Flow

```text
User Message

↓

Conversation Memory

↓

Retriever

↓

Prompt Builder

↓

System Prompt

+

Conversation History

+

Retrieved Context

+

Current Question

↓

Groq

↓

Assistant Response

↓

Conversation Updated
```

---

# 🧩 Technology Stack

| Layer | Technology |
|--------|------------|
| Language | Python 3.12 |
| API | FastAPI |
| Validation | Pydantic |
| Queue | RQ |
| Broker | Valkey |
| Vector Database | Qdrant |
| LLM | Groq |
| Embeddings | HuggingFace |
| Chunking | LangChain |
| Vector Search | Qdrant Client |
| Containers | Docker |
| Configuration | dotenv |
| CLI | Python |

---

# 📂 Project Structure

```text
app
│
├── api/
│   ├── routes/
│   ├── dependencies/
│   └── lifespan.py
│
├── cli/
│   ├── chat.py
│   ├── document.py
│   ├── upload.py
│   └── main.py
│
├── core/
│   ├── config.py
│   └── constants.py
│
├── db/
│   ├── qdrant.py
│   └── valkey.py
│
├── events/
│   ├── models.py
│   └── printer.py
│
├── schemas/
│
├── services/
│   ├── batching/
│   ├── chat/
│   ├── chunking/
│   ├── documents/
│   ├── embeddings/
│   ├── llm/
│   ├── loaders/
│   ├── prompts/
│   ├── rag/
│   ├── retrieval/
│   └── vectorstore/
│
├── workers/
│
├── uploads/
│
└── main.py
```

---

# 📁 Folder Responsibilities

## `api/`

Contains all REST API routes and request handling logic.

---

## `cli/`

Interactive command-line interface used for chatting and project utilities.

---

## `core/`

Application configuration, settings, constants, and shared configuration.

---

## `db/`

Database clients and connection management.

- Qdrant
- Valkey

---

## `events/`

Centralized event models and progress reporting.

Every major operation (loading, chunking, embedding, uploading, retrieval) emits structured events.

---

## `services/`

The heart of the application.

Every feature is implemented as an isolated service.

Examples:

- Loader
- Chunker
- Embedding Provider
- Retriever
- Prompt Builder
- Chat
- RAG
- Vector Store
- Document Manager

Each service follows a common interface and can easily be replaced.

---

## `workers/`

Background jobs executed by RQ workers.

Heavy operations such as document indexing never block the API.

---

## `uploads/`

Temporary storage for uploaded documents before indexing.

---

# 🎨 Design Principles

This project follows several software engineering principles.

- Single Responsibility Principle
- Dependency Inversion
- Factory Pattern
- Modular Design
- Service-Oriented Architecture
- Event-Driven Communication
- Separation of Concerns
- Replaceable Components

Every service has exactly one responsibility.

No service knows how another service is implemented internally.

This makes replacing the LLM, embedding model, vector database, or prompt builder extremely straightforward.

---
# ⚙️ Installation

## Prerequisites

Before running the project, make sure the following tools are installed.

| Tool | Version |
|------|---------|
| Python | 3.12+ |
| Docker Desktop | Latest |
| Docker Compose | Latest |
| uv | Latest |
| Git | Latest |

---

## Clone the Repository

```bash
git clone https://github.com/<your-username>/mini-rag.git

cd mini-rag
```

---

## Install Dependencies

This project uses **uv** for dependency management.

```bash
uv sync
```

or

```bash
uv pip install -r requirements.txt
```

---

# 🐳 Docker Setup

The application consists of multiple services.

| Service | Description |
|----------|-------------|
| API | FastAPI Backend |
| Worker | Background document indexing |
| Qdrant | Vector Database |
| Valkey | Queue Broker |

Start everything using Docker Compose.

```bash
docker compose up -d
```

To verify:

```bash
docker compose ps
```

Expected services:

```
api
worker
qdrant
valkey
```

---

## Stop Services

```bash
docker compose down
```

---

## View Logs

API

```bash
docker compose logs -f api
```

Worker

```bash
docker compose logs -f worker
```

Qdrant

```bash
docker compose logs -f qdrant
```

---

# 🔑 Environment Variables

Create a `.env` file in the project root.

Example:

```env
# ==========================
# Groq
# ==========================

GROQ_API_KEY=your_api_key
GROQ_MODEL=llama-3.3-70b-versatile

# ==========================
# Embeddings
# ==========================

EMBEDDING_MODEL=BAAI/bge-small-en-v1.5
EMBEDDING_DIMENSION=384
EMBEDDING_BATCH_SIZE=128

# ==========================
# Retrieval
# ==========================

RETRIEVAL_TOP_K=10
RETRIEVAL_SCORE_THRESHOLD=0.75

# ==========================
# Qdrant
# ==========================

QDRANT_HOST=qdrant
QDRANT_PORT=6333
QDRANT_COLLECTION=rag_system

# ==========================
# Valkey
# ==========================

VALKEY_HOST=valkey
VALKEY_PORT=6379

# ==========================
# Uploads
# ==========================

UPLOAD_DIR=app/uploads
```

---

# 🚀 Running the Project

Start Docker first.

```bash
docker compose up -d
```

After the containers are running, launch the application.

```bash
uv run python run.py
```

or

```bash
uv run python -m app.cli.main
```

This opens the interactive CLI.

```
============================================================
Mini RAG
============================================================

1. Chat
2. Upload Document
3. List Documents
0. Exit
```

---

# 🌐 REST API

Once the API container is running, open

```
http://localhost:8000/docs
```

Swagger UI provides an interactive interface for testing every endpoint.

---

## Upload a Document

```
POST /documents
```

Upload a supported file.

The API immediately returns.

Example response:

```json
{
  "document_id": "4f2b2d0d-4d88-4d52-bd8d-a4d5d24fd84d",
  "filename": "book.pdf",
  "status": "queued"
}
```

Document indexing happens asynchronously in the background worker.

---

## Health Check

```
GET /health
```

Returns the application health status.

Example:

```json
{
  "status": "ok"
}
```

---

# 💻 CLI

The project includes a lightweight interactive CLI.

Launch it with

```bash
uv run python run.py
```

Main menu:

```
============================================================
Mini RAG
============================================================

1. Chat
2. Upload Document
3. List Documents
0. Exit
```

---

## Chat

Start a conversation with your indexed knowledge base.

```
You > Explain Big O

Assistant >

Big O describes the upper bound of an algorithm's time complexity...
```

Features

- Streaming responses
- Conversation memory
- Source citations
- Session-based chat

---

## Upload Document

You can upload documents using Swagger.

```
http://localhost:8000/docs
```

Choose the `/documents` endpoint and upload your file.

The API returns immediately while the worker indexes the document in the background.

---

## List Documents

Displays every indexed document.

Example

```
===============================================================================================

Indexed Documents

===============================================================================================

#   File Name                                                   Chunks   Document ID

-----------------------------------------------------------------------------------------------

1   Cracking-the-Coding-Interview.pdf                            2287    d01eb2d7...

2   Designing-Data-Intensive-Applications.pdf                    1834    87e5d913...

-----------------------------------------------------------------------------------------------

Total Documents : 2

Total Chunks    : 4121

===============================================================================================
```

---

# 📁 Supported File Types

| Extension | Supported |
|-----------|-----------|
| PDF | ✅ |
| TXT | ✅ |
| Markdown (.md) | ✅ |

Adding support for additional document formats only requires implementing another loader.

---

# 📦 Background Processing

Document indexing never blocks the API.

```
Upload Request

↓

API

↓

RQ Queue

↓

Worker

↓

Processing

↓

Indexed
```

The upload endpoint returns immediately.

The worker performs:

- Document loading
- Chunking
- Metadata generation
- Batch embedding
- Point construction
- Vector upload

---

# 📡 Streaming Responses

Chat responses stream token-by-token from the LLM.

```
User

↓

Retriever

↓

Prompt Builder

↓

Groq

↓

Streaming Tokens

↓

CLI
```

This provides a much more responsive user experience than waiting for the full response.

---

# 📊 Progress Events

Long-running operations emit progress events.

Example:

```
📄 Loading document...

📄 Loaded 712 page(s).

✂️ Splitting document into chunks...

✂️ Created 2287 chunks.

📦 Processing 2287 chunks in 18 batches.

📦 Starting batch 1/18...

🧠 Generating embeddings...

🗄 Uploading vectors...

📦 Completed batch 1/18.

...

✅ Indexing completed successfully.
```

This makes it easy to monitor indexing progress in real time.

---

# 🧪 Development Workflow

Typical development cycle.

```bash
# Start infrastructure
docker compose up -d

# Run the application
uv run python run.py

# Upload documents
http://localhost:8000/docs

# Start chatting
Mini RAG → Chat
```

---

# 🛠 Troubleshooting

## Docker is not running

Start Docker Desktop before launching the project.

---

## No documents found

Verify that the worker has completed indexing successfully.

---

## Empty responses

Ensure:

- Documents are indexed.
- Retrieval score threshold is not too strict.
- Qdrant contains vectors.

---

## Groq authentication error

Check:

```
GROQ_API_KEY
```

in your `.env` file.

---

## Embedding model downloads every run

The HuggingFace model is cached after the first download.

The initial run may take slightly longer.

---
# 🧠 How Mini RAG Works

This section explains the complete Retrieval-Augmented Generation (RAG) pipeline implemented in this project, from document upload to answer generation.

Rather than relying on a single framework call, every stage of the pipeline has been designed as an independent service. This makes the system easier to understand, test, replace, and extend.

---

# 📄 Document Indexing Pipeline

When a user uploads a document, it goes through several stages before becoming searchable.

```text
                Upload Document
                       │
                       ▼
              Background Queue
                       │
                       ▼
                  RQ Worker
                       │
                       ▼
                Document Loader
                       │
                       ▼
                 Raw Documents
                       │
                       ▼
             Recursive Chunking
                       │
                       ▼
               Metadata Injection
                       │
                       ▼
                Batch Processing
                       │
                       ▼
              Embedding Generation
                       │
                       ▼
                 Point Builder
                       │
                       ▼
               Batch Vector Upload
                       │
                       ▼
                    Qdrant
```

---

# 📥 1. Document Loading

The first stage detects the document type and selects the appropriate loader.

Current supported formats:

- PDF
- TXT
- Markdown

Because loaders are abstracted behind a factory, adding another format only requires implementing a new loader.

Example:

```
book.pdf

↓

PDFLoader

↓

List[Document]
```

---

# ✂️ 2. Chunking

Large documents cannot be embedded directly.

Instead, they are split into smaller semantic chunks.

```
712 Pages

↓

Recursive Character Splitter

↓

2287 Chunks
```

Chunking improves:

- Retrieval accuracy
- Embedding quality
- Context utilization
- LLM performance

The chunk size and overlap can be configured independently.

---

# 🏷 3. Metadata Generation

Every chunk receives metadata before being indexed.

Example metadata:

```json
{
    "document_id": "...",
    "file_name": "book.pdf",
    "storage_path": "...",
    "chunk_index": 57,
    "page": 103,
    "file_type": ".pdf"
}
```

Metadata enables:

- Source citation
- Document management
- Filtering
- Future hybrid search
- Delete-by-document support

---

# 📦 4. Batch Processing

Instead of processing thousands of chunks simultaneously, the system processes them in batches.

```
2287 Chunks

↓

128

↓

128

↓

128

↓

...

↓

111
```

This dramatically reduces memory usage.

Advantages:

- Lower RAM consumption
- Better scalability
- Faster uploads
- Better progress reporting
- Easier parallelization in the future

Batch size is configurable.

```env
EMBEDDING_BATCH_SIZE=128
```

---

# 🧠 5. Embedding Generation

Each batch is converted into dense vector embeddings using HuggingFace models.

```
Text

↓

Embedding Model

↓

384-dimensional Vector
```

Current embedding model:

```
BAAI/bge-small-en-v1.5
```

The embedding provider is abstracted, making it easy to replace with:

- OpenAI
- VoyageAI
- Nomic
- Jina
- Ollama
- Custom models

without changing the indexing pipeline.

---

# 📍 6. Point Builder

Instead of relying on LangChain's automatic document insertion, the project constructs Qdrant points manually.

Each point contains:

```text
Point

├── id

├── vector

└── payload

      ├── text

      ├── document_id

      ├── file_name

      ├── page

      ├── chunk_index

      └── ...
```

This approach gives complete control over:

- payload structure
- metadata
- filtering
- retrieval
- future features

---

# 🗄 7. Vector Upload

Generated points are uploaded in batches.

```
128 Points

↓

Qdrant

↓

Stored
```

Each batch is uploaded independently.

If a failure occurs, only the current batch is affected.

---

# 📚 Indexed Document

A fully indexed document now exists as thousands of searchable vectors.

```
Book

↓

2287 Chunks

↓

2287 Embeddings

↓

2287 Points

↓

Qdrant Collection
```

---

# 🔍 Retrieval Pipeline

When the user asks a question, another pipeline begins.

```
User Question

↓

Embedding

↓

Vector Search

↓

Score Filtering

↓

Relevant Documents

↓

Prompt Builder

↓

LLM

↓

Streaming Answer
```

---

# 1. Query Embedding

The user question is embedded using the **same embedding model** used during indexing.

```
"What is Big O?"

↓

Embedding Model

↓

384-dimensional Query Vector
```

Using the same embedding space ensures semantic similarity.

---

# 2. Vector Search

The query vector is sent to Qdrant.

```
Query Vector

↓

Cosine Similarity

↓

Top K Results
```

Example:

```
Top K = 20
```

Qdrant returns:

```
Chunk

Score

Metadata
```

---

# 3. Score Threshold Filtering

Returning the nearest neighbors is not enough.

Sometimes the nearest document is still unrelated.

Therefore every result passes through a score filter.

```
Retrieved

↓

Score >= Threshold

↓

Accepted
```

Example:

```
0.91

Accepted

----------------

0.82

Accepted

----------------

0.41

Rejected
```

This prevents hallucinations caused by irrelevant context.

Configured via:

```env
RETRIEVAL_SCORE_THRESHOLD=0.75
```

---

# 4. Prompt Construction

The Prompt Builder combines four sources of information.

```
System Prompt

+

Conversation History

+

Retrieved Context

+

Current Question
```

↓

Prompt

The prompt builder is completely isolated from retrieval logic.

Changing prompt engineering never requires changing retrieval code.

---

# 💬 Conversation Memory

Mini RAG supports **session-based conversation memory**.

```
User

↓

Conversation

↓

Assistant

↓

Conversation

↓

User

↓

Conversation

↓

...
```

The conversation is stored **only in memory**.

No database is used.

When the session ends:

```
Conversation

↓

Destroyed
```

This keeps the implementation lightweight while enabling follow-up questions.

Example:

```
User

What is BFS?

↓

Assistant

...

↓

User

How is it different from DFS?
```

The second question automatically uses previous conversation history.

---

# 📝 Prompt Structure

Every request sent to the LLM contains:

```text
System Prompt

Conversation History

Retrieved Context

Current Question
```

The system prompt defines:

- assistant behavior
- citation rules
- hallucination prevention
- response format

---

# 🤖 LLM Generation

The constructed prompt is sent to Groq.

```
Prompt

↓

Groq

↓

Streaming Tokens
```

Streaming provides much faster perceived response time.

Instead of waiting for the entire answer, tokens arrive continuously.

---

# 📚 Source Citations

Every answer includes citations.

Example:

```
Sources

File:

Cracking the Coding Interview.pdf

Page:

38

Page:

39
```

This allows users to verify where information originated.

---

# 🔄 Complete RAG Flow

```text
User Question
        │
        ▼
Conversation
        │
        ▼
Embedding
        │
        ▼
Qdrant Search
        │
        ▼
Score Filter
        │
        ▼
Retrieved Chunks
        │
        ▼
Prompt Builder
        │
        ▼
System Prompt
Conversation
Retrieved Context
Current Question
        │
        ▼
Groq
        │
        ▼
Streaming Response
        │
        ▼
Conversation Updated
```

---

# 📢 Event System

Long-running operations emit structured events.

Examples:

```
📄 Loading document...

✂️ Splitting document...

🧠 Generating embeddings...

📦 Processing batch 7/18...

🗄 Uploading vectors...

🔍 Searching relevant documents...

📝 Building prompt...

🤖 Generating answer...
```

Benefits:

- Real-time progress
- Decoupled logging
- Better debugging
- Cleaner services

---

# 🧩 Factory Pattern

Almost every subsystem is accessed through a factory.

```
EmbeddingFactory

↓

Embedding Provider
```

```
LoaderFactory

↓

PDF Loader
```

```
VectorStoreFactory

↓

Qdrant
```

```
RetrieverFactory

↓

Retriever
```

Advantages:

- Loose coupling
- Easy testing
- Easy dependency replacement
- Better scalability

---

# 🛡 Error Handling

Critical operations are protected with exception handling.

If an error occurs during chat:

- the last user message is removed
- conversation state remains consistent

If indexing fails:

- the exception propagates
- worker logs the failure
- API remains responsive

---

# 🎯 Design Goals

The architecture was designed around several principles:

- Build every component from first principles.
- Keep each service focused on one responsibility.
- Make every dependency replaceable.
- Avoid tightly coupled business logic.
- Keep prompt engineering independent of retrieval.
- Allow future expansion without major refactoring.

This modular design makes it straightforward to add features such as hybrid search, reranking, OCR, image retrieval, local LLMs, or multi-user sessions while preserving the existing architecture.

---
# 🎯 Design Decisions

Every architectural decision in Mini RAG was made with three goals in mind:

- **Understand the internals of a RAG system**
- **Keep the architecture modular**
- **Make every component easily replaceable**

Rather than building a quick proof-of-concept, the project was designed as a foundation for future AI applications.

---

# 🏛 Software Architecture

Mini RAG follows a **layered, service-oriented architecture**.

```
Presentation Layer

↓

Application Services

↓

Business Logic

↓

Infrastructure

↓

External Services
```

Each layer has a single responsibility and communicates through well-defined abstractions.

---

# 🧩 Why Factory Pattern?

Every major dependency is accessed through a factory.

Example:

```
EmbeddingFactory

↓

Embedding Provider
```

instead of

```python
provider = HuggingFaceEmbedding(...)
```

This allows the application to swap implementations without modifying business logic.

Current factories include:

- LoaderFactory
- EmbeddingFactory
- RetrieverFactory
- PromptFactory
- VectorStoreFactory
- ChatFactory
- DocumentManagerFactory
- BatcherFactory

Advantages

- Dependency inversion
- Loose coupling
- Better testing
- Cleaner services
- Easier provider replacement

---

# 🔄 Why Service Classes?

Every feature is implemented as a service.

Examples:

```
ChatService

RAGService

Retriever

DocumentManager

VectorStore

EmbeddingProvider

Chunker

Loader
```

Each service performs one job only.

This follows the **Single Responsibility Principle (SRP)**.

---

# 📦 Why Batch Processing?

Generating embeddings for thousands of chunks at once can consume a large amount of memory and increase latency.

Instead, the project processes chunks in configurable batches.

```
2287 Chunks

↓

128

↓

128

↓

128

↓

...
```

Benefits

- Lower memory usage
- Better scalability
- Faster indexing
- Real-time progress reporting
- Future parallel processing support

---

# 📍 Why Manual Qdrant Points?

LangChain provides a convenient method for storing documents directly in Qdrant.

However, Mini RAG builds Qdrant points manually.

Instead of

```
Documents

↓

VectorStore.add_documents()
```

the project performs

```
Documents

↓

Embeddings

↓

Point Builder

↓

Points

↓

Qdrant
```

Advantages

- Full payload control
- Custom metadata
- Rich filtering
- Easier debugging
- Framework independence

---

# 🗂 Why Store Metadata?

Each chunk stores additional metadata such as

- Document ID
- File Name
- Page
- Chunk Index
- File Type
- Storage Path

Metadata enables

- Source citations
- Document management
- Filtering
- Future multi-document search
- Delete-by-document support

---

# 🔍 Why Score Threshold Filtering?

Vector databases always return the nearest vectors.

Nearest does **not** always mean **relevant**.

Without filtering

```
Question

↓

Top 20

↓

Always accepted
```

With filtering

```
Question

↓

Top 20

↓

Score Filter

↓

Relevant Context
```

This greatly reduces hallucinations.

---

# 💬 Why Session Memory?

Conversation memory exists only while the chat session is active.

```
User

↓

Conversation

↓

Assistant

↓

Conversation

↓

Exit

↓

Memory Destroyed
```

No conversation is stored permanently.

Advantages

- Lightweight
- Privacy-friendly
- No additional database
- Easy reset

---

# 📝 Why Prompt Builder?

Prompt engineering evolves frequently.

Instead of embedding prompts inside business logic, Mini RAG isolates prompt construction.

```
Retriever

↓

Prompt Builder

↓

LLM
```

Changing prompts never affects retrieval or vector search.

---

# 📡 Why Streaming?

Instead of waiting several seconds for an entire answer,

```
User

↓

Wait...

↓

Complete Response
```

Mini RAG streams responses.

```
User

↓

Token

↓

Token

↓

Token

↓

Completed
```

Benefits

- Better user experience
- Faster perceived latency
- More interactive chat

---

# 🎉 Key Features

✅ Modular architecture

✅ Service-oriented design

✅ Factory pattern

✅ Conversation-aware RAG

✅ Batch embedding generation

✅ Batch vector uploads

✅ Manual Qdrant integration

✅ Streaming responses

✅ Source citations

✅ Session memory

✅ Score threshold filtering

✅ Background indexing

✅ Rich metadata

✅ Event-driven progress reporting

---

# 📈 Current Capabilities

- Upload PDF, TXT and Markdown documents
- Automatic document chunking
- Batch embedding generation
- Semantic vector search
- Conversation-aware retrieval
- Streaming chat
- Document listing
- Source attribution
- Background indexing with RQ
- Docker deployment
- Interactive CLI
- REST API

---

# 🚀 Future Roadmap

The current implementation serves as a strong foundation for more advanced retrieval and agent capabilities.

## Retrieval

- [ ] Hybrid Search (BM25 + Dense Retrieval)
- [ ] Cross Encoder Re-ranking
- [ ] Metadata Filtering
- [ ] Multi-Collection Search
- [ ] Multi-Vector Retrieval
- [ ] Parent-Child Retrieval
- [ ] Context Compression
- [ ] Automatic Query Rewriting

---

## Documents

- [ ] DOCX Support
- [ ] HTML Support
- [ ] EPUB Support
- [ ] PowerPoint Support
- [ ] OCR for Images
- [ ] Image Extraction
- [ ] Table Extraction

---

## Chat

- [ ] Persistent Conversation Memory
- [ ] Multiple Chat Sessions
- [ ] Chat History Export
- [ ] Conversation Summarization
- [ ] Follow-up Question Optimization

---

## AI

- [ ] Local LLM Support (Ollama)
- [ ] OpenAI Support
- [ ] Anthropic Support
- [ ] Gemini Support
- [ ] Multiple Embedding Providers
- [ ] Automatic Model Selection

---

## Agents

- [ ] Tool Calling
- [ ] Web Search
- [ ] Calculator
- [ ] Python Code Execution
- [ ] SQL Tool
- [ ] Browser Automation
- [ ] File Editing

---

## API

- [ ] Chat REST API
- [ ] Streaming API (SSE)
- [ ] Authentication
- [ ] User Accounts
- [ ] Rate Limiting

---

## Frontend

- [ ] React Dashboard
- [ ] Drag-and-Drop Upload
- [ ] Chat Interface
- [ ] Document Manager
- [ ] Search UI
- [ ] Analytics Dashboard

---

# 🤝 Contributing

Contributions are welcome!

If you'd like to improve Mini RAG:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature/amazing-feature
```

3. Commit your changes.

```bash
git commit -m "Add amazing feature"
```

4. Push the branch.

```bash
git push origin feature/amazing-feature
```

5. Open a Pull Request.

Please ensure new features follow the existing architecture and coding style.

---

# 📚 Learning Objectives

This project was built to deeply understand how modern Retrieval-Augmented Generation systems work internally.

Rather than treating RAG as a black box, the goal is to explore and implement each component independently, including:

- Document ingestion
- Chunking strategies
- Embedding generation
- Vector storage
- Semantic retrieval
- Prompt engineering
- Conversation memory
- Streaming inference
- Background processing
- Clean software architecture

---

# 🙏 Acknowledgements

This project builds upon several excellent open-source technologies.

- FastAPI
- LangChain
- Qdrant
- HuggingFace
- Groq
- Docker
- RQ
- Valkey

Special thanks to the communities maintaining these tools and libraries.

---

# 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project under the terms of the license.

See the `LICENSE` file for details.

---

# ⭐ Support

If you found this project useful:

- ⭐ Star the repository
- 🍴 Fork it
- 🐛 Report issues
- 💡 Suggest new features
- 🤝 Contribute improvements

Your support helps make the project better for everyone.

---

# 👨‍💻 Author

**Sayan Dey**

Backend Developer • AI Engineer • DevOps Enthusiast

- 🌐 Portfolio: https://techwithstrider.vercel.app
- 💼 LinkedIn: https://linkedin.com/in/sayan-dey-b37843378
- 🐙 GitHub: https://github.com/sayan-dey12

---

<p align="center">
Built with ❤️ to understand Retrieval-Augmented Generation from first principles.
</p>