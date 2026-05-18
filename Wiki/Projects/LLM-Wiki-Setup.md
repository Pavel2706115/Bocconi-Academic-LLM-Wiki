---
tags:
  - "project"
topics:
  - "[[Wiki/Topics/Knowledge-Management]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/LLM-Wiki-Starter-Demo-Source.md"
source_count: 1
aliases:
  - "Wiki Setup"
---

# LLM Wiki Setup

## Objective

Build and maintain a functional LLM Wiki system for the Bocconi academic vault, following the wanderloots core setup guide.

## Status

Active — core system built, ready for source ingestion.

## Tasks

- [x] Initialize vault structure (Raw/Wiki/Schema layers)
- [x] Create AGENTS.md and Schema rules
- [x] Set up note templates
- [x] Build deterministic tooling (wiki_tool.py)
- [x] Complete first demo ingest
- [x] Pass all lint and audit checks
- [ ] Ingest existing course lecture notes into Wiki
- [ ] Build comprehensive topic and concept coverage

## Notes

The vault contains 517 raw markdown source files across 21 course folders, now organized under `Raw/Sources/`. Future ingestion will compile these into structured Wiki notes with full source traceability.

## Sources

- [[Raw/Sources/LLM-Wiki-Starter-Demo-Source|LLM Wiki Starter Demo Source]]
