import fitz

pdf_path = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\The_intelligent_investor.pdf"
doc = fitz.open(pdf_path)

print(f"Number of pages: {len(doc)}")
for i in range(80, 110):
    if i < len(doc):
        text = doc[i].get_text().strip()
        print(f"Page {i}: text length = {len(text)}")
        if text:
            print(f"  First 100 chars: {text[:100].replace('\n', ' ')}")
