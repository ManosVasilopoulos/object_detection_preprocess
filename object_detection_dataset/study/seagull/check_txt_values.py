from os.path import join
from os import listdir
from object_detection_dataset.datasets.seagull.seagull_txt_handler import Seagull_TXT_Handler

dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\ready_for_training\\seagull_for_yolov5'

if __name__ == '__main__':
    train_labels_dir = join(dataset_dir, 'train', 'labels')
    test_labels_dir = join(dataset_dir, 'validate', 'labels')

    dirs = [train_labels_dir, test_labels_dir]

    txt_handler = Seagull_TXT_Handler(dataset_dir)

    type_ = ['train', 'test']
    for i, labels_dir in enumerate(dirs):

        corrupted_list = []

        labels_list = listdir(labels_dir)

        for txt_name in labels_list:
            values = txt_handler.read_txt(txt_name, labels_dir)
            for object in values:
                for value in object[1:]:
                    if float(value) > 1:
                        print(float(value))
                        corrupted_list.append(txt_name)
                        break

        with open(join(dataset_dir, 'corrupted-' + type_[i] + '.txt'), 'w') as f:
            f.writelines(corrupted_list)