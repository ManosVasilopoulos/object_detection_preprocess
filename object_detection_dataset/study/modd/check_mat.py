from detection.handlers.mat_handler import MAT_Handler



if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MODD'
    mh = MAT_Handler(dataset_dir)

    mh.read_mat('01.mat')
    mh.investigate()