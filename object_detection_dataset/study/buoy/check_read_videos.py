from detection import Video_Handler
from detection import Image_Sequence_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Buoy'

    vh = Video_Handler(dataset_dir)

    ish = Image_Sequence_Handler(dataset_dir, exist=False)
    ish.create_base_dirs()

    for video_name in vh.videos_names:
        print('video_name:', video_name)
        vh.read_video(video_name)

        image_sequence = vh.video_to_image_sequence()
        print('Sequence shape:', image_sequence.shape)
        print('----------------------------------------\n')