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
    annotation_ids: list
    bboxes: list
    category_ids: list
    categories: list
    supercategories: list

    def __init__(self, dataset_dir: str, annotation_file_path=None):
        # Paths holder
        super().__init__(dataset_dir)

        if annotation_file_path:
            self.read_json(annotation_file_path)

            self.info = self.data['info']
            self.licenses = self.data['licenses']

            # For later
            csv_path = annotation_file_path.replace('.json', '.csv')

            # extract image data
            self.image_ids, self.image_names, \
            self.annotation_ids, self.bboxes, \
            self.category_ids, self.categories, self.supercategories = self.extract_image_data()

            df = DataFrame(
                list(
                    zip(
                        self.image_ids, self.image_names,
                        self.annotation_ids, self.bboxes,
                        self.category_ids, self.categories, self.supercategories
                    )
                ),
                columns=['image_ids', 'image_names', 'annotation_ids', 'bboxes', 'category_ids', 'categories', 'supercategories']
            )
            print('Saving in CSV at: ', csv_path)
            df.to_csv(csv_path)

    def set_annotation_path(self, annotation_file_path: str, extract_data: bool):
        self.read_json(annotation_file_path)
        if extract_data:
            self.info = self.data['info']
            self.licenses = self.data['licenses']

            # extract image data
            self.image_ids, self.image_names, \
            self.annotation_ids, self.bboxes, \
            self.category_ids, self.categories, self.supercategories = self.extract_image_data()

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
        image_ids = []
        image_names = []

        annotation_ids = []
        bboxes = []

        category_ids = []
        categories = []
        supercategories = []

        for val in self.data['images']:
            print('Working on image "{}"'.format(val['file_name']))
            image_ids.append(val['id'])
            image_names.append(val['file_name'])

            print('Searching for annotations of image_id:"{}"'.format(val['id']))
            bboxs, category_id, annotation_id = self.__find_bbox_of_id(val['id'])
            bboxes.append(bboxs)
            annotation_ids.append(annotation_id)
            category_ids.append(category_id)

            print('Searching for category of image_id:"{}" and annotation_id:"{}"'.format(val['id'], annotation_id))
            category, supercategory = self.__find_category_of_category_id(category_id)
            categories.append(category)
            supercategories.append(supercategory)

        self.image_ids, self.image_names, \
        self.annotation_ids, self.bboxes, \
        self.category_ids, self.categories, self.supercategories = image_ids, image_names,\
                                                                   annotation_ids, bboxes,\
                                                                   category_ids, categories, supercategories
        return image_ids, image_names, annotation_ids, bboxes, category_ids, categories, supercategories

    def __find_category_of_category_id(self, category_id: int):
        for val in self.data['categories']:
            print('Found Category.\n')
            if val['id'] == category_id:
                return val['name'], val['supercategory']

        print('Category not found.')
        return '', ''

    def __find_bbox_of_id(self, image_id: int):
        for val in self.data['annotations']:
            if val['image_id'] == image_id:
                print('Found Annotations with annotation_id: "{}".'.format(val['id']))
                if type(val['bbox'][0]) == int:
                    bboxes = [val['bbox']]
                else:
                    bboxes = val['bbox']
                return bboxes, val['category_id'], val['id']
        print('Annotations not found.')
        raise Exception("COCO_JSON_HandlerError: No bounding boxes found for image with image_id:'{}'".format(image_id))

if __name__ == '__main__':
    paths = ConfigPaths("E:\\Data Sets\\Detection\\COCO", False)
    dataset_dir = 'E:\\Data Sets\\Detection\\COCO'
    json_path = 'E:\\Data Sets\\Detection\\COCO\\outputs\\original_format\\instances_val2017.json'

    handler = COCO_JSON_Handler(dataset_dir, json_path)

