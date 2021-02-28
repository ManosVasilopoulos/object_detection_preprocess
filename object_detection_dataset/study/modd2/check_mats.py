from detection.datasets import MODD2_MAT_Handler
from os.path import join as os_path_join
from os import listdir as os_listdir

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MODD2'
    mh = MODD2_MAT_Handler(dataset_dir)

    mats = os_listdir(
        os_path_join(mh.original_format_dir, 'main', 'kope67-00-00025200-00025670')
    )
    for mat in mats:
        dict_ = mh.read_mat(
            os_path_join('main', 'kope67-00-00025200-00025670', mat)
        )
        mh.investigate(dict_)
        print('----------------------------------------------------')
