import re
from pathlib import Path

clipping_path = Path("Clippings/Full text of Economics for Dummies_.md")
target_path = Path("Raw/Sources/Economics-for-Dummies.md")

content = clipping_path.read_text(encoding="utf-8")

# Find the end of the frontmatter in the clipping
if content.startswith("---"):
    end = content.find("---", 3)
    if end != -1:
        # Strip the old frontmatter and keep the rest
        rest = content[end + 3:].strip()
    else:
        rest = content.strip()
else:
    rest = content.strip()

# Prepare the new frontmatter
new_frontmatter = """---
course: Economics
course_code: "00000"
tags:
  - "source"
Links:
Title: "Economics for Dummies"
Reference: "Antonioni & Flynn (2011)"
Created: 2026-05-21
Processed: true
---

"""

# Write to the target path
target_path.write_text(new_frontmatter + rest + "\n", encoding="utf-8")
print("Successfully copied and formatted Economics for Dummies clipping to Raw/Sources/Economics-for-Dummies.md")
