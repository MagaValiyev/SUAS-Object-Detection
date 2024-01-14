import os
import shutil
import random

def setup_directories(base_path, subfolders):
    for subfolder in subfolders:
        path = os.path.join(base_path, subfolder)
        if not os.path.exists(path):
            os.makedirs(path)

def copy_files(files, source_folder, destination_folder):
    for file in files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(destination_folder, file)
        shutil.copy2(source_path, destination_path)

def select_and_copy_files(source_folder, base_destination_folder, num_val=1000):
    # Setup necessary directories
    setup_directories(base_destination_folder, ['images/val', 'images/train', 'labels/val', 'labels/train'])

    jpg_files = [file for file in os.listdir(source_folder) if file.endswith('.jpg')]
    random.shuffle(jpg_files)

    val_files = jpg_files[:num_val]
    train_files = jpg_files[num_val:]

    # Copy image files
    copy_files(val_files, source_folder, os.path.join(base_destination_folder, 'images/val'))
    copy_files(train_files, source_folder, os.path.join(base_destination_folder, 'images/train'))

    # Copy label files
    val_labels = [file.replace('.jpg', '.txt') for file in val_files]
    train_labels = [file.replace('.jpg', '.txt') for file in train_files]

    copy_files(val_labels, source_folder, os.path.join(base_destination_folder, 'labels/val'))
    copy_files(train_labels, source_folder, os.path.join(base_destination_folder, 'labels/train'))

# Usage
source_folder = 'yolo_format'
base_destination_folder = 'model'
select_and_copy_files(source_folder, base_destination_folder)
