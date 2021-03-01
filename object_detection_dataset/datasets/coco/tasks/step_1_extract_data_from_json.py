from object_detection_dataset.constants._path_creator import ConfigPaths
from object_detection_dataset.datasets.coco.coco_json_handler import COCO_JSON_Handler
from os.path import join
if __name__ == '__main__':
    dataset_dir = 'E:\Data Sets\Detection\COCO\outputs\original_format'
    # dataset_dir = 'D:\Documents\Computer Vision\Object Detection\Datasets\COCO'
    paths = ConfigPaths(dataset_dir, False)
    json_path = join(dataset_dir, 'instances_train2017.json')

    handler = COCO_JSON_Handler(dataset_dir, json_path, extract_data=True)
    handler.set_json_dir(dataset_dir)
    handler.show_all_categories()
    handler.extract_categories(dataset_dir)