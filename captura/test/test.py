from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QComboBox, QCheckBox, QLabel, QLineEdit, QVBoxLayout

import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
        self.label = QLabel("Click here")
        self.setCentralWidget(self.label)
        
    def mouseMoveEvent(self, e):
        self.label.setText("mouseMoveEvent")
    
    def mousePressEvent(self, e):
        self.label.setText("mousePressEvent")

    def mouseReleaseEvent(self, e):
        self.label.setText("mouseReleaseEvent")

    def mouseDoubleClickEvent(self, e):
        self.label.setText("mouseDoubleClickEvent")
        
app = QApplication(sys.argv)        
window = MainWindow()
window.show()




app.exec()