import logging

from PyQt6.QtWidgets import QMainWindow, QWidget

from captura.ui.MainScrollArea import MainScrollArea
from captura.ui.Menubar import Menubar
from captura.ui.homepage import Homepage

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Captura")
        self.setMinimumSize(600, 400)
        self.resize(800, 600)

        self.homepage = Homepage(self)
        self.scroll_area = MainScrollArea(self.homepage)
        self.setCentralWidget(self.scroll_area)

        self.setMenuBar(Menubar(self))

    def navigate(self, page: QWidget):
        self.scroll_area.setWidget(page)
