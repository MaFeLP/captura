import logging
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QScrollArea

from captura.ui.homepage import Homepage


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Captura")
        self.setFixedSize(600, 400)

        self.scroll_area = QScrollArea()
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.homepage = Homepage(self)
        self.scroll_area.setWidget(self.homepage)

        self.setCentralWidget(self.scroll_area)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%dT%H:%M:%S",
        stream=sys.stdout,
        level="DEBUG",
    )

    logger = logging.getLogger(__name__)
    logger.info("Starting Captura version %s" % "v0.0.1")

    main_window = MainWindow()
    main_window.show()

    try:
        app.exec()
    except Exception as e:
        logger.critical("An unexpected error occurred", exc_info=e)
