from pydantic import BaseModel
from typing import Dict


class DocumentMetadata(BaseModel):
    filename: str
    file_type: str
    file_size: int


class DocumentResponse(BaseModel):
    document_id: str
    filename: str
    content: str
    metadata: Dict