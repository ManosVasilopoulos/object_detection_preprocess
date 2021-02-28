from object_detection_dataset.outputs_handler import Outputs_Handler
from scipy.io import loadmat as scipy_io_loadmat
from numpy import ndarray as np_ndarray
from os.path import join as os_path_join


class MAT_Handler(Outputs_Handler):
    mat_dict: dict
    mat_keys: list

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def read_mat(self, mat_name: str):
        mat_path = os_path_join(self.original_format_dir, mat_name)
        self.mat_dict = scipy_io_loadmat(mat_path)
        self.mat_keys = list(self.mat_dict.keys())
        return self.mat_dict

    def print_keys(self, dict_=None):
        if dict_ is not None:
            print(dict_.keys())
        else:
            print(self.mat_dict.keys())

    def investigate(self, mat_dict=None):
        if mat_dict is not None:
            self.__investigate(mat_dict)
        else:
            self.__investigate(self.mat_dict)

    """ ---------------------- Private Methods ---------------------- """

    def __investigate(self, mat_dict: dict):
        mat_keys = mat_dict.keys()
        for key in mat_keys:
            print('• Key:', key)
            if type(mat_dict[key]) == np_ndarray:
                print('- The shape of the value is:', mat_dict[key].shape)
                highest_index = min(10, mat_dict[key].shape[0])
                for i in range(highest_index):
                    if mat_dict[key].shape[1] > 3:
                        print('○ Value:\n', mat_dict[key][i, :3])
                    else:
                        print('○ Value:\n', mat_dict[key][i, :])
                    print('☼ dtype:', mat_dict[key].dtype,'\n')
                print('-------------------------------------------------\n')
            else:
                print('- The type of the value is:', type(mat_dict[key]))
                print('○ Value:', mat_dict[key], '\n-------------------------------------------------\n')
        print('◄▌ End of investigation \n\n')