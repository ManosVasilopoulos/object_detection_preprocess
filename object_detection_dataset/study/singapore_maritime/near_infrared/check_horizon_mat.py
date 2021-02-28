from detection.handlers.mat_handler import MAT_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Singapore Maritime - Near Infrared'

    mh = MAT_Handler(dataset_dir)

    mat_file = 'HorizonGT/MVI_0895_NIR_Haze_HorizonGT.mat'
    mh.read_mat(mat_file)

    mh.investigate()