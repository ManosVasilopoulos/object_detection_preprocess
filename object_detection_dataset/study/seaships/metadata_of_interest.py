import pymediainfo
from os import listdir
from os.path import join
from detection import Video_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL'
    videos_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\inputs\\videos\\Complete\\visible\\'
    videos_list = listdir(videos_dir)
    vh = Video_Handler(dataset_dir)
    for video in videos_list:
        video_path = join(videos_dir, video)
        vh.read_metadata('Complete/visible/' + video)
        media_info = pymediainfo.MediaInfo.parse(video_path)
        print('--------------------', video, '--------------------')
        for track in media_info.tracks:
            if track.track_type == 'General':
                print('Filename:', track.file_name)
                print('file_extension:', track.file_extension)
                print('file_size:', track.file_size)
                print('other_file_size:', track.other_file_size[4])
                print('duration:', track.format)
                print('overall_bit_rate_mode:', track.overall_bit_rate_mode)
                print('other_duration:', track.other_duration[0])
                print('frame_rate:', track.frame_rate)
                print('other_overall_bit_rate:', track.other_overall_bit_rate[0])
                print('frame_count:', track.frame_count)
                print('other_stream_size:', track.other_stream_size[4])
            elif track.track_type == 'Video':
                print('width:', track.width)
                print('height:', track.height)
                print('frame_rate_mode:', track.frame_rate_mode)
                print('frame_count:', track.frame_count)
