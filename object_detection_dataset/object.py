class Object:
    name: str  # object class

    # parts of body of human that indicate a pose - each part has its own BB - it's probably the class-pose
    pose: str

    # Object extends beyond BB
    truncated: int  # -1 or 1
    # Difficult to recognize - Not scored in evaluation
    difficult: int  # -1 or 1. if 0 then "Object.name" should be blank

    # Object is significantly occluded within BB
    occluded: int  # -1 or 1

    # Bounding Box Coordinates
    xmin: int
    xmax: int
    ymin: int
    ymax: int

    def __init__(
            self,
            name: str,
            xmin: int,
            xmax: int,
            ymin: int,
            ymax: int,
            pose='Unspecified',
            truncated=-1,
            difficult=-1,
            occluded=-1
    ):
        self.name = name
        self.pose = pose
        self.truncated = truncated
        self.difficult = difficult
        self.occluded = occluded
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
