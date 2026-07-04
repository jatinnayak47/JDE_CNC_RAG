from fastapi import APIRouter

from app.schemas.search import SearchRequest

from app.embeddings.embedding_service import (
    EmbeddingService
)

from app.vectorstore.qdrant_service import (
    QdrantService
)

router = APIRouter()


@router.post("/")
async def semantic_search(
    request: SearchRequest
):
    """
    Perform semantic search on indexed documents.
    """

    # Generate embedding for user query
    query_embedding = (
        EmbeddingService.generate_embedding(
            request.query
        )
    )

    # Search Qdrant
    results = QdrantService.search(
        query_embedding=query_embedding,
        top_k=request.top_k
    )

    response = []

    for result in results:

        response.append(
            {
                "score": result.score,
                "chunk_id": result.payload.get(
                    "chunk_id"
                ),
                "document_id": result.payload.get(
                    "document_id"
                ),
                "chunk_index": result.payload.get(
                    "chunk_index"
                ),
                "text": result.payload.get(
                    "text"
                )
            }
        )

    return {
        "query": request.query,
        "result_count": len(response),
        "results": response
    }