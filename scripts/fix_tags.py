import os
from pathlib import Path
from datetime import date

ROOT = Path("c:/Users/User/OneDrive - Università Commerciale Luigi Bocconi")
RAW_SOURCES = ROOT / "Raw" / "Sources"

def fix_frontmatter():
    sources = list(RAW_SOURCES.rglob("*.md"))
    for src in sources:
        try:
            text = src.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
            
        if text.startswith("---"):
            end_idx = text.find("---", 3)
            if end_idx != -1:
                fm_block = text[3:end_idx]
                rest = text[end_idx+3:]
                
                # Check for tags
                lines = fm_block.splitlines()
                has_source_tag = False
                in_tags = False
                new_lines = []
                tags_idx = -1
                
                for i, line in enumerate(lines):
                    if line.strip() == 'tags:':
                        tags_idx = len(new_lines)
                        in_tags = True
                    elif in_tags and line.strip().startswith('-'):
                        if '"source"' in line or "'source'" in line or ' source' in line or line.strip() == '- source':
                            has_source_tag = True
                    elif in_tags and line.strip() != "" and not line.strip().startswith('-'):
                        in_tags = False
                        
                    new_lines.append(line)
                
                if not has_source_tag:
                    if tags_idx != -1:
                        # Insert right after tags:
                        new_lines.insert(tags_idx + 1, '  - "source"')
                    else:
                        new_lines.append("tags:")
                        new_lines.append('  - "source"')
                        
                combined_fm = "\n".join(new_lines)
                src.write_text("---" + combined_fm + "\n---" + rest, encoding="utf-8")

if __name__ == "__main__":
    fix_frontmatter()
