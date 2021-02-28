from detection import Image_Sequence_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Boats'

    ih = Image_Sequence_Handler(dataset_dir, exist=True)

    seq_name = 'Boats1_rgb'

    ih.read_image_sequence(seq_name)
    ih.play_image_sequence()