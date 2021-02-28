from detection.handlers.mat_handler import MAT_Handler
from detection.inputs_handler import Inputs_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MAR-DCT-VIS'
    mh = MAT_Handler(dataset_dir)
    ih = Inputs_Handler(dataset_dir)

    mh.read_mat('HorizonGT/italy-occlusions-1HorizonGT.mat')
    mh.investigate()

    mh.read_mat('ObjectGT/italy-occlusions-1ObjectGT.mat')
    mh.investigate()
