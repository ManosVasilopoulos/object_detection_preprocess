from object_detection_dataset.task_definer import TaskDefiner


class Singapore_DatasetTaskDefiner(TaskDefiner):

    def define_task(self):
        self.dataset_tasks['object-detection_and_tracking'] = 1
        self.dataset_tasks['object-tracking'] = 1
        self.dataset_tasks['horizon-detection_and_tracking'] = 1
        self.dataset_tasks['classification'] = 0
        self.dataset_tasks['segmentation'] = 0
