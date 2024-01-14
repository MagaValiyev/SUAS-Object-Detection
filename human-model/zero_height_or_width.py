import os
import xml.etree.ElementTree as ET

def check_zero_dimensions(voc_folder):
    zero_dimension_files = []

    for file in os.listdir(voc_folder):
        if file.endswith('.xml'):
            tree = ET.parse(os.path.join(voc_folder, file))
            root = tree.getroot()

            image_size = root.find('size')
            image_width = int(image_size.find('width').text)
            image_height = int(image_size.find('height').text)

            # Check if width or height is zero
            if image_width == 0 or image_height == 0:
                zero_dimension_files.append(file)

    return zero_dimension_files

# Usage
voc_folder = 'human_images'
zero_dim_files = check_zero_dimensions(voc_folder)

# Output the list of files with zero dimensions
print("Files with zero width or height:")
for file in zero_dim_files:
    print(file)

print(len(zero_dim_files))