from fastapi import APIRouter, HTTPException
import traceback

from app.ingestion.ingestion_service import (
    IngestionService
)

from app.embeddings.embedding_service import (
    EmbeddingService
)

from app.vectorstore.qdrant_service import (
    QdrantService
)

router = APIRouter()


@router.post("/{document_id}")
async def index_document(
    document_id: str
):

    try:

        print(
            f"\nIndexing document: {document_id}"
        )

        document = (
            IngestionService.parse_document(
                document_id
            )
        )

        print(
            "Document parsed successfully"
        )

        chunks = document["chunks"]

        print(
            f"Chunks found: {len(chunks)}"
        )

        texts = [
            chunk["text"]
            for chunk in chunks
        ]

        embeddings = (
            EmbeddingService.generate_embeddings(
                texts
            )
        )

        print(
            f"Embeddings generated: {len(embeddings)}"
        )

        if not embeddings:

            raise Exception(
                "No embeddings generated"
            )

        for chunk, embedding in zip(
            chunks,
            embeddings
        ):
            chunk["embedding"] = embedding

        vector_size = len(
            embeddings[0]
        )

        print(
            f"Vector dimension: {vector_size}"
        )

        QdrantService.create_collection(
            vector_size=vector_size
        )

        print(
            "Collection ready"
        )

        QdrantService.insert_chunks(
            chunks
        )

        print(
            "Vectors inserted successfully"
        )

        return {
            "status": "success",
            "document_id": document_id,
            "chunks_indexed": len(chunks)
        }

    except Exception as e:

        print(
            "\n========== INDEX ERROR =========="
        )

        traceback.print_exc()

        print(
            "=================================\n"
        )

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )