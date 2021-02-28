import os
from detection_and_tracking.configuration.seagull import SeagullPaths
from detection_and_tracking.configuration.seagull import full_hd_dir, full_hd_annotated_dir
from detection_and_tracking.configuration.seagull import complete_visible_csv_path
import pandas as pd

seagull_paths = SeagullPaths()
# TODO - Fix maritime

if __name__ == '__main__':
    df = pd.read_csv(complete_visible_csv_path)
    for index, row in df.iterrows():
        frame_name = row['frame_name']
        try:
            os.rename(
                os.path.join(
                    full_hd_dir,
                    frame_name
                ),
                os.path.join(
                    full_hd_annotated_dir,
                    frame_name
                )
            )
            is_succesful = 'Succeeded'
        except FileNotFoundError:
            is_succesful = 'Failed'
        print(
            is_succesful,
            'Moved from:',
            os.path.join(
                full_hd_dir,
                frame_name
            )[100:],
            'To:',
            os.path.join(
                full_hd_annotated_dir,
                frame_name
            )[100:]
        )
