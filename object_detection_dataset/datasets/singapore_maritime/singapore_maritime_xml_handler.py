from object_detection_dataset.handlers.xml_handler import XML_Handler


class Singapore_XML_Handler(XML_Handler):

    def __init__(self, dataset_dir: str):
        super().__init__(dataset_dir)
