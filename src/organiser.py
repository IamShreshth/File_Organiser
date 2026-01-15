import os
import shutil 
import argparse
import subprocess
import logging
from config import FILE_CATEGORIES

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "organiser.log")

# Create logs directory if it doesn't exist
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

def is_quarantined(file_path):
    """
    Returns True if file has macOS quarantine attribute.
    """
    try:
        result = subprocess.run(
            ["xattr", file_path],
            capture_output=True,
            text=True
        )
        return "com.apple.quarantine" in result.stdout
    except Exception:
        return False

def organise_folder(folder_path,dry_run=False):
    logging.info(f"Started organizing folder: {folder_path}")
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)

        # Ignore folders
        if not os.path.isfile(item_path):
            continue
        # Skip macOS quarantined files
        if is_quarantined(item_path):
            print(f"[QUARANTINED] {item} (skipped)")
            logging.warning(f"Quarantined file skipped: {item}")
            continue



        name, extension = os.path.splitext(item)
        extension = extension.lower()

        destination_folder = "Others"

        # Decide category
        for category, extensions in FILE_CATEGORIES.items():
            if extension in extensions:
                destination_folder = category
                break

        # Create destination folder if not exists
        destination_path = os.path.join(folder_path, destination_folder)
        os.makedirs(destination_path, exist_ok=True)

        # Move file
        new_path = os.path.join(destination_path, item)
        
        # Check if file already exists and rename if needed
        if os.path.exists(new_path):
            base, ext = os.path.splitext(item)
            counter = 1
            while os.path.exists(new_path):
                new_item = f"{base}_{counter}{ext}"
                new_path = os.path.join(destination_path, new_item)
                counter += 1
            item = new_item  # Update item name for logging
        
        try:
            if dry_run:
                 print(f"[DRY RUN] {item} → {destination_folder}")
                 logging.info(f"[DRY RUN] {item} → {destination_folder}")

            else:
                shutil.move(item_path, new_path)
                print(f"Moved {item} → {destination_folder}")
                logging.info(f"Moved {item} → {destination_folder}")

        except PermissionError:
            print(f"[SKIPPED - PERMISSION] {item}")
            logging.warning(f"Permission denied for file: {item}")
            continue

        except OSError as e:
            print(f"[SKIPPED - OS ERROR] {item}: {e}")
            logging.error(f"OS error for file {item}: {e}")
            continue
    
    logging.info("Finished organizing folder")
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Automatically organise files in a folder"
    )

    parser.add_argument(
        "path",
        help="Path of the folder you want to organise"
    )

    parser.add_argument(
    "--dry-run",
    action="store_true",
    help="Show what would happen without moving files"
    )


    args = parser.parse_args()
    organise_folder(args.path, args.dry_run)


    








