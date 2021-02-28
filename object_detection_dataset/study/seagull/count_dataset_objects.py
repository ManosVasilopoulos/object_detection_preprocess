from detection_and_tracking.configuration.seagull import standard_csv_dir
import pandas as pd
import os

if __name__ == '__main__':
    df = pd.read_csv(
        os.path.join(standard_csv_dir, 'dataset.csv')
    )

    print(df)
    counter = 0
    for index, row in df.iterrows():
        counter += len(eval(row['class']))

    print('Counted objects:', counter)