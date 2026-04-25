Task: Classify

Given input text and a label set, return the best label and a short rationale. Prefer structured output:

```json
{ "label": "...", "confidence": 0.0, "reason": "..." }
```

If the input is ambiguous, return `"label": "unknown"` with an explanation.
