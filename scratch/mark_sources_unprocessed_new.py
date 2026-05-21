import os
import re

files_to_fix = [
    r"Raw/Sources/30001 STATISTICS/Lecture 10/Lecture 10 Key Points.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 13-14/Lecture 13-14 Slides Point estimation.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 13-14/THE GREAT PEPUS.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 15-16/Lecture 15-16 Interval Estimation.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 15-16/PEPUS-X.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 17-21/Lecture 17-21 Slides_Hypotheses Testing.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 17-21/PEPUS-XXX.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 2/Lecture 2 Slides.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 22-24/Lesson 22-24_Simple Linear Regression.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 22-24/Simple Linear Regression Annotated Output WOW!.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 22-24/Super Comprehensive Atomic Scheme for Simple Linear Regression (updated).md",
    r"Raw/Sources/30001 STATISTICS/Lecture 25-27/Categorical Variables in Multiple Linear Regression.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 25-27/Lecture 25_27 Slides - Multiple Regression.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 25-27/MLR Annotated Output.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 28/Lecture 28 Slides.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 3-4/Powerful Scheme of Tables and Charts.md",
    r"Raw/Sources/30001 STATISTICS/Lecture 8-9/Lecture 8-9 Slides.md",
    r"Raw/Sources/30006 FINANCIAL MARKETS AND INSTITUTIONS/Lectures/Lect21_notes_mcr.md"
]

workspace_root = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi"

for rel_path in files_to_fix:
    full_path = os.path.join(workspace_root, rel_path)
    if os.path.isfile(full_path):
        print(f"Fixing: {rel_path}")
        content = open(full_path, "r", encoding="utf-8", errors="replace").read()
        # Replace 'Processed: true' or 'processed: true' with 'Processed: false'
        new_content = re.sub(r"^Processed:\s*true", "Processed: false", content, flags=re.MULTILINE | re.IGNORECASE)
        # Also let's check if it doesn't have Processed at all or has it already false
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"Not found: {rel_path}")

print("Done fixing files!")
