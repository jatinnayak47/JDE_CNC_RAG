from pydantic import BaseModel
from typing import Dict


class Chunk(BaseModel):

    chunk_id: str

    document_id: str

    chunk_index: int

    text: str

    metadata: Dict