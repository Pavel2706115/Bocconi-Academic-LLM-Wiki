# Skill: LLM Wiki Maintain

## Purpose
Keep the Wiki healthy: rebuild indexes, update manifests, and ensure consistency.

## When to Use
- Periodically or when the user requests maintenance
- After bulk changes to the vault
- Before publishing or sharing the vault

## Steps

1. Run health check:
   ```bash
   python scripts/wiki_tool.py doctor
   ```
2. Rebuild catalog and indexes:
   ```bash
   python scripts/wiki_tool.py build
   ```
3. Update the source manifest:
   ```bash
   python scripts/wiki_tool.py source-scan --update --accept-covered
   ```
4. Validate everything:
   ```bash
   python scripts/wiki_tool.py lint
   python scripts/wiki_tool.py source-lint
   ```
5. Check for unprocessed sources:
   ```bash
   python scripts/wiki_tool.py source-delta
   ```
6. Review coverage:
   ```bash
   python scripts/wiki_tool.py source-coverage
   ```
7. Run public audit:
   ```bash
   python scripts/audit_public.py
   ```
8. Log maintenance activity if anything changed.

## Rules
- Maintenance should be non-destructive unless explicitly asked.
- Report findings to the user before making corrections.
