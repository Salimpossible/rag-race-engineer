from fastapi import FastAPI
from .api.routes import router as api_router
from .logging_config import configure_logging

configure_logging()

app = FastAPI(title="AI Scaffold")
app.include_router(api_router, prefix="/agent", tags=["agent"])


@app.get("/health")
def health():
    return {"status": "ok"}
