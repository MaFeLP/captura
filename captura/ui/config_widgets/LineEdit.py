from PyQt6.QtWidgets import QLineEdit
from typing import Callable

class LineEdit(QLineEdit):
    def __init__(self, field: dict, change_state: Callable[[str, str], None], parent=None):
        super().__init__(parent)
        
        self.id = field["id"]
        self.setPlaceholderText(field["label"])
        self.state = change_state
        
        self.textChanged.connect(self.on_text_changed)

    def on_text_changed(self, text: str):
        print(f"{self.id=}, {text=}")
        self.state(self.id, text)
