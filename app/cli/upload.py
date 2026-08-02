from pathlib import Path

import requests


API_URL = "http://localhost:8000/documents"


def main() -> None:

    print("=" * 60)
    print("Upload Document")
    print("=" * 60)

    while True:

        try:

            file_path = input("\nFile path ('exit' to quit): ").strip()

            if file_path.lower() in {
                "exit",
                "quit",
            }:
                break

            path = Path(file_path)

            if not path.exists():
                print("❌ File not found.")
                continue

            if not path.is_file():
                print("❌ Path is not a file.")
                continue

            print("⬆️  Uploading...")

            with path.open("rb") as file:

                response = requests.post(
                    API_URL,
                    files={
                        "file": (
                            path.name,
                            file,
                            "application/octet-stream",
                        )
                    },
                    timeout=300,
                )

            if response.status_code == 202:

                data = response.json()

                print("\n✅ Upload queued successfully.")
                print(f"Document ID : {data['document_id']}")
                print(f"File        : {data['filename']}")
                print(f"Status      : {data['status']}")

            else:

                print(
                    f"\n❌ Upload failed "
                    f"({response.status_code})"
                )

                try:
                    print(response.json())
                except Exception:
                    print(response.text)

        except KeyboardInterrupt:

            print("\nBye!")
            break

        except Exception as e:

            print(f"\nError: {e}")