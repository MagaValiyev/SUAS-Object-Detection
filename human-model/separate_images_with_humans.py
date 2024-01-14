import os
import shutil
from lxml import etree

def find_and_copy_files(source_folder, destination_folder, class_name="ins"):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    for file in os.listdir(source_folder):
        if file.endswith('.xml'):
            xml_path = os.path.join(source_folder, file)
            tree = etree.parse(xml_path)

            # Check if 'ins' class is present in the XML
            if tree.xpath(f"//name[text()='{class_name}']"):
                # Copy XML file
                shutil.copy2(xml_path, destination_folder)

                # Copy corresponding image file
                jpg_file = file.replace('.xml', '.jpg')
                jpg_path = os.path.join(source_folder, jpg_file)
                if os.path.exists(jpg_path):
                    shutil.copy2(jpg_path, destination_folder)

# Usage
source_folder = 'traffic_birdseye'
destination_folder = 'human_images'
find_and_copy_files(source_folder, destination_folder)
