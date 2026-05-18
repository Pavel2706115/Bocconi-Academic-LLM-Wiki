#!/usr/bin/env python3
"""audit_public.py — Check for obvious secrets, private keys, and machine-local paths.

Scans all tracked/staged files for patterns that should not be committed.
Uses only the Python standard library.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Patterns that indicate secrets or private data
SECRET_PATTERNS = [
    (r"-----BEGIN (RSA |DSA |EC |OPENSSH )?PRIVATE KEY-----", "Private key detected"),
    (r"AKIA[0-9A-Z]{16}", "AWS Access Key ID detected"),
    (r"(?i)(api[_-]?key|secret[_-]?key|password|token)\s*[:=]\s*['\"][^'\"]{8,}", "Possible secret/token"),
    (r"sk-[a-zA-Z0-9]{20,}", "OpenAI API key detected"),
    (r"ghp_[a-zA-Z0-9]{36}", "GitHub personal access token detected"),
]

# Machine-local path patterns
LOCAL_PATH_PATTERNS = [
    (r"C:\\Users\\[^\\]+\\(?!OneDrive)", "Windows local path detected"),
    (r"/home/[^/]+/", "Linux local path detected"),
    (r"/Users/[^/]+/(?!OneDrive)", "macOS local path detected"),
]

# File patterns to skip
SKIP_EXTENSIONS = {".pdf", ".png", ".jpg", ".jpeg", ".gif", ".mp4", ".mp3",
                   ".m4a", ".zip", ".tar", ".gz", ".exe", ".dll", ".pyc",
                   ".gitkeep", ".R", ".Rhistory"}
SKIP_DIRS = {".git", ".obsidian", "__pycache__", "node_modules", ".smart-env",
             ".aider.tags.cache.v4"}


def scan_file(path: Path) -> list[str]:
    """Scan a single file for secrets and local paths."""
    issues = []
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return issues

    for pattern, msg in SECRET_PATTERNS:
        if re.search(pattern, text):
            issues.append(f"{path.relative_to(ROOT)}: {msg}")

    for pattern, msg in LOCAL_PATH_PATTERNS:
        if re.search(pattern, text):
            issues.append(f"{path.relative_to(ROOT)}: {msg}")

    return issues


def main():
    print("=== audit_public ===")
    all_issues = []

    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        # Skip binary/cache files
        if path.suffix.lower() in SKIP_EXTENSIONS:
            continue
        # Skip excluded directories
        parts = set(path.relative_to(ROOT).parts)
        if parts & SKIP_DIRS:
            continue
        all_issues.extend(scan_file(path))

    if all_issues:
        for issue in all_issues:
            print(f"  ISSUE: {issue}")
        print(f"audit_public: FAIL ({len(all_issues)} issues)")
        sys.exit(1)
    else:
        print("  No secrets or local paths detected.")
        print("audit_public: PASS")
        sys.exit(0)


if __name__ == "__main__":
    main()
