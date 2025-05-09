"""Holds the wizard page for the template configuration."""

import logging
from typing import Callable

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton

from captura.config import Config
from captura.ui.Line import QHLine
from captura.ui.config_widgets.LCheckbox import LCheckbox
from captura.ui.config_widgets.LineEdit import LineEdit
from captura.ui.config_widgets.List import List

logger = logging.getLogger(__name__)


class Wizard(QWidget):
    def __init__(
        self,
        parent: QWidget,
        config: Config,
        goto_render: Callable[[Config, dict], None],
    ) -> None:
        """Creates a new wizard page from a configuration

        :param parent: The parent in which the widget will be created
        :param config: The configuration that the wizard should fill out
        :param goto_render: The function that will be called when the wizard is finished
        """
        super().__init__(parent)
        parent.setWindowTitle(f"Template: {config.name}")
        self.config = config
        self.goto_render = goto_render

        pagelayout = QVBoxLayout()
        pagelayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        pagelayout.setContentsMargins(0, 0, 0, 0)
        pagelayout.setSpacing(10)

        self.state = {}

        self.title_label = QLabel(config.name)
        self.title_label.setStyleSheet("font-size: 20px")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pagelayout.addWidget(self.title_label)

        for section in config.sections:
            section_label = QLabel(section["name"])
            section_label.setStyleSheet("font-size: 16px")
            pagelayout.addWidget(section_label)

            for field in section["fields"]:
                if field["type"] == "text":
                    field_widget = LineEdit(field, self.change_state, self)
                    pagelayout.addWidget(field_widget)

                elif field["type"] == "checkbox":
                    field_widget = LCheckbox(field, self.change_state, self)
                    pagelayout.addWidget(field_widget)

                elif field["type"] == "list":
                    field_widget = List(field, self.change_state, self)
                    pagelayout.addWidget(field_widget)

        pagelayout.addStretch()

        next_button = QPushButton("Next")
        next_button.clicked.connect(self.next_page)
        pagelayout.addWidget(QHLine())
        pagelayout.addWidget(next_button)

        self.setLayout(pagelayout)

    def change_state(self, id: str, value: any) -> None:
        """Changes the state of the wizard. This is called when a field is changed.

        :param id: The id of the field that was changed. The id is the key in the config dictionary and can later be used in the template to access the value.
        :param value: The new value of the field.
        """
        self.state[id] = value
        logger.debug(f"Updated wizard state: {self.state=}")

    def next_page(self) -> None:
        """The function that is called when the next button is pressed, aka. the user is done"""
        logger.debug("Wizard finished")
        self.goto_render(self.config, self.state)
