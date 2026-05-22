import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

# Pattern for mathematical alphanumeric symbols and foreign blocks
math_issues_pattern = re.compile(
    r'[\U0001d400-\U0001d7ff\u0d00-\u0d7f\u0d80-\u0dff\u1200-\u137f]'
)

lines_with_issues = []

for r, d, files in os.walk(vault_root):
    if any(p in Path(r).parts for p in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']):
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        if Path(r) == vault_root:
            continue
            
        full_path = Path(r) / f
        rel_file = full_path.relative_to(vault_root).as_posix()
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception:
            continue
            
        lines = content.splitlines()
        for idx, line in enumerate(lines):
            matches = math_issues_pattern.findall(line)
            if matches:
                lines_with_issues.append({
                    'file': rel_file,
                    'line_num': idx + 1,
                    'line_content': line,
                    'matches': sorted(list(set(matches)))
                })

report_path = vault_root / "scratch" / "math_lines_context.txt"
with open(report_path, "w", encoding="utf-8") as out:
    out.write(f"Found {len(lines_with_issues)} lines with potential mathematical unicode issues.\n\n")
    for item in lines_with_issues:
        out.write(f"File: {item['file']} (Line {item['line_num']})\n")
        out.write(f"Matches: {', '.join([f'{c} (U+{ord(c):04X})' for c in item['matches']])}\n")
        out.write(f"Content: {item['line_content']}\n")
        out.write("-" * 80 + "\n\n")

print("Report written successfully.")
print(f"Found {len(lines_with_issues)} lines to examine.")
