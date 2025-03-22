import logging
import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path

from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QDialogButtonBox,
    QVBoxLayout,
    QFileDialog,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
    QApplication,
    QMainWindow,
)

from captura.config import Config
from captura.template.renderer import render_all
from captura.ui.Line import QHLine
from captura.ui.config_widgets.LCheckbox import LCheckbox

logger = logging.getLogger(__name__)


class FinalizeRenderDialog(QDialog):
    def __init__(self, parent: QMainWindow, config: Config, values: dict):
        super().__init__(parent)
        self.parent = parent

        self.config = config
        self.values = values

        self.setWindowTitle("Template Erstellen")
        self.setWindowIcon(parent.windowIcon())

        font_bold_underline = QFont()
        font_bold_underline.setBold(True)
        font_bold_underline.setUnderline(True)

        # Dialog layout
        layout = QVBoxLayout()

        self.zip_checkbox = LCheckbox(
            {"label": "Als ZIP-Datei speichern?", "id": ""}, self.change_state, self
        )
        self.zip_checkbox_checked = False
        layout.addWidget(self.zip_checkbox)

        layout.addWidget(QHLine())

        self.path = QLineEdit(self)
        self.browse_button = QPushButton("Durchsuchen...")
        self.browse_button.clicked.connect(self.browse)
        self.save_widget = QWidget(self)
        self.save_layout = QHBoxLayout()
        self.save_layout.addWidget(QLabel("Datei speichern unter:"))
        self.save_layout.addWidget(self.path)
        self.save_layout.addWidget(self.browse_button)
        self.save_widget.setLayout(self.save_layout)
        layout.addWidget(self.save_widget)

        # Close button
        self.buttonbox = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        )
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)
        layout.addWidget(self.buttonbox)

        # Finalize layout
        self.setLayout(layout)

    def change_state(self, _: str, value: bool):
        self.zip_checkbox_checked = value

    def accept(self):
        logger.debug(f"Saving to file path: {self.path.text()}")

        if not self.path.text():
            QMessageBox.warning(
                self.parentWidget(), "Fehler", "Bitte wählen Sie einen Speicherort aus!"
            )
            return

        path = Path(self.path.text())

        with tempfile.TemporaryDirectory() as tmpdir:
            if self.zip_checkbox_checked:
                if self.config.single_file:
                    path = Path(tmpdir) / f"{path.name}.tex"
                else:
                    path = Path(tmpdir)

            try:
                render_all(path, self.config, self.values)
            except Exception as e:
                logger.exception(f"Failed to render template", exc_info=e)
                QMessageBox.warning(self.parentWidget(), "Fehler", str(e))
                super().reject()
                return

            if self.zip_checkbox_checked:
                with zipfile.ZipFile(Path(self.path.text()), "w") as zip_file:
                    for root, dirs, files in os.walk(tmpdir):
                        for file in files:
                            zip_file.write(os.path.join(root, file), file)

        super().accept()
        self.parent.close()

        QMessageBox.information(
            self.parentWidget(), "Fertig!", "Template erfolgreich erstellt!"
        )

        filepath = os.path.dirname(self.path.text())
        match sys.platform:
            case "Darwin":
                subprocess.call(("open", filepath))
            case "Windows":
                os.startfile(filepath)
            case _:
                subprocess.call(("xdg-open", filepath))

        QApplication.exit(0)

    def browse(self):
        if self.zip_checkbox_checked or self.config.single_file:
            filetype_filter = "Tex Dateien (*.tex);;Alle Dateien (*)"
            if self.zip_checkbox_checked:
                filetype_filter = "ZIP Dateien (*.zip);;Alle Dateien (*)"
            path = QFileDialog.getSaveFileName(
                self, "Datei Speichern unter...", filter=filetype_filter
            )[0]
        else:
            path = QFileDialog.getExistingDirectory(self, "Ordner Speichern unter...")
        if path:
            self.path.setText(path)
