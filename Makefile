PYTHON=python3
VENV=.venv

.PHONY: setup dev test eval validate-schemas

setup:
	./scripts/bootstrap.sh

dev:
	$(VENV)/bin/uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

test:
	$(VENV)/bin/pytest -q

eval:
	$(VENV)/bin/python scripts/run_evals.py

validate-schemas:
	$(VENV)/bin/python scripts/validate_schemas.py
