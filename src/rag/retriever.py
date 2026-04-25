"""retriever.py — query-time retrieval: embed question → search Qdrant → return top-k chunks."""

import logging
from typing import List, Dict

from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import NamedVector, Query

from src.config import EMBEDDING_MODEL, QDRANT_URL, QDRANT_COLLECTION

logger = logging.getLogger(__name__)

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
    """Find the top-k most relevant chunks for a given query."""
    query_text = f"query: {query}"
    model = _get_model()
    query_vector = model.encode(query_text, normalize_embeddings=True).tolist()

    client = _get_client()
    # query_points() replaces the deprecated search() in qdrant-client >= 1.7
    results = client.query_points(
        collection_name=QDRANT_COLLECTION,
        query=query_vector,
        limit=top_k,
        with_payload=True,
    ).points

    return [
        {
            "source": hit.payload["source"],
            "chunk_index": hit.payload["chunk_index"],
            "text": hit.payload["text"],
            "score": round(hit.score, 4),
        }
        for hit in results
    ]
