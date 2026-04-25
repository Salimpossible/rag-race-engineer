Purpose
-------
This repository is a generic, production-minded scaffold for building AI-driven services. It provides a reproducible layout for storing prompts, schemas, evaluations, and a small FastAPI service so developers and agents can work from durable context files.

Major layers
- API: `src/api/` exposes HTTP endpoints and validation via Pydantic.
- Agent: `src/agent/` contains prompt building, state management, and responder logic.
- RAG: `src/rag/` contains simple chunking and retrieval helpers to support grounded responses.
- Services: `src/services/` contains abstractions for AI providers and other external integrations.
- Schemas: `schemas/` contains JSON Schema contracts for inputs, outputs, and retrieved chunks.
- Evals: `evals/` contains evaluation cases and rubrics to validate agent behaviour.

Design principles
- Stable context in files, not chat: prompts, templates, and schemas are canonical and versioned in the repo.
- Deterministic interfaces first: design Pydantic/JSON Schema contracts before adding agent heuristics.
- Small composable modules: keep responsibilities focused to make changes clear and testable.

How prompts/schemas/evals work together
- Prompts provide the instruction surface used by agents (`prompts/`).
- Schemas define the structured inputs and outputs agents and services must conform to (`schemas/`).
- Evals exercise prompts+schemas to detect regressions and measure quality (`evals/`).

Expected future evolution
- Add provider-specific adapters to `src/services/` with OIDC support and secure secrets handling.
- Expand RAG ingestion pipelines in `src/rag/` for longer-term retrieval needs.
- Add CI workflows with SAST, dependency review, and schema validation.
