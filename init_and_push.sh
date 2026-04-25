#!/usr/bin/env bash
set -euo pipefail

# init_and_push.sh
# Initialize a git repo (if needed), commit files, create GitHub repo, and push.
# Uses GitHub CLI `gh` (must be logged in).

REPO_NAME="rag-race-engineer"

if ! command -v git >/dev/null 2>&1; then
  echo "git is not installed. Install git and retry." >&2
  exit 1
fi

if ! command -v gh >/dev/null 2>&1; then
  echo "GitHub CLI (gh) is not installed. Install it and run 'gh auth login' to authenticate." >&2
  exit 1
fi

cd "$(dirname "$0")" || exit 1

if [ ! -d .git ]; then
  git init
  echo "Initialized empty git repository."
fi

git add -A

if git diff --staged --quiet; then
  echo "No changes to commit." >&2
else
  git commit -m "chore: initial commit"
fi

# If remote named origin already exists, warn and abort to avoid unintended pushes
if git remote get-url origin >/dev/null 2>&1; then
  echo "Remote 'origin' already exists. Please verify remote or remove it and run the script again." >&2
  git remote -v
  exit 1
fi

echo "Creating GitHub repo ${REPO_NAME} and pushing..."
gh repo create "${REPO_NAME}" --public --source=. --remote=origin --push --confirm

echo "Repository created and pushed: https://github.com/$(gh api user --jq .login)/${REPO_NAME}"
