import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\The_intelligent_investor.pdf"
doc = fitz.open(pdf_path)

print(f"Number of pages: {len(doc)}")
for i in range(len(doc)):
    text = doc[i].get_text()
    if "index" in text.lower() and len(text) > 0:
        # Check if this page is primarily index entries
        lines = text.strip().split("\n")
        index_entries = sum(1 for line in lines if "," in line and any(char.isdigit() for char in line))
        if index_entries > len(lines) * 0.4:
            print(f"Page {i}: appears to be an INDEX page (has {index_entries} index-like lines out of {len(lines)})")
            # Let's print the first page that is an index
            break
