import pandas as pd


class StandardDataset:
    def __init__(self) -> None:
        super().__init__()

    def read_standard_csv(self, csv_path):
        df = pd.read_csv(csv_path, index_col=0)

        df['class'] = df['class'].apply(eval)
        df['xmin'] = df['xmin'].apply(eval)
        df['ymin'] = df['ymin'].apply(eval)
        df['xmax'] = df['xmax'].apply(eval)
        df['ymax'] = df['ymax'].apply(eval)

        return df
