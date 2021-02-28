from detection_and_tracking.handlers.video_handler import Video_Handler
from pandas import concat as pd_concat
from os.path import join as os_path_join

# TODO - Fix script

def main(folder: str):
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL'
    vh = Video_Handler(dataset_dir, video_subfolder_path=folder)
    videos_metadata = []
    for video in vh.videos_names:
        videos_metadata.append(vh.read_metadata(video))
    df = pd_concat(videos_metadata)
    df.to_csv(
        os_path_join(
            vh.video_folder,
            folder.replace('\\', '') + '-metadata.csv'
        )
    )


if __name__ == '__main__':
    folder = 'Incomplete'
    main(folder)
