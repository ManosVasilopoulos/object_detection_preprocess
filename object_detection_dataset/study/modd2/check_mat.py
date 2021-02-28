from detection.datasets import MODD2_MAT_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MODD2'
    mh = MODD2_MAT_Handler(dataset_dir)

    dict_ = mh.read_mat('main/kope67-00-00025200-00025670/00025363L.mat')
    mh.investigate(dict_)