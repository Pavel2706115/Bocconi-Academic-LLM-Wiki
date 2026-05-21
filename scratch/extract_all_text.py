import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

def extract_pdf_info(pdf_path, name):
    print(f"\n==================================================")
    print(f"ANALYZING: {name}")
    doc = fitz.open(pdf_path)
    print(f"Total Pages: {len(doc)}")
    
    # Print first page full text or first 2 pages
    full_text = ""
    for i in range(min(3, len(doc))):
        full_text += f"\n--- PAGE {i} ---\n" + doc[i].get_text()
        
    print(full_text[:3000])
    
    # Search for headings
    print("\n--- HEADINGS SEARCH ---")
    for i, page in enumerate(doc):
        text = page.get_text()
        for line in text.split("\n"):
            line = line.strip()
            # If line is short and uppercase, or starts with numbers/sections
            if len(line) > 3 and len(line) < 60 and (line.isupper() or line[0].isdigit() or "Abstract" in line or "Conclusion" in line):
                print(f"Page {i}: {line}")
    print(f"==================================================")

extract_pdf_info(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\most_similar_papers_to_this_one\Value_Investing_Essence_And_Ways_Of_Find.pdf", "Value Investing - Petrova")
extract_pdf_info(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\most_similar_papers_to_this_one\The_Efficient_Market_Hypothesis_theFinan.pdf", "EMH - Stephen Brown")
extract_pdf_info(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\most_similar_papers_to_this_one\The_rationality_of_index_investing_and_p.pdf", "Index Investing - Eagle")
