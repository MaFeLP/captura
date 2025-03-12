import logging
import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from captura.ui.MainScrollArea import MainScrollArea
from captura.ui.homepage import Homepage


def scroll_area_resize_event(self, event):
    self.widget().resize(event.size().width(), event.size().height())
    logger.debug(
        f"Resizing scroll area to {event.size().width()}x{event.size().height()}"
    )
    event.accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Captura")
        self.setMinimumSize(600, 400)
        self.resize(800, 600)

        self.homepage = Homepage(self)
        self.scroll_area = MainScrollArea(self.homepage)
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
