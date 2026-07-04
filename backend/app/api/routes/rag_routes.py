from fastapi import APIRouter

from app.schemas.question import (
    QuestionRequest
)

from app.rag.rag_service import (
    RAGService
)

router = APIRouter()


@router.post("/ask")
async def ask_question(
    request: QuestionRequest
):

    return (
        RAGService.answer_question(
            question=request.question,
            top_k=request.top_k
        )
    )