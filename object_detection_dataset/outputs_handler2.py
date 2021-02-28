from os.path import join as os_path_join
from os import makedirs as os_makedirs
from object_detection_dataset.constants._path_creator import ConfigPaths

class Outputs_Handler2:

    def __init__(self, dataset_dir: str):
        self.paths = ConfigPaths(dataset_dir, make_dirs=False)
        self.standard_csv_path = os_path_join(self.paths.standard_format_dir, 'all.csv')
