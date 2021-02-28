from object_detection_dataset.handlers.image_sequence_handler import Image_Sequence_Handler
from numpy import array as np_array
from os.path import join as os_path_join
from os import listdir as os_listdir
from numpy import ndarray as np_ndarray
from cv2 import waitKey as cv2_waitKey
from cv2 import imshow as cv2_imshow
from cv2 import imread as cv2_imread


class MODD2_Image_Sequence_Handler(Image_Sequence_Handler):
    left_sequence: np_ndarray
    right_sequence: np_ndarray

    def read_image_sequence(self, video_name: str):
        self.set_image_sequence_name(video_name)

        # Set video directory
        video_dir = os_path_join(
            self.im_seqs_dir,
            video_name
        )
        # List all the images included inside the video directory
        images_names = os_listdir(video_dir)

        # Sort the images with respect to their name
        sorted_images_names = sorted(images_names)

        # Read every image and store it in a list.
        # Turn this list to a numpy array.
        self.left_sequence = np_array(
            [cv2_imread(os_path_join(video_dir, img_name)) for img_name in sorted_images_names if
             img_name.endswith('L.jpg')]
        )
        self.right_sequence = np_array(
            [cv2_imread(os_path_join(video_dir, img_name)) for img_name in sorted_images_names if
             img_name.endswith('R.jpg')]
        )
        return self.left_sequence, self.right_sequence

    def play_image_sequence(self, frame_rate=25):
        """
        plot the images just like a video
        :return:
        """
        frame_duration = 1000 // frame_rate
        for i, img in enumerate(self.left_sequence):
            cv2_imshow('', img)
            cv2_waitKey(frame_duration)
            print('Frame-' + str(i + 1))
