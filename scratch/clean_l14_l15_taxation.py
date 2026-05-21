import re
from pathlib import Path

file_path = Path(r"C:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Sources\30264 PUBLIC FINANCE\L14 L15_Taxation.md")
content = file_path.read_text(encoding='utf-8')

# Remove lines that contain [Pasted image ...]
lines = content.splitlines()
new_lines = []
removed_count = 0

for line in lines:
    if "[Pasted image " in line:
        removed_count += 1
        continue
    new_lines.append(line)

new_content = "\n".join(new_lines) + "\n"
file_path.write_text(new_content, encoding='utf-8')
print(f"Removed {removed_count} lines from {file_path.name}")
