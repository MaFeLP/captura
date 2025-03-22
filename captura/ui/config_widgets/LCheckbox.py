from PyQt6.QtWidgets import QWidget, QLabel, QCheckBox, QHBoxLayout
from typing import Callable

class LCheckbox(QWidget):
    def __init__(self, field: dict, change_state: Callable[[str, bool], None], parent=None):
        super().__init__(parent)
        
        self.id = field["id"]
        self.change_state = change_state

        self.checkbox = QCheckBox()
        self.label = QLabel(field["label"])
        self.checkbox.stateChanged.connect(self.on_clicked)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.checkbox)
        

        
        layout.addSpacing(600)
        self.setLayout(layout)

    def on_clicked(self, state: bool):
        if state == 0:
            self.change_state(self.id, False)
        else:
            self.change_state(self.id, True)
