import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QCheckBox


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")

        widget = QCheckBox()

        # For tristate: widget.setCheckState(Qt.CheckState.PartiallyChecked)
        # Or: widget.setTristate(True)
        widget.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget)

    def show_state(self, s):
        print(s == Qt.CheckState.Checked.value)
        print(s)
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()