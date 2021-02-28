class AerialSample:
    filename: str
    width: 800
    height: 600
    class_: str
    xmin: int
    xmax: int
    ymin: int
    ymax: int

    def __init__(
            self,
            filename='',
            class_='',
            xmin=0,
            xmax=0,
            ymin=0,
            ymax=0
    ):
        self.filename = filename
        self.class_ = class_
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
