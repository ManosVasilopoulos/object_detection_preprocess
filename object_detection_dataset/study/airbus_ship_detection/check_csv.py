from detection.handlers.csv_handler import CSV_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\AirBus Ship Detection'

    csv_h = CSV_Handler(dataset_dir)

    csv_h.read_csv('masks/train_masks.csv')
    csv_h.investigate()
