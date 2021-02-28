from object_detection_dataset.handlers.xml_handler import XML_Handler
from pandas import DataFrame
from object_detection_dataset.object import Object
from numpy import isnan as np_isnan


class Airbus_XML_Handler(XML_Handler):
    database_name = 'AirBus Ship Detection'

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def df_to_xml(self, df: DataFrame):
        database_name = 'AirBus Ship Detection'

        # Initialize necessary variables
        objects = []
        i = 0
        # Get first row and its values
        row = df.iloc[i]
        image_name = row['filename']
        image_width = 768
        image_height = 768
        image_depth = 3
        name = '_'

        object_ = Object(name, int(row['xmin']), int(row['xmax']), int(row['ymin']), int(row['ymax']))
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
            name = '_'
            object_ = Object(name, int(row['xmin']), int(row['xmax']), int(row['ymin']), int(row['ymax']))

            if prev_image_name != image_name:
                self.save_to_pascal_voc_xml(
                    self.pascal_voc_xml_dir,
                    self.images_dir,
                    prev_image_name,
                    database_name,
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
            image_name,
            database_name,
            (image_width, image_height, image_depth),
            objects
        )

    def df_to_pascal_voc_xml(self, df: DataFrame):

        # Initialize necessary variables
        objects = []
        i = 0
        # Get first row and its values
        row = df.iloc[i]
        image_name = row['filename']
        image_width = 768
        image_height = 768
        image_depth = 3
        name = ''
        if np_isnan(row['xmin']):
            object_ = Object(name, -1, -1, -1, -1)
        else:
            object_ = Object(name, int(row['xmin']), int(row['xmax']), int(row['ymin']), int(row['ymax']))
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
            name = ''
            if np_isnan(row['xmin']):
                object_ = Object(name, -1, -1, -1, -1)
            else:
                object_ = Object(name, int(row['xmin']), int(row['xmax']), int(row['ymin']), int(row['ymax']))

            if prev_image_name != image_name:
                self.save_to_pascal_voc_xml(
                    self.pascal_voc_xml_dir,
                    self.images_dir,
                    prev_image_name,
                    self.database_name,
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
            self.database_name,
            (image_width, image_height, image_depth),
            objects
        )
