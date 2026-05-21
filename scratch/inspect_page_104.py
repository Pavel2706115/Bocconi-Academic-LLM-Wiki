import fitz
import sys

sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi\Raw\Files\Economics PDF Books\The_intelligent_investor.pdf"
doc = fitz.open(pdf_path)

print(f"--- PAGE 104 ---")
print(doc[104].get_text())
print("\n--- PAGE 103 ---")
print(doc[103].get_text())
