import os
import pandas as pd
from object_detection_dataset.constants._path_creator import ConfigPaths
import shutil

if __name__ == '__main__':
    coco__folder = 'E:\\Data Sets\\Detection\\COCO\\'
    coco_paths = ConfigPaths(coco__folder, make_dirs=True)

    coco_x_seagull_folder = 'E:\\Data Sets\\Detection\\Maritime\\COCO x SEAGULL\\'
    coco_x_seagull_paths = ConfigPaths(coco_x_seagull_folder, make_dirs=True)

    coco_x_seagull_df = pd.read_csv(os.path.join(coco_x_seagull_paths.standard_format_dir, 'coco_x_seagull.csv'))

    for index, row in coco_x_seagull_df.iterrows():

        image_name = row['filename']
        src = os.path.join(coco_paths.images_dir, 'train2017', image_name)
        dst = os.path.join(coco_x_seagull_paths.images_dir, image_name)
        print('copying', image_name)
        print('From:', src)
        print('To:', dst)

        shutil.copy(src, dst)
