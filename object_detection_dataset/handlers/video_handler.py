from object_detection_dataset.inputs_handler import Inputs_Handler
from cv2 import VideoCapture
from cv2 import destroyAllWindows as cv2_destroyAllWindows
from cv2 import waitKey as cv2_waitKey
from cv2 import imshow as cv2_imshow
from numpy import array as np_array
from os.path import join as os_path_join
from numpy import ndarray as np_ndarray
from pymediainfo import MediaInfo
from pandas import DataFrame
from os import makedirs as os_makedirs
from os.path import splitext as os_path_splitext
from os.path import basename as os_path_basename
from cv2 import imwrite as cv2_imwrite


class Video_Handler(Inputs_Handler):
    videos_subdir = 'videos'
    image_sequences_subdir = 'image_sequences'

    videos_paths: list
    video_capture: VideoCapture
    video_name: str
    images_sequence: np_ndarray
    title: str

    def __init__(self, dataset_dir):
        super().__init__(dataset_dir)

    def read_video(self, video_path: str):
        self.video_capture = VideoCapture(video_path)
        self.video_name = os_path_basename(video_path)
        return self.video_capture

    def play_video(self, video_capture=None, frame_rate=25, title='Video'):
        if video_capture is not None:
            self.__play_video(video_capture, frame_rate, title)
        else:
            self.__play_video(self.video_capture, frame_rate, self.title)

    def video_to_image_sequence(self, video_capture=None):
        if video_capture is not None:
            return self.__to_img_seq(video_capture)
        else:
            self.images_sequence = self.__to_img_seq(self.video_capture)
            return self.images_sequence

    def video_to_save_image_sequence(self, video_capture=None, video_name=None):
        if video_capture is not None:
            return self.__to_save_img_seq(video_capture, video_name)
        else:
            self.images_sequence = self.__to_save_img_seq(self.video_capture, self.video_name)
            return self.images_sequence

    def get_videos_path_list(self):
        return self.videos_paths

    def read_metadata(self, video_path: str) -> DataFrame:

        media_info = MediaInfo.parse(video_path)
        metadata = {}
        for track in media_info.tracks:
            if track.track_type == 'General':
                metadata['filename'] = [str(track.file_name)]
                metadata['file_extension'] = [str(track.file_extension)]
                metadata['file_size'] = [str(track.file_size)]
                metadata['other_file_size'] = [str(track.other_file_size[4])]
                metadata['duration'] = [str(track.duration)]
                metadata['other_duration'] = [str(track.other_duration[0])]
                metadata['frame_rate'] = [str(track.frame_rate)]
                metadata['other_overall_bit_rate'] = [str(track.other_overall_bit_rate[0])]
                metadata['frame_count'] = [str(track.frame_count)]
                metadata['other_stream_size'] = [str(track.other_stream_size[4])]
            elif track.track_type == 'Video':
                metadata['width'] = [str(track.width)]
                metadata['height'] = [str(track.height)]
                metadata['frame_rate_mode'] = [str(track.frame_rate_mode)]
                metadata['frame_count'] = [str(track.frame_count)]
        return DataFrame(metadata)

    """ --------------- Private Methods --------------- """

    def __to_save_img_seq(self, video_capture: VideoCapture, video_name: str):
        # Frame counter
        i = 0

        # To be 100% sure that we get the filename without the extension

        video_name = os_path_splitext(video_name)[0]
        image_sequence_dir = os_path_join(self.im_seqs_dir, video_name)
        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if ret:
                os_makedirs(
                    image_sequence_dir,
                    exist_ok=True
                )
                if video_name is None:
                    raise Exception(
                        'VideoHandlerError: if video_to_image_sequence receives a "save_sequences=True" then "video_name" must also receive a value. ')
                frame_name = '{0:06}'.format(i + 1) + '_' + video_name + '.jpg'
                # Save image
                cv2_imwrite(
                    os_path_join(image_sequence_dir, frame_name),
                    frame
                )
                # wait 1ms and make another check before 'breaking'
                if cv2_waitKey(1) & 0xFF == ord('q'):
                    break
                i += 1
            else:
                break

        print('Total frames of sequence read:', i - 1)

    def __to_img_seq(self, video_capture: VideoCapture):
        # Frame counter
        i = 1

        # image sequence
        image_seq = []
        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if ret:
                image_seq.append(frame)
                # wait 1ms and make another check before 'breaking'
                if cv2_waitKey(1) & 0xFF == ord('q'):
                    break
                i += 1
            else:
                break

        print('Total frames of sequence read:', i - 1)

        video_capture.release()
        cv2_destroyAllWindows()

        return np_array(image_seq)

    def __play_video(self, video_capture: VideoCapture, frame_rate: int, title: str):
        frame_duration = 1000 // frame_rate
        # Frame counter
        i = 1

        while video_capture.isOpened():
            ret, frame = video_capture.read()
            if ret:
                # display frame
                cv2_imshow(title, frame)
                # wait 40ms and make another check before 'breaking'
                if cv2_waitKey(frame_duration) & 0xFF == ord('q'):
                    break
                i += 1
            else:
                break

        print('Video player:', i, 'consecutive frames were displayed.')
