from fastapi import APIRouter, Depends

from app.dependencies.company import get_company
from app.services.callModel import ChatService
from app.models.chat import ChatMessage
from app.services.session_management import create_new_session, get_chat_from_session, add_message_to_session



router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    dependencies=[Depends(get_company)]
)

chat = ChatService()


@router.get("/new")
async def create_new_chat():
    return create_new_session()


@router.post("/{chat_id}")
async def get_chat(chat_id: str, body: ChatMessage):
    if add_message_to_session(chat_id, "user", body.content) is False:
        return {"error": "Failed to add message to session"}
    response = await chat.chat(get_chat_from_session(chat_id))
    return {"message": response}