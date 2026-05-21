import os
import re
from pathlib import Path

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

# 1. Update 10_Recap and 16_state intervention references
recap_ref_files = [
    r"Raw/Sources/30067 ECONOMIC HISTORY/1_The pre-industrial economy_30067.md",
    r"Raw/Sources/30067 ECONOMIC HISTORY/2_The Great Divergence_30067.md",
    r"Raw/Sources/30067 ECONOMIC HISTORY/3_New players, new institutions_30067.md",
    r"Raw/Sources/30067 ECONOMIC HISTORY/7_The industrialisation process Social Aspects - cl 15.md",
    r"Raw/Sources/30692 FINANCIAL ACCOUNTING - MODULE 1/2025 - 30692 - Course presentation v2025.09.03 print.md"
]

for rel_path in recap_ref_files:
    full_path = vault_root / rel_path
    if full_path.exists():
        content = full_path.read_text(encoding='utf-8')
        content = content.replace("10_Recap ", "10_Recap")
        full_path.write_text(content, encoding='utf-8')
        print(f"Updated 10_Recap in: {rel_path}")

# Update Economic History overview sources list
history_overview = vault_root / "Wiki/Concepts/30067-ECONOMIC-HISTORY-Overview.md"
if history_overview.exists():
    content = history_overview.read_text(encoding='utf-8')
    content = content.replace("10_Recap .md", "10_Recap.md")
    content = content.replace("16_state intervention - Europe and WWII .md", "16_state intervention - Europe and WWII.md")
    history_overview.write_text(content, encoding='utf-8')
    print("Updated 30067-ECONOMIC-HISTORY-Overview.md sources list")

# Update Bretton Woods System sources list
bretton_woods = vault_root / "Wiki/Concepts/Bretton-Woods-System.md"
if bretton_woods.exists():
    content = bretton_woods.read_text(encoding='utf-8')
    content = content.replace("16_state intervention - Europe and WWII .md", "16_state intervention - Europe and WWII.md")
    bretton_woods.write_text(content, encoding='utf-8')
    print("Updated Bretton-Woods-System.md sources list")


# 2. Clean Pasted Image links from all markdown files in vault_root
pasted_image_re1 = re.compile(r'!?\[\[Pasted image [^\]]+\.png\]\]', re.IGNORECASE)
pasted_image_re2 = re.compile(r'!?\[\[Pasted image [^\]]+\]\]', re.IGNORECASE)

for r, d, files in os.walk(vault_root):
    if any(p in Path(r).parts for p in ['.git', '.obsidian', '__pycache__', 'scratch']):
        continue
    for f in files:
        if not f.endswith('.md'):
            continue
        full_path = Path(r) / f
        try:
            content = full_path.read_text(encoding='utf-8')
        except Exception as e:
            print(f"Error reading {f}: {e}")
            continue
            
        # Clean any lines that contain ONLY a Pasted image link (and optional bullet/indent)
        lines = content.splitlines()
        new_lines = []
        modified = False
        for line in lines:
            stripped = line.strip()
            # If the line is exactly a pasted image bullet like "- ![[Pasted image 20260503110607.png]]"
            # or just contains that link and whitespace, we remove the line entirely
            if stripped.startswith("- ![[Pasted image") and stripped.endswith("]]"):
                modified = True
                continue
            if stripped.startswith("![[Pasted image") and stripped.endswith("]]"):
                modified = True
                continue
            if stripped.startswith("- [[Pasted image") and stripped.endswith("]]"):
                modified = True
                continue
            
            # Otherwise, strip any inline pasted image links
            new_line = pasted_image_re1.sub("", line)
            new_line = pasted_image_re2.sub("", new_line)
            if new_line != line:
                modified = True
            new_lines.append(new_line)
            
        if modified:
            full_path.write_text("\n".join(new_lines), encoding='utf-8')
            print(f"Cleaned Pasted image links in: {full_path.relative_to(vault_root).as_posix()}")


# 3. Clean Mock links from their respective files
mock_files = [
    (r"Raw/Sources/30006 FINANCIAL MARKETS AND INSTITUTIONS/Exercises/Lect4_exercises.md", "[[Mock_general_1_solutions]]", "Mock_general_1_solutions"),
    (r"Raw/Sources/30066 ECONOMICS - MODULE 2 (MACROECONOMICS)/Macroeconomics Exercise Book-1-227.md", "[[Mock_general_1]]", "Mock_general_1"),
    (r"Raw/Sources/30066 ECONOMICS - MODULE 2 (MACROECONOMICS)/Macroeconomics Exercise Book-228-446.md", "[[BIG STACK MOCK]]", "BIG STACK MOCK"),
    (r"Raw/Sources/30066 ECONOMICS - MODULE 2 (MACROECONOMICS)/Macroeconomics Exercise Book.md", "[[BIG STACK MOCK]]", "BIG STACK MOCK"),
    (r"Raw/Sources/30066 ECONOMICS - MODULE 2 (MACROECONOMICS)/Presentations/L12 Labor Market.md", "[[Mock_partial_3_solutions]]", "Mock_partial_3_solutions"),
    (r"Raw/Sources/30264 PUBLIC FINANCE/L18 L19_Taxes on savings.md", "[[Mock_general_1_solutions]]", "Mock_general_1_solutions")
]

for rel_path, old_link, new_text in mock_files:
    full_path = vault_root / rel_path
    if full_path.exists():
        content = full_path.read_text(encoding='utf-8')
        content = content.replace(old_link, new_text)
        full_path.write_text(content, encoding='utf-8')
        print(f"Updated mock link in: {rel_path}")


# 4. Clean workflow-examples example
workflow_examples = vault_root / "Schema/workflow-examples.md"
if workflow_examples.exists():
    content = workflow_examples.read_text(encoding='utf-8')
    content = content.replace("[[Raw/Sources/30001 STATISTICS/Lecture 5/Lecture 5 Slides]]", "'Raw/Sources/30001 STATISTICS/Lecture 5/Lecture 5 Slides'")
    workflow_examples.write_text(content, encoding='utf-8')
    print("Updated workflow-examples.md")


# 5. Clean Log placeholder
log_placeholder = vault_root / "Wiki/Logs/Antigravity-Session-May-18/implementation_plan.md"
if log_placeholder.exists():
    content = log_placeholder.read_text(encoding='utf-8')
    content = content.replace("[[Wiki/Concepts/...]]", "`Wiki/Concepts/...`")
    log_placeholder.write_text(content, encoding='utf-8')
    print("Updated log placeholder in Antigravity-Session-May-18/implementation_plan.md")


# 6. Map all overview concept topic links to their actual parent topics under Wiki/Topics/
topic_mappings = {
    "30001-STATISTICS-Overview.md": ("30001-STATISTICS", "Statistics"),
    "30006-FINANCIAL-MARKETS-AND-INSTITUTIONS-Overview.md": ("30006-FINANCIAL-MARKETS-AND-INSTITUTIONS", "Financial-Markets-and-Institutions"),
    "30017-CORPORATE-FINANCE-Overview.md": ("30017-CORPORATE-FINANCE", "Corporate-Finance"),
    "30060-MANAGEMENT-Overview.md": ("30060-MANAGEMENT", "Management"),
    "30065-ECONOMICS---MODULE-1-MICROECONOMICS-Overview.md": ("30065-ECONOMICS---MODULE-1-MICROECONOMICS", "Microeconomics"),
    "30066-ECONOMICS---MODULE-2-MACROECONOMICS-Overview.md": ("30066-ECONOMICS---MODULE-2-MACROECONOMICS", "Macroeconomics"),
    "30067-ECONOMIC-HISTORY-Overview.md": ("30067-ECONOMIC-HISTORY", "Economic-History"),
    "30264-PUBLIC-FINANCE-Overview.md": ("30264-PUBLIC-FINANCE", "Public-Finance"),
    "30692-FINANCIAL-ACCOUNTING---MODULE-1-Overview.md": ("30692-FINANCIAL-ACCOUNTING---MODULE-1", "Financial-Accounting"),
    "Cash-Flow-Statements-Overview.md": ("Cash-Flow-Statements", "Financial-Accounting"),
    "Consolidated-Financial-Sheets-Overview.md": ("Consolidated-Financial-Sheets", "Financial-Accounting"),
    "FSA-GAME-Overview.md": ("FSA-GAME", "Financial-Accounting"),
    "Income-Taxes-Overview.md": ("Income-Taxes", "Financial-Accounting"),
    "Investments-in-other-corporations-Overview.md": ("Investments-in-other-corporations", "Financial-Accounting"),
    "Owner's-Equity-Overview.md": ("Owner's-Equity", "Financial-Accounting"),
    "Exercises-Overview.md": ("Exercises", "Financial-Markets-and-Institutions"),
    "Presentations-Overview.md": ("Presentations", "Macroeconomics"),
    "Uncategorized-Overview.md": ("Uncategorized", "Knowledge-Management")
}

for filename, (old_topic, new_topic) in topic_mappings.items():
    file_path = vault_root / f"Wiki/Concepts/{filename}"
    if file_path.exists():
        content = file_path.read_text(encoding='utf-8')
        
        # Replace frontmatter
        content = content.replace(f"[[Wiki/Topics/{old_topic}]]", f"[[Wiki/Topics/{new_topic}]]")
        content = content.replace(f"\"[[Wiki/Topics/{old_topic}]]\"", f"\"[[Wiki/Topics/{new_topic}]]\"")
        
        # Replace body links
        content = content.replace(f"[[Wiki/Topics/{old_topic}|{old_topic.replace('-', ' ')} Topic]]", f"[[Wiki/Topics/{new_topic}|{new_topic.replace('-', ' ')} Topic]]")
        content = content.replace(f"[[Wiki/Topics/{old_topic}|{old_topic} Topic]]", f"[[Wiki/Topics/{new_topic}|{new_topic.replace('-', ' ')} Topic]]")
        content = content.replace(f"[[Wiki/Topics/{old_topic}|Exercises Topic]]", f"[[Wiki/Topics/{new_topic}|Exercises Topic]]")
        content = content.replace(f"[[Wiki/Topics/{old_topic}|Presentations Topic]]", f"[[Wiki/Topics/{new_topic}|Presentations Topic]]")
        content = content.replace(f"[[Wiki/Topics/{old_topic}|Uncategorized Topic]]", f"[[Wiki/Topics/{new_topic}|Uncategorized Topic]]")
        
        file_path.write_text(content, encoding='utf-8')
        print(f"Updated topic link in: Wiki/Concepts/{filename}")

print("Successfully cleaned up all unresolved links!")
