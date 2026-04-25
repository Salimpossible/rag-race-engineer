applyTo:
  - prompts/**
  - schemas/**
  - evals/**

Prompts and schema instructions
- Store canonical prompts in `prompts/`. Keep them short, composable, and versioned.
- Prefer templates and small task-specific prompts under `prompts/tasks/` and `prompts/templates/`.
- When changing a prompt that affects behavior, add or update an eval in `evals/cases.yaml`.
- Schemas in `schemas/` are the authoritative contracts. Update schema files and `tests/test_schemas.py` when changing fields.
- Avoid embedding credentials or provider-specific tokens in prompts.
