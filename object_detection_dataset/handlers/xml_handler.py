from object_detection_dataset.outputs_handler import Outputs_Handler
from pandas import DataFrame
from glob import glob as glob_glob
from os import listdir as os_listdir
from os.path import join as os_path_join
import xml.etree.ElementTree as ET
from object_detection_dataset.task_definer import TaskDefiner

"""
if task is object detection_and_tracking ==> object-dection = 1 else 0
if task is object tracking ==> object-tracking = 1 else 0
if task is horizon detection_and_tracking ==> horizon-detection_and_tracking = 1 else 0
if task includes classification ==> classification = 1 else 0

The new xml will be the standard for all the datasets.
It will include names that are not related to their tasks.
These names will have values -1.
For example:
- if <object-detection_and_tracking>1</object-detection_and_tracking> then <frame>-1</frame>
"""


class XML_Handler(Outputs_Handler):

    def __init__(self, dataset_dir: str, xml_subfolder_path=''):
        super().__init__(dataset_dir)

        if xml_subfolder_path != '':
            self.xml_subfolder_path = xml_subfolder_path
        else:
            self.xml_subfolder_path = os_path_join('outputs', 'standard_format')

        self.xml_dir = os_path_join(dataset_dir, self.xml_subfolder_path)
        self.images_dir = os_path_join(dataset_dir, 'inputs', 'images')

    def read_xml(self):
        pass

    def get_xml_path_list(self, directory):
        return [x for x in glob_glob(directory + '/*.xml')]

    def get_xml_list(self, directory: str) -> list:
        return [x for x in os_listdir(directory) if x.endswith('.xml')]

    # This is not the universal format anymore - SEE format_transformer/standard.csv
    def save_to_universal_xml(
            self,
            xml_dir: str,
            task_definer: TaskDefiner,
            img_folder: str,
            img_name: str,
            frame_number: int,
            video_name: str,
            database: str,
            img_shape: tuple,
            objects: list,
            horizon_points: list
    ):
        # <annotation>..</annotation>
        root = ET.Element('annotation')
        root.text = '\n\t'

        # <object_detection>..</object_detection>
        subelem = ET.SubElement(root, 'object-detection_and_tracking')
        subelem.text = str(task_definer.dataset_tasks['object-detection_and_tracking'])
        subelem.tail = '\n\t'

        # <horizon_detection>..</horizon_detection>
        subelem = ET.SubElement(root, 'horizon-detection_and_tracking')
        subelem.text = str(task_definer.dataset_tasks['horizon-detection_and_tracking'])
        subelem.tail = '\n\t'

        # <object_tracking>..</object_tracking>
        subelem = ET.SubElement(root, 'object-tracking')
        subelem.text = str(task_definer.dataset_tasks['object-tracking'])
        subelem.tail = '\n\t'

        # <classification>..</classification>
        subelem = ET.SubElement(root, 'classification')
        subelem.text = str(task_definer.dataset_tasks['classification'])
        subelem.tail = '\n\t'

        # <segmentation>..</segmentation>
        subelem = ET.SubElement(root, 'segmentation')
        subelem.text = str(task_definer.dataset_tasks['segmentation'])
        subelem.tail = '\n\t'

        # <folder>..</folder>
        subelem = ET.SubElement(root, 'folder')
        subelem.text = img_folder
        subelem.tail = '\n\t'

        # <filename>..</filename>
        subelem = ET.SubElement(root, 'filename')
        subelem.text = img_name
        subelem.tail = '\n\t'

        # <path>..</path>
        subelem = ET.SubElement(root, 'path')
        subelem.text = os_path_join(img_folder, img_name)
        subelem.tail = '\n\t'

        # <frame>..</frame>
        subelem = ET.SubElement(root, 'frame')
        subelem.text = str(frame_number)
        subelem.tail = '\n\t'

        # <video>..</video>
        subelem = ET.SubElement(root, 'video')
        subelem.text = str(video_name)
        subelem.tail = '\n\t'

        # <source>..</source>
        elem = ET.Element('source')
        root.append(elem)
        elem.text = '\n\t\t'
        elem.tail = '\n\t'

        subelem = ET.SubElement(elem, 'database')
        subelem.text = database
        subelem.tail = '\n\t'

        # <size>..</size>
        elem = ET.Element('size')
        root.append(elem)
        elem.text = '\n\t\t'
        elem.tail = '\n\t'

        subelem = ET.SubElement(elem, 'width')
        subelem.text = str(img_shape[0])
        subelem.tail = '\n\t\t'

        subelem = ET.SubElement(elem, 'height')
        subelem.text = str(img_shape[1])
        subelem.tail = '\n\t\t'

        subelem = ET.SubElement(elem, 'depth')
        subelem.text = str(img_shape[2])
        subelem.tail = '\n\t'

        # <segmented>..</segmented>
        subelem = ET.SubElement(root, 'segmented')
        subelem.text = '_'
        subelem.tail = '\n\t'

        # <objects>..</objects>
        for object_ in objects:
            elem = ET.Element('object')
            root.append(elem)
            elem.text = '\n\t\t'
            elem.tail = '\n'

            subelem = ET.SubElement(elem, 'name')
            subelem.text = object_.name
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'pose')
            subelem.text = object_.pose
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'truncated')
            subelem.text = str(object_.truncated)
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'difficult')
            subelem.text = str(object_.difficult)
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'occluded')
            subelem.text = str(object_.occluded)
            subelem.tail = '\n\t\t'

            """ Bounding Box of 1 object """
            subelem = ET.Element('bndbox')
            elem.append(subelem)
            subelem.text = '\n\t\t\t'
            subelem.tail = '\n\t'

            subsubelem = ET.SubElement(subelem, 'xmin')
            subsubelem.text = object_.xmin
            subsubelem.tail = '\n\t\t\t'
            subsubelem = ET.SubElement(subelem, 'xmax')
            subsubelem.text = object_.xmax
            subsubelem.tail = '\n\t\t\t'

            subsubelem = ET.SubElement(subelem, 'ymin')
            subsubelem.text = object_.ymin
            subsubelem.tail = '\n\t\t\t'
            subsubelem = ET.SubElement(subelem, 'ymax')
            subsubelem.text = object_.ymax
            subsubelem.tail = '\n\t\t'

        # <horizon>..</horizon>
        elem = ET.Element('horizon')
        root.append(elem)
        elem.text = '\n\t\t'
        elem.tail = '\n'

        for point in horizon_points:
            subelem = ET.SubElement(elem, 'point')
            subelem.text = '\n\t\t\t'
            subelem.tail = '\n'

            subsubelem = ET.SubElement(subelem, 'x')
            subsubelem.text = str(point.x)
            subsubelem.tail = '\n\t\t\t'

            subsubelem = ET.SubElement(subelem, 'y')
            subsubelem.text = str(point.y)
            subsubelem.tail = '\n\t\t\t'

        # Save xml on the folder specified
        save_path_file = os_path_join(xml_dir, img_name.replace('.jpg', '.xml'))
        tree = ET.ElementTree(root)
        with open(save_path_file, "wb") as f:
            tree.write(f)

    def save_to_pascal_voc_xml(
            self,
            xml_dir: str,
            img_folder: str,
            img_name: str,
            database: str,
            img_shape: tuple,
            objects: list
    ):
        # <annotation>..</annotation>
        root = ET.Element('annotation')
        root.text = '\n\t'

        # <folder>..</folder>
        subelem = ET.SubElement(root, 'folder')
        subelem.text = img_folder
        subelem.tail = '\n\t'

        # <filename>..</filename>
        subelem = ET.SubElement(root, 'filename')
        subelem.text = img_name
        subelem.tail = '\n\t'

        # <path>..</path>
        subelem = ET.SubElement(root, 'path')
        subelem.text = os_path_join(img_folder, img_name)
        subelem.tail = '\n\t'

        # <source>..</source>
        elem = ET.Element('source')
        root.append(elem)
        elem.text = '\n\t\t'
        elem.tail = '\n\t'

        subelem = ET.SubElement(elem, 'database')
        subelem.text = database
        subelem.tail = '\n\t'

        # <size>..</size>
        elem = ET.Element('size')
        root.append(elem)
        elem.text = '\n\t\t'
        elem.tail = '\n\t'

        subelem = ET.SubElement(elem, 'width')
        subelem.text = str(img_shape[0])
        subelem.tail = '\n\t\t'

        subelem = ET.SubElement(elem, 'height')
        subelem.text = str(img_shape[1])
        subelem.tail = '\n\t\t'

        subelem = ET.SubElement(elem, 'depth')
        subelem.text = str(img_shape[2])
        subelem.tail = '\n\t'

        # <segmented>..</segmented>
        subelem = ET.SubElement(root, 'segmented')
        subelem.text = '_'
        subelem.tail = '\n\t'

        # <objects>..</objects>
        for i, object_ in enumerate(objects):
            elem = ET.Element('object')
            root.append(elem)
            elem.text = '\n\t\t'
            if i == len(objects) - 1:
                elem.tail = '\n'
            else:
                elem.tail = '\n\t'

            subelem = ET.SubElement(elem, 'name')
            subelem.text = object_.name
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'pose')
            subelem.text = object_.pose
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'truncated')
            subelem.text = str(object_.truncated)
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'difficult')
            subelem.text = str(object_.difficult)
            subelem.tail = '\n\t\t'

            subelem = ET.SubElement(elem, 'occluded')
            subelem.text = str(object_.occluded)
            subelem.tail = '\n\t\t'

            """ Bounding Box of 1 object """
            subelem = ET.Element('bndbox')
            elem.append(subelem)
            subelem.text = '\n\t\t\t'
            subelem.tail = '\n\t'

            subsubelem = ET.SubElement(subelem, 'xmin')
            subsubelem.text = str(object_.xmin)
            subsubelem.tail = '\n\t\t\t'

            subsubelem = ET.SubElement(subelem, 'xmax')
            subsubelem.text = str(object_.xmax)
            subsubelem.tail = '\n\t\t\t'

            subsubelem = ET.SubElement(subelem, 'ymin')
            subsubelem.text = str(object_.ymin)
            subsubelem.tail = '\n\t\t\t'

            subsubelem = ET.SubElement(subelem, 'ymax')
            subsubelem.text = str(object_.ymax)
            subsubelem.tail = '\n\t\t'

        # Save xml on the folder specified
        save_path_file = os_path_join(xml_dir, img_name.replace('.jpg', '.xml'))
        tree = ET.ElementTree(root)
        with open(save_path_file, "wb") as f:
            tree.write(f)

    @staticmethod
    def xml_list_to_dataframe(directory: str) -> DataFrame:
        """
            xml_to_dataframe --> DataFrame
            path: path for the XML file that contains the dataset --> proper structure of XML is that of "LabelImg"
        """
        xml_list = []
        for xml_file in glob_glob(directory + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                value = (root.find('filename').text,
                         int(root.find('size')[0].text),
                         int(root.find('size')[1].text),
                         member[0].text,
                         int(member[4][0].text),
                         int(member[4][1].text),
                         int(member[4][2].text),
                         int(member[4][3].text)
                         )
                xml_list.append(value)
        column_name = ['filename', 'width', 'height',
                       'class', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = DataFrame(xml_list, columns=column_name)
        return xml_df

    def standard_xml_list_to_dataframe(self, directory: str) -> DataFrame:
        """
            xml_to_dataframe --> DataFrame
            path: path for the XML file that contains the dataset --> proper structure of XML is that of "LabelImg"
        """
        xml_list = []
        for xml_file in glob_glob(directory + '/*.xml'):
            tree = ET.parse(xml_file)
            root = tree.getroot()
            for member in root.findall('object'):
                bndbox = member.find('bndbox')
                value = (
                    root.find('folder').text,
                    root.find('filename').text,
                    int(root.find('size')[0].text),
                    int(root.find('size')[1].text),
                    member.find('name').text,
                    int(bndbox.find('xmin').text),
                    int(bndbox.find('ymin').text),
                    int(bndbox.find('xmax').text),
                    int(bndbox.find('ymax').text)
                )
                xml_list.append(value)
        column_name = ['folder', 'filename', 'width', 'height', 'class-name', 'xmin', 'ymin', 'xmax', 'ymax']
        xml_df = DataFrame(xml_list, columns=column_name)
        return xml_df
