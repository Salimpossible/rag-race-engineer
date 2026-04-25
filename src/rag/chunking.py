from typing import List, Dict


def chunk_text(text: str, chunk_size: int = 200) -> List[Dict]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i : i + chunk_size])
        chunks.append({"source": "inline", "score": 1.0, "text": chunk})
        i += chunk_size
    return chunks
