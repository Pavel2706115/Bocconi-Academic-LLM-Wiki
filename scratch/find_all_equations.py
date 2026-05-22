import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

# Let's search for:
# 1. Mathematical Alphanumeric Symbols: U+1D400 to U+1D7FF (using \U0001d400-\U0001d7ff)
# 2. Sinhalese/Malayalam/Ethiopic characters that shouldn't be in Italian/English academic text:
#    Malayalam: U+0D00 to U+0D7F
#    Sinhala: U+0D80 to U+0DFF
#    Ethiopic: U+1200 to U+137F
# 3. Triple-dollar signs: $$$

math_issues_pattern = re.compile(
    r'[\U0001d400-\U0001d7ff\u0d00-\u0d7f\u0d80-\u0dff\u1200-\u137f]'
)
triple_dollar_pattern = re.compile(r'\$\$\$')

files_with_math_issues = []

for r, d, files in os.walk(vault_root):
    if any(p in Path(r).parts for p in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']):
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        # Skip top level md files
        if Path(r) == vault_root:
            continue
            
        full_path = Path(r) / f
        rel_file = full_path.relative_to(vault_root).as_posix()
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            continue
            
        triple_matches = list(triple_dollar_pattern.finditer(content))
        math_issues_matches = math_issues_pattern.findall(content)
        
        if triple_matches or math_issues_matches:
            unique_unicode = sorted(list(set(math_issues_matches)))
            files_with_math_issues.append({
                'file': rel_file,
                'triple_count': len(triple_matches),
                'unicode_chars': unique_unicode
            })

report_path = vault_root / "scratch" / "math_issues_report.txt"
with open(report_path, "w", encoding="utf-8") as out:
    out.write(f"Found {len(files_with_math_issues)} files with mathematical issues.\n\n")
    for entry in files_with_math_issues:
        out.write(f"File: {entry['file']}\n")
        out.write(f"  Triple-dollar count: {entry['triple_count']}\n")
        if entry['unicode_chars']:
            chars_str = ", ".join([f"{c} (U+{ord(c):04X})" for c in entry['unicode_chars']])
            out.write(f"  Mathematical/Foreign Unicode characters ({len(entry['unicode_chars'])} types): {chars_str}\n")
        out.write("\n")

print("Report written successfully.")
print(f"Found {len(files_with_math_issues)} files with potential issues.")
for entry in files_with_math_issues:
    safe_file_name = entry['file'].encode('ascii', 'replace').decode('ascii')
    print(f" - {safe_file_name} (Triple count: {entry['triple_count']}, Special Unicode types: {len(entry['unicode_chars'])})")
