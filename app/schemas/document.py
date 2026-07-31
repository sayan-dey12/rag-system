from pydantic import BaseModel


class UploadResponse(BaseModel):
    document_id: str
    filename: str
    status: str


class DocumentMetadata(BaseModel):
    document_id: str
    filename: str
    content_type: str