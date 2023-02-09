from pathlib import Path
import time
import os
from data import Config

# add the parent directory to the sys.path list


# import the module from the parent directory
from main import FileMeticulous
from folder_extension import Folder, Extension


from pathlib import Path
from PyQt6.QtWidgets import (QWidget,
                             QLabel,
                             QPushButton,
                             QVBoxLayout,
                             QHBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class Home(QWidget):

    width = 484
    heigh = 55
    manager_fm = FileMeticulous()

    def __init__(self):

        super().__init__()

        self.setFixedSize(Home.width, 500)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        self.setLayout(layout)
        image_home = QLabel()
        image_home.setFixedSize(Home.width, Home.heigh)
        image_home.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_home.setPixmap(QPixmap("./image/organize.svg"))

        label_welcome = QLabel("Welcome in File Meticulous!")
        label_welcome.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_welcome.setFixedSize(Home.width, Home.heigh)
        label_welcome.setObjectName("labelWelcome")

        label_description = QLabel(
            "With  FM you can organize your files with only one click.")
        label_description.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_description.setFixedSize(Home.width, 20)
        label_description.setObjectName("labelDesc")

        image_classeur = QLabel()
        image_classeur.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_classeur.setPixmap(QPixmap("./image/classeur.png"))
        image_classeur.setFixedHeight(300)

        button_organize = QPushButton("Launch")
        # button_organize.setAlignment(Qt.AlignmentFlag.AlignCenter)
        button_organize.setFixedSize(117, 30)
        button_organize.setObjectName("btnOrganize")

        btn_org_widget = QWidget()
        btn_org_widget.setFixedSize(Home.width, Home.heigh)
        btn_org_layout = QHBoxLayout()
        btn_org_widget.setLayout(btn_org_layout)
        btn_org_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_file = QLabel("")
        self.label_file.setFixedSize(Home.width, 20)
        label_file_layout = QHBoxLayout()
        label_file_layout.setContentsMargins(0, 0, 0, 0)
        self.label_file.setLayout(label_file_layout)
        label_file_layout.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.label_file.setObjectName("fileMoving")

        button_organize.clicked.connect(self.organize)

        btn_org_layout.addWidget(button_organize)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(image_home)
        layout.addWidget(label_welcome)
        layout.addWidget(label_description)
        layout.addWidget(image_classeur)
        layout.addWidget(btn_org_widget)
        layout.addWidget(self.label_file)
        self.show()

    def organize(self):
        #  import time
        desktop = Home.manager_fm.destop_fm
        document = Home.manager_fm.document_fm
        download = Home.manager_fm.download_fm
        picture = Home.manager_fm.picture_fm
        video = Home.manager_fm.video_fm
        music = Home.manager_fm.music_fm
        # document = Path(document).resolve().parents[0]
        # ext = Home.manager_fm.filter_files(document, Extension.MP4.value)
        # print(f'location : {document}  extension: {Extension.MP4.value}')
        # print(ext)
        # self.filee = ext
        # self.timer = QTimer()
        # self.timer.singleShot(3000,self.listed)
        self.create_fm_folders(desktop)
        self.create_fm_folders(document)
        self.create_fm_folders(download)
        self.create_fm_folders(picture)
        self.create_fm_folders(video)
        self.create_fm_folders(music)
        
        self.create_extension_folders(Extension.MP4.value, document)
        self.create_extension_folders(Extension.DOC.value, document)
        self.create_extension_folders(Extension.DOCX.value, document)
        self.create_extension_folders(Extension.XLS.value, document)
        self.create_extension_folders(Extension.XLSX.value, document)
        self.create_extension_folders(Extension.XLSX.value, document)
        self.create_extension_folders(Extension.PPT.value, document)
        self.create_extension_folders(Extension.PPTX.value, document)
        self.create_extension_folders(Extension.ONE.value, document)
        self.create_extension_folders(Extension.PDF.value, document)
        self.create_extension_folders(Extension.TXT.value, document)
        self.create_extension_folders(Extension.PSD.value, document)
        self.create_extension_folders(Extension.PSB.value, document)
        self.create_extension_folders(Extension.PSDT.value, document)
        self.create_extension_folders(Extension.AI.value, document)
        self.create_extension_folders(Extension.EPS.value, document)
        self.create_extension_folders(Extension.IND.value, document)
        # Programming languages
        self.create_extension_folders(Extension.CPP.value, document)
        self.create_extension_folders(Extension.CS.value, document)
        self.create_extension_folders(Extension.CSS.value, document)
        self.create_extension_folders(Extension.JAVA.value, document)
        self.create_extension_folders(Extension.JS.value, document)
        self.create_extension_folders(Extension.PY.value, document)
        self.create_extension_folders(Extension.PHP.value, document)
        self.create_extension_folders(Extension.GO.value, document)
        self.create_extension_folders(Extension.TS.value, document)
        self.create_extension_folders(Extension.HTML.value, document)
        self.create_extension_folders(Extension.XML.value, document)
        self.create_extension_folders(Extension.KT.value, document)
        self.create_extension_folders(Extension.SCSS.value, document)
        self.create_extension_folders(Extension.SQL.value, document)
        self.create_extension_folders(Extension.SH.value, document)
        self.create_extension_folders(Extension.RB.value, document)
        self.create_extension_folders(Extension.ZIP.value, document)
        self.create_extension_folders(Extension.RAR.value, document)
        self.create_extension_folders(Extension.TAR.value, document)
        self.create_extension_folders(Extension.TARS.value, document)
        
        
        self.create_extension_folders(Extension.PNG.value, picture)
        self.create_extension_folders(Extension.JPG.value, picture)
        self.create_extension_folders(Extension.JPEG.value, picture)
        self.create_extension_folders(Extension.GIF.value, picture)
        self.create_extension_folders(Extension.SVG.value, picture)
        
        self.create_extension_folders(Extension.MP3.value, music)
        
        self.create_extension_folders(Extension.MP4.value, video)
        self.create_extension_folders(Extension.WAV.value, video)
        self.create_extension_folders(Extension.WMA.value, video)
        self.create_extension_folders(Extension.AVI.value, video)
        
        
        self.move_file('documents',document)
        self.move_file('desktop',desktop)
        self.move_file('downloads',download)
        self.move_file('pictures',picture)
        self.move_file('videos',video)
        self.move_file('music',music)

    # def listed(self):

    #     for file in self.filee['files']:

    #         self.label_file.setText(file)

    def create_fm_folders(self, path):
        parent = Path(path).resolve().parents[0]
        self.config = Config('config.json')
        self.config_json = self.config.conf
        Home.manager_fm.create_folder(parent, path)


    def create_extension_folders(self, key, path):
        
        parent = path 
        path = os.path.join(path,key)
        self.config = Config('config.json')
        self.config_json = self.config.conf

        if self.config_json[key] == True:
            Home.manager_fm.create_folder(parent, path)

            
    def move_file(self,directory_name, directory_path):

        self.config = Config('config.json')
        self.config_json = self.config.conf
        
        extensions = [extension.value for extension in Extension if self.config_json[extension.value] == True]
        
        picture_fm = Home.manager_fm.picture_fm
        video_fm = Home.manager_fm.video_fm
        document_fm = Home.manager_fm.document_fm
        
        type_picture = ['png','jpg','jpeg','gif','svg']
        type_video = ['mp4','wam','wma','avi',]
        type_pic_video = type_picture + type_video

                        
        if self.config_json[directory_name] == True:
            
            path_fm = directory_path
            parent_path_fm = Path(path_fm).resolve().parents[0]
            
            for extension in extensions:
                file = Home.manager_fm.filter_files(parent_path_fm, extension)
                
                if extension in type_picture:
                    picture = Path(picture_fm).resolve().parents[0]
                    i = 0
                    while i < len(file['files']):
                        new_path = os.path.join(picture_fm, extension)
                        new_path = os.path.join(new_path, file['files'][i]) 
                        Home.manager_fm.move_files(file['path_file'][i], new_path)
                        print(f"picture -> file_location: {file['path_file'][i]} new path: {new_path}")

                        i += 1
                        
                if extension in type_video:
                    video = Path(video_fm).resolve().parents[0]
                    i = 0
                    while i < len(file['files']):
                        new_path = os.path.join(video_fm, extension)
                        new_path = os.path.join(new_path, file['files'][i]) 
                        Home.manager_fm.move_files(file['path_file'][i], new_path)
                        print(f"video -> file_location: {file['path_file'][i]} new path: {new_path}")
                        i += 1
                        
                if extension not in type_pic_video:
                    document = Path(document_fm).resolve().parents[0]
                    i = 0
                    while i < len(file['files']):
                        new_path = os.path.join(document_fm, extension)
                        new_path = os.path.join(new_path, file['files'][i]) 
                        Home.manager_fm.move_files(file['path_file'][i], new_path)
                        print(f"document -> file_location: {file['path_file'][i]} new path: {new_path}")

                        i += 1
                    
            
