import os
from lxml import etree

def remove_non_human_objects(folder, class_name="ins"):
    for file in os.listdir(folder):
        if file.endswith('.xml'):
            xml_path = os.path.join(folder, file)
            tree = etree.parse(xml_path)
            root = tree.getroot()

            objects_to_remove = []

            # Collect all non-'ins' objects
            for obj in root.findall('object'):
                label = obj.find('name').text
                if label != class_name:
                    objects_to_remove.append(obj)

            # Remove collected objects
            for obj in objects_to_remove:
                root.remove(obj)

            # Save the modified XML
            tree.write(xml_path, pretty_print=True, xml_declaration=True)

# Usage
folder = 'human_images'
remove_non_human_objects(folder)
print('Finished')