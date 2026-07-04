import json
import os
import uuid
from datetime import UTC, datetime

from fastapi import APIRouter, File, HTTPException, UploadFile

from app.core.config import settings
from app.ingestion.ingestion_service import IngestionService

router = APIRouter()

REGISTRY_FILE = "data/registry.json"

ALLOWED_EXTENSIONS = {
    ".pdf",
    ".docx",
    ".txt"
}


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):
    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail=f"Unsupported file type: {extension}"
        )

    os.makedirs(
        settings.UPLOAD_DIR,
        exist_ok=True
    )

    document_id = str(uuid.uuid4())

    filename = f"{document_id}_{file.filename}"

    save_path = os.path.join(
        settings.UPLOAD_DIR,
        filename
    )

    content = await file.read()

    with open(save_path, "wb") as buffer:
        buffer.write(content)

    file_size = os.path.getsize(save_path)

    if not os.path.exists(REGISTRY_FILE):
        registry = {}
    else:
        with open(REGISTRY_FILE, "r") as registry_file:
            try:
                registry = json.load(
                    registry_file
                )
            except json.JSONDecodeError:
                registry = {}

    registry[document_id] = {
        "document_id": document_id,
        "filename": file.filename,
        "file_type": extension,
        "path": save_path,
        "file_size": file_size,
        "uploaded_at": datetime.now(
            UTC
        ).isoformat()
    }

    with open(
        REGISTRY_FILE,
        "w"
    ) as registry_file:
        json.dump(
            registry,
            registry_file,
            indent=4
        )

    return {
        "document_id": document_id,
        "filename": file.filename,
        "message": "File uploaded successfully"
    }


@router.post("/parse/{document_id}")
async def parse_document(
    document_id: str
):
    try:
        return IngestionService.parse_document(
            document_id
        )

    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )