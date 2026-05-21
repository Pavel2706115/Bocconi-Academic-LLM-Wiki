#!/usr/bin/env python3
"""wiki_tool.py — Deterministic LLM Wiki maintenance tool.

Uses only the Python standard library. Supports commands:
  doctor, build, lint, source-scan, source-lint, source-delta,
  source-coverage, search-catalog, log
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from pathlib import Path

# ── Ensure UTF-8 output on Windows ──────────────────────────────────────────
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ── Paths ────────────────────────────────────────────────────────────────────
ROOT = Path(__file__).resolve().parent.parent
RAW_SOURCES = ROOT / "Raw" / "Sources"
WIKI = ROOT / "Wiki"
SCHEMA = ROOT / "Schema"
CATALOG = WIKI / "catalog.jsonl"
WIKI_INDEX = WIKI / "index.md"
SOURCE_MANIFEST = SCHEMA / "source-manifest.jsonl"
WIKI_LOG = WIKI / "log.md"

ALLOWED_TAGS = {"topic", "concept", "entity", "project", "log"}
WIKI_SUBDIRS = ["Topics", "Concepts", "Entities", "Projects", "Logs"]

# ── YAML-lite parser (no external deps) ─────────────────────────────────────

def parse_frontmatter(path: Path) -> dict | None:
    """Return frontmatter dict or None if the file has no frontmatter."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("---", 3)
    if end == -1:
        return None
    block = text[3:end].strip()
    return _parse_yaml_lite(block)


def _parse_yaml_lite(block: str) -> dict:
    """Minimal YAML parser — handles scalars, simple lists, and nested lists."""
    result: dict = {}
    current_key = None
    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line or line.startswith("#"):
            continue
        # List item under current key
        if re.match(r"^\s+-\s+", line) or re.match(r'^\s+-\s*"', line):
            value = re.sub(r"^\s+-\s*", "", line).strip().strip('"').strip("'")
            if current_key and current_key in result:
                if isinstance(result[current_key], list):
                    result[current_key].append(value)
                else:
                    result[current_key] = [result[current_key], value]
            continue
        # Inline list: key: [a, b, c]
        m = re.match(r"^(\w[\w_]*):\s*\[(.*)]\s*$", line)
        if m:
            current_key = m.group(1)
            items = [i.strip().strip('"').strip("'") for i in m.group(2).split(",") if i.strip()]
            result[current_key] = items
            continue
        # Key: value
        m = re.match(r"^(\w[\w_]*):\s*(.*)", line)
        if m:
            current_key = m.group(1)
            val = m.group(2).strip().strip('"').strip("'")
            if val.lower() == "true":
                result[current_key] = True
            elif val.lower() == "false":
                result[current_key] = False
            elif val == "":
                result[current_key] = []  # likely a list follows
            else:
                try:
                    result[current_key] = int(val)
                except ValueError:
                    result[current_key] = val
            continue
    return result


# ── Helpers ──────────────────────────────────────────────────────────────────

def wiki_notes() -> list[Path]:
    """Return all .md files under Wiki/ subdirectories (not index.md)."""
    notes = []
    for sub in WIKI_SUBDIRS:
        d = WIKI / sub
        if d.is_dir():
            for f in sorted(d.rglob("*.md")):
                if f.name != "index.md":
                    notes.append(f)
    return notes


def source_notes() -> list[Path]:
    """Return all .md files under Raw/Sources/."""
    if not RAW_SOURCES.is_dir():
        return []
    return sorted(RAW_SOURCES.rglob("*.md"))


def rel(path: Path) -> str:
    """Return path relative to ROOT using forward slashes."""
    return str(path.relative_to(ROOT)).replace("\\", "/")


# ── Commands ─────────────────────────────────────────────────────────────────

def cmd_doctor():
    """Non-mutating health check."""
    ok = True
    print("=== doctor ===")

    # Python version
    v = sys.version_info
    print(f"Python {v.major}.{v.minor}.{v.micro}")
    if v.major < 3 or v.minor < 9:
        print("  WARN: Python 3.9+ recommended")

    # Folder checks
    for d in ["Raw/Sources", "Raw/Files", "Wiki/Topics", "Wiki/Concepts",
              "Wiki/Entities", "Wiki/Projects", "Wiki/Logs", "Schema",
              "_templates", ".agents/skills", "scripts"]:
        p = ROOT / d
        status = "OK" if p.is_dir() else "MISSING"
        if status == "MISSING":
            ok = False
        print(f"  {d}: {status}")

    # Catalog
    if CATALOG.is_file():
        lines = [l for l in CATALOG.read_text(encoding="utf-8").splitlines() if l.strip()]
        print(f"  catalog.jsonl: {len(lines)} entries")
    else:
        print("  catalog.jsonl: NOT FOUND")

    # Source manifest
    if SOURCE_MANIFEST.is_file():
        lines = [l for l in SOURCE_MANIFEST.read_text(encoding="utf-8").splitlines() if l.strip()]
        print(f"  source-manifest.jsonl: {len(lines)} entries")
    else:
        print("  source-manifest.jsonl: NOT FOUND")

    # Note counts
    wn = wiki_notes()
    sn = source_notes()
    print(f"  Wiki notes: {len(wn)}")
    print(f"  Raw sources (.md): {len(sn)}")

    if ok:
        print("doctor: PASS")
    else:
        print("doctor: ISSUES FOUND")
    return ok


def cmd_build():
    """Generate catalog.jsonl, Wiki/index.md, and per-folder index files."""
    print("=== build ===")
    entries = []
    for note in wiki_notes():
        fm = parse_frontmatter(note)
        if fm is None:
            continue
        tags = fm.get("tags", [])
        tag = tags[0] if isinstance(tags, list) and tags else (tags if isinstance(tags, str) else "")
        entry = {
            "path": rel(note),
            "title": note.stem.replace("-", " "),
            "tag": tag,
            "topics": fm.get("topics", []),
            "sources": fm.get("sources", []),
            "updated": fm.get("updated", ""),
        }
        entries.append(entry)

    # Write catalog
    CATALOG.parent.mkdir(parents=True, exist_ok=True)
    with open(CATALOG, "w", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, ensure_ascii=False) + "\n")
    print(f"  catalog.jsonl: {len(entries)} entries written")

    # Write Wiki/index.md
    lines = ["# Wiki Index\n", f"_Generated {date.today().isoformat()}_\n"]
    for sub in WIKI_SUBDIRS:
        sub_entries = [e for e in entries if e["path"].startswith(f"Wiki/{sub}/")]
        lines.append(f"\n## {sub} ({len(sub_entries)})\n")
        for e in sub_entries:
            lines.append(f"- [[{e['path']}|{e['title']}]]")
        # Per-folder index
        idx_path = WIKI / sub / "index.md"
        idx_lines = [f"# {sub} Index\n", f"_Generated {date.today().isoformat()}_\n"]
        for e in sub_entries:
            idx_lines.append(f"- [[{e['path']}|{e['title']}]]")
        idx_path.write_text("\n".join(idx_lines) + "\n", encoding="utf-8")

    WIKI_INDEX.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("  Wiki/index.md: written")
    print("  Per-folder indexes: written")
    print("build: DONE")


def cmd_lint():
    """Validate compiled Wiki note frontmatter."""
    print("=== lint ===")
    errors = []
    for note in wiki_notes():
        fm = parse_frontmatter(note)
        p = rel(note)
        if fm is None:
            errors.append(f"{p}: no frontmatter")
            continue
        # Tag check
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        valid_tags = [t for t in tags if t in ALLOWED_TAGS]
        if not valid_tags:
            errors.append(f"{p}: no valid tag (found {tags})")
        # Source count check
        sources = fm.get("sources", [])
        if isinstance(sources, str):
            sources = [sources] if sources else []
        sc = fm.get("source_count", 0)
        if sc != len(sources):
            errors.append(f"{p}: source_count={sc} but {len(sources)} sources listed")
        # Source existence check
        for src in sources:
            # Clean wikilink syntax
            clean = src.strip("[]").split("|")[0]
            src_path = ROOT / clean
            if not src_path.is_file():
                errors.append(f"{p}: source not found: {clean}")

        # Topic-specific checks
        tag = valid_tags[0] if valid_tags else None
        is_topic_dir = p.startswith("Wiki/Topics/")
        if is_topic_dir and tag != "topic":
            errors.append(f"{p}: note in Wiki/Topics/ must have the 'topic' tag (found '{tag}')")
        elif not is_topic_dir and tag == "topic":
            errors.append(f"{p}: note with 'topic' tag must be located in Wiki/Topics/ directory")

        if tag == "topic":
            try:
                content = note.read_text(encoding="utf-8", errors="replace")
                if not re.search(r"^##\s+Overview\b", content, re.MULTILINE):
                    errors.append(f"{p}: topic note missing '## Overview' heading")
                if not re.search(r"^##\s+Core\s+Concepts\b", content, re.MULTILINE):
                    errors.append(f"{p}: topic note missing '## Core Concepts' heading")
                if not re.search(r"^##\s+Key\s+Takeaways\b", content, re.MULTILINE):
                    errors.append(f"{p}: topic note missing '## Key Takeaways' heading")
            except Exception as e:
                errors.append(f"{p}: failed to read file content for body checks: {e}")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        print(f"lint: FAIL ({len(errors)} errors)")
        return False
    print(f"  {len(wiki_notes())} notes checked")
    print("lint: PASS")
    return True


def cmd_source_scan(update=False, accept_covered=False):
    """List Raw sources and optionally update source-manifest.jsonl."""
    print("=== source-scan ===")
    sources = source_notes()
    # Build coverage map: which wiki notes cover which sources
    coverage: dict[str, list[str]] = {}
    for note in wiki_notes():
        fm = parse_frontmatter(note)
        if fm is None:
            continue
        for src in fm.get("sources", []):
            clean = src.strip("[]").split("|")[0]
            coverage.setdefault(clean, []).append(rel(note))

    manifest = []
    for src in sources:
        fm = parse_frontmatter(src)
        r = rel(src)
        title = ""
        processed = False
        if fm:
            title = fm.get("Title", "") or fm.get("title", "") or src.stem
            processed = fm.get("Processed", False) or fm.get("processed", False)
        else:
            title = src.stem
        covered_by = coverage.get(r, [])
        if accept_covered and covered_by:
            processed = True
        entry = {
            "path": r,
            "title": title,
            "processed": processed,
            "covered_by": covered_by,
            "updated": date.today().isoformat(),
        }
        manifest.append(entry)
        status = "covered" if covered_by else ("processed" if processed else "unprocessed")
        print(f"  {r}: {status}")

    if update:
        SOURCE_MANIFEST.parent.mkdir(parents=True, exist_ok=True)
        with open(SOURCE_MANIFEST, "w", encoding="utf-8") as f:
            for e in manifest:
                f.write(json.dumps(e, ensure_ascii=False) + "\n")
        print(f"  source-manifest.jsonl: {len(manifest)} entries written")

    print(f"source-scan: {len(sources)} sources found")


def cmd_source_lint():
    """Validate source note frontmatter."""
    print("=== source-lint ===")
    errors = []
    # Load manifest coverage if exists
    manifest_map: dict[str, dict] = {}
    if SOURCE_MANIFEST.is_file():
        for line in SOURCE_MANIFEST.read_text(encoding="utf-8").splitlines():
            if line.strip():
                entry = json.loads(line)
                manifest_map[entry["path"]] = entry

    for src in source_notes():
        fm = parse_frontmatter(src)
        p = rel(src)
        if fm is None:
            # Many existing notes won't have frontmatter — this is a warning, not an error
            continue
        # Required fields
        for field in ["Title", "Reference", "Created", "Processed"]:
            if field not in fm and field.lower() not in fm:
                errors.append(f"{p}: missing field '{field}'")
        tags = fm.get("tags", [])
        if isinstance(tags, str):
            tags = [tags]
        if "source" not in tags:
            errors.append(f"{p}: tags must include 'source'")
        # If processed, check coverage
        processed = fm.get("Processed", fm.get("processed", False))
        if processed:
            manifest_entry = manifest_map.get(p, {})
            covered = manifest_entry.get("covered_by", [])
            if not covered:
                errors.append(f"{p}: marked Processed=true but no Wiki coverage found")

    if errors:
        for e in errors:
            print(f"  ERROR: {e}")
        print(f"source-lint: FAIL ({len(errors)} errors)")
        return False
    print(f"  {len(source_notes())} sources checked")
    print("source-lint: PASS")
    return True


def cmd_source_delta():
    """Show Raw sources not represented in the manifest."""
    print("=== source-delta ===")
    manifest_paths: set[str] = set()
    if SOURCE_MANIFEST.is_file():
        for line in SOURCE_MANIFEST.read_text(encoding="utf-8").splitlines():
            if line.strip():
                manifest_paths.add(json.loads(line)["path"])

    missing = []
    for src in source_notes():
        r = rel(src)
        if r not in manifest_paths:
            missing.append(r)
            print(f"  MISSING: {r}")

    if not missing:
        print("  All sources are in the manifest.")
    print(f"source-delta: {len(missing)} unmanifested sources")


def cmd_source_coverage():
    """Show which Raw sources are covered by compiled Wiki notes."""
    print("=== source-coverage ===")
    coverage: dict[str, list[str]] = {}
    for note in wiki_notes():
        fm = parse_frontmatter(note)
        if fm is None:
            continue
        for src in fm.get("sources", []):
            clean = src.strip("[]").split("|")[0]
            coverage.setdefault(clean, []).append(rel(note))

    covered = 0
    total = 0
    for src in source_notes():
        r = rel(src)
        total += 1
        covers = coverage.get(r, [])
        if covers:
            covered += 1
            print(f"  COVERED: {r} -> {covers}")
        else:
            print(f"  UNCOVERED: {r}")

    pct = (covered / total * 100) if total else 0
    print(f"source-coverage: {covered}/{total} ({pct:.1f}%) sources covered")


def cmd_search_catalog(query: str):
    """Search compiled Wiki notes through the catalog."""
    print(f"=== search-catalog: '{query}' ===")
    if not CATALOG.is_file():
        print("  catalog.jsonl not found. Run 'build' first.")
        return

    terms = query.lower().split()
    results = []
    for line in CATALOG.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        entry = json.loads(line)
        text = json.dumps(entry).lower()
        if all(t in text for t in terms):
            results.append(entry)

    if results:
        for r in results:
            print(f"  [{r['tag']}] {r['title']} — {r['path']}")
    else:
        print("  No matches found.")
    print(f"search-catalog: {len(results)} results")


def cmd_log(title: str, details: str):
    """Append a short entry to Wiki/log.md."""
    print("=== log ===")
    entry = f"\n## {date.today().isoformat()} — {title}\n\n{details}\n"
    if WIKI_LOG.is_file():
        existing = WIKI_LOG.read_text(encoding="utf-8")
    else:
        existing = "# Wiki Log\n"
    WIKI_LOG.write_text(existing + entry, encoding="utf-8")
    print(f"  Logged: {title}")
    print("log: DONE")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="LLM Wiki maintenance tool")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("doctor", help="Health check")
    sub.add_parser("build", help="Generate catalog and indexes")
    sub.add_parser("lint", help="Validate Wiki note frontmatter")

    ss = sub.add_parser("source-scan", help="Scan Raw sources")
    ss.add_argument("--update", action="store_true", help="Update source-manifest.jsonl")
    ss.add_argument("--accept-covered", action="store_true", help="Mark covered sources as processed")

    sub.add_parser("source-lint", help="Validate source frontmatter")
    sub.add_parser("source-delta", help="Show unmanifested sources")
    sub.add_parser("source-coverage", help="Show source coverage")

    sc = sub.add_parser("search-catalog", help="Search the catalog")
    sc.add_argument("--query", required=True, help="Search query")

    lg = sub.add_parser("log", help="Add a log entry")
    lg.add_argument("--title", required=True)
    lg.add_argument("--details", required=True)

    args = parser.parse_args()

    if args.command == "doctor":
        ok = cmd_doctor()
        sys.exit(0 if ok else 1)
    elif args.command == "build":
        cmd_build()
    elif args.command == "lint":
        ok = cmd_lint()
        sys.exit(0 if ok else 1)
    elif args.command == "source-scan":
        cmd_source_scan(update=args.update, accept_covered=args.accept_covered)
    elif args.command == "source-lint":
        ok = cmd_source_lint()
        sys.exit(0 if ok else 1)
    elif args.command == "source-delta":
        cmd_source_delta()
    elif args.command == "source-coverage":
        cmd_source_coverage()
    elif args.command == "search-catalog":
        cmd_search_catalog(args.query)
    elif args.command == "log":
        cmd_log(args.title, args.details)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
