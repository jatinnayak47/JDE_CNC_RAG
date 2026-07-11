from fastapi import FastAPI

from app.api.routes.document_routes import (
    router as document_router
)

from app.api.routes.embedding_routes import (
    router as embedding_router
)

from app.api.routes.vector_routes import (
    router as vector_router
)

from app.api.routes.search_routes import (
    router as search_router
)

from app.api.routes.rag_routes import (
    router as rag_router
)

from app.api.routes.chat_routes import (
    router as chat_router
)

from app.api.routes.ticket_routes import (
    router as ticket_router
)

from app.vectorstore.ticket_qdrant_service import (
    TicketQdrantService
)

app = FastAPI(
    title="JDE CNC RAG",
    version="1.0.0"
)


@app.on_event("startup")
async def startup_event():

    print("Starting JDE CNC RAG...")

    # Create ticket collection if it does not exist
    TicketQdrantService.create_collection()

    print("Ticket collection initialized")


app.include_router(
    document_router,
    prefix="/api/v1/documents",
    tags=["Documents"]
)

app.include_router(
    embedding_router,
    prefix="/api/v1/embeddings",
    tags=["Embeddings"]
)

app.include_router(
    vector_router,
    prefix="/api/v1/index",
    tags=["Vector Store"]
)

app.include_router(
    search_router,
    prefix="/api/v1/search",
    tags=["Search"]
)

app.include_router(
    rag_router,
    prefix="/api/v1/rag",
    tags=["RAG"]
)

app.include_router(
    chat_router,
    prefix="/api/v1/chat",
    tags=["Chat"]
)

app.include_router(
    ticket_router,
    prefix="/api/v1/tickets",
    tags=["Tickets"]
)


@app.get("/")
def root():
    return {
        "message": "JDE CNC RAG API Running"
    }