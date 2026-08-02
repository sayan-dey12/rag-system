from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class IndexedDocument:

    document_id: str

    file_name: str

    chunk_count: int