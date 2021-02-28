from object_detection_dataset.constants._path_creator import ConfigPaths

dataset_dir = 'E:\\Data Sets\\Detection\\Maritime\\SEAGULL\\'

class SeagullPaths:

    def __init__(self):
        self.paths = ConfigPaths(dataset_dir)
