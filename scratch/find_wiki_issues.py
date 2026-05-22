from pathlib import Path

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")
report_path = vault_root / "scratch" / "math_issues_report.txt"

content = report_path.read_text(encoding='utf-8')

entries = content.split("File: ")
wiki_files = []

for entry in entries[1:]:
    lines = entry.split("\n")
    filename = lines[0].strip()
    if filename.startswith("Wiki/"):
        wiki_files.append(filename)

print(f"Found {len(wiki_files)} Wiki files in report:")
for wf in wiki_files:
    print(f" - {wf}")
