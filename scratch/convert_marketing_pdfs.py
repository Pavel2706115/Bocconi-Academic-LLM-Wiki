import os
import sys
import pymupdf4llm
from pathlib import Path

# Reconfigure stdout to prevent encoding errors on non-ASCII characters in paths
sys.stdout.reconfigure(encoding='utf-8')

# Paths
ROOT = Path(__file__).resolve().parent.parent
SRC_DIR = ROOT / "Raw" / "Files" / "30705 MARKETING"
DEST_DIR = ROOT / "Raw" / "Sources" / "30705 MARKETING"

def convert_all():
    print(f"Scanning for PDFs in 30705 MARKETING folder...")
    if not SRC_DIR.is_dir():
        print(f"Error: Source directory 30705 MARKETING does not exist.")
        return
        
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    
    # Sort files to convert in numerical order if possible
    pdf_files = sorted(SRC_DIR.glob("*.pdf"), key=lambda p: p.name)
    
    for pdf_path in pdf_files:
        md_name = pdf_path.stem + ".md"
        md_path = DEST_DIR / md_name
        
        print(f"Converting {pdf_path.name} to {md_name}...")
        try:
            markdown_content = pymupdf4llm.to_markdown(str(pdf_path))
            
            # Format raw markdown nicely with standard YAML frontmatter for raw sources
            # course: Marketing, course_code: 30705, tag: source, course_30705
            frontmatter = f"""---
course: Marketing
course_code: "30705"
tags:
  - source
  - course_30705
Links:
Title: "Marketing 30705 - {pdf_path.stem}"
Reference: Course Material
Created: 2026-05-29
Processed: false
---

"""
            # Clean up the markdown content slightly
            clean_content = markdown_content.replace('\r\n', '\n')
            
            # Write to destination
            md_path.write_text(frontmatter + clean_content, encoding="utf-8")
            print(f"Success: Saved to {md_name}")
        except Exception as e:
            print(f"Error converting {pdf_path.name}: {e}")

if __name__ == "__main__":
    convert_all()
