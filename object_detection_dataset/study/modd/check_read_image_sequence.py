from detection.datasets import MODD2_Image_Sequence_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MODD2'

    ih = MODD2_Image_Sequence_Handler(dataset_dir, exist=True)

    seq_name = 'kope67-00-00025200-00025670/framesRectified'

    ih.read_image_sequence(seq_name)
    ih.play_image_sequence()
