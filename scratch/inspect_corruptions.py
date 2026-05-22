import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

# Pattern for Malayalam, Sinhala, Ethiopic characters
pattern = re.compile(r'([\u0d00-\u0d7f\u0d80-\u0dff\u1200-\u137f])')

seen_contexts = {}

for root, dirs, files in os.walk(vault_root):
    if any(p in Path(root).parts for p in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']):
        continue
    for file in files:
        if not file.endswith('.md'):
            continue
        file_path = Path(root) / file
        try:
            lines = file_path.read_text(encoding='utf-8').splitlines()
        except Exception:
            continue
        
        for idx, line in enumerate(lines):
            matches = pattern.findall(line)
            if matches:
                for char in set(matches):
                    if char not in seen_contexts:
                        seen_contexts[char] = []
                    # Keep at most 5 context examples
                    if len(seen_contexts[char]) < 5:
                        seen_contexts[char].append((file_path.relative_to(vault_root).as_posix(), idx + 1, line))

for char, contexts in sorted(seen_contexts.items(), key=lambda x: ord(x[0])):
    print(f"Character: {char} (U+{ord(char):04X})")
    for file, line_num, text in contexts:
        safe_line = text.strip()
        print(f"  [{file}:{line_num}]: {safe_line}")
    print()
