#!/usr/bin/env python3
"""Validate JSON Schema files under ./schemas"""
import json
from pathlib import Path
import sys
from jsonschema import Draft7Validator, exceptions


def main():
    base = Path(__file__).resolve().parents[1]
    schema_dir = base / "schemas"
    failed = 0
    for p in schema_dir.glob("*.json"):
        try:
            with p.open() as f:
                schema = json.load(f)
            Draft7Validator.check_schema(schema)
            print(f"OK: {p.name}")
        except Exception as e:
            print(f"INVALID: {p.name} -> {e}")
            failed += 1
    if failed:
        sys.exit(2)


if __name__ == "__main__":
    main()
