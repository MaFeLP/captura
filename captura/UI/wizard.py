import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QFont
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QVBoxLayout, QCheckBox, QPushButton, QTextEdit, QComboBox, QSpacerItem
from custom_widgets import LCheckbox

app = QApplication(sys.argv)

default_font = QFont("Roboto", 20)
app.setFont(default_font)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Template: Test - editing")
        self.setFixedSize(QSize(600, 400))
        self.setStyleSheet("background-color: #0b8843;")
        
        pagelayout = QVBoxLayout()
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        pagelayout.setContentsMargins(0, 0, 0, 0)
        pagelayout.setSpacing(10)
        
        self.checkbox1_state = False
        
        self.checkbox1 = LCheckbox('Titelseite')
        self.checkbox1.checkbox.stateChanged.connect(self.update_checkbox_state)
        pagelayout.addWidget(self.checkbox1, alignment=Qt.AlignmentFlag.AlignHCenter)
        
        
        self.checkbox2 = LCheckbox('Inhaltsverzeichnis')
        pagelayout.addWidget(self.checkbox2, alignment=Qt.AlignmentFlag.AlignCenter)
        
        self.Combobox1 = QComboBox()
        self.Combobox1.addItems(['2', '4', '6', '8', '10', '12', '14', '16', '18', '20', '22', '24'])
        pagelayout.addWidget(self.Combobox1)
        
     
        
        dummy_widget = QWidget()
        dummy_widget.setLayout(pagelayout)
        self.setCentralWidget(dummy_widget)
    
    
    def update_checkbox_state(self, state):
        self.checkbox1_state = state == Qt.CheckState.Checked.value  # Convert state properly
        print(f"Updated state: {self.checkbox1_state}")  # Debug print
        
window = MainWindow()
window.show()
app.exec()