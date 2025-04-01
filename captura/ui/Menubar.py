"""Holds the Menubar of the application."""

import logging

from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QAction, QIcon, QDesktopServices
from PyQt6.QtWidgets import QMenuBar, QApplication, QMessageBox, QMainWindow

from captura.ui.dialog.AboutDialog import AboutDialog
from captura.util import import_new_template

logger = logging.getLogger(__name__)


class Menubar(QMenuBar):
    def __init__(self, parent: QMainWindow) -> None:
        """The Menubar of the application.

        :param parent: The parent widget of the menubar, should the main window.
        """
        super().__init__(parent)
        self.parent = parent

        self.__file_menu()
        self.__help_menu()

    def __help_menu(self) -> None:
        """A helper function to create the help menu and add it to the menubar."""
        help_menu = self.addMenu("&Help")

        help_action = QAction(QIcon.fromTheme("help"), "&Help", self)
        help_action.setShortcut("F1")
        help_action.setStatusTip("Show help")
        help_action.triggered.connect(
            lambda: QDesktopServices.openUrl(
                QUrl("https://mafelp.github.io/captura/user/")
            )
        )
        help_menu.addAction(help_action)

        about_action = QAction("&About", self)
        about_action.setStatusTip("Über Captura")
        about_action.triggered.connect(lambda: AboutDialog(self.parent).show())
        help_menu.addAction(about_action)

    def __file_menu(self) -> None:
        """A helper function to create the file menu and add it to the menubar."""
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

    def __exit(self) -> None:
        """A helper function to close the application."""
        self.parent.close()
        QApplication.exit(0)

    def __import(self) -> None:
        """A helper function to import a new template."""
        import_new_template(self.parent, lambda: self.parent.homepage.reload(), logger)

    def __not_implemented(self) -> None:
        """A helper function to show a message box when a feature is not yet implemented."""
        logger.warning("Not implemented")
        QMessageBox.warning(self, "Not implemented", "Not implemented")
