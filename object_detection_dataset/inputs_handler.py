from os.path import join as os_path_join
from os import makedirs as os_makedirs


class Inputs_Handler:
    def __init__(self, dataset_dir):
        self.dataset_dir = dataset_dir
        self.inputs_dir = os_path_join(self.dataset_dir, 'inputs')
        self.images_dir = os_path_join(self.inputs_dir, 'images')
        self.non_annot_images_dir = os_path_join(self.inputs_dir, 'non_annotated_images')
        self.videos_dir = os_path_join(self.inputs_dir, 'videos')
        self.im_seqs_dir = os_path_join(self.inputs_dir, 'image_sequences')
        self.non_annot_im_seqs_dir = os_path_join(self.inputs_dir, 'non_annotated_image_sequences')
        self.demo_dir = os_path_join(self.inputs_dir, 'demo')

    def create_base_dirs(self):
        os_makedirs(self.inputs_dir, exist_ok=True)
        os_makedirs(self.images_dir, exist_ok=True)
        os_makedirs(self.non_annot_images_dir, exist_ok=True)
        os_makedirs(self.videos_dir, exist_ok=True)
        os_makedirs(self.im_seqs_dir, exist_ok=True)
        os_makedirs(self.non_annot_im_seqs_dir, exist_ok=True)
        os_makedirs(self.demo_dir, exist_ok=True)
