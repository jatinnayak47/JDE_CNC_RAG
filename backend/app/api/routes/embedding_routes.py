from fastapi import APIRouter

from app.embeddings.embedding_service import (
    EmbeddingService,
)
from app.ingestion.ingestion_service import (
    IngestionService,
)

router = APIRouter()


@router.post("/{document_id}")
async def generate_embeddings(
    document_id: str
):

    document = IngestionService.parse_document(
        document_id
    )

    chunks = document["chunks"]

    chunk_texts = [
        chunk["text"]
        for chunk in chunks
    ]

    embeddings = (
        EmbeddingService.generate_embeddings(
            chunk_texts
        )
    )

    embedded_chunks = []

    for chunk, embedding in zip(
        chunks,
        embeddings
    ):

        embedded_chunks.append(
            {
                **chunk,
                "embedding": embedding
            }
        )

    return {
        "document_id": document_id,
        "chunk_count": len(
            embedded_chunks
        ),
        "chunks": embedded_chunks
    }