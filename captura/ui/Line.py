"""Helper classes to create horizontal and vertical lines in a GUI."""

from PyQt6.QtWidgets import QFrame, QSizePolicy


class QHLine(QFrame):
    """a horizontal separation line"""

    def __init__(self) -> None:
        super().__init__()
        self.setMinimumWidth(1)
        self.setFixedHeight(20)
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)


class QVLine(QFrame):
    """a vertical separation line"""

    def __init__(self) -> None:
        super().__init__()
        self.setFixedWidth(20)
        self.setMinimumHeight(1)
        self.setFrameShape(QFrame.Shape.VLine)
        self.setFrameShadow(QFrame.Shadow.Sunken)
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
