import logging
import os

from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QMenuBar, QApplication, QWidget, QMessageBox

from captura.ui.dialog.AboutDialog import AboutDialog
from captura.util import import_new_template

logger = logging.getLogger(__name__)


class Menubar(QMenuBar):
    def __init__(self, parent: QWidget):
        super().__init__(parent)
        self.parent = parent

        self.__file_menu()
        self.__help_menu()

    def __help_menu(self):
        help_menu = self.addMenu("&Help")

        help_action = QAction(QIcon.fromTheme("help"), "&Help", self)
        help_action.setShortcut("F1")
        help_action.setStatusTip("Show help")
        help_action.triggered.connect(self.__not_implemented)
        help_menu.addAction(help_action)

        about_action = QAction(QIcon(f"{os.path.dirname(__file__)}/assets/logo_512x512.png"), "&About", self)
        about_action.setStatusTip("Über Captura")
        about_action.triggered.connect(lambda: AboutDialog(self.parent).show())
        help_menu.addAction(about_action)

    def __file_menu(self):
        file_menu = self.addMenu("&File")

        import_action = QAction(QIcon.fromTheme("document-import"), "Import", self)
        import_action.setShortcut("Ctrl+I")
        import_action.setStatusTip("Import a new template")
        import_action.triggered.connect(self.__import)
        file_menu.addAction(import_action)

        file_menu.addSeparator()

        exit_action = QAction(QIcon.fromTheme("application-exit"), "Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.setStatusTip("Exit application")
        exit_action.triggered.connect(self.__exit)
        file_menu.addAction(exit_action)

    def __exit(self):
        self.parent.close()
        QApplication.exit(0)

    def __import(self):
        import_new_template(self.parent, lambda: self.parent.homepage.reload(), logger)

    def __not_implemented(self):
        logger.warning("Not implemented")
        QMessageBox.warning(self, "Not implemented", "Not implemented")
