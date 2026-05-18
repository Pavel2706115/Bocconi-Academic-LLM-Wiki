---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/Knowledge-Management]]"
status: seed
created: 2026-05-18
updated: 2026-05-18
sources:
  - "Raw/Sources/LLM-Wiki-Starter-Demo-Source.md"
source_count: 1
aliases:
  - "Two-Layer Architecture"
  - "Raw vs Wiki"
---

# Source-Wiki Separation

## Definition

Source-Wiki Separation is the foundational design principle of an LLM Wiki. It mandates a strict division between **Raw sources** (original, unedited material) and **compiled Wiki notes** (concise, reusable knowledge entries).

## Key Properties

- **Raw sources** live in `Raw/Sources/` and are never modified after ingestion
- **Wiki notes** live in `Wiki/` and are created by distilling useful claims from sources
- Every Wiki note must reference at least one Raw source via the `sources` frontmatter field
- The `source_count` field must always match the number of entries in `sources`

## Examples

A lecture slide deck (`Raw/Sources/30001 STATISTICS/Lecture 1 Slides.md`) might produce:
- `Wiki/Concepts/Descriptive-Statistics.md`
- `Wiki/Concepts/Inferential-Statistics.md`
- `Wiki/Topics/Statistics.md`

Each compiled note links back to the original lecture source.

## Related Concepts

- [[Wiki/Topics/Knowledge-Management|Knowledge Management]]
- Catalog-first search workflow
- Deterministic maintenance tooling

## Sources

- [[Raw/Sources/LLM-Wiki-Starter-Demo-Source|LLM Wiki Starter Demo Source]]
