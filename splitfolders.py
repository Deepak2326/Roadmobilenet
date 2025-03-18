

import os
import pandas as pd
import shutil

# Paths (Update these!)
csv_file = "C:\\Users\\Lenovo\\Desktop\\DEEPU\\Dataset\\puthiyath\\Csv file\\Dataset_Info.csv" # CSV file path
images_folder = "C:\\Users\\Lenovo\\Desktop\\DEEPU\\Dataset\\puthiyath\\Unified Dataset\\Unified Dataset" # Folder where images are stored
output_folder = "C:\\Users\\Lenovo\\Desktop\\DEEPU\\Dataset\\puthiyath\\Unified Dataset\\splitted" # Folder where organized images will be saved


# Create category folders (A, B, C, S)
categories = ["A", "B", "C", "S"]
for category in categories:
    os.makedirs(os.path.join(output_folder, category), exist_ok=True)

# Load CSV
df = pd.read_csv(csv_file)

# CSV column names (Update if different)
image_column = "Image ID"
label_column = "Level"

# Function to find correct file extension
def find_image_file(image_name):
    for ext in [".jpg", ".png", ".jpeg"]:
        file_path = os.path.join(images_folder, image_name + ext)
        if os.path.exists(file_path):
            return file_path
    return None  # Return None if no match found

# Move images
for index, row in df.iterrows():
    image_name = row[image_column]  # Get filename from CSV
    label = row[label_column]  # Get category (A, B, C, S)

    source_path = find_image_file(image_name)  # Find the correct image file
    if source_path:
        dest_path = os.path.join(output_folder, label, os.path.basename(source_path))
        shutil.move(source_path, dest_path)
        print(f"✅ Moved: {image_name} → {label}/")
    else:
        print(f"⚠️ File not found: {image_name}")

print("✅ Image sorting complete!")

