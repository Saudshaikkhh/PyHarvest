#!/usr/bin/env python3
import os
from pathlib import Path

def get_user_inputs():
    """
    Prompt the user for:
      1. folder path to scan
      2. output TXT filename
      3. whether to recurse into subfolders
    Returns a tuple: (folder: Path, output_file: Path, recurse: bool)
    """
    folder_input = input("Enter the full path of the folder to scan: ").strip()
    output_input = input(
        "Enter the desired output TXT filename (e.g., all_code.txt)\n"
        "(press Enter to use 'collected_code.txt'): "
    ).strip() or "collected_code.txt"
    recurse_flag = input("Recurse into subfolders? (y/n): ").strip().lower().startswith('y')

    folder = Path(folder_input).expanduser().resolve()
    output_file = Path(output_input).expanduser().resolve()
    return folder, output_file, recurse_flag

def collect_py_files(folder: Path, recurse: bool = True):
    """Yield all .py files in `folder` (recursively if recurse=True)."""
    for root, _, files in os.walk(folder) if recurse else [(str(folder), [], os.listdir(folder))]:
        for f in files:
            if f.endswith('.py'):
                yield Path(root) / f

def write_collection(py_files, output_file: Path):
    """Write each .py file’s name and content into the single TXT."""
    with output_file.open('w', encoding='utf-8') as out:
        for path in py_files:
            out.write(f"file name : {path.name}\n")
            out.write("code:\n")
            try:
                code = path.read_text(encoding='utf-8')
            except UnicodeDecodeError:
                code = path.read_text(encoding='latin-1')
            out.write(code.rstrip() + "\n")
            out.write("------\n\n")

def main():
    folder, output_file, recurse_flag = get_user_inputs()

    if not folder.is_dir():
        print(f"✖️  No folder found at {folder}. Double-check your path and try again.")
        return

    py_files = list(collect_py_files(folder, recurse=recurse_flag))
    if not py_files:
        print("🤷  Huh, couldn’t find any .py files. Are you in the right directory?")
        return

    write_collection(py_files, output_file)
    print(f"✅  Pulled in {len(py_files)} file(s) and wrote them to {output_file}")

if __name__ == "__main__":
    main()
