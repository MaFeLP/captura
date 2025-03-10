import logging
from zipfile import ZipFile

from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QFileDialog, QWidget
from yaml import YAMLError, safe_load

from captura import config
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
            self.archive = ZipFile(file_path, "r")
            config_string = self.archive.read("config.yml")
            yaml_config = safe_load(config_string)
            self.logger.debug("Loaded template configuration")
            config.validate(yaml_config)
            self.logger.debug("Found configuration %s" % config_string)
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
                self.parent, "Invalid template configuration", err, 3, self.logger
            )
