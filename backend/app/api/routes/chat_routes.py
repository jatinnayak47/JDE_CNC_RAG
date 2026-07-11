from fastapi import APIRouter

from app.chat.chat_service import (
    ChatService
)

router = APIRouter()


@router.post("/clear")

async def clear_chat():

    ChatService.clear()

    return {
        "message":
            "Conversation history cleared."
    }