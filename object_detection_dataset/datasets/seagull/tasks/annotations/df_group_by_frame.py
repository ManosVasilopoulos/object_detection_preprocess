from detection_and_tracking.datasets.seagull.seagull_csv_handler import Seagull_CSV_Handler
from detection_and_tracking.configuration.seagull import dataset_dir
from os.path import join as os_path_join


def main(csv_name: str):
    csv_directory = 'C:\\Users\\emmanouil.vasilopoul\\Documents\\i-SENSE\\Effector\\Datasets\\Detection\\SEAGULL\\outputs\\standard_format\\z_processed_txt_to_csv\\detection_and_tracking'
    csv_handler = Seagull_CSV_Handler(dataset_dir)

    csv_path = os_path_join(csv_directory, csv_name)

    df = csv_handler.read_csv(csv_path)
    new_df = csv_handler.get_group_by_frame_dataframe(df)

    new_df.to_csv(os_path_join(csv_directory, csv_name.replace('.csv', '-grouped.csv')))


if __name__ == '__main__':
    main('all-complete-visible-detection_and_tracking.csv')
    main('all-incomplete-visible-detection_and_tracking.csv')
