from detection import Image_Sequence_Handler
from os import listdir as os_listdir
from os.path import join as os_path_join

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Singapore Maritime - VIS Onshore'

    ish = Image_Sequence_Handler(dataset_dir, exist=True)

    videos = os_listdir(ish.im_seqs_dir)
    counter = 0
    for video_name in videos:
        counter += len(
            os_listdir(
                os_path_join(ish.im_seqs_dir, video_name)
            )
        )
    print('Total images:', counter)
