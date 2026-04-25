# AI Project Scaffold

This repository is a lightweight, production-minded scaffold for AI-driven services. It stores canonical prompts, JSON schemas, evaluation cases, and a small FastAPI app so developers and AI agents can work from durable project context.

Why this structure is AI-friendly
- Prompts are versioned in `prompts/` so agents and Copilot can load canonical instructions.
- Schemas in `schemas/` provide deterministic contracts for inputs/outputs.
- Evals in `evals/` enable regression checks when prompts or logic change.

Quickstart

1. Bootstrap environment

```bash
make setup
source .venv/bin/activate
```

2. Run locally

```bash
make dev
```

3. Run tests

```bash
make test
```

Repo structure (top-level)

- `src/` : application code (API, agent, RAG, services)
- `prompts/` : system, task prompts, templates
- `schemas/` : JSON Schema contracts
- `evals/` : evaluation cases and rubric
- `scripts/` : bootstrap, schema validation, eval runner
- `docs/` : architecture, setup, and decisions

Next steps
- Replace the `AIClient` stub with a provider integration and update evals.
- Add CI workflows that validate schemas and run evals on PRs.
# rag-race-engineer

Repository scaffold for the Rag Race Engineer project.

This repo was prepared for quick initialization and pushing to GitHub.

Usage:

- Run `./init_and_push.sh` to initialize git, create the GitHub repo `rag-race-engineer`, and push the initial commit (requires `git` and `gh` authenticated).
- Or run the manual commands shown in the script.

Files added by the helper script:

- `README.md` (this file)
- `.gitignore`
- `init_and_push.sh`
