from PyQt6.QtWidgets import QWidget, QLabel, QCheckBox, QHBoxLayout


class LCheckbox(QWidget):
    def __init__(self, label_text, parent=None):
        super().__init__(parent)

        self.checkbox = QCheckBox()
        self.label = QLabel(label_text)

        layout = QHBoxLayout()
        layout.addWidget(self.checkbox)
        layout.addWidget(self.label)

        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)
        self.setLayout(layout)
        self.layout().setContentsMargins(0, 0, 0, 0)
