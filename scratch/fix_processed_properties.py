import os
import re
import json
import sys
from pathlib import Path

# Ensure UTF-8 stdout configuration for Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

vault_root = Path(r"c:\Users\User\OneDrive - Università Commerciale Luigi Bocconi")

def fix_types_json():
    types_path = vault_root / ".obsidian" / "types.json"
    if not types_path.exists():
        print("types.json not found!")
        return False
        
    try:
        data = json.loads(types_path.read_text(encoding="utf-8"))
        if "types" in data and "Processed" in data["types"]:
            if data["types"]["Processed"] != "checkbox":
                data["types"]["Processed"] = "checkbox"
                types_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
                print("Updated .obsidian/types.json: set Processed to 'checkbox'.")
                return True
            else:
                print(".obsidian/types.json already has Processed set to 'checkbox'.")
        else:
            if "types" not in data:
                data["types"] = {}
            data["types"]["Processed"] = "checkbox"
            types_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
            print("Added Processed to .obsidian/types.json as 'checkbox'.")
            return True
    except Exception as e:
        print(f"Error updating types.json: {e}")
    return False

def clean_frontmatter_processed(content):
    if not content.startswith("---"):
        return content, False
        
    end = content.find("---", 3)
    if end == -1:
        return content, False
        
    frontmatter = content[3:end]
    lines = frontmatter.splitlines()
    changed = False
    new_lines = []
    
    for line in lines:
        # Match case-insensitive processed: <val>
        m = re.match(r'^(\s*)processed\s*:\s*(.*)', line, re.IGNORECASE)
        if m:
            indent = m.group(1)
            val = m.group(2).strip().lower()
            
            # Standardize value to literal true/false
            if val in ['true', '"true"', "'true'", 'yes', '"yes"', "'yes'", '1']:
                new_val = "true"
            elif val in ['false', '"false"', "'false'", 'no', '"no"', "'no'", '0']:
                new_val = "false"
            else:
                # Keep other values unchanged, but clean quotes if any
                new_val = val.strip('"\'')
                
            new_line = f"{indent}Processed: {new_val}"
            if new_line != line:
                new_lines.append(new_line)
                changed = True
            else:
                new_lines.append(line)
        else:
            new_lines.append(line)
            
    if changed:
        new_fm = "\n".join(new_lines)
        # Ensure trailing newline in frontmatter is preserved
        if not new_fm.endswith("\n") and frontmatter.endswith("\n"):
            new_fm += "\n"
        return "---" + new_fm + content[end:], True
        
    return content, False

def fix_all_md_files(dry_run=False):
    modified_count = 0
    total_files = 0
    
    for root, dirs, files in os.walk(vault_root):
        # Exclude directories
        dirs[:] = [d for d in dirs if d not in ['.git', '.obsidian', '.aider.tags.cache.v4', '__pycache__', 'scratch']]
        for file in files:
            if not file.endswith('.md'):
                continue
                
            file_path = Path(root) / file
            total_files += 1
            
            try:
                original_content = file_path.read_text(encoding='utf-8')
            except Exception as e:
                print(f"Error reading {file_path}: {e}")
                continue
                
            cleaned_content, changed = clean_frontmatter_processed(original_content)
            if changed:
                if dry_run:
                    print(f"[DRY-RUN] Would modify: {file_path}")
                else:
                    file_path.write_text(cleaned_content, encoding='utf-8')
                    print(f"Modified: {file_path}")
                modified_count += 1
                
    print(f"\nProcessing complete!")
    print(f"Total markdown files scanned: {total_files}")
    print(f"Total files modified: {modified_count}")
    return modified_count

if __name__ == "__main__":
    import sys
    dry_run = "--write" not in sys.argv
    print(f"Starting Processed property fix (Dry Run: {dry_run})")
    
    if not dry_run:
        fix_types_json()
    else:
        print("[DRY-RUN] Would update .obsidian/types.json to set Processed to 'checkbox'.")
        
    fix_all_md_files(dry_run=dry_run)
