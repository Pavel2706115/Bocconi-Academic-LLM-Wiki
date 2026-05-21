import os
import re
from pathlib import Path

workspace_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")
raw_sources_dir = workspace_root / "Raw" / "Sources"

INFERENCE = {
    "30001 STATISTICS": ("Statistics", "30001"),
    "30006 FINANCIAL MARKETS AND INSTITUTIONS": ("Financial Markets and Institutions", "30006"),
    "30017 CORPORATE FINANCE": ("Corporate Finance", "30017"),
    "30060 MANAGEMENT": ("Management", "30060"),
    "30065 ECONOMICS - MODULE 1 (MICROECONOMICS)": ("Economics - Module 1 (Microeconomics)", "30065"),
    "30066 ECONOMICS - MODULE 2 (MACROECONOMICS)": ("Economics - Module 2 (Macroeconomics)", "30066"),
    "30067 ECONOMIC HISTORY": ("Economic History", "30067"),
    "30264 PUBLIC FINANCE": ("Public Finance", "30264"),
    "30692 FINANCIAL ACCOUNTING - MODULE 1": ("Financial Accounting - Module 1", "30692"),
    "30693 FINANCIAL ACCOUNTING - MODULE 2": ("Financial Accounting - Module 2", "30693"),
    "30705 MARKETING": ("Marketing", "30705")
}

def infer_course_info(path):
    path_str = str(path).replace("\\", "/")
    for key, (course_name, course_code) in INFERENCE.items():
        if key.replace("\\", "/") in path_str:
            return course_name, course_code
    return None, None

processed_count = 0

for root, _, files in os.walk(raw_sources_dir):
    for file in files:
        if file.lower().endswith(".md"):
            full_path = Path(root) / file
            content = full_path.read_text(encoding="utf-8", errors="replace")
            
            if not content.startswith("---"):
                print(f"Skipping (no frontmatter): {full_path.relative_to(workspace_root)}")
                continue
                
            # Find the end of frontmatter
            end_match = re.search(r"Processed:\s*(true|false)\s*---", content, re.IGNORECASE)
            if end_match:
                end_pos = end_match.end()
                frontmatter_block = content[:end_pos]
                body_content = content[end_pos:]
                processed_val = end_match.group(1).lower() == "true"
            else:
                end_pos = content.find("---", 3)
                if end_pos == -1:
                    print(f"Skipping (malformed frontmatter): {full_path.relative_to(workspace_root)}")
                    continue
                frontmatter_block = content[:end_pos + 3]
                body_content = content[end_pos + 3:]
                
                proc_m = re.search(r"Processed:\s*(true|false)", frontmatter_block, re.IGNORECASE)
                if proc_m:
                    processed_val = proc_m.group(1).lower() == "true"
                else:
                    processed_val = False
            
            lines = frontmatter_block.splitlines()
            
            def get_val(key_name):
                for line in lines:
                    m = re.match(r"^" + re.escape(key_name) + r":\s*(.*)", line, re.IGNORECASE)
                    if m:
                        return m.group(1).strip()
                return None
                
            course = get_val("course")
            course_code = get_val("course_code")
            title = get_val("Title") or get_val("title")
            reference = get_val("Reference") or get_val("reference")
            created = get_val("Created") or get_val("created")
            
            # Infer course and course_code if missing or "None"
            inf_course, inf_code = infer_course_info(full_path)
            
            if not course or course.strip('"').strip("'").lower() == "none":
                course = inf_course or "Public Finance"
            else:
                course = course.strip('"').strip("'")
                
            if not course_code or course_code.strip('"').strip("'").lower() == "none":
                course_code = inf_code or "30264"
            else:
                course_code = course_code.strip('"').strip("'")
                
            # Reconstruct tags block
            tags_block = f'  - "source"\n  - course_{course_code}'
            
            # Reconstruct frontmatter
            new_fm = []
            new_fm.append("---")
            new_fm.append(f"course: {course}")
            new_fm.append(f'course_code: "{course_code}"')
            new_fm.append("tags:")
            new_fm.append(tags_block)
            new_fm.append("Links:")
            
            # Format Title line nicely
            if title:
                # If it already has quotes, keep it. Otherwise, if it has special characters, wrap it
                if not (title.startswith('"') and title.endswith('"')) and not (title.startswith("'") and title.endswith("'")):
                    title = f'"{title}"'
                new_fm.append(f"Title: {title}")
            else:
                new_fm.append(f"Title: \"{file[:-3]}\"")
                
            if reference:
                if not (reference.startswith('"') and reference.endswith('"')) and not (reference.startswith("'") and reference.endswith("'")):
                    reference = f'"{reference}"'
                new_fm.append(f"Reference: {reference}")
            else:
                new_fm.append('Reference: "Course Material"')
                
            if created:
                new_fm.append(f"Created: {created}")
            else:
                new_fm.append("Created: 2026-05-18")
                
            new_fm.append(f"Processed: {'true' if processed_val else 'false'}")
            new_fm.append("---")
            
            new_frontmatter = "\n".join(new_fm) + "\n"
            
            # Ensure body_content starts with newline
            if not body_content.startswith("\n"):
                body_content = "\n" + body_content
                
            new_content = new_frontmatter + body_content
            
            # Write back to file
            full_path.write_text(new_content, encoding="utf-8")
            processed_count += 1

print(f"Successfully standardized {processed_count} files!")
