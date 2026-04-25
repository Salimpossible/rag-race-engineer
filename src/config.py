import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

APP_ENV = os.getenv("APP_ENV", "development")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
AI_PROVIDER = os.getenv("AI_PROVIDER", "mock")
AI_MODEL = os.getenv("AI_MODEL", "mock-model")

# RAG — Embedding
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "intfloat/e5-large-v2")

# RAG — Chunking
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "400"))   # tokens per chunk
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", "80"))  # overlap in tokens

# RAG — Qdrant
QDRANT_URL = os.getenv("QDRANT_URL", "http://qdrant:6333")
QDRANT_COLLECTION = os.getenv("QDRANT_COLLECTION", "race_engineer")

# RAG — Knowledge base location
KNOWLEDGE_DIR = BASE_DIR / "knowledge" / "curated"

# LLM — Ollama
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://ollama:11434")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "qwen2.5:7b")
