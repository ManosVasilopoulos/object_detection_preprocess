from object_detection_dataset.constants.paths.seagull import dataset_dir
from os.path import join
from os import listdir
from pathlib import Path

"""
This script creates empty txt files for objectless images (for YOLOv5)
"""


def main(images_dir: str):
    images_path = Path(images_dir)
    labels_path = join(images_path.parent, 'labels')

    images_list = listdir(images_dir)

    for image_filename in images_list:
        txt_name = image_filename[:-3] + 'txt'
        with open(join(labels_path, txt_name), 'w+') as f:
            pass


if __name__ == '__main__':
    images_dir = join(dataset_dir, 'inputs', 'images', 'no_objects', 'images')

    main(images_dir)
