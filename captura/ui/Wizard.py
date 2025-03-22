from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QLineEdit

from captura.config import Config
from captura.ui.config_widgets.LCheckbox import LCheckbox
from captura.ui.config_widgets.LineEdit import LineEdit
from captura.ui.config_widgets.List import List


class Wizard(QWidget):
    def __init__(self, parent: QWidget, config: Config):
        super().__init__(parent)
        parent.setWindowTitle(f"Template: {config.name}")

        pagelayout = QVBoxLayout()
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        pagelayout.setContentsMargins(0, 0, 0, 0)
        pagelayout.setSpacing(10)

        self.state = {}

        self.title_label = QLabel(config.name)
        self.title_label.setStyleSheet("font-size: 20px")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(self.title_label)

        for section in config.sections:
            section_label = QLabel(section["name"])
            section_label.setStyleSheet("font-size: 16px")
            pagelayout.addWidget(section_label)

            for field in section["fields"]:
                if field["type"] == "text":
                    field_widget = LineEdit(field, self.change_state, self)
                    pagelayout.addWidget(field_widget)

                elif field["type"] == "checkbox":
                    field_widget = LCheckbox(field, self.change_state, self)
                    pagelayout.addWidget(field_widget)

                elif field["type"] == "list":
                    field_widget = List(field, self.change_state, self)
                    pagelayout.addWidget(field_widget)

        self.setLayout(pagelayout)

    def change_state(self, id: str, value: any):
        self.state[id] = value
        print(self.state)
