import json
from pathlib import Path


def test_schemas_exist_and_loadable():
    base = Path(__file__).resolve().parents[1]
    schema_dir = base / "schemas"
    files = ["agent_input.schema.json", "agent_output.schema.json", "retrieved_chunk.schema.json"]
    for f in files:
        p = schema_dir / f
        assert p.exists(), f"Missing schema: {f}"
        with p.open() as fh:
            data = json.load(fh)
            assert isinstance(data, dict)
