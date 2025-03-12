import logging
import math

from PyQt6.QtGui import QResizeEvent
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
        self.library_templates = get_library_templates()
        self.library_templates_widgets = [
            TemplateDelegate(parent, config, lambda x: print(x))
            for config in self.library_templates
        ]
        self.templates_per_row = math.floor(
            self.size().width() / TemplateDelegate.WIDTH
        )

        if len(self.library_templates) == 0:
            dialog = QMessageBox.question(
                self.parent,
                "Leere Bibliothek",
                "Keine Vorlagen vorhanden. Möchten Sie eine importieren?",
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )

            if dialog == QMessageBox.StandardButton.Yes:
                self.on_select_file()

            return

        self.create_layout()

    def create_layout(self, templates_per_row: int = 3):
        idx, idy = 0, 0
        for template in self.library_templates_widgets:
            self.layout.removeWidget(template)
            self.layout.addWidget(template, idy, idx)
            idx += 1
            if idx >= templates_per_row:
                idx = 0
                idy += 1

        self.setLayout(self.layout)

    def resizeEvent(self, event: QResizeEvent):
        templates_per_row = math.floor(event.size().width() / TemplateDelegate.WIDTH)

        if self.templates_per_row == templates_per_row:
            event.accept()
            return

        self.create_layout(templates_per_row)
        self.templates_per_row = templates_per_row
        event.accept()

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
