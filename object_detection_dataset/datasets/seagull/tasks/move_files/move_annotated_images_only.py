import os
from detection_and_tracking.configuration.seagull import SeagullPaths, standard_format_dir
from detection_and_tracking.configuration.seagull import images_annotated_dir, images_visible_dir
from ast import literal_eval
import pandas as pd
import csv
import sys

seagull_paths = SeagullPaths()
# TODO - Fix Paths

def read_csv(csv_path: str):
    with open(csv_path, 'r') as csv_stream:
        csv_reader = csv.reader(csv_stream, delimiter=',', quotechar='\"')
        line_count = -1
        for row in csv_reader:
            try:

                print('line:', line_count, row[0], '------', row[1], '------', row[2])
            except:
                print('Faulty line:', line_count, row[0])
                print(row[0].split(','))
                sys.exit()
            line_count += 1


if __name__ == '__main__':
    dataset_csv_path = os.path.join(
        standard_format_dir,
        'dataset.csv'
    )
    # df = read_csv(dataset_csv_path)
    df = pd.read_csv(dataset_csv_path,
                     converters={
                         'class': literal_eval,
                         'xmin': literal_eval,
                         'ymin': literal_eval,
                         'xmax': literal_eval,
                         'ymax': literal_eval
                     })
    for index, row in df.iterrows():
        frame_name = row['frame_name']
        try:
            os.rename(
                os.path.join(
                    images_visible_dir,
                    frame_name
                ),
                os.path.join(
                    images_annotated_dir,
                    frame_name
                )
            )
            is_succesful = 'Succeeded'
        except FileNotFoundError:
            is_succesful = 'Failed'
        except TypeError:
            print(row['Unnamed: 0'])
            sys.exit()
        # print(is_succesful,'moving from:', os.path.join(images_visible_dir,frame_name)[100:],'To:', os.path.join(images_annotated_dir, frame_name)[100:])
