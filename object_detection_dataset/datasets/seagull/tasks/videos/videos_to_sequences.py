from detection_and_tracking.handlers.video_handler import Video_Handler
from detection_and_tracking.handlers.image_sequence_handler import Image_Sequence_Handler
from detection_and_tracking.configuration.seagull import complete_visible_videos_dir, complete_no_objects_videos_dir, \
    incomplete_visible_videos_dir, dataset_dir
from os.path import join as os_path_join
from os import listdir as os_listdir

if __name__ == '__main__':
    img_seq_handler = Image_Sequence_Handler(dataset_dir, exist=False)
    video_handler = Video_Handler(dataset_dir)

    paths_of_videos_to_convert = [
                                     (complete_visible_videos_dir, video_name) for video_name in
                                     os_listdir(complete_visible_videos_dir)
                                 ] + [
                                     (complete_no_objects_videos_dir, video_name) for video_name in
                                     os_listdir(complete_no_objects_videos_dir)
                                 ] + [
                                     (incomplete_visible_videos_dir, video_name) for video_name in
                                     os_listdir(incomplete_visible_videos_dir)
                                 ]

    for dir_, video_name in paths_of_videos_to_convert:
        path = os_path_join(dir_, video_name)
        print('Reading video: ----', video_name, '----')
        video_capture = video_handler.read_video(path)
        print('Converting to image-sequence: ----', video_name, '----')
        video_handler.video_to_save_image_sequence(video_capture, video_name)
