"""openai_routes.py — OpenAI-compatible /v1/chat/completions endpoint.

This makes the RAG stack look like a standard OpenAI model to any client
(Open WebUI, curl, Python openai SDK, etc.).

Request format (OpenAI standard):
  POST /v1/chat/completions
  { "model": "rag-race-engineer", "messages": [{"role": "user", "content": "..."}] }

Response format (OpenAI standard):
  { "choices": [{"message": {"role": "assistant", "content": "..."}}], ... }
"""

import time
import uuid
import httpx
import logging

from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Optional

from src.agent.prompt_builder import build_prompt
from src.config import OLLAMA_URL, OLLAMA_MODEL

logger = logging.getLogger(__name__)
router = APIRouter()


# --- OpenAI-compatible request/response models ---

class ChatMessage(BaseModel):
    role: str      # "system", "user", or "assistant"
    content: str


class ChatCompletionRequest(BaseModel):
    model: str
    messages: List[ChatMessage]
    temperature: Optional[float] = 0.7
    stream: Optional[bool] = False


class ChatCompletionResponse(BaseModel):
    id: str
    object: str = "chat.completion"
    created: int
    model: str
    choices: list


# --- Helper: extract last user message ---

def _get_user_input(messages: List[ChatMessage]) -> str:
    """Return the last user message content."""
    for msg in reversed(messages):
        if msg.role == "user":
            return msg.content
    return ""


# --- Endpoint ---

@router.post("/v1/chat/completions")
def chat_completions(request: ChatCompletionRequest):
    user_input = _get_user_input(request.messages)

    # RAG: retrieve context + build grounded prompt
    prompt = build_prompt(task="default", user_input=user_input)

    # Call Ollama with the enriched prompt
    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": prompt["system"]},
            {"role": "user",   "content": prompt["user"]},
        ],
        "stream": False,
        "temperature": request.temperature,
    }

    try:
        response = httpx.post(
            f"{OLLAMA_URL}/v1/chat/completions",
            json=payload,
            timeout=120.0,
        )
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"Ollama call failed: {e}")
        answer = "Sorry, I could not generate a response at this time."

    # Return OpenAI-compatible response
    return {
        "id": f"chatcmpl-{uuid.uuid4().hex}",
        "object": "chat.completion",
        "created": int(time.time()),
        "model": request.model,
        "choices": [
            {
                "index": 0,
                "message": {"role": "assistant", "content": answer},
                "finish_reason": "stop",
            }
        ],
        "usage": {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0},
    }


# --- Model list endpoint (required by Open WebUI to discover available models) ---

@router.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "rag-race-engineer",
                "object": "model",
                "created": 1700000000,
                "owned_by": "local",
            }
        ],
    }
