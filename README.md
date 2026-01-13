# File organiser

## What this project does
Automatically organises files in a given folder based on file type.

## How it works (logic)
1. Takes a folder path as input from the user
2. Scans all files in the folder
3. Identifies file type using file extension
4. Creates category folders if they do not exist
5. Moves files into their folders

## File classification logic
Files are categorized based on their extensions.
Each extension is mapped to a folder name in `config.py`.  
If a file extension does not match any category, it is moved to the **Others** folder.

## Configuration
File type rules are stored separately in `config.py`to keep the logic modular and easy to extend.

## How to Run
## Basic usage

```bash
python3 organiser.py <target_folder>

python3 organiser.py <target_folder> --dry-run



