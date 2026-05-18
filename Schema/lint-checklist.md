# Lint Checklist

Pre-commit validation rules enforced by `scripts/wiki_tool.py lint` and `source-lint`.

## Compiled Wiki Notes (`Wiki/`)

- [ ] Has YAML frontmatter block
- [ ] `tags` contains exactly one allowed value: `topic`, `concept`, `entity`, `project`, or `log`
- [ ] `source_count` equals `len(sources)`
- [ ] Each entry in `sources` points to an existing file under `Raw/Sources/`
- [ ] `status` is one of: `seed`, `draft`, `reviewed`, `stable`
- [ ] `created` and `updated` are valid dates in `YYYY-MM-DD` format
- [ ] Note body is non-empty

## Source Notes (`Raw/Sources/`)

- [ ] Has YAML frontmatter block
- [ ] `Title` is non-empty
- [ ] `Reference` is non-empty
- [ ] `Created` is a valid date
- [ ] `Processed` is a boolean
- [ ] `tags` includes `source`
- [ ] If `Processed` is `true`, at least one Wiki note covers this source

## Catalog (`Wiki/catalog.jsonl`)

- [ ] Each line is valid JSON
- [ ] Each entry has: `path`, `title`, `tag`, `topics`, `sources`, `updated`
- [ ] All `path` values point to existing files

## Source Manifest (`Schema/source-manifest.jsonl`)

- [ ] Each line is valid JSON
- [ ] Each entry has: `path`, `title`, `processed`, `covered_by`, `updated`
