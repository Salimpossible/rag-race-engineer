"""prompt_builder.py — builds the final prompt injecting RAG context.

Flow:
  1. Retrieve top-k chunks from Qdrant relevant to the user input
  2. Format them as a context block
  3. Inject into the system prompt so the LLM answers grounded in knowledge
"""

from pathlib import Path
from typing import Dict

from src.rag.retriever import retrieve


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""


def build_prompt(task: str, user_input: str) -> Dict[str, str]:
    """Build system + user prompt with RAG context injected.

    Returns a dict with `system` and `user` keys.
    """
    base = Path(__file__).resolve().parents[3]
    prompts_dir = base / "prompts"

    system_base = _read(prompts_dir / "system.md")
    task_prompt = _read(prompts_dir / "tasks" / f"{task}.md")

    # Retrieve relevant chunks from vector DB
    chunks = retrieve(user_input, top_k=5)
    context_block = "\n\n---\n\n".join(
        f"[Source: {c['source']}]\n{c['text']}" for c in chunks
    )

    system = f"""{system_base.strip()}

## Relevant Knowledge
Use the following context to answer the driver's question.
Only use information present in the context below.

{context_block}"""

    user = f"{task_prompt}\n\nInput:\n{user_input}".strip()

    return {"system": system, "user": user}
