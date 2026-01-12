import os
import shutil 
from config import FILE_CATEGORIES

def organize_folder(folder_path):
    items = os.listdir(folder_path)

    for item in items:
        item_path = os.path.join(folder_path, item)

        # Ignore folders
        if not os.path.isfile(item_path):
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
        shutil.move(item_path, new_path)

        print(f"Moved {item} → {destination_folder}")

if __name__ == "__main__":
    target_folder = "../test_folder"
    organize_folder(target_folder)

