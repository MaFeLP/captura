import logging
from zipfile import ZipFile

from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QFileDialog, QWidget
from yaml import YAMLError

from captura.template.library import load_new_template
from captura.util import error_exit


class Homepage(QVBoxLayout):
    archive: None | ZipFile = None

    def __init__(self, parent: QWidget):
        super().__init__()

        self.parent = parent
        self.logger = logging.getLogger(__name__)

        self.select_file = QPushButton("Datei auswählen")
        self.select_file.clicked.connect(self.on_select_file)

        self.addWidget(self.select_file)

    def on_select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            filter="Captura Vorlagen (*.captura);; ZIP-Dateien (*.zip);; Alle Dateien (*)",
        )
        self.logger.debug("Opening file '%s'" % file_path)

        try:
            load_new_template(file_path)
        except KeyError as err:
            error_exit(
                self.parent, "Invalid template configuration", err, 1, self.logger
            )
        except YAMLError as err:
            error_exit(
                self.parent, "Error parsing the configuration", err, 2, self.logger
            )
        except ValueError as err:
            error_exit(
                self.parent, "Invalid template configuration", err, 1, self.logger
            )
