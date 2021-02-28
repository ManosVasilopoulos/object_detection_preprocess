from detection.handlers.mat_handler import MAT_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Buoy'
    mh = MAT_Handler(dataset_dir)

    mh.read_mat('HorizonGT/buoyGT_2_5_3_0HorizonGT.mat')
    mh.investigate()