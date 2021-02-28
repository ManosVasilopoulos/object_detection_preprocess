import pandas as pd
from detection_and_tracking.datasets.seagull.seagull_xml_handler import Seagull_XML_Handler
from detection_and_tracking.configuration.seagull import SeagullPaths

seagull_paths = SeagullPaths()
dataset_dir = seagull_paths.dataset_dir

# TODO - Fix maritime given
if __name__ == '__main__':
    xml_handler = Seagull_XML_Handler(dataset_dir)
    df = pd.read_csv(complete_visible_extended_csv_path)

    for index, row in df.iterrows():
        if row['image_width'] != 1920:
            continue
        try:
            xml_handler.row_to_xml(row, full_hd_test_dir, row['image_width'], row['image_height'], row['image_depth'])
            print('Done')
        except Exception as e:
            print('Failed', e)
            continue