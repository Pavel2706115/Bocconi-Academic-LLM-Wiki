import fitz

pdf_path = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\The_intelligent_investor.pdf"
doc = fitz.open(pdf_path)

print(f"Number of pages: {len(doc)}")
for i in range(min(15, len(doc))):
    text = doc[i].get_text().strip()
    images = doc[i].get_images()
    print(f"Page {i}: text length = {len(text)}, images = {len(images)}")
    if text:
        print(f"--- TEXT SNIPPET PAGE {i} ---")
        print(text[:200])
        print("----------------------------")
