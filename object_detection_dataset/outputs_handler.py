from os.path import join as os_path_join
from os import makedirs as os_makedirs


class Outputs_Handler:
    original_outputs_subdir = '\\outputs\\original_format'
    standard_outputs_subdir = '\\outputs\\standard_format'

    def __init__(self, dataset_dir: str):
        self.dataset_dir = dataset_dir
        self.outputs_dir = os_path_join(self.dataset_dir, 'outputs')

        self.original_format_dir = os_path_join(self.outputs_dir, 'original_format')
        self.standard_format_dir = os_path_join(self.outputs_dir, 'standard_format')
        self.models_annotations_dir = os_path_join(self.outputs_dir, 'models_format')

        self.maritime_xml_dir = os_path_join(self.standard_format_dir, 'maritime')
        self.pascal_voc_xml_dir = os_path_join(self.standard_format_dir, 'pascal_voc')
        self.standard_csv_dir = os_path_join(self.standard_format_dir, 'standard_csv')

        self.coco_json_dir = os_path_join(self.models_annotations_dir, 'COCO')
        self.create_ml_dir = os_path_join(self.models_annotations_dir, 'CreateML')
        self.pascal_voc_dir = os_path_join(self.models_annotations_dir, 'PASCAL VOC')
        self.retinanet_keras_dir = os_path_join(self.models_annotations_dir, 'RetinaNet Keras')
        self.tensorflow_object_detection_dir = os_path_join(self.models_annotations_dir, 'Tensorflow Object Detection')
        self.yolo_darknet_dir = os_path_join(self.models_annotations_dir, 'YOLO Darknet')
        self.yolo_v3_keras_dir = os_path_join(self.models_annotations_dir, 'YOLO v3 Keras')
        self.yolo_v3_pytorch_dir = os_path_join(self.models_annotations_dir, 'YOLO v3 PyTorch')
        self.yolo_v4_pytorch_dir = os_path_join(self.models_annotations_dir, 'YOLO v4 PyTorch')
        self.yolo_v5_pytorch_dir = os_path_join(self.models_annotations_dir, 'YOLO v5 PyTorch')

    def create_base_dirs(self):
        os_makedirs(self.outputs_dir, exist_ok=True)
        os_makedirs(self.original_format_dir, exist_ok=True)
        os_makedirs(self.standard_format_dir, exist_ok=True)
        os_makedirs(self.maritime_xml_dir, exist_ok=True)
        os_makedirs(self.pascal_voc_xml_dir, exist_ok=True)
        os_makedirs(self.standard_csv_dir, exist_ok=True)

        os_makedirs(self.models_annotations_dir, exist_ok=True)
        os_makedirs(self.coco_json_dir, exist_ok=True)
        os_makedirs(self.create_ml_dir, exist_ok=True)
        os_makedirs(self.pascal_voc_dir, exist_ok=True)
        os_makedirs(self.retinanet_keras_dir, exist_ok=True)
        os_makedirs(self.tensorflow_object_detection_dir, exist_ok=True)
        os_makedirs(self.yolo_darknet_dir, exist_ok=True)
        os_makedirs(self.yolo_v3_keras_dir, exist_ok=True)
        os_makedirs(self.yolo_v3_pytorch_dir, exist_ok=True)
        os_makedirs(self.yolo_v4_pytorch_dir, exist_ok=True)
        os_makedirs(self.yolo_v5_pytorch_dir, exist_ok=True)



