import logging
from typing import Callable

from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QWidget, QMessageBox, QFileDialog
from yaml import YAMLError

from captura.template.library import load_new_template


def error_exit(
    parent: QWidget, msg: str, e: Exception, exit_code: int, logger: logging.Logger
):
    logger.critical(msg, exc_info=e)
    QMessageBox.critical(parent, "Error", msg + f"\n\n{e}")
    QCoreApplication.exit(exit_code)


def import_new_template(
    parent: QWidget, reload_homepage: Callable[[], None], logger: logging.Logger
):
    file_path, _ = QFileDialog.getOpenFileName(
        filter="Captura Vorlagen (*.captura);; ZIP-Dateien (*.zip);; Alle Dateien (*)",
    )

    if not file_path:
        return

    logger.debug("Opening file '%s'" % file_path)

    try:
        load_new_template(file_path)
    except (KeyError, ValueError) as err:
        error_exit(parent, "Invalid template configuration", err, 1, logger)
    except YAMLError as err:
        error_exit(parent, "Error parsing the configuration", err, 2, logger)

    reload_homepage()
