import pandas as pd

if __name__ == '__main__':
    directory = 'E:\\Data Sets\\Detection\\COCO\\outputs\\standard_format\\'
    data_path = directory + 'seagull.csv'
    df = pd.read_csv(data_path)
    df['class'] = df['class'].apply(eval)
    df['class'] = df['class'].apply(lambda x: [9 for _ in x])
    df.to_csv(directory + 'updated_seagull.csv')
