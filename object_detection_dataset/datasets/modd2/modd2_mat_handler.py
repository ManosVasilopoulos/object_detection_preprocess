from object_detection_dataset.handlers.mat_handler import MAT_Handler


class MODD2_MAT_Handler(MAT_Handler):
    mat_keys = [
        '__header__',
        '__version__',
        '__globals__',
        'annotations'
    ]

    def investigate(self, mat_dict=None):
        # Print __header__

        # Print __version__

        # Print __globals__

        # Print annotations
        data = mat_dict['annotations']
        inner_data = data[0, 0]
        print(inner_data.dtype)
        print(inner_data[0].shape, inner_data.dtype[0])
        print(inner_data[1].shape, inner_data.dtype[1])
