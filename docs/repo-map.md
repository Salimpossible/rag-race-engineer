Top-level folder map

- `src/` : Application code. Edit this when adding endpoints, services, or agent logic.
- `prompts/` : Canonical system, task prompts and templates. Update when agent behavior needs tuning.
- `schemas/` : JSON Schema contracts for agent inputs/outputs and retrieval chunks.
- `evals/` : Evaluation cases and rubric for validating AI behaviors and regressions.
- `scripts/` : Small operational scripts (bootstrap, schema validation, eval runner).
- `docs/` : Architecture, setup, decisions, and repository map — human-focused guidance.
- `.github/` : Copilot and path-scoped instructions to guide AI agents and developers.

When to edit
- Edit `prompts/` for behavioural changes; accompany edits with `evals/` updates.
- Edit `schemas/` when altering public contracts; update `tests/` accordingly.
- Edit `src/` for implementation, and add tests in `tests/` for coverage.
