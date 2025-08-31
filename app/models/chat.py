from pydantic import BaseModel, Field
from typing import List, Literal, Optional

class ChatMessage(BaseModel):
    role: Literal["user", "assistant", "system"] = Field(..., description="Message role")
    content: str = Field(..., description="Message content")

class ChatRequest(BaseModel):
    messages: List[ChatMessage] = Field(..., description="Conversation history")

class ChatResponse(BaseModel):
    reply: str = Field(..., description="Model-generated reply")
    usage_tokens: Optional[int] = Field(None, description="Number of tokens used")