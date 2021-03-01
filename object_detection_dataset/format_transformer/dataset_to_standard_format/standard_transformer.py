from abc import ABC, abstractmethod
from pandas import DataFrame


class StandardTransformer(ABC):
    standard_column_names = ['filename', 'frame', 'frame_name', 'class', 'xmin', 'ymin', 'xmax', 'ymax', 'width',
                             'height', 'depth']
    standard_df: DataFrame

    def get_all_columns(self):
        l1 = self.create_filename_column()
        l2 = self.create_frame_column()
        l3 = self.create_frame_name_column()
        l4 = self.create_class_column()
        l5, l6, l7, l8 = self.create_xy_columns()
        l9 = self.create_width_column()
        l10 = self.create_height_column()
        l11 = self.create_depth_column()

        return l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11

    def get_all_column_names(self):
        return self.standard_column_names

    @abstractmethod
    def create_filename_column(self):
        pass

    @abstractmethod
    def create_frame_column(self):
        pass

    @abstractmethod
    def create_frame_name_column(self):
        pass

    @abstractmethod
    def create_class_column(self):
        pass

    @abstractmethod
    def create_xy_columns(self):
        pass

    @abstractmethod
    def create_width_column(self):
        pass

    @abstractmethod
    def create_height_column(self):
        pass

    @abstractmethod
    def create_depth_column(self):
        pass
