import os
import re

concepts_dir = "Wiki/Concepts"
for filename in os.listdir(concepts_dir):
    if not filename.endswith(".md"):
        continue
    filepath = os.path.join(concepts_dir, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Check if the content has the [[Raw/Sources/30705 MARKETING/...]] pattern in frontmatter
    # We want to match: - "[[Raw/Sources/30705 MARKETING/Presentation X.md]]"
    new_content = re.sub(
        r'-\s*"\[\[Raw/Sources/30705 MARKETING/Presentation (\d+)\.md\]\]"',
        r'- "Raw/Sources/30705 MARKETING/Presentation \1.md"',
        content
    )
    
    if new_content != content:
        with open(filepath, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_content)
        print(f"Cleaned brackets in {filename}")
