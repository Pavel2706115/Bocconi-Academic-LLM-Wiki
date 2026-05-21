import os
import re

directory = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Sources\30067 ECONOMIC HISTORY"

for filename in sorted(os.listdir(directory)):
    if not filename.endswith(".md"):
        continue
    filepath = os.path.join(directory, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    headings = []
    for idx, line in enumerate(lines):
        if line.startswith("## "):
            headings.append((idx + 1, line.strip()))
            
    # Find consecutive identical headings
    duplicates = []
    for i in range(len(headings) - 1):
        if headings[i][1] == headings[i+1][1]:
            duplicates.append((headings[i], headings[i+1]))
            
    if duplicates:
        print(f"\nFile: {filename}")
        for d in duplicates:
            print(f"  Duplicate heading: '{d[0][1]}' at line {d[0][0]} and line {d[1][0]}")
