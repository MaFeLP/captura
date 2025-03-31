"""Holds the main scroll area for the application.

This is the main scroll area for the application. It is used to hold the main widget of the application.

The main scroll area only has a vertical scroll bar and no horizontal scroll bar."""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QScrollArea, QWidget


class MainScrollArea(QScrollArea):
    def __init__(self, child: QWidget) -> None:
        """The main scroll area for the application.

        The scroll area resizes itself appropriately to the window size and only has a vertical scroll bar.

        :param child: The child widget to be displayed in the scroll area.
        """
        super().__init__()
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setWidgetResizable(True)
        self.setWidget(child)

    def resizeEvent(self, event: QResizeEvent) -> None:
        """The event that is called when the window is resized. This will update the layout of the templates to fit the new size

        :param event: Event properties
        """
        self.widget().resize(event.size().width(), event.size().height())
        event.accept()
