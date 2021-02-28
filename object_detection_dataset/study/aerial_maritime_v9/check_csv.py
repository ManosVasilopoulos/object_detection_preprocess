from detection.handlers.csv_handler import CSV_Handler

if __name__ == '__main__':
    dataset_dir = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\Aerial Maritime v9'
    csv_h = CSV_Handler(dataset_dir)

    print(csv_h.standard_format_dir)
    csv_h.read_csv('all.csv')

    csv_h.investigate()