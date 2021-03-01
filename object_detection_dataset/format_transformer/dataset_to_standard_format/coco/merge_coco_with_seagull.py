import pandas as pd
from object_detection_dataset.format_transformer.standard_format_to_model.standard_dataset import StandardDataset


def fix_class_numbers(classes: list):
    for i in range(len(classes)):
        class_no = classes[i]
        # Car
        if class_no == 3:
            classes[i] = 1
        # Motorcycle
        elif class_no == 4:
            classes[i] = 2
        # Airplane
        elif class_no == 5:
            classes[i] = 3
        # Boat
        elif class_no == 9:
            classes[i] = 4
        # Bird
        elif class_no == 16:
            classes[i] = 5
        # Frisbee
        elif class_no == 34:
            classes[i] = 6
        # Skis
        elif class_no == 35:
            classes[i] = 7
        # Snowboard
        elif class_no == 36:
            classes[i] = 8
        # Kite
        elif class_no == 38:
            classes[i] = 9
        # surfboard
        elif class_no == 42:
            classes[i] = 10
        # Every other object of COCO
        else:
            classes[i] = 11

    return classes


def filter_coco(coco_df: pd.DataFrame):
    new_frame = pd.DataFrame([], columns=coco_df.columns)

    for index, row in coco_df.iterrows():
        classes = row['class']
        for class_ in classes:
            if class_ in [3, 4, 5, 9, 16, 34, 35, 36, 38, 42]:
                row['class'] = fix_class_numbers(classes)
                new_frame = new_frame.append(row, ignore_index=True)
    return new_frame


if __name__ == '__main__':
    directory = 'E:\\Data Sets\\Detection\\COCO\\outputs\\standard_format\\'
    data_path = directory + 'updated_seagull.csv'

    standard = StandardDataset()
    seagull_df = standard.read_standard_csv(data_path)
    print(seagull_df.head(n=2))

    data_path = directory + 'standard_instances_train2017.csv'
    coco_df = standard.read_standard_csv(data_path)
    new_coco_df = filter_coco(coco_df)

    print(new_coco_df.head(n=2))
    # df = pd.concat([coco_df, seagull_df])

    df = new_coco_df.append(seagull_df)
    df.to_csv(directory + 'coco_x_seagull_fixed_class_numbers.csv')
