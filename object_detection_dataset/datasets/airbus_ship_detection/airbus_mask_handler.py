from pandas import DataFrame
from numpy import asarray as np_asarray
from numpy import uint8 as np_uint8
from numpy import zeros as np_zeros
from os.path import join as os_path_join
from numpy import concatenate as np_concatenate
from numpy import ndarray as np_ndarray
from numpy import where as np_where
from numpy import amax as np_amax
from numpy import amin as np_amin


class AirBus_Mask_Handler:

    def mask_to_bbox(self, mask: np_ndarray):
        # Step 1 - Find the coordinates that the mask has a value different than 0
        # The result will be 2 array arr_x = [x1, x2, .. xn] & arr_y = [y1, y2, .., yn]
        # The arrays are matched like: (x1, y1), (x2, y2), .., (xn, yn)
        arr_y, arr_x = np_where(mask != 0)

        # Step 2 - Find the minima and the maxima of the 2 arrays
        y_min = np_amin(arr_y)
        y_max = np_amax(arr_y)
        x_min = np_amin(arr_x)
        x_max = np_amax(arr_x)
        return y_min, y_max, x_min, x_max

    # The images in the dataset that do not have a matching list of encoded pixels will be used as test samples
    def separate_train_test_from_csv(self, df):
        """
        :param df: dataframe from the initial-original csv with the dataset - Train & Test samples are mixed up
        :return: train_dataframe, test_dataframe
        """
        train_df = self.__get_dataframe_without_nan(df)
        test_df = self.__get_dataframe_with_nan_only(df)
        return train_df, test_df

    def masks_to_bboxes(self, df):
        pass

    def add_path_to_dataframe(self, directory: str, df: DataFrame):
        # Step 1 - get the list of the images' names
        images_names = df.loc[:, 'ImageId'].to_list()

        # Step 2 - create the path for every image'name --> The order of the arrays is the same
        paths = [os_path_join(directory, image_name) for image_name in images_names]
        df.insert(0, 'path', paths, allow_duplicates=True)
        return df

    # ref: https://www.kaggle.com/paulorzp/run-length-encode-and-decode
    def rle_decode(self, mask_string: str, shape=(768, 768)):
        '''
        mask_rle: run-length as string formated (start length)
        shape: (height,width) of array to return
        Returns numpy array, 1 - mask, 0 - background

        '''
        s = mask_string.split()
        starts, lengths = [np_asarray(x, dtype=int) for x in (s[0:][::2], s[1:][::2])]
        starts -= 1
        ends = starts + lengths
        img = np_zeros(shape[0] * shape[1], dtype=np_uint8)
        for lo, hi in zip(starts, ends):
            img[lo:hi] = 255
        return img.reshape(shape).T  # Needed to align to RLE direction

    # ref.: https://www.kaggle.com/stainsby/fast-tested-rle
    def rle_encode(self, img: np_ndarray):
        '''
        img: numpy array, 1 - mask, 0 - background
        Returns run length as string formated
        '''
        pixels = img.flatten()
        pixels = np_concatenate([[0], pixels, [0]])
        runs = np_where(pixels[1:] != pixels[:-1])[0] + 1
        runs[1::2] -= runs[::2]
        return ' '.join(str(x) for x in runs)

    def __get_dataframe_with_nan_only(self, df: DataFrame):
        """ These rows will represent the test samples """
        is_nan = df.isnull()
        row_has_nan = is_nan.any(axis=1)
        rows_with_nan = df[row_has_nan]

        return rows_with_nan

    def __get_dataframe_without_nan(self, df: DataFrame):
        return df.dropna(axis=0)
