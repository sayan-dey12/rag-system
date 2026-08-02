from app.events.models import EventType, RAGEvent


def print_event(event: RAGEvent) -> None:

    match event.type:

        case EventType.LOADER:
            print(f"📄 {event.message}")

        case EventType.CHUNKER:
            print(f"✂️  {event.message}")

        case EventType.EMBEDDING:
            print(f"🧠 {event.message}" , flush=True)

        case EventType.VECTORSTORE:
            print(f"🗄️  {event.message}" , flush=True)

        case EventType.RETRIEVAL:
            print(f"🔍 {event.message}")

        case EventType.PROMPT:
            print(f"📝 {event.message}")

        case EventType.LLM:
            print(f"🤖 {event.message}")

        case EventType.TOOL:
            print(f"🛠️  {event.message}")

        case EventType.DONE:
            print(f"\n✅ {event.message}")

        case EventType.ERROR:
            print(f"❌ {event.message}")
            
        case EventType.BATCH:
            print(f"📦 {event.message}" , flush=True)