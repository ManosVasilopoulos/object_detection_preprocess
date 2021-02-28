from detection_and_tracking.configuration.seagull import standard_format_dir, yolo_v4_pytorch_dir, dataset_dir
from detection_and_tracking.outputs_handler import Outputs_Handler
import pandas as pd
from os.path import join
from random import shuffle

"""
YOLO has 3 types of file:
1. image.jpg
2. image.txt --> 5 columns ==> class, xmin, ymin, w, h | normalized
3. classes.txt

YOLO v4 has in one folder:
1) all images
2) _annotations.txt ---> imagename object_1 object_2 ...
3) _classes.txt --> class0\nclass1\nclass2...

object_i --> xmin,ymin,xmax,ymax,class_number
"""


def yolo_v4_annotations(image_name, xmin_arr, ymin_arr, xmax_arr, ymax_arr, classes_arr, txt_name='_annotations.txt'):
    with open(join(yolo_v4_pytorch_dir, txt_name), 'a+') as f:
        line = image_name
        for i in range(len(xmin_arr)):
            line += ' {},{},{},{},{}'.format(xmin_arr[i], ymin_arr[i], xmax_arr[i], ymax_arr[i], classes_arr[i])
        line += '\n'
        f.write(line)


def yolo_v4_classes():
    with open(join(yolo_v4_pytorch_dir, '_classes.txt'), 'w+') as f:
        f.write('object')


def train_test_split(df, index_list):
    for i in range(len(df) - 9358):
        index = index_list[i]
        row = df.iloc[index]
        frame_name = row['frame_name']
        classes = eval(row['class'])
        xmins = eval(row['xmin'])
        ymins = eval(row['ymin'])
        xmaxs = eval(row['xmax'])
        ymaxs = eval(row['ymax'])
        width = row['width']
        height = row['height']
        yolo_v4_annotations(frame_name, xmins, ymins, xmaxs, ymaxs, classes, 'train_annotations.txt')

    for i in range(len(df) - 9358, len(df)):
        index = index_list[i]
        row = df.iloc[index]
        frame_name = row['frame_name']
        classes = eval(row['class'])
        xmins = eval(row['xmin'])
        ymins = eval(row['ymin'])
        xmaxs = eval(row['xmax'])
        ymaxs = eval(row['ymax'])
        width = row['width']
        height = row['height']
        yolo_v4_annotations(frame_name, xmins, ymins, xmaxs, ymaxs, classes, 'test_annotations.txt')

    yolo_v4_classes()


def main(should_I_shuffle: bool):
    oh = Outputs_Handler(dataset_dir)
    oh.create_base_dirs()
    df = pd.read_csv(join(standard_format_dir, 'dataset.csv'))

    index_list = [x for x in range(len(df))]
    if should_I_shuffle:
        shuffle(index_list)
        train_test_split(df, index_list)
    else:
        for index, row in df.iterrows():
            frame_name = row['frame_name']
            classes = eval(row['class'])
            xmins = eval(row['xmin'])
            ymins = eval(row['ymin'])
            xmaxs = eval(row['xmax'])
            ymaxs = eval(row['ymax'])
            width = row['width']
            height = row['height']

            yolo_v4_annotations(frame_name, xmins, ymins, xmaxs, ymaxs, classes)

        yolo_v4_classes()


if __name__ == '__main__':
    main(should_I_shuffle=True)
