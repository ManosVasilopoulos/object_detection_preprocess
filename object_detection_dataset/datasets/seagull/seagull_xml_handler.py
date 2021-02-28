from object_detection_dataset.handlers.xml_handler import XML_Handler
from object_detection_dataset.object import Object


class Seagull_XML_Handler(XML_Handler):

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)

    def row_to_xml(self, row, img_folder, img_width=1920, img_height=1080, img_depth=3):
        # Extract the data from DataFrame's row
        filename = row['filename']
        frame = row['frame']
        frame_name = row['frame_name']

        xmins = eval(row['xmin'])
        ymins = eval(row['ymin'])
        xmaxs = [xmins[i] + x for i, x in enumerate(eval(row['width']))]
        ymaxs = [ymins[i] + x for i, x in enumerate(eval(row['height']))]

        objects_ids = eval(row['object_id'])

        # Create an objects list
        objects = []
        for i in range(len(xmins)):
            objects.append(
                Object(
                    objects_ids[i],
                    xmins[i],
                    xmaxs[i],
                    ymins[i],
                    ymaxs[i]
                )
            )

        self.save_to_pascal_voc_xml(img_folder, img_folder, frame_name, 'Seagull', (img_width,img_height, img_depth), objects)
