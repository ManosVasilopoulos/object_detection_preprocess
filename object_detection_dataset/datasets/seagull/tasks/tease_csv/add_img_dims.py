from detection_and_tracking.configuration.seagull import complete_visible_csv_path, dataset_dir
import pandas as pd
from detection_and_tracking.datasets.seagull.seagull_csv_handler import Seagull_CSV_Handler

if __name__ == '__main__':
    dh = Seagull_CSV_Handler(dataset_dir)

    df = pd.read_csv(complete_visible_csv_path)

    new_df = dh.add_img_dimension(df)
    new_df.to_csv(complete_visible_csv_path.replace('.csv', '-extended.csv'))
