Use retrieved chunks to ground answers. For each chunk include `source`, `score`, and `text`.

When composing final answers, cite the most relevant chunk(s) by `source`.

Example chunk structure:

```
{ "source": "file.md", "score": 0.92, "text": "..." }
```
