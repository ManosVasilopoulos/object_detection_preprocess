from object_detection_dataset.inputs_handler import Inputs_Handler
from numpy import array as np_array
from os.path import join as os_path_join
from os import listdir as os_listdir
from os import makedirs as os_makedirs
from numpy import ndarray as np_ndarray
from object_detection_dataset.handlers.image_handler import Image_Handler
from cv2 import waitKey as cv2_waitKey
from cv2 import imshow as cv2_imshow
from cv2 import imwrite as cv2_imwrite
from cv2 import imread as cv2_imread


class Image_Sequence_Handler(Inputs_Handler):
    image_sequence: np_ndarray
    image_sequence_name: str
    video_name: str

    def __init__(self, dataset_dir: str, exist: bool, image_sequence_folder=None):
        """
        :param dataset_dir: directory of the dataset
        :param exist: boolean variable. Denotes if the Images Sequence
        :param image_sequences_folder: name of the folder. Default value 'image_sequences'
        """
        super().__init__(dataset_dir)

        # TODO --> overwrite the video and image sequences subdirectory
        if image_sequence_folder is not None:
            pass

        if exist:
            self.sequences_names = os_listdir(self.im_seqs_dir)
            self.sequences_paths = [os_path_join(self.im_seqs_dir, x) for x in self.sequences_names]

        self.image_handler = Image_Handler(dataset_dir)

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
        """ In an example the colors where not right
        self.image_sequence = np_array(
            [self.image_handler.load_image(os_path_join(video_dir, img_name)) for img_name in sorted_images_names]
        )
        """
        self.image_sequence = np_array(
            [cv2_imread(os_path_join(video_dir, img_name)) for img_name in sorted_images_names]
        )

        return self.image_sequence

    def save_image_sequence(self, img_seq=None, video_name=None):
        if img_seq is not None:
            if video_name is None:
                raise Exception('Images_Sequence_Handler_Error: "video_name" must have a value. Now "video_name=None".')
            video_name = self.__get_fixed_video_name(video_name)
            self.__save_image_sequence(img_seq, video_name)
        else:
            self.__save_image_sequence(self.image_sequence, self.video_name)

    def set_image_sequence(self, image_sequence: np_ndarray):
        self.image_sequence = image_sequence

    # TODO --> include more video formats
    def set_image_sequence_name(self, video_name: str):
        self.video_name = self.__get_fixed_video_name(video_name)
        self.image_sequence_name = self.video_name

    # TODO --> implement 'play_image_sequence' method
    def play_image_sequence(self, frame_rate=25):
        """
        plot the images just like a video
        :return:
        """
        frame_duration = 1000 // frame_rate
        for i, img in enumerate(self.image_sequence):
            cv2_imshow('', img)
            cv2_waitKey(frame_duration)
            print('Frame-' + str(i + 1))

    # TODO --> implement 'image_sequence_to_video' method
    def image_sequence_to_video(self):
        """
        create a video capture (CV2) and save it as 'AVI'
        :return:
        """
        pass

    """ --------------- Private Methods --------------- """

    def __save_image_sequence(self, img_seq, video_name):
        # Step 1 - Create folder if it does not exist
        image_sequence_dir = os_path_join(self.im_seqs_dir, video_name)
        os_makedirs(
            image_sequence_dir,
            exist_ok=True
        )
        # Step 2 - For every image:
        for i, img in enumerate(img_seq):
            # Step 2.1 - Save image in the directory as 'xxxxxx' + "video_name".jpg
            # Set image name
            frame_name = '{0:06}'.format(i + 1) + '_' + video_name + '.jpg'
            # Save image
            cv2_imwrite(
                os_path_join(image_sequence_dir, frame_name),
                img
            )
            """
            self.image_handler.save_image(
                os_path_join(image_sequence_dir, frame_name),
                img
            )
            """

    def __get_fixed_video_name(self, video_name):
        if video_name.endswith('.avi'):
            return video_name[:-4]
        elif video_name.endswith('.AVI'):
            return video_name[:-4]
        elif video_name.endswith('.Avi'):
            return video_name[:-4]
        elif video_name.endswith('.mp4'):
            return video_name[:-4]
        elif video_name.endswith('.MP4'):
            return video_name[:-4]
        elif video_name.endswith('.Mp4'):
            return video_name[:-4]
        else:
            return video_name
