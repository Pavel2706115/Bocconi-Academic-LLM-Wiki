import os
import re

def build_note_index(vault_path):
    note_names = []
    for root, _, files in os.walk(vault_path):
        # Avoid .smart-env and other hidden dirs if necessary
        if '.smart-env' in root:
            continue
        for file in files:
            if file.lower().endswith('.md'):
                name = os.path.splitext(file)[0]
                if len(name) > 4: # Ignore very short names to prevent false positives
                    note_names.append(name)
    # Sort by length descending so longer phrases match first
    note_names.sort(key=len, reverse=True)
    return note_names

def clean_markdown(content, note_names):
    # 1. Remove picture artifacts
    content = re.sub(r'\*\*==>\s*picture\s*\[.*?\]\s*intentionally omitted\s*<==\*\*\n*', '', content)
    
    # 2. Remove standalone page numbers
    content = re.sub(r'(?m)^\s*\d+\s*$\n', '', content)
    
    # 3. Remove Source lines
    content = re.sub(r'(?m)^\s*Source:.*$\n?', '', content)
    
    # 4. Remove excess empty lines (more than 2 consecutive newlines to double newline)
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    # 5. Semantic Linking
    links = {}
    def mask_link(match):
        placeholder = f"__LINK_{len(links)}__"
        links[placeholder] = match.group(0)
        return placeholder

    # Mask existing wikilinks
    content = re.sub(r'\[\[.*?\]\]', mask_link, content)
    # Mask standard markdown links
    content = re.sub(r'\[.*?\]\(.*?\)', mask_link, content)
    # Mask markdown headers to avoid linking inside headers
    content = re.sub(r'(?m)^#+\s+.*$', mask_link, content)
    
    for name in note_names:
        # Avoid extremely broad or short names
        if len(name) <= 4: continue
        
        escaped_name = re.escape(name)
        # Match whole word, case-insensitive
        pattern = r'(?<![a-zA-Z0-9])(' + escaped_name + r')(?![a-zA-Z0-9])'
        
        # Link up to 3 occurrences per note
        content, _ = re.subn(pattern, r'[[\1]]', content, count=3, flags=re.IGNORECASE)

    # Unmask
    for placeholder, original in reversed(list(links.items())):
        content = content.replace(placeholder, original)
        
    return content

def process_vault(vault_path):
    print("Building note index...", flush=True)
    note_names = build_note_index(vault_path)
    print(f"Found {len(note_names)} valid note names for linking.", flush=True)
    
    processed = 0
    for root, _, files in os.walk(vault_path):
        if '.smart-env' in root:
            continue
        for file in files:
            if file.lower().endswith('.md'):
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                try:
                    print(f"Processing {file_path} (Size: {file_size} bytes)...", flush=True)
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        
                    # 1. Remove picture artifacts
                    new_content = re.sub(r'\*\*==>\s*picture\s*\[.*?\]\s*intentionally omitted\s*<==\*\*\n*', '', content)
                    
                    # 2. Remove standalone page numbers
                    new_content = re.sub(r'(?m)^\s*\d+\s*$\n', '', new_content)
                    
                    # 3. Remove Source lines
                    new_content = re.sub(r'(?m)^\s*Source:.*$\n?', '', new_content)
                    
                    # 4. Remove excess empty lines
                    new_content = re.sub(r'\n{3,}', '\n\n', new_content)
                    
                    # 5. Semantic Linking (Skip if file is too large, e.g., > 1MB)
                    if file_size < 1000000:
                        links = {}
                        def mask_link(match):
                            placeholder = f"__LINK_{len(links)}__"
                            links[placeholder] = match.group(0)
                            return placeholder

                        new_content = re.sub(r'\[\[.*?\]\]', mask_link, new_content)
                        new_content = re.sub(r'\[.*?\]\(.*?\)', mask_link, new_content)
                        new_content = re.sub(r'(?m)^#+\s+.*$', mask_link, new_content)
                        
                        for name in note_names:
                            if len(name) <= 4: continue
                            escaped_name = re.escape(name)
                            pattern = r'(?<![a-zA-Z0-9])(' + escaped_name + r')(?![a-zA-Z0-9])'
                            new_content, _ = re.subn(pattern, r'[[\1]]', new_content, count=3, flags=re.IGNORECASE)

                        for placeholder, original in reversed(list(links.items())):
                            new_content = new_content.replace(placeholder, original)
                    else:
                        print(f"  Skipping semantic linking for {file_path} due to large size.", flush=True)
                    
                    if content != new_content:
                        with open(file_path, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                    processed += 1
                except Exception as e:
                    print(f"Error processing {file_path}: {e}", flush=True)
                    
    print(f"Processed {processed} files.", flush=True)

if __name__ == "__main__":
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    process_vault(script_dir)
