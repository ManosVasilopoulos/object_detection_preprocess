from detection_and_tracking.handlers.csv_handler import CSV_Handler
from pandas import DataFrame
from numpy import array as np_array


class Seagull_CSV_Handler(CSV_Handler):

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def get_group_by_frame_dataframe(self, df: DataFrame) -> DataFrame:

        transformed_data = []

        xmins = []
        ymins = []
        widths = []
        heights = []
        objects_ids = []

        prev_filename = ''
        prev_frame = ''
        prev_frame_name = ''
        i = 0
        for index, row in df.iterrows():
            filename = row['filename']
            frame = row['frame']
            xmin = row['xmin']
            ymin = row['ymin']
            width = row['width']
            height = row['height']
            object_id = row['object_id']
            frame_name = '{0:06}'.format(frame) + '_' + filename + '.jpg'

            if filename == prev_filename:
                if frame == prev_frame:
                    xmins.append(xmin)
                    ymins.append(ymin)
                    widths.append(width)
                    heights.append(height)
                    objects_ids.append(object_id)
                else:
                    transformed_data.append(
                        [prev_filename, prev_frame, xmins, ymins, widths, heights, objects_ids, prev_frame_name]
                    )
                    xmins = [xmin]
                    ymins = [ymin]
                    widths = [width]
                    heights = [height]
                    objects_ids = [object_id]
            else:
                if prev_filename != '':
                    transformed_data.append(
                        [prev_filename, prev_frame, xmins, ymins, widths, heights, objects_ids, prev_frame_name]
                    )
                xmins = [xmin]
                ymins = [ymin]
                widths = [width]
                heights = [height]
                objects_ids = [object_id]

            i += 1

            prev_filename = filename
            prev_frame = frame
            prev_frame_name = frame_name

        return DataFrame(np_array(transformed_data),
                         columns
                         =['filename', 'frame', 'xmin', 'ymin', 'width', 'height', 'object_id', 'frame_name'])

    # TODO: will need to be changed. This is a temp solution for a specific matter
    def add_img_dimension(self, df: DataFrame):
        img_widths = []
        img_heights = []
        img_depths = []
        for index, row in df.iterrows():
            if row['filename'] == '2015-04-22-16-05-15_jai_eo' or row['filename'] == '2015-04-23-14-09-25_jai_eo':
                img_widths.append(1024)
                img_heights.append(768)
            else:
                img_widths.append(1920)
                img_heights.append(1080)
            img_depths.append(3)

        df['image_width'] = img_widths

        df['image_height'] = img_heights

        df['image_depth'] = img_depths
        return df

    def add_frame_name(self, df: DataFrame):
        pass
