
# 📁 File Organiser

A simple, safe, and powerful **command-line tool** to automatically organise files in a folder based on their file types.


---

##  What This Project Does

**File Organiser** scans a folder and neatly arranges files into category folders such as:

- 📄 Documents  
- 🖼️ Images  
- 🎵 Music  
- 🎬 Videos  
- 💻 Code  
- 📦 Archives  
- 📁 Others (fallback)

No manual dragging. No mess. Just clean folders.

---

## How It Works (Logic)

1. Takes a **folder path** as input
2. Scans all **files** in the folder (ignores sub-folders)
3. Detects file type using the **file extension**
4. Creates category folders if they don’t exist
5. Moves files into their respective folders
6. Safely skips:
   - macOS quarantined files
   - permission-restricted files
7. Logs all actions for debugging

---

##  File Classification Logic

- File types are mapped to categories using extensions
- Rules are defined in **`config.py`**
- Unknown extensions go into the **`Others`** folder

This keeps the core logic clean and easy to extend.

---

##  Configuration

All file-type rules live in:

```text
config.py
```

## How to Run
Basic Usage
```
python3 organiser.py <target_folder>
```
Dry Run 
( Preview what would happen without moving any files) :
```
python3 organiser.py <target_folder> --dry-run
```
## macOS Quarantine Handling

Some files downloaded from the internet are quarantined by macOS.
These files are detected
They are skipped safely
A warning is printed and logged
If you trust the files, you can manually remove quarantine:

```
xattr -dr com.apple.quarantine <target_folder>
```

Then re-run the organiser.

## Logging

All actions are logged to:

```text
logs/organiser.logn
```
Logs include:
1. Files moved
2. Files skipped
3. Permission errors
4. Quarantine warnings
