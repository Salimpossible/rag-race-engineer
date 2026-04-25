applyTo:
  - Makefile
  - scripts/**
  - .env.example
  - pyproject.toml

Infrastructure & scripts
- Scripts in `scripts/` should be cross-platform where reasonable (POSIX by default) and idempotent.
- The `Makefile` provides standard developer flows. Keep targets documented in `docs/setup.md`.
- `.env.example` lists required environment variables only; do not commit secrets.
- `pyproject.toml` should pin minimal runtime dependencies and list dev tools for tests.

Security & operations
- Use OIDC for cloud providers (when added). Avoid long-lived credentials in CI.
