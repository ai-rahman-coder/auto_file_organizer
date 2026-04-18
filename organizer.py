import os
import json
import shutil

# Get your home directory (works on any system)
HOME = os.path.expanduser("~")

# Load config
with open("config.json") as f:
    config = json.load(f)

folder_path = os.path.join(HOME, config["base_path"])
file_types = config["categories"]

def get_unique_filename(dest_folder, filename):
    base, ext = os.path.splitext(filename)
    counter = 1

    new_filename = filename
    while os.path.exists(os.path.join(dest_folder, new_filename)):
        new_filename = f"{base}_{counter}{ext}"
        counter += 1

    return new_filename


for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        file_lower = file.lower()
        moved = False

        for folder, extensions in file_types.items():
            if file_lower.endswith(tuple(extensions)):
                new_folder = os.path.join(folder_path, folder)
                os.makedirs(new_folder, exist_ok=True)

                unique_name = get_unique_filename(new_folder, file)
                shutil.move(file_path, os.path.join(new_folder, unique_name))

                print(f"Moved: {file} → {folder}/{unique_name}")
                moved = True
                break

        if not moved:
            others_folder = os.path.join(folder_path, "Others")
            os.makedirs(others_folder, exist_ok=True)

            unique_name = get_unique_filename(others_folder, file)
            shutil.move(file_path, os.path.join(others_folder, unique_name))

            print(f"Moved: {file} → Others/{unique_name}")