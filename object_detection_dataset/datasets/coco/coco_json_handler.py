from pandas import DataFrame
from os.path import join as os_path_join
import json
from object_detection_dataset.handlers.json_handler import JSON_Handler
from pycocotools.coco import COCO
from pycocotools.mask import toBbox
from object_detection_dataset.constants._path_creator import ConfigPaths
import sys


class COCO_JSON_Handler(JSON_Handler):
    image_ids: list
    image_names: list
    widths: list
    heights: list
    annotation_ids: list
    bboxes: list
    category_ids: list
    categories: list
    supercategories: list

    df: DataFrame

    def __init__(self, dataset_dir: str, annotation_file_path=None, extract_data=False):
        # Paths holder
        super().__init__(dataset_dir)

        if annotation_file_path:
            self.read_json(annotation_file_path)

            if extract_data:
                self.fill_with_data()
                csv_path = annotation_file_path.replace('.json', '.csv')
                self.turn_into_csv(csv_path, self.df)

    def fill_with_data(self):
        self.info = self.data['info']
        self.licenses = self.data['licenses']

        # extract image data
        self.image_ids, self.image_names, \
        self.annotation_ids, self.bboxes, \
        self.category_ids, self.categories, self.supercategories = self.extract_image_data()

        # Transform data extracted to DataFrame and save to CSV
        self.df = DataFrame(
            list(
                zip(
                    self.image_ids, self.image_names,
                    self.annotation_ids, self.bboxes,
                    self.category_ids, self.categories, self.supercategories
                )
            ),
            columns=['image_ids', 'image_names', 'annotation_ids', 'bboxes', 'category_ids', 'categories',
                     'supercategories']
        )

    def turn_into_csv(self, save_path: str, df: DataFrame):
        print('Saving in CSV at: ', save_path)
        df.to_csv(save_path)

    def get_image_ids(self):
        return self.image_ids

    def get_image_names(self):
        return self.image_names

    def get_annotation_ids(self):
        return self.annotation_ids

    def get_bboxes(self):
        return self.bboxes

    def get_category_ids(self):
        return self.category_ids

    def get_categories(self):
        return self.categories

    def get_supercategories(self):
        return self.supercategories

    def extract_image_data(self):
        # ---- Image Data ----
        image_ids = []  # list of int
        image_names = []  # list of str
        widths = []
        heights = []

        """ for the lists below, each element corresponds to one image """
        # ---- Annotation Data ----
        # Each element is a list of annotation-IDs that correspond to one image
        annotation_ids = []  # list of list of int

        # Each element is a list of BBoxes that correspond to one image
        bboxes = []  # list of lists of lists of float (list of list of bboxes)

        # ---- Category Data ----
        # Each element is a list of categories that correspond to one image
        # each category corresponds to one bounding box
        category_ids = []  # list of lists of int
        categories = []
        supercategories = []

        for val in self.data['images']:
            print('Working on image "{}"'.format(val['file_name']))
            image_ids.append(val['id'])
            image_names.append(val['file_name'])
            widths.append(val['width'])
            heights.append(val['height'])

            print('Searching for annotations of image_id:"{}"'.format(val['id']))
            bboxs, category_id, annotation_id = self.__find_bbox_of_id(val['id'])
            bboxes.append(bboxs)
            annotation_ids.append(annotation_id)
            category_ids.append(category_id)

            print('Searching for category of image_id:"{}" and annotation_id:"{}"'.format(val['id'], annotation_id))
            category_s, supercategory_s = self.__find_category_of_category_id(category_id)
            categories.append(category_s)
            supercategories.append(supercategory_s)

        self.image_ids, self.image_names, self.widths, self.heights, \
        self.annotation_ids, self.bboxes, \
        self.category_ids, self.categories, self.supercategories = image_ids, image_names, widths, heights, \
                                                                   annotation_ids, bboxes, \
                                                                   category_ids, categories, supercategories
        return image_ids, image_names, annotation_ids, bboxes, category_ids, categories, supercategories

    def show_all_categories(self, save=True):
        for category in self.data['categories']:
            print(category)

    def extract_categories(self, filedir: str):
        with open(os_path_join(filedir, 'categories.txt'), 'w+') as f:
            f.writelines([str(x) + '\n' for x in self.data['categories']])

    def __find_category_of_category_id(self, category_ids: list):
        categories, supercategories = [], []
        for category_id in category_ids:
            for val in self.data['categories']:
                if val['id'] == category_id:
                    categories.append(val['name'])
                    supercategories.append(val['supercategory'])
        return categories, supercategories

    def __find_bbox_of_id(self, image_id: int):
        total_bboxes = []
        category_ids = []
        id_list = []
        for val in self.data['annotations']:
            if val['image_id'] == image_id:
                total_bboxes.append(val['bbox'])
                category_ids.append(val['category_id'])
                id_list.append(val['id'])
        return total_bboxes, category_ids, id_list


if __name__ == '__main__':
    dataset_dir = 'E:\Data Sets\Detection\COCO\outputs\original_format'
    # dataset_dir = 'D:\Documents\Computer Vision\Object Detection\Datasets\COCO'
    paths = ConfigPaths(dataset_dir, False)
    json_path = os_path_join(dataset_dir, 'instances_train2017.json')

    handler = COCO_JSON_Handler(dataset_dir, json_path, extract_data=True)
    handler.set_json_dir(dataset_dir)
    handler.show_all_categories()
    handler.extract_categories(dataset_dir)
