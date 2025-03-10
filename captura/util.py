import logging

from PyQt6.QtCore import QCoreApplication
from PyQt6.QtWidgets import QWidget, QMessageBox


def error_exit(
        parent: QWidget, msg: str, e: Exception, exit_code: int, logger: logging.Logger
):
    logger.critical(msg, exc_info=e)
    QMessageBox.critical(parent, "Error", msg + f"\n\n{e}")
    QCoreApplication.exit(exit_code)
