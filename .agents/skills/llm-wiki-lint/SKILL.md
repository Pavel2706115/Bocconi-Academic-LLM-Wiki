# Skill: LLM Wiki Lint

## Purpose
Validate all Wiki and source notes against the schema before commits.

## When to Use
- Before any meaningful commit
- After creating or updating Wiki notes
- After source ingestion

## Steps

1. Run the full maintenance gate:
   ```bash
   python scripts/wiki_tool.py doctor
   python scripts/wiki_tool.py build
   python scripts/wiki_tool.py lint
   python scripts/wiki_tool.py source-lint
   python scripts/audit_public.py
   ```
2. Review any errors or warnings.
3. Fix issues:
   - Missing frontmatter fields → add them.
   - Mismatched `source_count` → recalculate.
   - Broken source links → fix paths or remove dead links.
   - Invalid tags → use only allowed tags.
4. Re-run until all checks pass.

## Rules
- Never commit with lint errors.
- Do not suppress or ignore warnings without user approval.
