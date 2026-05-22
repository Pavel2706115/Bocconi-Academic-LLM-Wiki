import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")
report_path = vault_root / "scratch" / "math_issues_report.txt"

content = report_path.read_text(encoding='utf-8')

entries = content.split("File: ")
corrupted_files = []

for entry in entries[1:]:
    lines = entry.split("\n")
    filename = lines[0].strip()
    
    has_corrupt = False
    corrupt_chars = []
    
    match = re.search(r'Mathematical/Foreign Unicode characters.*:\s*(.*)', entry)
    if match:
        char_tokens = match.group(1).split(", ")
        for tok in char_tokens:
            if "U+0D" in tok or "U+12" in tok or "U+13" in tok:
                has_corrupt = True
                corrupt_chars.append(tok)
                
    if has_corrupt:
        corrupted_files.append((filename, corrupt_chars))

print(f"Found {len(corrupted_files)} files with specific Malayalam/Sinhalese/Ethiopic character distortions:")
for fn, chars in corrupted_files:
    safe_fn = fn.encode('ascii', 'replace').decode('ascii')
    safe_chars = [c.encode('ascii', 'replace').decode('ascii') for c in chars]
    print(f" - {safe_fn}: {', '.join(safe_chars)}")
