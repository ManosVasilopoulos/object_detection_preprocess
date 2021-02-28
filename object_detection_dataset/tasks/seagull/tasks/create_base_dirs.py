from detection.inputs_handler import Inputs_Handler
from detection.outputs_handler import Outputs_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\'
    ih = Inputs_Handler(dataset_dir)
    ih.create_base_dirs()
    oh = Outputs_Handler(dataset_dir)
    oh.create_base_dirs()
