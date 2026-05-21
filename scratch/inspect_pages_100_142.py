import fitz

pdf_path = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\The_intelligent_investor.pdf"
doc = fitz.open(pdf_path)

print(f"Number of pages: {len(doc)}")
for i in [100, 110, 120, 130, 140]:
    if i < len(doc):
        print(f"\n--- PAGE {i} SNIPPET ---")
        print(doc[i].get_text().strip()[:400])
        print("-----------------------")
