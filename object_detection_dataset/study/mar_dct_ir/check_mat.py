from detection.handlers.mat_handler import MAT_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MAR-DCT-IR'
    mh = MAT_Handler(dataset_dir)

    mh.read_mat('HorizonGT/ir-1HorizonGT.mat')
    mh.investigate()