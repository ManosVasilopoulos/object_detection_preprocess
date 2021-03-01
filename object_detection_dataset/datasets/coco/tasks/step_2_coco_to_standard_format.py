import pandas as pd
import os
from object_detection_dataset.datasets.coco.coco_standard_transformer import COCO_StandardTransformer

if __name__ == '__main__':
    annot_dir = "E:\\Data Sets\\Detection\\COCO\\outputs\\original_format\\"
    data_filename = 'instances_train2017.csv'

    train_data_path = os.path.join(annot_dir, data_filename)

    transformer = COCO_StandardTransformer(train_data_path)
    transformer.save_to_csv(data_filename)
