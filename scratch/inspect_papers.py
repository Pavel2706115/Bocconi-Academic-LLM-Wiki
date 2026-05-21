import fitz
import sys
import os

sys.stdout.reconfigure(encoding='utf-8')

papers_dir = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\most_similar_papers_to_this_one"
key_papers = [
    "Value_Investing_Essence_And_Ways_Of_Find.pdf",
    "The_Efficient_Market_Hypothesis_theFinan.pdf",
    "The_rationality_of_index_investing_and_p.pdf"
]

for paper in key_papers:
    p_path = os.path.join(papers_dir, paper)
    if os.path.exists(p_path):
        doc = fitz.open(p_path)
        print(f"\n==================================================")
        print(f"PAPER: {paper}")
        print(f"Pages: {len(doc)}")
        print(f"Metadata: {doc.metadata}")
        print("--- FIRST 600 CHARACTERS ---")
        print(doc[0].get_text().strip()[:600])
        print("==================================================")
