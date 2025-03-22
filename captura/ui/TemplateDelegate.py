import os
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QMouseEvent, QPixmap, QEnterEvent
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QFrame, QApplication

from captura.config import Config


class TemplateDelegate(QFrame):
    # Preserve A4 Aspect Ratio for the preview image
    WIDTH = 180
    HEIGHT = 300

    def __init__(
        self, parent: QWidget, config: Config, load_template: Callable[[Config], None]
    ):
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

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.load_template(self.config)

    def enterEvent(self, event: QEnterEvent):
        QApplication.setOverrideCursor(Qt.CursorShape.PointingHandCursor)
        self.setFrameShadow(QFrame.Shadow.Plain)

    def leaveEvent(self, _):
        QApplication.setOverrideCursor(Qt.CursorShape.ArrowCursor)
        self.setFrameShadow(QFrame.Shadow.Raised)
