import os
from random import shuffle
from shutil import copyfile

if __name__ == '__main__':
    destination_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\ready_for_training\\yolo_v5_dataset\\'
    images_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\inputs\\images\\annotated_dataset'
    generated_labels_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\outputs\\models_format\\YOLO v5 PyTorch\\labels\\'

    train_images_dir = os.path.join(destination_dir, 'train', 'images')
    valid_images_dir = os.path.join(destination_dir, 'validate', 'images')

    train_labels_dir = os.path.join(destination_dir, 'train', 'labels')
    valid_labels_dir = os.path.join(destination_dir, 'validate', 'labels')

    images_list = os.listdir(images_dir)

    #
    # shuffle(images_list)

    for i in range(5000):
        image = images_list[i]
        label = image.replace('.jpg', '.txt')

        copyfile(
            os.path.join(images_dir, image),
            os.path.join(valid_images_dir, image)
        )
        """
        os.rename(
            os.path.join(images_dir, image),
            os.path.join(valid_images_dir, image)
        )
        """
        os.rename(
            os.path.join(generated_labels_dir, label),
            os.path.join(valid_labels_dir, label)
        )

    for i in range(5000, len(images_list)):
        image = images_list[i]
        label = image.replace('.jpg', '.txt')

        copyfile(
            os.path.join(images_dir, image),
            os.path.join(train_images_dir, image)
        )
        """
        os.rename(
            os.path.join(images_dir, image),
            os.path.join(train_images_dir, image)
        )
        """
        os.rename(
            os.path.join(generated_labels_dir, label),
            os.path.join(train_labels_dir, label)
        )
