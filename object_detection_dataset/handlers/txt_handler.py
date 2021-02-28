from object_detection_dataset.outputs_handler import Outputs_Handler
from os.path import join as os_path_join
from numpy import ndarray as np_ndarray
from numpy import array as np_array


class TXT_Handler(Outputs_Handler):

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def read_txt(self, txt_name: str, txt_dir='') -> np_ndarray:
        txt_path = self._standard_check(txt_name, txt_dir)

        with open(txt_path, 'r') as txt:
            lines = txt.readlines()

        lines_list = []
        for line in lines:
            data = [txt_name.replace('.gt.txt', '')] + line.split()
            lines_list.append(data)

        return np_array(lines_list)

    def investigate(self, txt_name: str, txt_dir=''):
        txt_path = self._standard_check(txt_name, txt_dir)

        with open(txt_path, 'r') as txt:
            lines = txt.readlines()

        for i, line in enumerate(lines):
            print('Line-' + str(i + 1) + ':', line)
            if i + 1 == 20:
                break

    def _standard_check(self, txt_name: str, txt_dir: str):
        if txt_dir == '':
            return os_path_join(self.original_format_dir, txt_name)
        else:
            return os_path_join(txt_dir, txt_name)
