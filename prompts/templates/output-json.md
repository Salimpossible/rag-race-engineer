When a structured JSON output is requested, follow this wrapper:

```
{ "title": "...", "summary": "...", "sections": [ {"heading":"...","body":"..."} ] }
```

Ensure the JSON conforms to the `agent_output` schema in `schemas/agent_output.schema.json`.
