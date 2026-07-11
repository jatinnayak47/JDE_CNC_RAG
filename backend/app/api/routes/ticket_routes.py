import os

from fastapi import (
    APIRouter,
    UploadFile,
    File
)

from app.tickets.ticket_service import (
    TicketService
)

router = APIRouter()

UPLOAD_DIR = "data/tickets"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


@router.post("/upload")
async def upload_ticket_file(
    file: UploadFile = File(...)
):

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(
        file_path,
        "wb"
    ) as f:
        f.write(
            await file.read()
        )

    return (
        TicketService.ingest_excel(
            file_path
        )
    )