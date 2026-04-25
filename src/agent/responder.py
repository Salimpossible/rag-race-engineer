"""responder.py — sends the built prompt to Ollama and returns the answer.

Ollama exposes an OpenAI-compatible /v1/chat/completions endpoint.
We call it directly with httpx (no extra SDK needed).
"""

import httpx
import logging

from ..models import AgentOutput
from .state import AgentState
from .prompt_builder import build_prompt
from src.config import OLLAMA_URL, OLLAMA_MODEL

logger = logging.getLogger(__name__)


def respond(input_text: str, state: AgentState, task: str = "default") -> AgentOutput:
    """Retrieve context, build prompt, call Ollama, return structured output."""

    prompt = build_prompt(task, input_text)

    payload = {
        "model": OLLAMA_MODEL,
        "messages": [
            {"role": "system", "content": prompt["system"]},
            {"role": "user",   "content": prompt["user"]},
        ],
        "stream": False,
    }

    try:
        response = httpx.post(
            f"{OLLAMA_URL}/v1/chat/completions",
            json=payload,
            timeout=120.0,  # qwen2.5:7b on CPU can be slow
        )
        response.raise_for_status()
        answer = response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        logger.error(f"Ollama call failed: {e}")
        answer = "Sorry, I could not generate a response at this time."

    state.push("assistant", answer)
    return AgentOutput(title="Race Engineer", summary=answer)
