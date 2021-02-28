from detection import Image_Sequence_Handler
from detection import Video_Handler
from os import listdir as os_listdir

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Singapore Maritime - VIS Onshore'

    ish = Image_Sequence_Handler(dataset_dir, exist=False)
    vh = Video_Handler(dataset_dir)

    videos_names = os_listdir(ish.videos_dir)

    for video_name in videos_names:
        vh.read_video(video_name)
        seq = vh.video_to_image_sequence()
        ish.save_image_sequence(seq, video_name)