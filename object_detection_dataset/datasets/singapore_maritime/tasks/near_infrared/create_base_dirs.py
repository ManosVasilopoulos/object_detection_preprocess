from detection import Image_Sequence_Handler
from detection.handlers.mat_handler import MAT_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Singapore Maritime - Near Infrared'

    mat_h = MAT_Handler(dataset_dir)
    mat_h.create_base_dirs()
    ish = Image_Sequence_Handler(dataset_dir, exist=False)
    ish.create_base_dirs()