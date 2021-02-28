import os
from detection_and_tracking.configuration.seagull import dataset_dir

if __name__ == '__main__':
    yolov5_dir = os.path.join(dataset_dir, 'ready_for_training', 'yolo_v5_dataset')
    validate_dir = os.path.join(yolov5_dir, 'validate', 'labels')

    counter = 0
    for txt_file in os.listdir(validate_dir):
        with open(os.path.join(validate_dir, txt_file), 'r+') as f:
            lines = f.readlines()
            counter = counter + len(lines)

    print('Number of objects in test data:', counter)
