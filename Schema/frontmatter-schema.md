# Frontmatter Schema

This document defines the required YAML frontmatter fields for each note type.

## Source Notes (`Raw/Sources/`)

```yaml
---
Title: ""
Author: ""
Reference: ""
ContentType:
  - "markdown"
Created: YYYY-MM-DD
Processed: false
tags:
  - "source"
---
```

### Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `Title` | string | Yes | Human-readable title of the source |
| `Author` | string | Yes | Original author or creator |
| `Reference` | string | Yes | Citation, URL, or identifier |
| `ContentType` | list | Yes | Format types: `markdown`, `pdf`, `video`, etc. |
| `Created` | date | Yes | Date the source was added to the vault |
| `Processed` | boolean | Yes | Whether the source has been compiled into Wiki notes |
| `tags` | list | Yes | Must include `source` |

## Compiled Wiki Notes (`Wiki/`)

```yaml
---
tags:
  - "concept"
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
aliases: []
---
```

### Field Descriptions

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `tags` | list | Yes | Exactly one of: `topic`, `concept`, `entity`, `project`, `log` |
| `topics` | list | Yes | Related topic note links |
| `status` | string | Yes | One of: `seed`, `draft`, `reviewed`, `stable` |
| `created` | date | Yes | Date the note was created |
| `updated` | date | Yes | Date of last meaningful edit |
| `sources` | list | Yes | Links to Raw source notes that support this note |
| `source_count` | integer | Yes | Must equal `len(sources)` |
| `aliases` | list | No | Alternative names or abbreviations |

### Topic Note Constraints (`Wiki/Topics/`)

In addition to the general Compiled Wiki Note fields above, any note with the `topic` tag is subject to strict constraints to keep high-level subjects standardized:
1. **Directory Location**: Must reside strictly under `Wiki/Topics/`. Conversely, all notes under `Wiki/Topics/` must have the `topic` tag.
2. **Structural Sections**: Must contain exactly three H2 headings in its body:
   - `## Overview` — Summarizes the high-level subject, scope, and course module boundaries.
   - `## Core Concepts` — Links and lists the primary concepts (`Wiki/Concepts/`) associated with the subject.
   - `## Key Takeaways` — Lists the central academic/practical takeaways of the subject.

