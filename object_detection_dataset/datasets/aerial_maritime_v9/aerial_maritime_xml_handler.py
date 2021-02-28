from object_detection_dataset.handlers.xml_handler import XML_Handler
from pandas import DataFrame
from object_detection_dataset.datasets.aerial_maritime_v9.task import Aerial_Maritime_Task_Definer
from object_detection_dataset.object import Object


class Aerial_Maritime_XML_Handler(XML_Handler):

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

        self.task_definer = Aerial_Maritime_Task_Definer()

    def df_to_pascal_voc_xml(self, df: DataFrame):

        # Initialize necessary variables
        objects = []
        i = 0
        # Get first row and its values
        row = df.iloc[i]
        image_name = row['filename']
        image_width = row['width']
        image_height = row['width']
        image_depth = 3
        name = row['class']
        object_ = Object(name, row['xmin'], row['xmax'], row['ymin'], row['ymax'])
        # Each row includes one object - add the row's object to the image's objects-list before creating the XML
        objects.append(object_)

        # Update the loop variables
        prev_image_name = image_name
        i += 1
        # Get the rows of the table
        n_rows = len(df.index)
        while i < n_rows:
            # Next row of data from CSV
            row = df.iloc[i]
            # Initialize necessary values
            image_name = row['filename']
            name = row['class']
            object_ = Object(name, row['xmin'], row['xmax'], row['ymin'], row['ymax'])

            if prev_image_name != image_name:
                self.save_to_pascal_voc_xml(
                    self.pascal_voc_xml_dir,
                    self.images_dir,
                    prev_image_name,
                    'Aerial Maritime v9',
                    (image_width, image_height, image_depth),
                    objects
                )
                objects = []
            objects.append(object_)
            prev_image_name = image_name
            i += 1

        # As the function is structured, for the last image an XML will not be created if we do not add another call
        # to save_to_pascal_voc_xml methods
        self.save_to_pascal_voc_xml(
            self.pascal_voc_xml_dir,
            self.images_dir,
            prev_image_name,
            'Aerial Maritime v9',
            (image_width, image_height, image_depth),
            objects
        )

    # This should have less code
    def df_to_pascal_voc_xml2(self, df: DataFrame):

        # Initialize necessary variables
        objects = []
        i = 0
        # Get first row and its values
        row = df.iloc[i]
        image_name = row['filename']
        image_width = row['width']
        image_height = row['width']
        image_depth = 3
        name = row['class']
        object_ = Object(name, row['xmin'], row['xmax'], row['ymin'], row['ymax'])
        # Each row includes one object - add the row's object to the image's objects-list before creating the XML
        objects.append(object_)

        # Update the loop variables
        prev_image_name = image_name
        i += 1
        # Get the rows of the table
        n_rows = len(df.index)
        while i < n_rows:
            # Next row of data from CSV
            row = df.iloc[i]
            # Initialize necessary values
            image_name = row['filename']
            name = row['class']
            object_ = Object(name, row['xmin'], row['xmax'], row['ymin'], row['ymax'])

            if prev_image_name != image_name:
                self.save_to_pascal_voc_xml(
                    self.pascal_voc_xml_dir,
                    self.images_dir,
                    prev_image_name,
                    'Aerial Maritime v9',
                    (image_width, image_height, image_depth),
                    objects
                )
                objects = []
            objects.append(object_)
            prev_image_name = image_name
            i += 1

        # As the function is structured, for the last image an XML will not be created if we do not add another call
        # to save_to_pascal_voc_xml methods
        self.save_to_pascal_voc_xml(
            self.pascal_voc_xml_dir,
            self.images_dir,
            prev_image_name,
            'Aerial Maritime v9',
            (image_width, image_height, image_depth),
            objects
        )

