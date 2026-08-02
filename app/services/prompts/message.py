from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PromptMessage:
    role: str
    content: str