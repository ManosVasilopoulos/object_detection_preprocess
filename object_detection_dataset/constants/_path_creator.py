from os.path import join
from os import makedirs


class ConfigPaths:
    def __init__(self, dataset_dir, make_dirs=True):
        self.dataset_dir = dataset_dir

        self.inputs_dir = join(self.dataset_dir, 'inputs')
        self.outputs_dir = join(self.dataset_dir, 'outputs')

        """ Inputs """
        # videos
        self.videos_dir = join(self.inputs_dir, 'videos')

        self.complete_videos_dir = join(self.videos_dir, 'complete')
        self.complete_visible_videos_dir = join(self.complete_videos_dir, 'visible')
        self.complete_infrared_videos_dir = join(self.complete_videos_dir, 'infrared')

        self.incomplete_videos_dir = join(self.videos_dir, 'incomplete')
        self.incomplete_visible_videos_dir = join(self.incomplete_videos_dir, 'visible')
        self.incomplete_infrared_videos_dir = join(self.incomplete_videos_dir, 'infrared')

        self.no_objects_videos_dir = join(self.videos_dir, 'no_bjects')
        self.no_objects_visible_videos_dir = join(self.no_objects_videos_dir, 'visible')
        self.no_objects_infrared_videos_dir = join(self.no_objects_videos_dir, 'infrared')

        self.unavailable_videos_dir = join(self.videos_dir, 'unavailable')
        self.unavailable_visible_videos_dir = join(self.unavailable_videos_dir, 'visible')
        self.unavailable_infrared_videos_dir = join(self.unavailable_videos_dir, 'infrared')

        # images
        self.images_dir = join(self.inputs_dir, 'images')

        self.complete_images_dir = join(self.images_dir, 'complete')
        self.complete_visible_images_dir = join(self.complete_images_dir, 'visible')
        self.complete_infrared_images_dir = join(self.complete_images_dir, 'infrared')

        self.incomplete_images_dir = join(self.videos_dir, 'incomplete')
        self.incomplete_visible_images_dir = join(self.incomplete_images_dir, 'visible')
        self.incomplete_infrared_images_dir = join(self.incomplete_images_dir, 'infrared')

        self.no_objects_images_dir = join(self.videos_dir, 'no_bjects')
        self.no_objects_visible_images_dir = join(self.no_objects_images_dir, 'visible')
        self.no_objects_infrared_images_dir = join(self.no_objects_images_dir, 'infrared')

        self.unavailable_images_dir = join(self.videos_dir, 'unavailable')
        self.unavailable_visible_images_dir = join(self.unavailable_images_dir, 'visible')
        self.unavailable_infrared_images_dir = join(self.unavailable_images_dir, 'infrared')

        """ OTHER """
        self.other_files_dir = join(self.dataset_dir, 'other_files')
        self.dataset_annotations_path = join(self.dataset_dir, 'data_report\\unified_sheet.csv')

        """ Outputs """
        # Original Format
        self.original_format_dir = join(self.outputs_dir, 'original_format')
        self.complete_visible_txt_dir = join(self.original_format_dir, '\\complete\\visible')
        self.complete_infrared_txt_dir = join(self.original_format_dir, '\\complete\\infrared')
        self.incomplete_visible_txt_dir = join(self.original_format_dir, '\\incomplete\\visible')
        self.incomplete_infrared_txt_dir = join(self.original_format_dir, '\\incomplete\\infrared')

        # Outputs > Standard Format
        self.standard_format_dir = join(self.outputs_dir, 'standard_format')
        # TODO - Design a workflow that Creates folders for each step of the "standarization" process
        """
        self.step_1_dir = join(self.standard_format_dir, 'step_1_txt_to_csv')
        self.step_2_dir = join(self.standard_format_dir, 'step_2_group_frames')
        self.step_3_dir = join(self.standard_format_dir, 'step_3_add_images_sizes')
        self.step_4_dir = join(self.standard_format_dir, 'step_4_transform_to_standard')
        """

        # Outputs > Models' Formats
        models_annotations_dir = join(self.outputs_dir, 'models_formats')

        self.coco_dir = join(models_annotations_dir, 'coco')
        self.create_ml_dir = join(models_annotations_dir, 'create_ml')
        self.pascal_voc_dir = join(models_annotations_dir, 'pascal_voc')
        self.retinanet_keras_dir = join(models_annotations_dir, 'retinanet_keras')
        self.tensorflow_object_detection_dir = join(models_annotations_dir, 'tensorflow_object_detection')
        self.yolo_darknet_dir = join(models_annotations_dir, 'yolo_darknet')
        self.yolo_v3_keras_dir = join(models_annotations_dir, 'yolo_v3_keras')
        self.yolo_v3_pytorch_dir = join(models_annotations_dir, 'yolo_v3_pytorch')
        self.yolo_v4_pytorch_dir = join(models_annotations_dir, 'yolo_v4_pytorch')
        self.yolo_v5_pytorch_dir = join(models_annotations_dir, 'yolo_v5_pytorch')

        self.yolo_v5_pytorch_labels_dir = join(self.yolo_v5_pytorch_dir, 'labels')

        # Create Directory Tree
        if make_dirs:
            for var in vars(self):
                print('Making Directory:', var)
                makedirs(var, exist_ok=True)
