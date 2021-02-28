from os import listdir
from os.path import join
from detection import Video_Handler
from pandas import concat as pd_concat
if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL'
    videos_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\inputs\\videos\\Complete\\visible\\'
    videos_list = listdir(videos_dir)
    vh = Video_Handler(dataset_dir)
    videos_metadata = []
    for video in videos_list:
        video_path = join(videos_dir, video)
        videos_metadata.append(vh.read_metadata('Complete/visible/' + video))
    df = pd_concat(videos_metadata)
    print(df)