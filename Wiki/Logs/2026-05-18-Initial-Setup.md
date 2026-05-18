---
tags:
  - "log"
topics:
  - "[[Wiki/Topics/Knowledge-Management]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/LLM-Wiki-Starter-Demo-Source.md"
source_count: 1
aliases: []
---

# 2026-05-18 — Initial LLM Wiki Setup

## Log Entry — 2026-05-18

### What Changed

Transformed the Bocconi academic Obsidian vault into an LLM Wiki system:

- Created the two-layer folder structure (Raw/Sources + Wiki)
- Moved 21 course folders (517 markdown files) into `Raw/Sources/`
- Built AGENTS.md, Schema rules, and 6 note templates
- Created `wiki_tool.py` with 10 deterministic commands
- Set up `audit_public.py` and git pre-commit hooks
- Completed first demo ingest with 4 compiled Wiki notes

### Details

- **Topic note**: Knowledge-Management.md
- **Concept note**: Source-Wiki-Separation.md
- **Project note**: LLM-Wiki-Setup.md
- **Log note**: this note

### Next Steps

- Begin ingesting actual course lecture notes from `Raw/Sources/`
- Build topic and concept coverage across all courses
- Run periodic maintenance to keep indexes and manifests current
