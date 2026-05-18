import os
import re
from pathlib import Path
from datetime import date

ROOT = Path("c:/Users/User/OneDrive - Università Commerciale Luigi Bocconi")
RAW_SOURCES = ROOT / "Raw" / "Sources"
WIKI = ROOT / "Wiki"

def parse_title(path, text):
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip().replace('"', "'")
    return path.stem.replace('"', "'")

def process_sources():
    sources = list(RAW_SOURCES.rglob("*.md"))
    course_map = {}
    
    for src in sources:
        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
            
        rel_path = src.relative_to(ROOT).as_posix()
        course_name = src.parent.name if src.parent != RAW_SOURCES else "Uncategorized"
        
        if course_name not in course_map:
            course_map[course_name] = []
        course_map[course_name].append(rel_path)
        
        today = date.today().isoformat()
        
        if text.startswith("---"):
            # Has frontmatter, we need to inject missing fields
            end_idx = text.find("---", 3)
            if end_idx != -1:
                fm_block = text[3:end_idx].strip()
                rest = text[end_idx+3:]
                
                # Check what's missing
                lines = fm_block.splitlines()
                has_title = any(l.lower().startswith("title:") for l in lines)
                has_ref = any(l.lower().startswith("reference:") for l in lines)
                has_created = any(l.lower().startswith("created:") for l in lines)
                has_processed = any(l.lower().startswith("processed:") for l in lines)
                
                new_fm = []
                if not has_title:
                    title = parse_title(src, text)
                    new_fm.append(f'Title: "{title}"')
                if not has_ref:
                    new_fm.append('Reference: "Course Material"')
                if not has_created:
                    new_fm.append(f'Created: {today}')
                if not has_processed:
                    new_fm.append('Processed: true')
                    
                # Handle tags
                if not any(l.startswith("tags:") for l in lines):
                    new_fm.append('tags:\n  - "source"')
                else:
                    # check if source is in tags
                    if "source" not in fm_block:
                        # Append source to existing tags block... this is tricky with regex, let's just append
                        new_fm.append('  - "source"')
                
                # Reconstruct
                combined_fm = fm_block + "\n" + "\n".join(new_fm)
                src.write_text("---\n" + combined_fm + "\n---" + rest, encoding="utf-8")
        else:
            # No frontmatter at all
            title = parse_title(src, text)
            fm = f"""---
Title: "{title}"
Author: "Bocconi"
Reference: "Course Material"
ContentType:
  - "markdown"
Created: {today}
Processed: true
tags:
  - "source"
---
"""
            src.write_text(fm + "\n" + text, encoding="utf-8")

    # Generate Wiki notes
    for course, files in course_map.items():
        if not files: continue
        
        clean_course = course.replace(" ", "-").replace("(", "").replace(")", "").replace(".", "")
        
        # Topic Note
        topic_path = WIKI / "Topics" / f"{clean_course}.md"
        sources_yaml = "\n".join(f'  - "[[{f}]]"' for f in files)
        
        topic_content = f"""---
tags:
  - "topic"
topics: []
status: seed
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
sources:
{sources_yaml}
source_count: {len(files)}
aliases:
  - "{course}"
---

# {course}

## Overview

High-level overview of {course}.

## Core Concepts

- [[Wiki/Concepts/{clean_course}-Overview|{course} Overview]]

## Key Takeaways

- Collection of all materials for {course}.

## Sources

<!-- Auto-populated from frontmatter `sources` field -->
"""
        topic_path.parent.mkdir(parents=True, exist_ok=True)
        topic_path.write_text(topic_content, encoding="utf-8")
        
        # Concept Note
        concept_path = WIKI / "Concepts" / f"{clean_course}-Overview.md"
        concept_content = f"""---
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/{clean_course}]]"
status: seed
created: {date.today().isoformat()}
updated: {date.today().isoformat()}
sources:
{sources_yaml}
source_count: {len(files)}
aliases:
  - "{course} Overview"
---

# {course} Overview

## Definition

Overview concept covering all raw materials for {course}.

## Key Properties

- Provides comprehensive index of course sources.

## Examples

- Course slides and transcripts.

## Related Concepts

- [[Wiki/Topics/{clean_course}|{course} Topic]]

## Sources

<!-- Auto-populated from frontmatter `sources` field -->
"""
        concept_path.parent.mkdir(parents=True, exist_ok=True)
        concept_path.write_text(concept_content, encoding="utf-8")
        
if __name__ == "__main__":
    process_sources()
