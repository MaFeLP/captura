import logging
import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QMainWindow, QApplication

from captura.config import Config
from captura.ui.Homepage import Homepage
from captura.ui.MainScrollArea import MainScrollArea
from captura.ui.Menubar import Menubar
from captura.ui.Wizard import Wizard
from captura.ui.dialog.FinalizeRenderDialog import FinalizeRenderDialog

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

        self.setWindowIcon(QIcon(f"{os.path.dirname(__file__)}/assets/logo_512x512.png"))

    def navigate_to_wizard(self, config: Config):
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        wizard = Wizard(self, config, self.goto_render)
        self.scroll_area.setWidget(wizard)

    def goto_render(self, config: Config, state: dict):
        dialog = FinalizeRenderDialog(self, config, state)
        dialog.show()
