"""chunking.py — splits markdown text into overlapping token-aware chunks.

Why overlap?
  A chunk boundary can cut a sentence in half. With overlap, each chunk
  shares some tokens with the previous one, so no context is lost at edges.

Why token-based (not word-based)?
  Embedding models have a token limit (e5-large-v2: 512 tokens).
  Counting words is imprecise — one word can be 1-4 tokens.
"""

from typing import List, Dict
import tiktoken

from src.config import CHUNK_SIZE, CHUNK_OVERLAP

# cl100k_base is the tokenizer used by most modern models (GPT-4, e5, etc.)
_tokenizer = tiktoken.get_encoding("cl100k_base")


def chunk_text(text: str, source: str = "unknown") -> List[Dict]:
    """
    Split `text` into overlapping chunks of ~CHUNK_SIZE tokens.

    Args:
        text:   raw markdown content
        source: filename or identifier — stored as metadata in Qdrant

    Returns:
        list of dicts with keys: source, chunk_index, text
    """
    tokens = _tokenizer.encode(text)
    chunks = []
    i = 0
    chunk_index = 0

    while i < len(tokens):
        token_slice = tokens[i: i + CHUNK_SIZE]
        chunk_text_str = _tokenizer.decode(token_slice)
        chunks.append({
            "source": source,
            "chunk_index": chunk_index,
            "text": chunk_text_str,
        })
        chunk_index += 1
        i += CHUNK_SIZE - CHUNK_OVERLAP  # step forward by (size - overlap)

    return chunks
