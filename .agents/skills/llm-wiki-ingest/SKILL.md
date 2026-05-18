# Skill: LLM Wiki Ingest

## Purpose
Transform Raw source material into compiled Wiki notes.

## When to Use
- User adds new source material to `Raw/Sources/`
- User asks to process or compile a source

## Steps

1. Read the source note in `Raw/Sources/`.
2. Search the catalog for existing related notes:
   ```bash
   python scripts/wiki_tool.py search-catalog --query "<key terms>"
   ```
3. Open relevant existing Wiki notes to avoid duplication.
4. Extract key claims, concepts, and facts from the source.
5. Create or update Wiki notes under the appropriate subfolder:
   - `Wiki/Topics/` for broad subject overviews
   - `Wiki/Concepts/` for focused explanations
   - `Wiki/Entities/` for people, institutions, tools
   - `Wiki/Projects/` for project-level tracking
6. For each compiled note:
   - Use the correct template from `_templates/`.
   - Add the Raw source path to `sources`.
   - Set `source_count` to match `len(sources)`.
   - Set `status` to `seed` for new notes.
7. Mark the source as `Processed: true`.
8. Run the maintenance gate:
   ```bash
   python scripts/wiki_tool.py build
   python scripts/wiki_tool.py lint
   python scripts/wiki_tool.py source-scan --update --accept-covered
   python scripts/wiki_tool.py source-lint
   ```
9. Add a log entry summarizing the ingest.

## Rules
- Never invent citations. Only link to actual Raw sources.
- Keep Wiki notes concise and focused — one concept per note.
- Preserve the original source text in `Raw/Sources/` unchanged.
