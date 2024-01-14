import os
import xml.etree.ElementTree as ET

def convert_voc_to_yolo(voc_folder, yolo_folder, class_mapping):
    if not os.path.exists(yolo_folder):
        os.makedirs(yolo_folder)

    for file in os.listdir(voc_folder):
        if file.endswith('.xml'):
            tree = ET.parse(os.path.join(voc_folder, file))
            root = tree.getroot()

            image_size = root.find('size')
            image_width = int(image_size.find('width').text)
            image_height = int(image_size.find('height').text)

            yolo_data = []

            for obj in root.iter('object'):
                class_name = obj.find('name').text
                class_id = class_mapping.get(class_name)

                if class_id is None:
                    continue

                xmlbox = obj.find('bndbox')
                b = (
                    float(xmlbox.find('xmin').text),
                    float(xmlbox.find('ymin').text),
                    float(xmlbox.find('xmax').text),
                    float(xmlbox.find('ymax').text)
                )

                yolo_box = convert_to_yolo_format(b, image_width, image_height)
                yolo_data.append(f"{class_id} {' '.join(map(str, yolo_box))}")

            # Write data to TXT file
            yolo_file_name = os.path.splitext(file)[0] + '.txt'
            with open(os.path.join(yolo_folder, yolo_file_name), 'w') as yolo_file:
                yolo_file.write('\n'.join(yolo_data))

def convert_to_yolo_format(box, width, height):
    dw = 1. / width
    dh = 1. / height
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = box[2] - box[0]
    h = box[3] - box[1]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return x, y, w, h

# Usage
voc_folder = 'human_images'
yolo_folder = 'yolo_format'
class_mapping = {'ins': 0} # Modify as per your classes

convert_voc_to_yolo(voc_folder, yolo_folder, class_mapping)
print('Finished')
