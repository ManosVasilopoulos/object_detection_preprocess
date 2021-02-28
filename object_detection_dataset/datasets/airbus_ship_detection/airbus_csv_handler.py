from object_detection_dataset.datasets.airbus_ship_detection.airbus_mask_handler import AirBus_Mask_Handler
from object_detection_dataset.handlers.csv_handler import CSV_Handler
from os.path import join as os_path_join
from os import makedirs as os_makedirs
from pandas import DataFrame


class AirBus_CSV_Handler(CSV_Handler):
    """
    The main use of this class will be to create a csv file with 5 columns
    1) Filename
    2) xmin
    3) xmax
    4) ymin
    5) ymax
    Each row will describe one bounding box => more than 1 rows
    """
    decoded_df: DataFrame
    decoded_data_dict = {
        'filename': [],
        'xmin': [],
        'xmax': [],
        'ymin': [],
        'ymax': []
    }

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

        decoded_csv_dir = os_path_join(self.original_format_dir, 'decoded')
        os_makedirs(decoded_csv_dir, exist_ok=True)

        self.mask_handler = AirBus_Mask_Handler()

    def decode_data(self, original_df: DataFrame):
        for index, row in original_df.iterrows():
            filename = row['ImageId']
            print('- Handling:', filename)
            encoded_pixels = row['EncodedPixels']

            # If there are no objects in the image
            # encoded_pixels = nan
            # type(nan) = float
            if type(encoded_pixels) == float:
                y_min, y_max, x_min, x_max = '', '', '', ''
            else:
                decoded_data = self.mask_handler.rle_decode(encoded_pixels)
                y_min, y_max, x_min, x_max = self.mask_handler.mask_to_bbox(decoded_data)

            self.decoded_data_dict['filename'].append(filename)
            self.decoded_data_dict['xmin'].append(x_min)
            self.decoded_data_dict['xmax'].append(x_max)
            self.decoded_data_dict['ymin'].append(y_min)
            self.decoded_data_dict['ymax'].append(y_max)

        df = DataFrame(self.decoded_data_dict)
        return df
