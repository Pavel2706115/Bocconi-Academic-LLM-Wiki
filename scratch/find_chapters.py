import fitz
import re

pdf_path = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\The_intelligent_investor.pdf"
doc = fitz.open(pdf_path)

print("--- DETECTED CHAPTER HEADINGS IN THE PDF ---")
for i, page in enumerate(doc):
    text = page.get_text()
    for line in text.split("\n"):
        line = line.strip()
        if re.search(r"^(CHAPTER|Chapter)\s+\d+", line) or re.search(r"^INTRODUCTION\b", line, re.IGNORECASE):
            print(f"Page {i}: {line}")
