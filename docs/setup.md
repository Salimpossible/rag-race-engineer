Quick setup

Requirements
- Python 3.10+ recommended

Create a venv and install

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
```

Makefile helpers
- `make setup` : run `scripts/bootstrap.sh` to create venv and install deps
- `make dev` : start the app locally (uvicorn)
- `make test` : run pytest
- `make eval` : run evaluation runner
- `make validate-schemas` : run schema validation script

Run locally

```bash
make dev
# or
uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
```

Tests

```bash
make test
```

Evals

```bash
make eval
```

Schema validation

```bash
make validate-schemas
```

Troubleshooting
- If imports fail, ensure the virtualenv is active and the package is installed in editable mode.
- If port is in use, change `--port` when starting uvicorn.
