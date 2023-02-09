import sys
from home import Home
from about import About
from settings import Settings
from loader import LoadFM
from pathlib import Path
from PyQt6.QtWidgets import (QApplication,
                             QMainWindow,
                             QPushButton,
                             QCheckBox,
                             QLabel,
                             QVBoxLayout,
                             QHBoxLayout,
                             QWidget,)

from PyQt6.QtGui import (QIcon,
                         QPixmap,
                         QGuiApplication)

from PyQt6.QtCore import (Qt,
                          QTimer,)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setFixedSize(700, 500)
        
        self.home = Home()
        self.about = About()
        self.settings = Settings()
        self.about.setVisible(False)
        self.settings.setVisible(False)

        
        main = QWidget(self)
        main.setFixedSize(700, 500)
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.main_layout.addWidget(self.panelLeft())
        self.main_layout.addWidget(self.home)
        self.main_layout.addWidget(self.about)
        self.main_layout.addWidget(self.settings)
        main.setLayout(self.main_layout)

        # self.show()

    def getMainLayout(self):
        """ getter for main layout """
        return self.main_layout

    def panelLeft(self):
        """create the left panel with the menu navigation """

        left = QWidget(self)
        left.setFixedSize(216, 500)
        left.setObjectName("left")
        layout_left = QVBoxLayout()
        layout_left.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout_left.setContentsMargins(0, 0, 0, 0)
        header = QWidget(left)
        header.setFixedSize(216, 80)
        header_layout = QHBoxLayout()

        self.btn_home = QPushButton("Home")
        self.btn_history = QPushButton("History")
        self.btn_settings = QPushButton("settings")
        self.btn_about = QPushButton("about")

        menu = QWidget(left)
        menu.setFixedSize(216, 200)
        menu.setObjectName("menu")
        menu_layout = QVBoxLayout()
        menu_layout.setContentsMargins(0, 0, 0, 0)

        header_layout.setContentsMargins(0, 0, 0, 0)
        # this is the icon of the left panel
        label_icon = QLabel()
        label_icon.setFixedSize(50, 50)
        label_icon.setPixmap(QPixmap('./image/logo.png'))
        # this is the title of the left panel
        label_tilte = QLabel("File Meticulous")
        label_tilte.setObjectName("titleLabel")

        # add logout button
        btn_logout = QPushButton()
        # btn_logout.setFixedSize(50,50)
        btn_logout.setIcon(QIcon('./image/logout.svg'))
        bottom = QWidget(left)
        bottom_layout = QVBoxLayout()
        bottom_layout.setContentsMargins(0, 0, 0, 0)
        bottom.setLayout(bottom_layout)
        
        # add event on each button
        self.btn_home.clicked.connect(self.displayHome)
        self.btn_about.clicked.connect(self.displayAbout)
        self.btn_settings.clicked.connect(self.displaySettings)
        btn_logout.clicked.connect(self.close)

        # add the logout button to the menu

        # add widget to the header
        header_layout.addWidget(label_icon)
        header_layout.addWidget(label_tilte)
        # add widgets to the left panel
        layout_left.addWidget(header)
        layout_left.addWidget(menu)
        layout_left.addWidget(bottom)
        #  add widgets  to the menu
        menu_layout.addWidget(self.btn_home)
        menu_layout.addWidget(self.btn_history)
        menu_layout.addWidget(self.btn_settings)
        menu_layout.addWidget(self.btn_about)
        # add widget to the bottom
        bottom_layout.addWidget(btn_logout)

        header.setLayout(header_layout)
        left.setLayout(layout_left)
        menu.setLayout(menu_layout)

        return left


    def displayHome(self):
        """display the home and hide the others contents"""
        # self.animation = QPropertyAnimation(self.home, b'geometry')
        # self.animation.setEasingCurve(QEasingCurve.Type.InElastic)
        # self.animation.setStartValue(self.home.geometry())
        # self.animation.setEndValue(self.home.geometry().translated(0, self.home.height()))
        # self.animation.setDuration(1000)
        # self.animation.start()


        self.home.setVisible(True)
        self.about.setVisible(False)
        self.settings.setVisible(False)
    
    def displayAbout(self):
        """display the about and hide the others contents"""
        self.home.setVisible(False)
        self.about.setVisible(True)
        self.settings.setVisible(False)
        
    def displaySettings(self):
        """display the settings and hide the others contents"""
        self.home.setVisible(False)
        self.about.setVisible(False)
        self.settings.setVisible(True)
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(Path('style.qss').read_text())
    window = MainWindow()

    app_loader = LoadFM()
    app_loader.show()
    # time for the loading process
    import time
    time.sleep(0)

    # run the app_loader during 3s and show window after 3 seconds
    QTimer.singleShot(2800, app_loader.close)
    QTimer.singleShot(2800, window.show)
    app.processEvents()
    sys.exit(app.exec())
