import logging
import math

from PyQt6.QtGui import QResizeEvent
from PyQt6.QtWidgets import QWidget, QGridLayout, QMessageBox

from captura.template.library import get_library_templates
from captura.ui.TemplateDelegate import TemplateDelegate
from captura.util import import_new_template


class Homepage(QWidget):
    def __init__(self, parent: QWidget):
        super().__init__()

        self.parent = parent
        self.logger = logging.getLogger(__name__)
        self.layout = QGridLayout()

        # Library will be initialized in self.load_templates()
        self.library_templates = []
        self.library_templates_widgets = []
        self.templates_per_row = 0
        self.load_templates()

        if len(self.library_templates) == 0:
            dialog = QMessageBox.question(
                self.parent,
                "Leere Bibliothek",
                "Keine Vorlagen vorhanden. Möchten Sie eine importieren?",
                buttons=QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            )

            if dialog == QMessageBox.StandardButton.Yes:
                import_new_template(parent, self.reload, self.logger)

            return

        self.create_layout()

    def reload(self):
        self.load_templates()
        self.create_layout()

    def load_templates(self):
        self.library_templates = get_library_templates()
        self.library_templates_widgets = [
            TemplateDelegate(self.parent, config, lambda x: print(x))
            for config in self.library_templates
        ]
        self.templates_per_row = math.floor(
            self.size().width() / TemplateDelegate.WIDTH
        )

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
