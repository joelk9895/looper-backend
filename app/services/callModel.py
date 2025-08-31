from openai import OpenAI
from typing import List, Dict
from app.core.config import settings

class ChatService:
    def __init__(self):
        self.client = OpenAI(
            base_url=settings.OPENROUTER_BASE_URL,
            api_key=settings.OPENROUTER_API_KEY,
        )

    async def chat(self, messages: List[Dict[str, str]], model: str = "openai/gpt-4o") -> str:
        """
        Send a list of messages to the model and return the response.
        messages: [{"role": "system"|"user"|"assistant", "content": "..."}]
        """
        completion = await self.client.chat.completions.create(
            model=model,
            messages=messages
        )
        return completion.choices[0].message.content