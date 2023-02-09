import sys
import time
from PyQt6.QtWidgets import (
                             QWidget,
                             QLabel,
                             QVBoxLayout)
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt


class LoadFM(QWidget):
    
    def __init__(self):
        
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setGeometry(400, 200, 600, 340)
        self.setStyleSheet("background-color:white; ")
        label = QLabel()
        labelCompany = QLabel("Powered by ing. Manigat")
        labelCompany.setStyleSheet("font-size:9px;\
                                color: #567189;\
                                font-weight: bold;\
                                text-transform: uppercase;")

        labelCompany.setAlignment(Qt.AlignmentFlag.AlignBottom)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        movie = QMovie('./image/logoMeticulou.gif')
        label.setMovie(movie)
        movie.start()
        self.layout = QVBoxLayout()
        self.layout.addWidget(label)
        self.layout.addWidget(labelCompany)
        self.setLayout(self.layout)
        # self.show()
        
    

