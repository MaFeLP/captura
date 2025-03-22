import logging

from PyQt6.QtWidgets import QMainWindow

from captura.config import Config
from captura.ui.Homepage import Homepage
from captura.ui.MainScrollArea import MainScrollArea
from captura.ui.Menubar import Menubar
from captura.ui.Wizard import Wizard

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Captura")
        self.setMinimumSize(600, 400)
        self.resize(800, 600)

        self.homepage = Homepage(self, self.navigate_to_wizard)
        self.scroll_area = MainScrollArea(self.homepage)
        self.setCentralWidget(self.scroll_area)

        self.setMenuBar(Menubar(self))

    def navigate_to_wizard(self, config: Config):
        wizard = Wizard(self, config)
        self.scroll_area.setWidget(wizard)
