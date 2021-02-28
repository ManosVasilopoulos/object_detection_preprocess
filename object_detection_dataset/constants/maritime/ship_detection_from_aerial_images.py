from object_detection_dataset.constants._path_creator import ConfigPaths

dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\z Ship Detection from Aerial Images\\'


class ShipDetectionPaths:

    def __init__(self):
        self.paths = ConfigPaths(dataset_dir)
