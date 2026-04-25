from fastapi import FastAPI
from .api.routes import router as agent_router
from .api.openai_routes import router as openai_router
from .logging_config import configure_logging

configure_logging()

app = FastAPI(title="RAG Race Engineer")

# Original agent API
app.include_router(agent_router, prefix="/agent", tags=["agent"])

# OpenAI-compatible API — used by Open WebUI and any OpenAI SDK client
app.include_router(openai_router, tags=["openai"])


@app.get("/health")
def health():
    return {"status": "ok"}
