---
tags:
  - "log"
topics: []
status: final
created: 2026-05-18
updated: 2026-05-18
sources: []
source_count: 0
aliases: []
---

# Walkthrough: LLM Wiki Transformation

## What Was Done

Transformed the Bocconi academic Obsidian vault into a fully functional LLM Wiki system following the [wanderloots-llm-wiki-core-setup-v1.0.0](file:///D:/Antigravity/wanderloots-llm-wiki-core-setup-v1.0.0.md) guide, and then systematically ingested 10 entire Bocconi courses into the structured Wiki schema.

## Phase 2: Full Vault Ingestion

Systematically converted the 232+ raw source files from 10 Bocconi courses into structured, cross-linked Wiki notes:
1. **Topic Notes**: Created 9 core `Topic` notes mapping to the main academic domains (e.g., Statistics, Corporate Finance, Microeconomics).
2. **Concept Notes**: Created 59 interlinked `Concept` notes extracting the theoretical and technical knowledge from across the vault (e.g., Net Present Value, IS-LM Model, Perfect Competition, Hypothesis Testing).
3. **Entity Notes**: Created 9 `Entity` notes for key historical figures and institutions (e.g., John Maynard Keynes, Adam Smith, the Federal Reserve, the IMF).
4. **Traceability**: All 162 total Wiki notes accurately link back to their originating `Raw/Sources/` files using the `sources` and `source_count` frontmatter arrays.

## Git History (8 tutorial commits)

| Commit | Step | Description |
|--------|------|-------------|
| `90948a1` | 00 | Expanded `.gitignore`, created `Welcome.md` |
| `343755f` | 01 | Created folder structure, moved 21 course folders → `Raw/Sources/` |
| `02f777c` | 02 | Created `AGENTS.md`, Schema rules, 4 agent skills |
| `57efef6` | 03 | Created 6 note templates (source, concept, topic, entity, project, log) |
| `600444a` | 04 | Created `wiki_tool.py` (10 commands), `audit_public.py`, git hooks |
| `e94a3fb` | 05 | Demo source + 4 compiled Wiki notes |
| `0525a16` | 06 | Generated catalog, manifest, indexes; all checks pass |
| `5183823` | 07 | Ingest full vault: 9 Topics, 59 Concepts, 9 Entities across 10 courses |

## Vault Structure

```
C:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\
├── AGENTS.md                    # Agent behavior rules
├── Welcome.md                   # Vault landing page
├── Raw/
│   ├── Sources/                 # 518 source notes (21 course folders)
│   │   ├── 30001 STATISTICS/
│   │   ├── 30017 CORPORATE FINANCE/
│   │   ├── ... (19 more course folders)
│   │   └── LLM-Wiki-Starter-Demo-Source.md
│   └── Files/                   # Binary files (gitignored)
├── Wiki/
│   ├── catalog.jsonl            # Machine-readable note catalog (162 entries)
│   ├── index.md                 # Master index
│   ├── Topics/                  # 10 Topic notes
│   ├── Concepts/                # 60 Concept notes
│   ├── Projects/                # 1 Project note
│   ├── Logs/                    # 2 Log notes
│   └── Entities/                # 9 Entity notes
├── Schema/
│   ├── frontmatter-schema.md
│   ├── workflow-examples.md
│   ├── lint-checklist.md
│   ├── naming-conventions.md
│   ├── command-reference.md
│   └── source-manifest.jsonl    # 232 source entries
├── _templates/                  # 6 note templates
├── .agents/skills/              # 4 agent skills (ingest, query, lint, maintain)
├── scripts/
│   ├── wiki_tool.py             # Core deterministic tool
│   ├── audit_public.py          # Secret/path scanner
│   ├── install_hooks.sh         # Git hook installer
│   ├── convert_pdfs_to_md.py    
│   └── copy_md_files.py         
└── .githooks/pre-commit         # Auto-runs build+lint+source-lint
```

## Validation Results

All checks pass following the mass ingestion:

| Command | Result |
|---------|--------|
| `wiki_tool.py doctor` | ✅ PASS — all folders OK, 162 Wiki notes, 232 sources |
| `wiki_tool.py build` | ✅ catalog (162 entries), index, per-folder indexes written |
| `wiki_tool.py lint` | ✅ PASS — 162 notes checked, no errors |
| `wiki_tool.py source-scan` | ✅ 232 sources successfully added to manifest |
| `wiki_tool.py source-lint` | ✅ PASS — 232 sources checked against manifest |
| `audit_public.py` | ✅ PASS — no secrets or local paths |

## How to Use Going Forward

### Ingest a new source
1. Add cleaned markdown to `Raw/Sources/`
2. Run: `python scripts/wiki_tool.py search-catalog --query "topic"`
3. Create/update Wiki notes in `Wiki/`
4. Run the maintenance gate (build → lint → source-scan → source-lint)

### Query the Wiki
```bash
python scripts/wiki_tool.py search-catalog --query "your topic"
```

### Run maintenance
```bash
python scripts/wiki_tool.py doctor
python scripts/wiki_tool.py build
python scripts/wiki_tool.py lint
python scripts/wiki_tool.py source-lint
python scripts/audit_public.py
```
