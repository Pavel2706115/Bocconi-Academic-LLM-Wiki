import os
import fitz  # PyMuPDF

def convert_pdf_to_md(pdf_path, md_path):
    """Convert a PDF file to a Markdown file."""
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text("text")
    with open(md_path, 'w', encoding='utf-8') as md_file:
        md_file.write(text)

def scan_and_convert(directory):
    """Recursively scan directories and convert PDFs to Markdown."""
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.pdf'):
                pdf_path = os.path.join(root, file)
                md_path = os.path.splitext(pdf_path)[0] + '.md'
                convert_pdf_to_md(pdf_path, md_path)
                print(f"Converted: {pdf_path} to {md_path}")

if __name__ == "__main__":
    scan_and_convert(os.getcwd())
