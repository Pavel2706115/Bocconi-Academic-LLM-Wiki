# Command Reference

All commands are run from the vault root directory.

## wiki_tool.py

### `doctor`
Non-mutating health check. Verifies folders, Python version, catalog, manifest, and note counts.
```bash
python scripts/wiki_tool.py doctor
```

### `build`
Generate `Wiki/catalog.jsonl`, `Wiki/index.md`, and per-folder index files.
```bash
python scripts/wiki_tool.py build
```

### `lint`
Validate compiled Wiki note frontmatter: tags, source_count, source links.
```bash
python scripts/wiki_tool.py lint
```

### `source-scan`
List Raw sources and optionally update the source manifest.
```bash
python scripts/wiki_tool.py source-scan
python scripts/wiki_tool.py source-scan --update
python scripts/wiki_tool.py source-scan --update --accept-covered
```

### `source-lint`
Validate source note frontmatter and coverage state.
```bash
python scripts/wiki_tool.py source-lint
```

### `source-delta`
Show Raw sources not represented in the manifest.
```bash
python scripts/wiki_tool.py source-delta
```

### `source-coverage`
Show which Raw sources are covered by compiled Wiki notes.
```bash
python scripts/wiki_tool.py source-coverage
```

### `search-catalog`
Search compiled Wiki notes through the catalog.
```bash
python scripts/wiki_tool.py search-catalog --query "your search terms"
```

### `log`
Append a log entry to `Wiki/log.md`.
```bash
python scripts/wiki_tool.py log --title "Title" --details "What happened"
```

## audit_public.py

Scan for obvious secrets, private keys, and machine-local paths.
```bash
python scripts/audit_public.py
```

## Pre-Commit Hook

Install the git hooks:
```bash
bash scripts/install_hooks.sh
```

The pre-commit hook automatically runs `build`, `lint`, and `source-lint`.
