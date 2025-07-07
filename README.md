# PyHarvest

A lightweight Python utility for collecting and consolidating Python source files from a directory into a single text file. PyHarvest simplifies code review, documentation, and archival processes by gathering all `.py` files and their contents into one organized output file.

## Features

- **Flexible Directory Scanning**: Scan any specified directory for Python files
- **Recursive or Shallow Search**: Choose whether to include subdirectories
- **Consolidated Output**: All Python files are combined into a single, well-formatted text file
- **Encoding Support**: Handles both UTF-8 and Latin-1 encoded files
- **User-Friendly Interface**: Interactive prompts guide you through the process
- **Error Handling**: Graceful handling of missing directories and encoding issues

## Requirements

- Python 3.6 or higher
- No external dependencies required

## Installation

1. Download the `PyHarvest.py` script
2. Make it executable (Unix/Linux/macOS):
   ```bash
   chmod +x PyHarvest.py
   ```

## Usage

Run the script from your terminal or command prompt:

```bash
python3 PyHarvest.py
```

The script will prompt you for:

1. **Folder Path**: The directory containing Python files to collect
2. **Output Filename**: Name for the consolidated text file (defaults to `collected_code.txt`)
3. **Recursion Option**: Whether to include subdirectories (`y` for yes, `n` for no)

### Example Session

```
Enter the full path of the folder to scan: /home/user/my_project
Enter the desired output TXT filename (e.g., all_code.txt)
(press Enter to use 'collected_code.txt'): project_code.txt
Recurse into subfolders? (y/n): y
✅ Pulled in 15 file(s) and wrote them to project_code.txt
```

## Output Format

The generated text file contains each Python file in the following format:

```
file name : example.py
code:
[Python code content here]
------

file name : another_file.py
code:
[Python code content here]
------
```

## Use Cases

- **Code Review**: Consolidate project files for easier review
- **Documentation**: Create comprehensive code snapshots for documentation
- **Backup**: Generate text-based backups of Python projects
- **Analysis**: Prepare code for analysis tools or AI assistants
- **Sharing**: Create single-file representations of multi-file projects

## Error Handling

- Validates directory existence before processing
- Handles encoding issues by attempting UTF-8 first, then falling back to Latin-1
- Provides clear feedback when no Python files are found
- Displays helpful error messages for common issues

## License

This project is released under the MIT License.
