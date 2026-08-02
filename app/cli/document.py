from app.services.documents.factory import (
    DocumentManagerFactory,
)

def main() -> None:
    

    manager = DocumentManagerFactory.get_manager()

    documents = manager.list_documents()

    print("=" * 95)
    print("Indexed Documents")
    print("=" * 95)
    print()

    print(
        f"{'#':<4}"
        f"{'File Name':<60}"
        f"{'Chunks':>8}   "
        f"{'Document ID'}"
    )

    print("-" * 95)

    total_chunks = 0

    for index, document in enumerate(documents, start=1):

        total_chunks += document.chunk_count

        name = (
            document.file_name[:55] + "..."
            if len(document.file_name) > 58
            else document.file_name
        )

        print(
            f"{index:<4}"
            f"{name:<60}"
            f"{document.chunk_count:>8}   "
            f"{document.document_id[:8]}..."
        )

    print("-" * 95)
    print(f"Total Documents : {len(documents)}")
    print(f"Total Chunks    : {total_chunks}")
    print("=" * 95)