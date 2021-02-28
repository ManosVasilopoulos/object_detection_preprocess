from object_detection_dataset.datasets.seagull import Seagull_TXT_Handler
from object_detection_dataset import dataset_dir, complete_visible_txt_dir

if __name__ == '__main__':
    txt_handler = Seagull_TXT_Handler(dataset_dir)
    txt_handler.txts_to_csv(complete_visible_txt_dir)