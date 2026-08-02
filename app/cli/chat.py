from app.events.printer import print_event
from app.services.chat.factory import ChatFactory


def main() -> None:

    chat = ChatFactory.get_service()

    print("=" * 60)
    print("Mini RAG Chat")
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        try:

            question = input("\nYou > ").strip()

            if not question:
                continue

            if question.lower() in {
                "exit",
                "quit",
            }:
                break

            print("\nAssistant > ", end="", flush=True)

            first_token = True

            for token in chat.stream(
                question,
                on_event=print_event,
            ):

                if first_token:
                    print("\nAssistant > ", end="", flush=True)
                    first_token = False

                print(token, end="", flush=True)

            print()

        except KeyboardInterrupt:

            print("\nBye!")
            break

        except Exception as e:

            print(f"\nError: {e}")