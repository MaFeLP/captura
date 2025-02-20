from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QComboBox, QCheckBox

import sys

app = QApplication(sys.argv)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.button_is_checked = True
        self.setWindowTitle("My App")
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.when_button_clicked)
        self.button.clicked.connect(self.when_button_checked)
        
        self.button.setChecked(self.button_is_checked)
        
        self.setCentralWidget(self.button)
    
    def when_button_clicked(self):
        print("Clicked!")
    
    def when_button_checked(self, when_button_clicked):
        print('Checkstate:', when_button_clicked)

    
        
        
window = MainWindow()
window.show()



app.exec()