from detection_and_tracking.datasets.seagull.seagull_txt_handler import Seagull_TXT_Handler
from detection_and_tracking.configuration.seagull import dataset_dir, SeagullPaths
from pandas import read_csv as pd_read_csv

seagull_paths = SeagullPaths()
# TODO - Fix maritime

if __name__ == '__main__':
    txt_handler = Seagull_TXT_Handler(dataset_dir)

    dataset_info_df = pd_read_csv(dataset_annotations_info, delimiter=';')

    txt_handler.txts_to_tracking_csv(complete_visible_txt_dir, csv_name='all-complete-visible-tracking.csv', dataset_info_df=dataset_info_df)
    txt_handler.txts_to_detection_csv(complete_visible_txt_dir, csv_name='all-complete-visible-detection_and_tracking.csv')

    txt_handler.txts_to_tracking_csv(complete_infrared_txt_dir, csv_name='all-complete-infrared-tracking.csv', dataset_info_df=dataset_info_df)
    txt_handler.txts_to_detection_csv(complete_infrared_txt_dir, csv_name='all-complete-infrared-detection_and_tracking.csv')

    txt_handler.txts_to_detection_csv(incomplete_visible_txt_dir, csv_name='all-incomplete-visible-detection_and_tracking.csv')
