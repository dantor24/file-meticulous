import sys
import webbrowser
from pathlib import Path
from PyQt6.QtWidgets import (QWidget,
                             QLabel,
                             QApplication,
                             QPushButton,
                             QVBoxLayout,
                             QHBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class About(QWidget):

    width = 484
    heigh = 55

    def __init__(self):

        super().__init__()
        self.setFixedSize(About.width, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        self.setLayout(layout)
        image_about = QLabel()
        image_about.setFixedSize(About.width, About.heigh)
        image_about.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_about.setPixmap(QPixmap("./image/about.png"))

        label_welcome = QLabel("About File Meticulous")
        label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_welcome.setFixedSize(About.width, About.heigh)
        label_welcome.setObjectName("labelWelcome")
        
        link_github = "<a href='https://github.com/dantor24'>visit our GitHub repository.</a>"
        txt_about = f"File Meticulous is a powerful tool that helps you keep all your files organized and easy to find. With its user-friendly interface, you can sort, categorize and search for files in just a few clicks. Say goodbye to cluttered and disorganized files, and hello to a more efficient and streamlined system. Get started today and bring organization to your laptop {link_github}"
        label_description = QLabel(txt_about)
        # open the link to your default browser
        label_description.setOpenExternalLinks(True)
        label_description.linkActivated.connect(lambda: webbrowser.open(link_github))
        # swap the label_description for long description
        label_description.setWordWrap(True)
        label_description.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        label_description.setFixedSize(About.width, 150)
        label_description.setObjectName("labelDescAbout")
        
        label_creator = QLabel("Powered by ing. Aymerick Y. Manigat, version 1.0 ")
        label_creator.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_creator.setFixedSize(About.width, 30)
        label_creator.setObjectName("labelCreator")

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(image_about)
        layout.addWidget(label_welcome)
        layout.addWidget(label_description)
        layout.addWidget(label_creator)
        self.show()

