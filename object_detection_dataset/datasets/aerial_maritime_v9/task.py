from object_detection_dataset.task_definer import TaskDefiner


class AerialMaritimeTask(TaskDefiner):

    def define_task(self):
        self.dataset_tasks['object-detection_and_tracking'] = 1
        self.dataset_tasks['object-tracking'] = 0
        self.dataset_tasks['horizon-detection_and_tracking'] = 0
        self.dataset_tasks['classification'] = 1
        self.dataset_tasks['segmentation'] = 0
