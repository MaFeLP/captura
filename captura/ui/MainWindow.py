import logging
from pathlib import Path

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QFileDialog, QApplication

from captura.config import Config
from captura.template.renderer import render_all
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
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        wizard = Wizard(self, config)
        self.scroll_area.setWidget(wizard)

    def goto_render(self, config):
        values = {
            "title": "Titel",
            "author": "Autor",
        }

        if config.single_file:
            path = QFileDialog.getSaveFileName(
                self, "Speichern unter...", filter="Tex Dateien"
            )
            if not path[0]:
                return
        else:
            path = QFileDialog.getExistingDirectory(self, "Speichern unter...")
            if not path:
                return
        render_all(Path(path), config, values)
