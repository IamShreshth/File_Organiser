# File organiser

## What this project does
Automatically organises files in a given folder based on file type.

## How it works (logic)
1. Takes a folder path as input
2. Scans all files in the folder
3. Identifies file type using file extension
4. Moves files into categorized folders

## File classification logic
Files are categorized based on their extensions.
Each extension is mapped to a folder name.
If a file extension does not match any category,
it is moved to the Others folder.

## Configuration
File type rules are stored separately in `config.py`
to keep the logic modular and easy to extend.
