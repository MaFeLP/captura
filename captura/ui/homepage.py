import logging

from PyQt6.QtWidgets import QFileDialog, QWidget, QGridLayout, QMessageBox
from yaml import YAMLError

from captura.template.library import load_new_template, get_library_templates
from captura.ui.template_delegate import TemplateDelegate
from captura.util import error_exit


class Homepage(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()

        self.parent = parent
        self.logger = logging.getLogger(__name__)
        self.layout = QGridLayout()
        # self.setMinimumSize(540, 640)
        library_templates = get_library_templates()

        if len(library_templates) == 0:
            dialog = QMessageBox.question(
                self.parent,
                "Leere Bibliothek",
                "Keine Vorlagen vorhanden. Möchten Sie eine importieren?",
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )

            if dialog == QMessageBox.StandardButton.Yes:
                self.on_select_file()

            return

        idx, idy = 0, 0
        for template in library_templates:
            self.layout.addWidget(
                TemplateDelegate(self.parent, template, lambda x: print(x)), idy, idx
            )
            idx += 1
            if idx >= 3:
                idx = 0
                idy += 1

        self.setLayout(self.layout)

    def on_select_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            filter="Captura Vorlagen (*.captura);; ZIP-Dateien (*.zip);; Alle Dateien (*)",
        )

        if not file_path:
            return

        self.logger.debug("Opening file '%s'" % file_path)

        try:
            load_new_template(file_path)
        except (KeyError, ValueError) as err:
            error_exit(
                self.parent, "Invalid template configuration", err, 1, self.logger
            )
        except YAMLError as err:
            error_exit(
                self.parent, "Error parsing the configuration", err, 2, self.logger
            )
