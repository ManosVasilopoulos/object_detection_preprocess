from object_detection_dataset.constants._path_creator import ConfigPaths
import pandas as pd
from os.path import join
from argparse import ArgumentParser
"""
YOLO has 3 types of file:
1. image.jpg
2. image.txt --> 5 columns ==> class, xmin, ymin, w, h | normalized
3. classes.txt
"""

if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--dataset_dir', help='Root folder of dataset.')

    dataset_dir = ''
    paths = ConfigPaths(dataset_dir)
    df = pd.read_csv(join(paths.standard_format_dir, 'dataset.csv'), index_col=0)

    for index, row in df.iterrows():
        frame_name = row['frame_name']
        classes = eval(row['class'])
        xmins = eval(row['xmin'])
        ymins = eval(row['ymin'])
        xmaxs = eval(row['xmax'])
        ymaxs = eval(row['ymax'])
        width = row['width']
        height = row['height']

        with open(join(paths.yolo_v5_pytorch_labels_dir, frame_name.replace('.jpg', '.txt')), 'w+') as f:
            for i in range(len(xmins)):
                xmin = xmins[0]
                ymin = ymins[0]
                xmax = xmaxs[0]
                ymax = ymaxs[0]

                w = xmax - xmin
                h = ymax - ymin

                x_center = xmin + w / 2
                y_center = ymin + h / 2

                norm_w = w / width
                norm_h = h / height

                norm_x_center = x_center / width
                norm_y_center = y_center / height

                line = '{} {} {} {} {}\n'.format(classes[0], norm_x_center, norm_y_center, norm_w, norm_h)
                f.write(line)
