import os
from tqdm import tqdm
from utils import get_code_paths

def cleanup_trailing_newlines(file_path: str) -> bool:
    """
    Cleans up trailing newlines from a file.

    Reads a file, strips all trailing whitespace, ensures it ends with exactly
    one newline, and writes it back if changes were made.

    Args:
        file_path: The path to the file to clean up.

    Returns:
        True if the file was updated, False otherwise.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            original_content = f.read()

        # Strip all trailing whitespace (including newlines, spaces, etc.)
        stripped_content = original_content.rstrip()

        # Ensure the file ends with a single newline (a common convention)
        # Handle the edge case of an empty file
        if not stripped_content:
            cleaned_content = ""
        else:
            cleaned_content = stripped_content + '\n'

        # Only write back to the file if the content has actually changed
        if original_content != cleaned_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(cleaned_content)
            return True
            
    except Exception as e:
        print(f"Error processing file {file_path}: {e}")

    return False

def main():
    """
    Main function to iterate through code files and clean them up.
    """
    base_dir = os.path.join(os.path.dirname(__file__), '..', 'base')
    updated_files_count = 0
    
    print("Scanning files to remove trailing newlines...")

    for task_id in tqdm(range(1, 401), desc="Processing Tasks"):
        for base_path in get_code_paths("base_*", task_id, skip_generated=True):
            if cleanup_trailing_newlines(base_path):
                updated_files_count += 1
    
    print(f"\nCleanup complete. {updated_files_count} file(s) were updated.")

if __name__ == '__main__':
    main()