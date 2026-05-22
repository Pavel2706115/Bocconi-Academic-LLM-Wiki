import os
import sys
from pathlib import Path

# Ensure UTF-8 stdout configuration for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")
chars_to_find = "ഥതҧ෡෠෢෨መෝො෍ቊቐሼቀቁቑ"

def scan():
    for root, dirs, files in os.walk(vault_root):
        dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian', '__pycache__', 'scratch']]
        for file in files:
            if not file.endswith('.md'):
                continue
            path = Path(root) / file
            try:
                content = path.read_text(encoding='utf-8')
            except Exception as e:
                continue
            
            lines = content.splitlines()
            for idx, line in enumerate(lines):
                found = [c for c in chars_to_find if c in line]
                if found:
                    print(f"{path.relative_to(vault_root)}:L{idx+1}: contains {found}")
                    print(f"  Line: {line}")

if __name__ == "__main__":
    scan()
