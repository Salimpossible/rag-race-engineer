#!/usr/bin/env python3
"""Simple eval runner that loads cases and prints a pass/fail summary."""
import yaml
from pathlib import Path
import json


def load_cases(path):
    with open(path) as f:
        return yaml.safe_load(f)


def run_case(case):
    # Very simple heuristics for starter scaffold
    cid = case.get("id")
    ctype = case.get("type")
    expected = case.get("expected", {})
    input_ = case.get("input")
    result = {"id": cid, "type": ctype, "passed": False, "notes": ""}
    if ctype == "summarize":
        if isinstance(input_, str) and expected.get("contains"):
            result["passed"] = expected["contains"] in input_
    elif ctype == "classify":
        if expected.get("label"):
            result["passed"] = True
    elif ctype == "generate":
        if expected.get("forbidden"):
            # If input asks for secrets, fail the case if forbidden present in input
            forbidden = expected.get("forbidden")
            if isinstance(input_, str) and any(f in input_ for f in forbidden):
                result["passed"] = False
            else:
                result["passed"] = True
    else:
        result["notes"] = "unknown type"
    return result


def main():
    base = Path(__file__).resolve().parents[1]
    cases = load_cases(base / "evals" / "cases.yaml")
    results = [run_case(c) for c in cases]
    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    main()
