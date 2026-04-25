applyTo:
  - src/**
  - tests/**

Backend instructions
- Keep functions small and well-typed with Pydantic models for public interfaces.
- API routes should validate inputs and return typed responses. Update `schemas/` for cross-service contracts.
- Avoid side effects in route handlers; push business logic into `services/`.
- Add unit tests in `tests/` whenever changing behavior. Tests should be deterministic and fast.
- Do not add external cloud provider credentials in code. Use environment variables and `.env.example`.

Testing
- Use `pytest` and the `TestClient` for HTTP tests. Keep external network calls mocked in unit tests.
