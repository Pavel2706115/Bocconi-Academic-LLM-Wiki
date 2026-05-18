#!/usr/bin/env bash
# install_hooks.sh — Install git hooks for the LLM Wiki
set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
HOOKS_DIR="$REPO_ROOT/.githooks"

if [ ! -d "$HOOKS_DIR" ]; then
    echo "ERROR: .githooks/ directory not found at $HOOKS_DIR"
    exit 1
fi

git config core.hooksPath "$HOOKS_DIR"
echo "Git hooks path set to $HOOKS_DIR"
echo "Pre-commit hook will run: build, lint, source-lint"
