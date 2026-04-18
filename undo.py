import os
import shutil

base_path = os.path.expanduser("~/Downloads")

for root, dirs, files in os.walk(base_path):
    for file in files:
        file_path = os.path.join(root, file)

        # Skip files already in root Downloads
        if root == base_path:
            continue

        new_path = os.path.join(base_path, file)

        # Handle duplicate names
        if os.path.exists(new_path):
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(new_path):
                new_path = os.path.join(base_path, f"{base}_{counter}{ext}")
                counter += 1

        shutil.move(file_path, new_path)

# Remove empty folders
for folder in os.listdir(base_path):
    folder_path = os.path.join(base_path, folder)
    if os.path.isdir(folder_path) and not os.listdir(folder_path):
        os.rmdir(folder_path)

print("All files moved back to Downloads")
