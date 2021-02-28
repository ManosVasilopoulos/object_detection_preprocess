from detection import Image_Sequence_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\MODD2'

    ih = Image_Sequence_Handler(dataset_dir, exist=True)

    seq_name = 'kope67-00-00004500-00005050'

    ih.read_image_sequence(seq_name)
    ih.play_image_sequence()
