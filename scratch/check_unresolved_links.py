import os
import re
from pathlib import Path

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

# Gather all existing files in the vault (case-insensitive for resolution matching)
all_files = {}
for r, d, files in os.walk(vault_root):
    # Skip .git, .obsidian, etc.
    if any(p in Path(r).parts for p in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']):
        continue
    for f in files:
        full_path = Path(r) / f
        rel_path = full_path.relative_to(vault_root).as_posix()
        name_lower = f.lower()
        stem_lower = Path(f).stem.lower()
        
        # Index by rel_path (lowercase)
        all_files[rel_path.lower()] = rel_path
        # Also index by base name / stem to resolve short links
        all_files[name_lower] = rel_path
        all_files[stem_lower] = rel_path

print(f"Indexed {len(all_files)} file keys in the vault.")

# Match Obsidian wikilinks: [[target]] or [[target|display]]
# We need to handle headers/anchors as well: [[target#anchor]]
wikilink_re = re.compile(r'\[\[([^\]\|]+)(?:\|[^\]]*)?\]\]')

unresolved = []

# Scan all markdown files
for r, d, files in os.walk(vault_root):
    if any(p in Path(r).parts for p in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']):
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        full_path = Path(r) / f
        rel_file = full_path.relative_to(vault_root).as_posix()
        
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {rel_file}: {e}")
            continue
            
        links = wikilink_re.findall(content)
        for link in links:
            # Strip trailing/leading spaces
            link_target = link.strip()
            
            # Skip empty links
            if not link_target:
                continue
                
            # Handle headers: e.g. "Note Name#Header" -> "Note Name"
            if '#' in link_target:
                link_target = link_target.split('#')[0].strip()
                # If it's a local header link like [[#Header]], skip it
                if not link_target:
                    continue
            
            # Resolve link target
            resolved = False
            
            # Try matching absolute/relative path with .md suffix first
            targets_to_try = [
                link_target.lower(),
                (link_target + ".md").lower(),
                Path(link_target).name.lower(),
                Path(link_target + ".md").name.lower(),
                Path(link_target).stem.lower()
            ]
            
            for t in targets_to_try:
                if t in all_files:
                    resolved = True
                    break
                    
            if not resolved:
                unresolved.append((rel_file, link))

print(f"\nFound {len(unresolved)} unresolved links:")
for file, link in unresolved:
    print(f" - In {file}: [[{link}]]")
