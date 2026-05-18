# Workflow Examples

## Example 1: Ingest a New Lecture

**Scenario**: User adds `Raw/Sources/30001 STATISTICS/Lecture 5/Lecture 5 Slides.md`.

1. Agent runs: `python scripts/wiki_tool.py search-catalog --query "statistics descriptive"`
2. Agent finds `Wiki/Concepts/Descriptive-Statistics.md` already exists.
3. Agent updates the existing concept note with new claims from Lecture 5.
4. Agent adds `[[Raw/Sources/30001 STATISTICS/Lecture 5/Lecture 5 Slides]]` to `sources`.
5. Agent increments `source_count`.
6. Agent runs build + lint gate.
7. Agent adds a log entry: "Updated Descriptive-Statistics with Lecture 5 material."

## Example 2: Create a New Concept

**Scenario**: Lecture mentions "Time Value of Money" — no Wiki note exists.

1. Agent creates `Wiki/Concepts/Time-Value-of-Money.md` using the concept template.
2. Agent fills in the frontmatter: `tags: [concept]`, `sources: [...]`, `source_count: 1`.
3. Agent writes a concise explanation with key formulas.
4. Agent links to the relevant topic note (e.g., `topics: ["[[Wiki/Topics/Corporate-Finance]]"]`).
5. Agent runs build + lint gate.

## Example 3: Answer a Study Question

**Scenario**: User asks "What is the difference between population and sample?"

1. Agent runs: `python scripts/wiki_tool.py search-catalog --query "population sample"`
2. Agent opens matching Wiki note.
3. If insufficient, agent opens the linked Raw source for full context.
4. Agent responds with the answer, citing both the Wiki note and Raw source.
