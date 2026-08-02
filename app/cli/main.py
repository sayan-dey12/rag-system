from app.cli.chat import main as chat
from app.cli.document import main as documents
from app.cli.upload import main as upload


def main() -> None:

    while True:

        print("\n" + "=" * 60)
        print("Mini RAG")
        print("=" * 60)
        print("1. Chat")
        print("2. Upload Document")
        print("3. List Documents")
        print("0. Exit")

        choice = input("\nSelect: ").strip()

        match choice:

            case "1":
                chat()

            case "2":
                upload()

            case "3":
                documents()

            case "0":
                print("\nBye!")
                break

            case _:
                print("\n❌ Invalid choice.")
                
                
if __name__ == "__main__":
    main()