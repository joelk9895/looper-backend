import redis
import json
from uuid import uuid4
from datetime import timedelta

from app.core.config import settings
from app.core.db import r

MAX_MESSAGES = 50
SESSION_TTL = timedelta(hours=3)

def create_new_session():
    chat_id = str(uuid4())
    system_message = {"role": "system", "content": "You are a helpful assistant"}
    r.rpush(chat_id, json.dumps(system_message))
    r.expire(chat_id, SESSION_TTL)
    return {"chat_id": chat_id}

def get_chat_from_session(chat_id: str):
    messages = r.lrange(chat_id, 0, -1)
    if messages:
        r.expire(chat_id, SESSION_TTL)
    return [json.loads(msg) for msg in messages]

def add_message_to_session(chat_id: str, role: str, content: str):
    message = {"role": role, "content": content}
    if r.exists(chat_id):
        if r.llen(chat_id) >= MAX_MESSAGES:
            r.lpop(chat_id)
        r.rpush(chat_id, json.dumps(message))
        r.expire(chat_id, SESSION_TTL)
        return True
    return False