import os
import re

# File paths
src_file = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Sources\30067 ECONOMIC HISTORY\6_The industrialisation process_2.md"
dest_file = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\scratch\6_test_out.md"

# Read original
with open(src_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1. Patterns for metadata lines to remove
metadata_patterns = [
    re.compile(r'^\d{4}/\d{4}$'), # 2024/2025
    re.compile(r'^30067\s*-\s*cl\s*-\s*\d+$'), # 30067 - cl - 15
    re.compile(r'^30067\s*-\s*cl-\s*\d+$'), # 30067 - cl- 15
    re.compile(r'^30067\s*-\s*cl\b.*$'), # 30067 - cl...
    re.compile(r'^30067$'),
    re.compile(r'^(a\.y\.|a\.y|A\.Y\.|A\.Y)\.?\s*\d{4}/\d{4}(\s*30067)?$'),
    re.compile(r'^Sonia Schifano$', re.IGNORECASE),
    re.compile(r'^Economic\s+history\b.*$', re.IGNORECASE),
    re.compile(r'^cl\s*-\s*\d+$'),
]

# 2. Arrows to bullet points
arrow_regex = r"(?:[➔➢➢➔➢➔➔➢➔➤➔➜➝➞➟➡➢➢➔]|->|-->|=>|==>|→|⟶|⟹|⟾|➢)"
bullet_arrow_pat = re.compile(rf"^\s*-\s*{arrow_regex}\s*")
start_arrow_pat = re.compile(rf"^\s*{arrow_regex}\s*")

# Filter out metadata lines and format arrows
cleaned_lines = []
for line in lines:
    clean = line.strip()
    
    # Check if frontmatter boundary
    # We do not touch frontmatter content
    # Let's check if we are in frontmatter
    # (Actually we can just skip lines before the first --- and second --- closing fence)
    
    # Let's check metadata pattern
    is_metadata = False
    for pat in metadata_patterns:
        if pat.match(clean):
            is_metadata = True
            break
            
    if is_metadata:
        continue # Skip this line
        
    # Format arrows to normal bullets
    if bullet_arrow_pat.match(line):
        line = bullet_arrow_pat.sub("- ", line)
    elif start_arrow_pat.match(line) and not clean.startswith("---") and not clean.startswith("##"):
        line = start_arrow_pat.sub("- ", line)
        
    cleaned_lines.append(line)

# 3. Remove duplicate consecutive headings
deduped_lines = []
last_heading = None

# Track if we are inside frontmatter
in_frontmatter = False
frontmatter_fence_count = 0

for line in cleaned_lines:
    clean = line.strip()
    
    if clean == "---":
        frontmatter_fence_count += 1
        in_frontmatter = (frontmatter_fence_count == 1)
        deduped_lines.append(line)
        continue
        
    if in_frontmatter:
        deduped_lines.append(line)
        continue
        
    # Check if heading
    if line.startswith("## "):
        heading_text = clean[3:].strip()
        if heading_text == last_heading:
            # Skip this duplicate heading line!
            continue
        else:
            last_heading = heading_text
            deduped_lines.append(line)
    else:
        deduped_lines.append(line)

# 4. Clean up multiple empty lines that might have been left over
final_lines = []
for line in deduped_lines:
    if line.strip() == "" and final_lines and final_lines[-1].strip() == "":
        continue
    final_lines.append(line)

with open(dest_file, "w", encoding="utf-8") as f:
    f.writelines(final_lines)

print("Test output written successfully.")
