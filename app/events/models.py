from collections.abc import Callable
from dataclasses import dataclass, field
from enum import Enum
from time import time
from typing import Any


class EventType(str, Enum):

    RETRIEVAL = "retrieval"
    PROMPT = "prompt"
    LLM = "llm"
    TOOL = "tool"
    SYSTEM = "system"
    
    DONE = "done"
    ERROR = "error"  
    
    LOADER = "loader"
    CHUNKER = "chunker"
    EMBEDDING = "embedding"
    VECTORSTORE = "vectorstore"


@dataclass(slots=True, frozen=True)
class RAGEvent:

    type: EventType
    message: str

    data: dict[str, Any] = field(default_factory=dict)

    timestamp: float = field(default_factory=time)


type EventCallback = Callable[[RAGEvent], None]