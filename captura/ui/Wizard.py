from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox

from captura.config import Config
from captura.ui.config_widgets.LCheckbox import LCheckbox


class Wizard(QWidget):
    def __init__(self, parent: QWidget, config: Config):
        super().__init__(parent)
        parent.setWindowTitle(f"Template: {config.name}")

        pagelayout = QVBoxLayout()
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        pagelayout.setContentsMargins(0, 0, 0, 0)
        pagelayout.setSpacing(10)

        self.checkbox1_state = False

        self.checkbox1 = LCheckbox("Titelseite")
        self.checkbox1.checkbox.stateChanged.connect(self.update_checkbox_state)
        pagelayout.addWidget(self.checkbox1, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.checkbox2 = LCheckbox("Inhaltsverzeichnis")
        pagelayout.addWidget(self.checkbox2, alignment=Qt.AlignmentFlag.AlignCenter)

        self.Combobox1 = QComboBox()
        self.Combobox1.addItems(
            ["2", "4", "6", "8", "10", "12", "14", "16", "18", "20", "22", "24"]
        )
        pagelayout.addWidget(self.Combobox1)

        self.setLayout(pagelayout)

    def update_checkbox_state(self, state):
        self.checkbox1_state = (
                state == Qt.CheckState.Checked.value
        )  # Convert state properly
        print(f"Updated state: {self.checkbox1_state}")  # Debug print
