from detection_and_tracking.format_transformer.dataset_to_standard_csv.seagull.handlers.seagull_csv_handler import \
    Seagull_CSV_Handler
from detection_and_tracking.configuration.seagull import dataset_dir
from detection_and_tracking.configuration.seagull import standard_format_dir
from os.path import join as os_path_join

if __name__ == '__main__':
    csv_handler = Seagull_CSV_Handler(dataset_dir)

    csv_path = os_path_join(standard_format_dir, 'dataset.csv')

    df = csv_handler.read_csv(csv_path)

    print(type(eval(df['xmin'].iloc[0])))
    print(type(eval(df['xmin'].iloc[0])[0]))
    print(eval(df['xmin'].iloc[0])[0])
    print(df['xmin'].iloc[0])