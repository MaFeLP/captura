from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QComboBox, QLabel, QLineEdit

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

        self.state = {}
        
        self.title_label = QLabel(config.name)
        self.title_label.setStyleSheet("font-size: 20px")
        pagelayout.addWidget(self.title_label)
        
        self.test_labellol = QLabel(config.sections[0]["fields"][0]["id"])
        pagelayout.addWidget(self.test_labellol)
  #      for section in config.sections:
   #         section_label = QLabel(section.name)
    #        pagelayout.addWidget(section_label)
#
 #           for field in section.fields:
  #              if field.type == "text":
   #                 field_widget = QLineEdit()
    #                field_widget.setPlaceholderText(field.label)
     #               field_widget.textChanged.connect(lambda text: self.state.__setitem__(field.id, text))
      #              pagelayout.addWidget(field_widget)        

        



        self.setLayout(pagelayout)
        


    def update_checkbox_state(self, state):
        self.checkbox1_state = (
                state == Qt.CheckState.Checked.value
        )  # Convert state properly
        print(f"Updated state: {self.checkbox1_state}")  # Debug print
