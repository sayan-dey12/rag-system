import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.queue.rq import queue
from app.schemas.document import UploadResponse
from app.workers.jobs import index_document

router = APIRouter(prefix="/documents", tags=["Documents"])

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".md",
}


@router.post(
    "",
    response_model=UploadResponse,
    status_code=status.HTTP_202_ACCEPTED,
)
def upload_document(file: UploadFile = File(...)):

    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported file type.",
        )

    document_id = str(uuid4())

    saved_path = UPLOAD_DIR / f"{document_id}{extension}"

    print(f"UPLOAD_DIR = {UPLOAD_DIR.resolve()}")
    print(f"SAVING TO = {saved_path.resolve()}")

    with saved_path.open("wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    print(f"EXISTS = {saved_path.exists()}")

    absolute_path = saved_path.resolve()
    queue.enqueue(
        index_document,
        document_id,
        str(absolute_path),
        file.filename,
    )

    return UploadResponse(
        document_id=document_id,
        filename=file.filename,
        status="queued",
    )