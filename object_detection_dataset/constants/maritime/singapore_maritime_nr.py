from object_detection_dataset.constants._path_creator import ConfigPaths

dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Singapore Maritime - Near Infrared\\'


class SingaporePaths:

    def __init__(self):
        self.paths = ConfigPaths(dataset_dir)
