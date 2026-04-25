# Multi-stage build — keeps final image lean

# --- Stage 1: dependency install ---
FROM python:3.11-slim AS builder

WORKDIR /app

# Install build deps
RUN apt-get update && apt-get install -y --no-install-recommends gcc && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml .
# Install only runtime deps (no dev extras)
RUN pip install --no-cache-dir --prefix=/install \
    fastapi \
    uvicorn \
    "pydantic<2" \
    pyyaml \
    jsonschema \
    sentence-transformers \
    qdrant-client \
    tiktoken \
    httpx

# --- Stage 2: final image ---
FROM python:3.11-slim

WORKDIR /app

# Copy installed packages from builder
COPY --from=builder /install /usr/local

# Copy source code
COPY src/ ./src/
COPY prompts/ ./prompts/
COPY knowledge/ ./knowledge/

ENV PYTHONPATH=/app
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
