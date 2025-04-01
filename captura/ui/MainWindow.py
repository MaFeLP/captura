"""Holds the main window of the application."""

import logging

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QApplication

from captura.config import Config
from captura.ui.Homepage import Homepage
from captura.ui.MainScrollArea import MainScrollArea
from captura.ui.Menubar import Menubar
from captura.ui.Wizard import Wizard
from captura.ui.dialog.FinalizeRenderDialog import FinalizeRenderDialog

logger = logging.getLogger(__name__)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """The Main Window of the application.

        This is the main window of the application. It holds the homepage or the wizard and the menubar.
        """
        super().__init__()

        self.setWindowTitle("Captura")
        self.setMinimumSize(600, 400)
        self.resize(800, 600)

        self.homepage = Homepage(self, self.navigate_to_wizard)
        self.scroll_area = MainScrollArea(self.homepage)
        self.setCentralWidget(self.scroll_area)

        self.setMenuBar(Menubar(self))

    def navigate_to_wizard(self, config: Config) -> None:
        """A function that handles navigation to the wizard.

        It is connected as a signal to the different templates in the homepage.

        :param config: The config that will be used to render the wizard and the template.
        """
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        wizard = Wizard(self, config, self.goto_render)
        self.scroll_area.setWidget(wizard)

    def goto_render(self, config: Config, state: dict) -> None:
        """The function that is called, when the user has completed a wizard

        :param config: The config that was used to display the wizard.
        :param state: The state of the wizard. It holds the information that is needed to render the template.
        """
        dialog = FinalizeRenderDialog(self, config, state)
        dialog.show()
