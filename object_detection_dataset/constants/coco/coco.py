from object_detection_dataset.constants._path_creator import ConfigPaths

dtst_dir = 'E:\\Data Sets\\Detection\\COCO'


class COCOPaths:

    def __init__(self, dataset_dir=None):
        if dataset_dir:

            self.paths = ConfigPaths(dataset_dir)
        else:
            self.paths = ConfigPaths(dtst_dir)
