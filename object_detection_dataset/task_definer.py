from abc import ABC
from abc import abstractmethod

"""
This class must be inhereted by a Configuration class of a dataset.
"""


class TaskDefiner(ABC):
    dataset_tasks = {
        'object-detection_and_tracking': 0,
        'object-tracking': 0,
        'horizon-detection_and_tracking': 0,
        'classification': 0,
        'segmentation': 0
    }

    def __init__(self):
        self.define_task()

    @abstractmethod
    def define_task(self):
        pass
