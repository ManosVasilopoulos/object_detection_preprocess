from pandas import DataFrame
from pandas import read_json
from os.path import join as os_path_join
import os
import json
from object_detection_dataset.outputs_handler2 import Outputs_Handler2


class JSON_Handler(Outputs_Handler2):
    data: dict
    json_filedir: str
    json_filename: str
    json_filepath: str

    def get_data(self):
        if self.data:
            return self.data
        else:
            print("No data has been read. Use 'JSON_Handler.read_json'.")
            return {}

    def set_json_dir(self, json_dir: str):
        self.json_filedir = json_dir

    def set_json_filename(self, filename: str):
        self.json_filename = filename

    def set_json_filepath(self, filepath: str):
        self.json_filepath = filepath

    def read_json(self, json_path: str):
        with open(json_path) as json_file:
            self.data = json.load(json_file)
        return self.data

    def inspect_json(self, data: dict, indent=0):
        space = "    " * indent
        for attr in data:
            type_ = type(data[attr])
            print(space + "- Attribute:", attr, "Type:", type_, end=" ")
            if type_ == dict:
                print()
                self.inspect_json(data[attr], indent + 1)
            elif type_ == list:
                print("- First element of array")
                elem = data[attr][0]
                if type(elem) == dict:
                    print('    ----- Inner Dictionary -----')
                    self.inspect_json(elem, indent + 1)
                else:
                    print(space + "    ", data[attr][0])
            else:
                print("- Value:", data[attr])


from object_detection_dataset.constants._path_creator import ConfigPaths

if __name__ == '__main__':
    dataset_dir = 'E:\Data Sets\Detection\COCO\outputs\original_format'
    # dataset_dir = 'D:\Documents\Computer Vision\Object Detection\Datasets\COCO'

    paths = ConfigPaths(dataset_dir, False)
    handler = JSON_Handler(dataset_dir)

    json_path = os_path_join(dataset_dir, 'instances_val2017.json')
    data = handler.read_json(json_path)
    handler.inspect_json(data)
