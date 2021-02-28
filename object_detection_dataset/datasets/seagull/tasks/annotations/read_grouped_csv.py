from detection_and_tracking.datasets.seagull.seagull_csv_handler import Seagull_CSV_Handler
from detection_and_tracking.configuration.seagull import dataset_dir
from os.path import join as os_path_join

if __name__ == '__main__':
    csv_directory = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\outputs\\standard_format\\z_processed_txt_to_csv\\detection_and_tracking'
    csv_handler = Seagull_CSV_Handler(dataset_dir)

    csv_path = os_path_join(csv_directory, 'all-complete-visible-detection_and_tracking-grouped.csv')

    df = csv_handler.read_csv(csv_path)

    test_row = df.iloc[13535]
    xmin = test_row['xmin']
    print(xmin, type(xmin))
    l = eval(xmin)
    for n in l:
        print(n, type(n))
