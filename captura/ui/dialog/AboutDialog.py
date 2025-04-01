import os
import sys

import jinja2
import yaml
from PyQt6.QtCore import PYQT_VERSION_STR, QT_VERSION_STR, Qt
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtWidgets import (
    QDialog,
    QWidget,
    QDialogButtonBox,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QApplication,
    QHBoxLayout,
)

from captura.ui.Line import QHLine


class AboutDialog(QDialog):
    def __init__(self, parent: QWidget):
        super().__init__(parent)

        self.setWindowTitle("Über Captura")
        self.setWindowIcon(parent.windowIcon())

        font_bold_underline = QFont()
        font_bold_underline.setBold(True)
        font_bold_underline.setUnderline(True)

        # Dialog layout
        layout = QVBoxLayout()

        # Logo and self
        title = QLabel("Captura")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Arial", 24))
        app_logo = QLabel()
        app_pixmap = QPixmap(
            f"{os.path.dirname(__file__)}/../assets/logo_512x512.png"
        ).scaled(
            64,
            64,
            Qt.AspectRatioMode.KeepAspectRatio,
            Qt.TransformationMode.SmoothTransformation,
        )
        app_logo.setPixmap(app_pixmap)
        name_layout = QHBoxLayout()
        name_layout.addWidget(app_logo)
        name_layout.addWidget(title)
        name_layout.addStretch(0)
        name_widget = QWidget(self)
        name_widget.setLayout(name_layout)
        layout.addWidget(name_widget)

        # Application information
        layout.addWidget(QLabel(f"Captura ({QApplication.applicationVersion()})"))
        app_homepage = QLabel(
            'Homepage: <a href="https://github.com/MaFeLP/captura/">https://github.com/MaFeLP/captura/</a>'
        )
        app_homepage.setOpenExternalLinks(True)
        layout.addWidget(app_homepage)
        app_issues = QLabel(
            'Issues/Bugs: <a href="https://github.com/MaFeLP/captura/issues/">https://github.com/MaFeLP/captura/issues/</a>'
        )
        app_issues.setOpenExternalLinks(True)
        layout.addWidget(app_issues)

        layout.addWidget(QHLine())

        # Authors
        authors = QLabel("Authors")
        authors.setFont(font_bold_underline)
        layout.addWidget(authors)
        author1 = QLabel(
            'MaFeLP &lt;<a href="mailto:mafelp@proton.me">mafelp@proton.me</a>&gt;'
        )
        author1.setOpenExternalLinks(True)
        layout.addWidget(author1)
        author2 = QLabel("SquidlesYT")
        layout.addWidget(author2)

        layout.addWidget(QHLine())

        # Components
        components = QLabel("Components")
        components.setFont(font_bold_underline)
        layout.addWidget(components)
        jinja_version = QLabel(
            f'<a href="https://jinja.palletsprojects.com/en/stable/"> Jinja2 ({jinja2.__version__})</a>, BSD-3-Clause'
        )
        jinja_version.setOpenExternalLinks(True)
        layout.addWidget(jinja_version)
        pyyaml_version = QLabel(
            f'<a href="https://pyyaml.org/">PyYAML ({yaml.__version__})</a>, MIT'
        )
        pyyaml_version.setOpenExternalLinks(True)
        layout.addWidget(pyyaml_version)
        python_version = QLabel(
            f'<a href="https://www.python.org/">Python ({sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})</a>, PSFv2'
        )
        python_version.setOpenExternalLinks(True)
        layout.addWidget(python_version)
        pyqt_version = QLabel(
            f'<a href="https://www.riverbankcomputing.com/software/pyqt/">PyQt ({PYQT_VERSION_STR})</a>, GPLv3'
        )
        pyqt_version.setOpenExternalLinks(True)
        layout.addWidget(pyqt_version)
        qt_version = QLabel(
            f'<a href="https://doc.qt.io/qt-6/">Qt ({QT_VERSION_STR})</a>, GPLv3'
        )
        qt_version.setOpenExternalLinks(True)
        layout.addWidget(qt_version)
        self.about_qt_button = QPushButton("About Qt")
        self.about_qt_button.clicked.connect(QApplication.aboutQt)
        layout.addWidget(self.about_qt_button)

        layout.addWidget(QHLine())

        # Copyright
        copyright_label = QLabel("© 2025 Captura Contributors")
        layout.addWidget(copyright_label)

        # Close button
        self.ok_button = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        self.ok_button.accepted.connect(self.accept)
        layout.addWidget(self.ok_button)

        # Finalize layout
        self.setLayout(layout)
