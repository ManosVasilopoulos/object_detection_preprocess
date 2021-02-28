from detection_and_tracking.handlers.txt_handler import TXT_Handler
from os import listdir as os_listdir
from os.path import join as os_path_join
from pandas import DataFrame
from pandas import concat as pd_concat
from numpy import ndarray as np_ndarray
from numpy import array as np_array


class Seagull_TXT_Handler(TXT_Handler):
    original_format_column_names = ['filename', 'frame', 'xmin', 'ymin', 'width', 'height',
                                    'object_id', '1_temp_0_final']

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def txts_to_tracking_csv(self, txt_dir='', csv_name='all-tracking.csv', dataset_info_df=None):
        # Check the directory from which the txt-files will be loaded from
        txt_dir = self._standard_check('', txt_dir)

        # List all txt-files
        txts_list = [x for x in os_listdir(txt_dir) if '.txt' in x]

        dfs_list = []
        # For every txt-file receive a DataFrame and put it in a list
        for txt_file in txts_list:
            np_data = self.read_txt(txt_file, txt_dir)

            np_data = self.__add_objectless_frames(np_data, dataset_info_df)
            df = DataFrame(np_data, columns=self.original_format_column_names)

            dfs_list.append(df)
        # Unify all DataFrames of the list
        df = pd_concat(dfs_list)

        # Prepare the CSV's path
        csv_path = os_path_join(txt_dir, csv_name)
        # Save Unified DataFrame to csv-file
        df.to_csv(csv_path)

    def txts_to_detection_csv(self, txt_dir='', csv_name='all-detection_and_tracking.csv'):
        # Check the directory from which the txt-files will be loaded from
        txt_dir = self._standard_check('', txt_dir)

        # List all txt-files
        txts_list = [x for x in os_listdir(txt_dir) if '.txt' in x]

        dfs_list = []
        # For every txt-file receive a DataFrame and put it in a list
        for txt_file in txts_list:
            np_data = self.read_txt(txt_file, txt_dir)

            df = DataFrame(np_data, columns=self.original_format_column_names)

            dfs_list.append(df)
        # Unify all DataFrames of the list
        df = pd_concat(dfs_list)

        # Prepare the CSV's path
        csv_path = os_path_join(txt_dir, csv_name)
        # Save Unified DataFrame to csv-file
        df.to_csv(csv_path)

    def __add_objectless_frames(self, np_data: np_ndarray, dataset_info_df=None) -> np_ndarray:
        filename = np_data[0, 0]
        a = []
        if dataset_info_df is None:
            first_frame = int(np_data[0, 1])

            for i in range(first_frame - 1):
                a.append(np_array([filename, i + 1, -1, -1, -1, -1, -1, 1]))
            for row in np_data:
                a.append(row)
        else:
            for index, row in dataset_info_df.iterrows():
                if row['filename'][:-4] == filename:

                    start_frame = int(row['start_frame'])
                    end_frame = int(row['end_frame'])
                    frame_count = int(row['frame_count'])

                    for i in range(start_frame - 1):
                        a.append(np_array([filename, i + 1, -1, -1, -1, -1, -1, 1]))
                    for np_row in np_data:
                        a.append(np_row)
                    for i in range(end_frame + 1, frame_count + 1):
                        a.append(np_array([filename, i + 1, -1, -1, -1, -1, -1, 1]))

        return np_array(a)
