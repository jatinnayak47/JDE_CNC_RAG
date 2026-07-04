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


app = FastAPI(
    title="JDE CNC RAG",
    version="1.0.0"
)


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


@app.get("/")
def root():
    return {
        "message": "JDE CNC RAG API Running"
    }