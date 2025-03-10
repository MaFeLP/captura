from typing import Callable

from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel, QFrame

from captura.config import Config


class TemplateDelegate(QFrame):
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
        pixmap = QPixmap("captura/ui/img/no_template_image.png")
        widget = QLabel()
        widget.setPixmap(pixmap)
        widget.setScaledContents(True)
        widget.setFixedSize(150, 200)
        self.setFixedSize(180, 270)

        layout.addWidget(widget)
        layout.addWidget(QLabel(config.name))
        layout.addWidget(QLabel(config.version))

        self.setLayout(layout)

    def mouseReleaseEvent(self, event: QMouseEvent):
        self.load_template(self.config)
