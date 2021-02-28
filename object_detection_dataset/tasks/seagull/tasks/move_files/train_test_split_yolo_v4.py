import os
from random import shuffle

if __name__ == '__main__':
    folder_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\ready_for_training\\yolo_v4_dataset'

    images_dir = os.path.join(folder_dir, 'all')

    train_images_dir = os.path.join(folder_dir, 'train')
    train_annotaions_path = os.path.join(train_images_dir, 'train_annotations.txt')

    test_images_dir = os.path.join(folder_dir, 'test')
    test_annotaions_path = os.path.join(test_images_dir, 'test_annotations.txt')

    with open(train_annotaions_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            image_name = line.split(' ')[0]
            os.rename(
                os.path.join(images_dir, image_name),
                os.path.join(train_images_dir, image_name)
            )

    with open(test_annotaions_path, 'r') as f:
        lines = f.readlines()

        for line in lines:
            image_name = line.split(' ')[0]
            os.rename(
                os.path.join(images_dir, image_name),
                os.path.join(test_images_dir, image_name)
            )


