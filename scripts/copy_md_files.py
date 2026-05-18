import os
import shutil

def copy_markdown_files():
    # The folder you are currently in (Bocconi)
    source_dir = os.getcwd()
    
    # The new master folder where all the copies will go
    dest_dir = os.path.join(source_dir, "Markdown_Export")

    # Create the export folder if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    copied_count = 0
    print("Starting to copy Markdown files...\n")

    # Walk through all folders
    for root, dirs, files in os.walk(source_dir):
        # Stop the script from accidentally scanning its own export folder
        if "Markdown_Export" in dirs:
            dirs.remove("Markdown_Export")
            
        for file in files:
            # Look ONLY for markdown files
            if file.lower().endswith('.md'):
                source_file = os.path.join(root, file)
                
                # Figure out the relative path to keep your folders organized exactly the same
                relative_path = os.path.relpath(root, source_dir)
                target_folder = os.path.join(dest_dir, relative_path)
                
                # Create the corresponding sub-folder in the export directory
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)
                    
                # Copy the file over
                target_file = os.path.join(target_folder, file)
                shutil.copy2(source_file, target_file)
                
                print(f"Copied: {file}")
                copied_count += 1

    print(f"\nDone! Successfully copied {copied_count} markdown files to the 'Markdown_Export' folder.")

if __name__ == "__main__":
    copy_markdown_files()