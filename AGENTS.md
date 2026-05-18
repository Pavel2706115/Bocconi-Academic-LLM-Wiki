# AGENTS.md — LLM Wiki Agent Protocol

This file defines the rules every AI agent **must** follow when reading or writing to this vault.

## Core Principles

1. **Raw vs Wiki separation**: `Raw/Sources/` contains original source material (lecture notes, slides, transcripts). Never edit Raw sources unless explicitly asked. Never treat them as compiled knowledge.
2. **Write knowledge to Wiki only**: Reusable, compiled knowledge notes belong in `Wiki/` — organized under `Topics/`, `Concepts/`, `Entities/`, `Projects/`, or `Logs/`.
3. **Source traceability**: Every compiled Wiki note **must** link back to one or more Raw sources in its `sources` frontmatter field. The `source_count` field must equal the length of `sources`. Do not invent citations or create unsupported claims.
4. **Catalog-first search**: Before opening broad Raw context, search `Wiki/catalog.jsonl` for existing compiled notes. Open Raw sources only when compiled notes are insufficient or the user asks for source-level verification.
5. **Maintenance gates**: Run `build`, `lint`, and `source-lint` checks before every meaningful commit.

## Folder Map

| Path | Purpose | Who writes |
|------|---------|------------|
| `Raw/Sources/` | Original lecture slides, notes, transcripts | User (or PDF converter) |
| `Raw/Files/` | Binary files (PDFs, images) — gitignored | User |
| `Wiki/Topics/` | High-level topic overviews | Agent |
| `Wiki/Concepts/` | Focused concept explanations | Agent |
| `Wiki/Entities/` | People, institutions, tools | Agent |
| `Wiki/Projects/` | Project tracking notes | Agent |
| `Wiki/Logs/` | Timestamped activity logs | Agent |
| `Schema/` | Rules, specs, manifests | Agent (setup only) |
| `_templates/` | Note templates | Agent (setup only) |
| `.agents/skills/` | Agent skill definitions | Agent (setup only) |
| `scripts/` | Deterministic tooling | Agent (setup only) |

## Allowed Wiki Tags

Only these tags may appear in compiled Wiki notes:

- `topic`
- `concept`
- `entity`
- `project`
- `log`

## Workflow: Ingesting a New Source

1. Place cleaned Markdown in `Raw/Sources/`.
2. Run `search-catalog` for related topics.
3. Open only the most relevant compiled Wiki notes.
4. Create or update focused notes in `Wiki/`.
5. Add Raw source links to `sources`.
6. Keep `source_count` accurate.
7. Run `build`, `lint`, `source-scan --update --accept-covered`, and `source-lint`.
8. Add a log entry if the ingest meaningfully changed the Wiki.

## Workflow: Answering a Question

1. Start with `Wiki/index.md`.
2. Search the catalog: `python scripts/wiki_tool.py search-catalog --query "user topic"`.
3. Open the most relevant Wiki notes.
4. Open Raw sources only when the compiled note is insufficient.
5. Cite both the compiled note and Raw source when the answer depends on source material.

## Pre-Commit Gate

Before every meaningful commit, run:

```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```
