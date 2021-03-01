from object_detection_dataset.format_transformer.dataset_to_standard_format.standard_transformer import \
    StandardTransformer
from pandas import DataFrame
import pandas as pd
import numpy as np
import os


class COCO_StandardTransformer(StandardTransformer):
    pre_standard_df: DataFrame

    def __init__(self, data_path: str) -> None:
        super().__init__()
        self.pre_standard_path = data_path
        self.data_dir, self.pre_standard_filename = os.path.split(data_path)

        # Read data from CSV file
        df = pd.read_csv(data_path)

        # Each value is a string, if left as it is. We need to use 'eval' to convert them to Python Lists
        df['annotation_ids'] = df['annotation_ids'].apply(eval)
        df['bboxes'] = df['bboxes'].apply(eval)
        df['category_ids'] = df['category_ids'].apply(eval)
        df['categories'] = df['categories'].apply(eval)
        df['supercategories'] = df['supercategories'].apply(eval)

        # Store as object variable
        self.pre_standard_df = df

        # Get all data in the proper way, to create standard structure
        c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11 = self.get_all_columns()
        self.standard_df = DataFrame(
            data=np.column_stack([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11]),
            columns=self.get_all_column_names()
        )
        self.save_to_csv(filename=self.pre_standard_filename.replace('.csv', ''))

    def save_to_csv(self, filename: str):
        if filename[-4:] != '.csv':
            filename += '.csv'
        self.standard_df.to_csv(os.path.join(self.data_dir, 'standard_' + filename), index=False)

    def create_filename_column(self):
        return self.pre_standard_df['image_names'].tolist()

    def create_frame_column(self):
        return len(self.pre_standard_df.index) * ['']

    def create_frame_name_column(self):
        return self.pre_standard_df['image_names'].tolist()

    def create_class_column(self):
        return self.pre_standard_df['category_ids'].tolist()

    def create_xy_columns(self):
        xmins = []
        ymins = []
        xmaxs = []
        ymaxs = []

        for img_bboxes in self.pre_standard_df['bboxes']:
            xmin_s = []
            ymin_s = []
            xmax_s = []
            ymax_s = []
            for bbox in img_bboxes:
                xmin_s.append(bbox[0])
                ymin_s.append(bbox[1])
                xmax_s.append(bbox[0] + bbox[2])
                ymax_s.append(bbox[1] + bbox[3])

            xmins.append(xmin_s)
            ymins.append(ymin_s)
            xmaxs.append(xmax_s)
            ymaxs.append(ymax_s)

        return xmins, ymins, xmaxs, ymaxs

    # TODO: replace -1
    def create_width_column(self):
        return len(self.pre_standard_df.index) * [-1]

    # TODO: replace -1
    def create_height_column(self):
        return len(self.pre_standard_df.index) * [-1]

    def create_depth_column(self):
        return len(self.pre_standard_df.index) * [3]
