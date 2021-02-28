from object_detection_dataset.inputs_handler import Inputs_Handler
from imageio import imread
from imageio import imwrite
from numpy import ndarray as np_ndarray
from numpy import dot as np_dot
from skimage.color import rgb2gray
from os.path import join as os_path_join


class Image_Handler(Inputs_Handler):
    width: int
    height: int
    depth: int
    image: np_ndarray

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def read_image(self, image_name: str):
        image_path = os_path_join(
            self.images_dir,
            image_name
        )
        self.image = imread(image_path)
        return self.image

    def load_image(self, image_path: str):
        self.image = imread(image_path)
        return self.image

    def save_image(self, image_path: str, image=None):
        if image is not None:
            imwrite(image_path, image)
        else:
            imwrite(image_path, self.image)

    def get_grayscale(self, image=None):
        if image is not None:
            return np_dot(image[..., :3], [0.2989, 0.5870, 0.1140])
        else:
            return np_dot(self.image[..., :3], [0.2989, 0.5870, 0.1140])

    def get_grayscale2(self, image=None):
        if image is not None:
            return rgb2gray(image)
        else:
            return rgb2gray(self.image)
