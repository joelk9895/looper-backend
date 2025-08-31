from fastapi import APIRouter, Depends, Request
from httpx import request
from app.dependencies.company import get_company
from app.services.callModel import ChatService
from uuid import uuid4

router = APIRouter(
    prefix="/chat",
    tags=["chat"],
    dependencies=[Depends(get_company)]
)

chat = ChatService()
#TODO: Later move to redis
sessions = {}

@router.get("/new")
async def create_new_chat():
    chat_id = str(uuid4())
    sessions[chat_id] = [{"role": "system", "content": "You are a helpful assistant"}]
    return {"chat_id": chat_id}

@router.post("/{chat_id}")
async def get_chat(chat_id: str, request: Request):
    if chat_id not in sessions:
        return {"error": "Chat session not found"}
    data = await request.json()
    user_message = data.get("message")
    sessions[chat_id].append({"role": "user", "content": user_message})
    response = await chat.chat(sessions[chat_id])

    return {"message": response}
