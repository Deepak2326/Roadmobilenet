import os
import hashlib

def get_image_hash(image_path):
    """Generate a hash for an image file."""
    with open(image_path, "rb") as f:
        return hashlib.md5(f.read()).hexdigest()

def check_duplicates(dataset_path):
    """Check and remove duplicate images in the dataset."""
    hashes = {}
    duplicates = []

    for class_folder in os.listdir(dataset_path):
        class_path = os.path.join(dataset_path, class_folder)
        if os.path.isdir(class_path):
            for img_file in os.listdir(class_path):
                img_path = os.path.join(class_path, img_file)
                img_hash = get_image_hash(img_path)

                if img_hash in hashes:
                    duplicates.append(img_path)
                else:
                    hashes[img_hash] = img_path

    # Display results
    if duplicates:
        print("🚨 Found Duplicate Images:", duplicates)
        for dup in duplicates:
            os.remove(dup)  # Uncomment this line to automatically delete duplicates
            print(f"🗑 Deleted: {dup}")
    else:
        print("✅ No duplicate images found!")

# Replace with your dataset path
dataset_path = "C:\\Users\\Lenovo\\Desktop\\DEEPU\\Project\\major"
check_duplicates(dataset_path)


