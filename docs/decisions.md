Architectural Decisions (starter)

1. Python + FastAPI
- Rationale: modern, lightweight, type-friendly web framework with Pydantic integration.

2. Prompt files stored in repo
- Rationale: stable, versioned prompts reduce repeated chat context and improve reproducibility.

3. JSON Schema contracts
- Rationale: explicit contracts make integrations and evals deterministic and testable.

4. Eval-first AI development
- Rationale: every prompt or behavior change should be accompanied by an eval case to avoid regressions.

5. Lightweight RAG-ready structure
- Rationale: provide chunking and retrieval stubs that can be extended for grounding, but avoid heavy infra.
