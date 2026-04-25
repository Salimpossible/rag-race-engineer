"""ingest.py — full ingestion pipeline: load → chunk → embed → upsert to Qdrant.

Flow:
  1. Read every .md file from KNOWLEDGE_DIR
  2. Chunk each file with overlap (chunking.py)
  3. Batch-embed all chunks using e5-large-v2
     Note: e5 models expect a "passage: " prefix for documents (not queries)
  4. Upsert vectors + metadata into Qdrant

Run once to populate the vector DB. Re-run after adding new .md files.
"""

import uuid
import logging
from pathlib import Path
from typing import List, Dict

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct

from src.config import (
    EMBEDDING_MODEL,
    QDRANT_URL,
    QDRANT_COLLECTION,
    KNOWLEDGE_DIR,
)
from src.rag.chunking import chunk_text

logger = logging.getLogger(__name__)

# e5-large-v2 outputs 1024-dimensional vectors
EMBEDDING_DIM = 1024
BATCH_SIZE = 32  # chunks per embedding batch — tune down if OOM


def _load_documents(knowledge_dir: Path) -> List[Dict]:
    """Read all .md files and return list of {source, text} dicts."""
    docs = []
    for md_file in sorted(knowledge_dir.glob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        docs.append({"source": md_file.name, "text": text})
        logger.info(f"Loaded: {md_file.name} ({len(text)} chars)")
    return docs


def _ensure_collection(client: QdrantClient) -> None:
    """Create the Qdrant collection if it doesn't exist yet."""
    existing = [c.name for c in client.get_collections().collections]
    if QDRANT_COLLECTION not in existing:
        client.create_collection(
            collection_name=QDRANT_COLLECTION,
            vectors_config=VectorParams(size=EMBEDDING_DIM, distance=Distance.COSINE),
        )
        logger.info(f"Created Qdrant collection: {QDRANT_COLLECTION}")
    else:
        logger.info(f"Collection already exists: {QDRANT_COLLECTION}")


def run_ingestion() -> None:
    """Entry point — call this to ingest all knowledge documents."""
    logger.info("Starting ingestion pipeline")

    # 1. Load documents
    docs = _load_documents(KNOWLEDGE_DIR)
    if not docs:
        logger.warning(f"No .md files found in {KNOWLEDGE_DIR}")
        return

    # 2. Chunk all documents
    all_chunks: List[Dict] = []
    for doc in docs:
        chunks = chunk_text(doc["text"], source=doc["source"])
        all_chunks.extend(chunks)
    logger.info(f"Total chunks to embed: {len(all_chunks)}")

    # 3. Embed — e5 models require "passage: " prefix for documents
    model = SentenceTransformer(EMBEDDING_MODEL)
    texts_to_embed = [f"passage: {c['text']}" for c in all_chunks]

    embeddings = []
    for i in range(0, len(texts_to_embed), BATCH_SIZE):
        batch = texts_to_embed[i: i + BATCH_SIZE]
        batch_embeddings = model.encode(batch, normalize_embeddings=True)
        embeddings.extend(batch_embeddings)
        logger.info(f"Embedded batch {i // BATCH_SIZE + 1}/{-(-len(texts_to_embed) // BATCH_SIZE)}")

    # 4. Upsert to Qdrant
    client = QdrantClient(url=QDRANT_URL)
    _ensure_collection(client)

    points = [
        PointStruct(
            id=str(uuid.uuid4()),
            vector=embeddings[idx].tolist(),
            payload={
                "source": chunk["source"],
                "chunk_index": chunk["chunk_index"],
                "text": chunk["text"],
            },
        )
        for idx, chunk in enumerate(all_chunks)
    ]

    client.upsert(collection_name=QDRANT_COLLECTION, points=points)
    logger.info(f"Upserted {len(points)} vectors into '{QDRANT_COLLECTION}'")


if __name__ == "__main__":
    logging.basicConfig(level="INFO")
    run_ingestion()
