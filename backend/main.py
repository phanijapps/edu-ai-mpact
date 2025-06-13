import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from openai import AsyncOpenAI

app = FastAPI(title="Edu AI Mpact")

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

async def get_client() -> AsyncOpenAI:
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise RuntimeError("OPENROUTER_API_KEY not set")
    return AsyncOpenAI(api_key=api_key, base_url="https://openrouter.ai/api/v1")

@app.post("/api/chat", response_model=ChatResponse)
async def chat(req: ChatRequest, client: AsyncOpenAI = Depends(get_client)):
    try:
        completion = await client.chat.completions.create(
            model="openrouter/auto",
            messages=[{"role": "user", "content": req.message}]
        )
        return {"response": completion.choices[0].message.content}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
