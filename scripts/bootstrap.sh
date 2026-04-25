#!/usr/bin/env bash
set -euo pipefail

python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -e .
echo "Bootstrap complete. Activate with: source .venv/bin/activate"
