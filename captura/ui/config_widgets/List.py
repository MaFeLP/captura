from PyQt6.QtWidgets import (
    QWidget,
    QLineEdit,
    QPushButton,
    QLabel,
    QVBoxLayout,
    QHBoxLayout,
)
from typing import Callable
from captura.ui.config_widgets.LineEdit import LineEdit


class List(QWidget):
    def __init__(
        self, field: dict, change_state: Callable[[str, list], None], parent=None
    ):
        super().__init__(parent)

        self.id = field["id"]
        self.change_state = change_state
        self.state = [""]

        self.label = QLabel(field["label"])
        self.lineedit = LineEdit(field, self.change_state, self)
        self.button = QPushButton("+")
        self.button.clicked.connect(self.add_item)
        self.lineedit.textChanged.connect(self.on_text_changed)

        self.widgetlayout = QVBoxLayout()
        self.widgetlayout.addWidget(self.label)
        self.widgetlayout.addWidget(self.button)
        self.widgetlayout.addWidget(self.lineedit)

        self.setLayout(self.widgetlayout)

    def update_state(self, index: int, value: str):
        self.state[index] = value
        self.change_state(self.id, self.state)

    def add_item(self):
        self.state.append("")
        field = {"id": len(self.state) - 1, "label": ""}
        self.widgetlayout.addWidget(LineEdit(field, self.update_state, self))

    def on_text_changed(self, text: str):
        self.update_state(0, text)
