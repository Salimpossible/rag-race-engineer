This repository is a production-minded AI project scaffold optimized for GitHub Copilot and AI-assisted development.

What this repo is for
- Provide a durable, reproducible starting point for building AI-driven apps.
- Store prompts, schemas, and evals as first-class artifacts so agents can reason from files.

Project organization
- `src/` : application code (API, agent, RAG, services).
- `prompts/`: versioned prompts and templates used by agents.
- `schemas/`: JSON Schema contracts for inputs/outputs and retrieved chunks.
- `evals/`: evaluation cases and rubrics to validate AI behavior.
- `scripts/`: small operational scripts (bootstrap, validations, eval runner).
- `docs/`: architecture, setup, decisions, and repo map.

Coding rules
- Keep changes small and verifiable; add tests or eval cases for behavior changes.
- Prefer deterministic, typed interfaces (Pydantic/JSON Schema) over ad-hoc dicts.
- Prompts belong in `prompts/` and are source-controlled. Do not inline unsaved prompts in code.

How to run, test, lint, validate
- Use `Makefile` targets: `make setup`, `make dev`, `make test`, `make eval`, `make validate-schemas`.
- `scripts/bootstrap.sh` creates a venv and installs pinned dependencies from `pyproject.toml`.
- Use `scripts/validate_schemas.py` to verify JSON Schema files.

Prompts, schemas, evals handling
- Treat `prompts/` as authoritative prompt source. Keep prompts stable and composable.
- Update `schemas/` when changing API or agent contracts and add tests in `tests/`.
- Add evaluation cases to `evals/cases.yaml` when changing agent behavior and update `evals/rubric.md`.

Safety and consistency
- Do not invent commands, paths, or shortcuts in code/comments. Use the repo tree as truth.
- Avoid adding secrets or hardcoded keys. Use `.env` and `.env.example`.

Changes and PRs
- Keep PRs focused. Add or update tests/evals/docs for any behavior change.
- If you modify prompts or schemas, include a corresponding eval case or unit test.

This file is the repository-wide Copilot guidance and should be consulted by AI assistants and humans.
