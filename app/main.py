from fastapi import FastAPI 
from .routers import chat, data

app = FastAPI()

app.include_router(chat.router)
app.include_router(data.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}