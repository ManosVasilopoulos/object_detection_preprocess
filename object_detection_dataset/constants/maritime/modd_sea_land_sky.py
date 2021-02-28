from object_detection_dataset.constants._path_creator import ConfigPaths

dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MODD-sea_land_sky_segmentation\\'


class MODDPaths:

    def __init__(self):
        self.paths = ConfigPaths(dataset_dir)
