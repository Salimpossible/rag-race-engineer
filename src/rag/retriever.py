"""retriever.py — query-time retrieval: embed question → search Qdrant → return top-k chunks.

Flow:
  1. Prepend "query: " prefix (required by e5 models for queries — different from "passage: ")
  2. Embed the question with the same model used during ingestion
  3. Search Qdrant for the top-k nearest vectors (cosine similarity)
  4. Return the chunk texts + metadata for injection into the LLM prompt
"""

import logging
from typing import List, Dict

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient

from src.config import EMBEDDING_MODEL, QDRANT_URL, QDRANT_COLLECTION

logger = logging.getLogger(__name__)

# Module-level singletons — loaded once, reused across requests
_model: SentenceTransformer | None = None
_client: QdrantClient | None = None


def _get_model() -> SentenceTransformer:
    global _model
    if _model is None:
        logger.info(f"Loading embedding model: {EMBEDDING_MODEL}")
        _model = SentenceTransformer(EMBEDDING_MODEL)
    return _model


def _get_client() -> QdrantClient:
    global _client
    if _client is None:
        _client = QdrantClient(url=QDRANT_URL)
    return _client


def retrieve(query: str, top_k: int = 5) -> List[Dict]:
    """
    Find the top-k most relevant chunks for a given query.

    Args:
        query:  the driver's question or issue description
        top_k:  number of chunks to retrieve (default 5)

    Returns:
        list of dicts with keys: source, chunk_index, text, score
    """
    # e5 models require "query: " prefix for questions (asymmetric retrieval)
    query_text = f"query: {query}"
    model = _get_model()
    query_vector = model.encode(query_text, normalize_embeddings=True).tolist()

    client = _get_client()
    results = client.search(
        collection_name=QDRANT_COLLECTION,
        query_vector=query_vector,
        limit=top_k,
        with_payload=True,
    )

    return [
        {
            "source": hit.payload["source"],
            "chunk_index": hit.payload["chunk_index"],
            "text": hit.payload["text"],
            "score": round(hit.score, 4),
        }
        for hit in results
    ]
