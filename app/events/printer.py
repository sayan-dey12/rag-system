from app.events.models import EventType, RAGEvent


def print_event(event: RAGEvent) -> None:

    match event.type:

        case EventType.RETRIEVAL:
            print(f"🔍 {event.message}")

        case EventType.PROMPT:
            print(f"📝 {event.message}")

        case EventType.LLM:
            print(f"🤖 {event.message}")

        case EventType.TOOL:
            print(f"🛠️  {event.message}")

        case EventType.SYSTEM:
            print(f"⚙️  {event.message}")
            
        case EventType.DONE:
            print(f"✅ {event.message}")