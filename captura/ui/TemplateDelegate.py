"""Holds the TemplateDelegate class."""

import os
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPixmap, QEnterEvent
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QFrame, QApplication

from captura.config import Config


class TemplateDelegate(QFrame):
    # Preserve A4 Aspect Ratio for the preview image
    WIDTH = 180
    """Width of the template preview image. In combination with HEIGHT, this preserves the A4 aspect ratio."""
    HEIGHT = 300
    """Height of the template preview image. In combination with WIDTH, this preserves the A4 aspect ratio."""

    def __init__(
        self, parent: QWidget, config: Config, load_template: Callable[[Config], None]
    ) -> None:
        """Create a new widget to display information about a widget

        :param parent: The parent widget on which this widget is displayed
        :param config: The config that this widget should display
        :param load_template: The function that is called when the widget is clicked. Accepts a Config object as an argument, to start the wizard
        """
        super().__init__()
        self.parent = parent
        self.config = config
        self.load_template = load_template

        self.setFrameShape(QFrame.Shape.Box)
        self.setFrameShadow(QFrame.Shadow.Raised)

        layout = QVBoxLayout()

        pixmap = (
            QPixmap(str(config.get_directory() / "template.png"))
            if (config.get_directory() / "template.png").exists()
            else QPixmap(f"{os.path.dirname(__file__)}/assets/no_template_image.png")
        )
        widget = QLabel("Template Image")
        widget.setPixmap(pixmap)
        widget.setScaledContents(True)
        widget.setFixedSize(self.WIDTH - 17, self.HEIGHT - 70)
        self.setFixedSize(self.WIDTH, self.HEIGHT)

        layout.addWidget(widget)
        layout.addWidget(QLabel(config.name))
        layout.addWidget(QLabel(config.version))

        self.setLayout(layout)

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        """The element has been clicked.

        This function will call the load_template function with the config of this widget.

        :param event: The event that triggered this function
        """
        self.load_template(self.config)

    def enterEvent(self, event: QEnterEvent) -> None:
        """The mouse hovered over this element.

        This function will change the cursor to a pointing hand and modify the frame shadow to achieve a hover effect.

        :param event: The event that triggered this function
        """
        QApplication.setOverrideCursor(Qt.CursorShape.PointingHandCursor)
        self.setFrameShadow(QFrame.Shadow.Plain)

    def leaveEvent(self, _) -> None:
        """The mouse does not hover over this element anymore.

        This function will revert all the changes made in the enterEvent function.
        """
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        self.setFrameShadow(QFrame.Shadow.Raised)
