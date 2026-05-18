# Skill: LLM Wiki Query

## Purpose
Answer user questions by searching compiled Wiki notes before Raw sources.

## When to Use
- User asks a question about vault content
- User wants to find information on a topic

## Steps

1. Start with `Wiki/index.md` for an overview.
2. Search the catalog:
   ```bash
   python scripts/wiki_tool.py search-catalog --query "<user question keywords>"
   ```
3. Open the top matching Wiki notes.
4. If the compiled note is sufficient, answer from it.
5. If more detail is needed, follow `sources` links to the Raw source notes.
6. Cite both the Wiki note and Raw source when answering.

## Rules
- Always search the catalog before opening Raw sources.
- Prefer compiled Wiki notes over Raw sources for answers.
- If no Wiki note exists, inform the user and offer to compile one from Raw sources.
- Never fabricate information not present in the vault.
