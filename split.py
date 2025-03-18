import os
import shutil
import random

def split_data(source_dir, train_dir, test_dir, split_ratio=0.8):
    for category in os.listdir(source_dir):
        category_path = os.path.join(source_dir, category)
        if os.path.isdir(category_path):
            images = os.listdir(category_path)
            random.shuffle(images)
            
            split_point = int(len(images) * split_ratio)
            train_images = images[:split_point]
            test_images = images[split_point:]

            os.makedirs(os.path.join(train_dir, category), exist_ok=True)
            os.makedirs(os.path.join(test_dir, category), exist_ok=True)

            for img in train_images:
                shutil.move(os.path.join(category_path, img), os.path.join(train_dir, category, img))
            
            for img in test_images:
                shutil.move(os.path.join(category_path, img), os.path.join(test_dir, category, img))

source = "C:/Users/Lenovo/Desktop/DEEPU/Dataset/classified into 3"
train = "C:/Users/Lenovo/Desktop/DEEPU/Project/vs code/path_to_train_data/train"
test = "C:/Users/Lenovo/Desktop/DEEPU/Project/vs code/path_to_train_data/test"

split_data(source, train, test, split_ratio=0.8)
