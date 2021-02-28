from pandas import DataFrame
from pandas import read_csv
from os.path import join as os_path_join
from object_detection_dataset.outputs_handler import Outputs_Handler


class CSV_Handler(Outputs_Handler):
    original_df: DataFrame
    standard_df: DataFrame

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

        self.standard_csv_path = os_path_join(self.standard_format_dir, 'all.csv')

    def read_csv(self, csv_path: str):
        self.original_df = read_csv(csv_path, delimiter=',')
        return self.original_df

    def save_to_csv(self, csv_path: str, df: DataFrame):
        df.to_csv(csv_path)

    def investigate(self):
        print('----- CSV Report -----')
        print('• Keys:', self.original_df.keys())
        print('• Columns:', self.original_df.columns)
        print('• dtypes:\n', self.original_df.dtypes)
        print('• Number of axes:', self.original_df.ndim)
        print('• Number of elements in this object:', self.original_df.size)
        print('- The first 5 rows of the DataFrame:\n', self.original_df.head(), '\n----- End of Report -----')

    """
    def create_standard_csv(self, df):
        header = ['folder', 'filename', 'object-dection', 'object-tracking', 'horizon-detection_and_tracking', 'classification',
                  'frame', 'video', 'width', 'height', 'class-name', 'xmin', 'ymin', 'xmax', 'ymax']

    def create_standard_csv2(self, df):
        header = ['folder', 'filename', 'object-dection', 'object-tracking', 'horizon-detection_and_tracking', 'classification',
                  'frame', 'video', 'width', 'height', 'class-name', 'x', 'y', 'w', 'h']

    def create_pascal_voc_csv(self, df):
        header = ['folder', 'filename', 'width', 'height', 'class-name', 'x', 'y', 'w', 'h']
    """
