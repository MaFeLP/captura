from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QScrollArea, QWidget


class MainScrollArea(QScrollArea):
    def __init__(self, child: QWidget):
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(child)

    def resizeEvent(self, event):
        self.widget().resize(event.size().width(), event.size().height())
        event.accept()
