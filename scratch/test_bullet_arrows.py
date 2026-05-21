import os
import re

directory = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Sources\30067 ECONOMIC HISTORY"

# Unicode arrows and standard arrow symbols
arrow_regex = r"(?:[➔➢➢➔➢➔➔➢➔➤➔➜➝➞➟➡➢➢➔]|->|-->|=>|==>|→|⟶|⟹|⟾|➢)"

# 1. Bullet point followed by an arrow
bullet_arrow_pat = re.compile(rf"^\s*-\s*{arrow_regex}\s*")
# 2. Line starting with an arrow
start_arrow_pat = re.compile(rf"^\s*{arrow_regex}\s*")

report_lines = []

for filename in sorted(os.listdir(directory)):
    if not filename.endswith(".md"):
        continue
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
        
    for idx, line in enumerate(lines):
        clean_line = line.strip()
        if bullet_arrow_pat.match(line):
            replaced = bullet_arrow_pat.sub("- ", line)
            report_lines.append(f"{filename}:{idx+1}: BULLET_ARROW: '{clean_line}' -> '{replaced.strip()}'\n")
        elif start_arrow_pat.match(line) and not clean_line.startswith("---") and not clean_line.startswith("##"):
            replaced = start_arrow_pat.sub("- ", line)
            report_lines.append(f"{filename}:{idx+1}: START_ARROW:  '{clean_line}' -> '{replaced.strip()}'\n")

with open(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\scratch\bullet_arrows_report.txt", "w", encoding="utf-8") as f:
    f.writelines(report_lines)

print(f"Report written. Found {len(report_lines)} matching lines.")
