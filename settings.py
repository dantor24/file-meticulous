import sys
from data import Config
from pathlib import Path
from PyQt6.QtWidgets import (QWidget,
                             QLabel,
                             QCheckBox,
                             QVBoxLayout,
                             QGridLayout,)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class Settings(QWidget):

    width = 484
    heigh = 30

    def __init__(self):

        super().__init__()
        self.config = Config('config.json')
        self.config_json = self.config.conf
        self.config.write_file(self.config_json)
        
        self.setFixedSize(Settings.width, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 10, 0, 0)
        self.setLayout(layout)
        image_Settings = QLabel()
        image_Settings.setFixedSize(Settings.width, 55)
        image_Settings.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_Settings.setPixmap(QPixmap("./image/setting_icon.png"))

        label_welcome = QLabel("Check Repertories To Organize")
        label_welcome.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        label_welcome.setFixedSize(Settings.width, Settings.heigh)
        label_welcome.setObjectName("labelSetting")
        
        label_type = QLabel("Specified Types")
        label_type.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label_type.setFixedSize(Settings.width, Settings.heigh)
        label_type.setObjectName("labelSetting")
        
        check_container = QWidget()
        check_container.setFixedSize(Settings.width, 70)
        check_container.setObjectName("checkContainer")
        check_container_layout = QGridLayout()
        check_container_layout.setContentsMargins(0, 0, 0, 0)
        check_container_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        
        check_container.setLayout(check_container_layout)
        
        btn_check_desktop = QCheckBox("Desktop",self)
        btn_check_desktop.setChecked(self.config_json['desktop'])
        btn_check_desktop.setFixedSize(150,35)
        btn_check_documents = QCheckBox("Documents",self)
        btn_check_documents.setChecked(self.config_json['documents'])
        btn_check_documents.setFixedWidth(150)
        btn_check_music = QCheckBox("Music",self)
        btn_check_music.setChecked(self.config_json['music'])
        btn_check_music.setFixedWidth(150)
        btn_check_downloads = QCheckBox("Downloads")
        btn_check_downloads.setChecked(self.config_json['downloads'])
        btn_check_pictures = QCheckBox("Pictures",self)
        btn_check_pictures.setChecked(self.config_json['pictures'])
        btn_check_videos = QCheckBox("Videos",self)
        btn_check_videos.setChecked(self.config_json['videos'])
        
        # add event that will edit the json file to save state of the configuration
        btn_check_desktop.stateChanged.connect(self.checkbox_slot)
        btn_check_documents.stateChanged.connect(self.checkbox_slot)
        btn_check_downloads.stateChanged.connect(self.checkbox_slot)
        btn_check_music.stateChanged.connect(self.checkbox_slot)
        btn_check_pictures.stateChanged.connect(self.checkbox_slot)
        btn_check_videos.stateChanged.connect(self.checkbox_slot)
        
        check_container_layout.addWidget(btn_check_desktop,0,0)
        check_container_layout.addWidget(btn_check_documents,0,1)
        check_container_layout.addWidget(btn_check_downloads,0,2)
        check_container_layout.addWidget(btn_check_music,1,0)
        check_container_layout.addWidget(btn_check_pictures,1,1)
        check_container_layout.addWidget(btn_check_videos,1,2)
        
        check_container_type = QWidget()
        check_container_type.setFixedSize(Settings.width, 300)
        check_container_type.setObjectName("checkContainer")
        check_container_layout_type = QGridLayout()
        check_container_layout_type.setContentsMargins(0, 0, 0, 0)
        check_container_layout_type.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        
        
        check_container_type.setLayout(check_container_layout_type)
        
        btn_check_doc = QCheckBox("doc",self)
        btn_check_doc.setChecked(self.config_json['doc'])
        btn_check_doc.setFixedSize(70,35)
        btn_check_docx = QCheckBox("docx",self)
        btn_check_docx.setChecked(self.config_json['docx'])
        btn_check_docx.setFixedWidth(70)
        btn_check_xls = QCheckBox("xls",self)
        btn_check_xls.setChecked(self.config_json['xls'])
        btn_check_xls.setFixedWidth(70)
        btn_check_xlsx = QCheckBox("xlsx",self)
        btn_check_xlsx.setChecked(self.config_json['xlsx'])
        btn_check_xlsx.setFixedWidth(70)
        btn_check_ppt = QCheckBox("ppt",self)
        btn_check_ppt.setChecked(self.config_json['ppt'])
        btn_check_ppt.setFixedWidth(70)
        btn_check_onepkg = QCheckBox("onepkg",self)
        btn_check_onepkg.setChecked(self.config_json['onepkg'])
        btn_check_onepkg.setFixedWidth(70)
        btn_check_one = QCheckBox("one",self)
        btn_check_one.setChecked(self.config_json['one'])
        btn_check_txt = QCheckBox("txt",self)
        btn_check_txt.setChecked(self.config_json['txt'])
        btn_check_png = QCheckBox("png",self)
        btn_check_png.setChecked(self.config_json['png'])
        btn_check_jpeg = QCheckBox("jpeg",self)
        btn_check_jpeg.setChecked(self.config_json['jpeg'])
        btn_check_jpg = QCheckBox("jpg",self)
        btn_check_jpg.setChecked(self.config_json['jpg'])
        btn_check_gif = QCheckBox("gif",self)
        btn_check_gif.setChecked(self.config_json['gif'])
        btn_check_mp3 = QCheckBox("mp3",self)
        btn_check_mp3.setChecked(self.config_json['mp3'])
        btn_check_mp3.setFixedSize(70,35)
        btn_check_mp4 = QCheckBox("mp4",self)
        btn_check_mp4.setChecked(self.config_json['mp4'])
        btn_check_wma = QCheckBox("wma",self)
        btn_check_wma.setChecked(self.config_json['wma'])
        btn_check_wav = QCheckBox("wav",self)
        btn_check_wav.setChecked(self.config_json['wav'])
        btn_check_avi= QCheckBox("avi",self)
        btn_check_avi.setChecked(self.config_json['avi'])
        btn_check_psd = QCheckBox("psd",self)
        btn_check_psd.setChecked(self.config_json['psd'])
        btn_check_psb = QCheckBox("psb",self)
        btn_check_psb.setChecked(self.config_json['psb'])
    
        btn_check_psdt = QCheckBox("psdt",self)
        btn_check_psdt.setChecked(self.config_json['psdt'])
        btn_check_ai = QCheckBox("ai",self)
        btn_check_ai.setChecked(self.config_json['ai'])
        btn_check_eps= QCheckBox("eps",self)
        btn_check_eps.setChecked(self.config_json['eps'])
        btn_check_svg = QCheckBox("svg",self)
        btn_check_svg.setChecked(self.config_json['svg'])
        btn_check_ind = QCheckBox("ind",self)
        btn_check_ind.setChecked(self.config_json['ind']) 
        btn_check_c = QCheckBox("c",self)
        btn_check_c.setChecked(self.config_json['c'])
        btn_check_c.setFixedSize(70,35)
        btn_check_cpp = QCheckBox("cpp",self)
        btn_check_cpp.setChecked(self.config_json['cpp'])
        btn_check_cs = QCheckBox("cs",self)
        btn_check_cs.setChecked(self.config_json['cs'])
        btn_check_css= QCheckBox("css",self)
        btn_check_css.setChecked(self.config_json['css'])
        btn_check_java = QCheckBox("java",self)
        btn_check_java.setChecked(self.config_json['java'])
        btn_check_js = QCheckBox("js",self)
        btn_check_js.setChecked(self.config_json['js'])
        btn_check_py = QCheckBox("py",self)
        btn_check_py.setChecked(self.config_json['py'])
        btn_check_php = QCheckBox("php",self)
        btn_check_php.setChecked(self.config_json['php'])
        btn_check_go= QCheckBox("go",self)
        btn_check_go.setChecked(self.config_json['go']) 
        btn_check_ts = QCheckBox("ts",self)
        btn_check_ts.setChecked(self.config_json['ts'])
        btn_check_html = QCheckBox("html",self)
        btn_check_html.setChecked(self.config_json['html'])
        btn_check_xml = QCheckBox("xml",self)
        btn_check_xml.setChecked(self.config_json['xml'])
        btn_check_kt = QCheckBox("kt",self)
        btn_check_kt.setChecked(self.config_json['kt']) 
        btn_check_scss = QCheckBox("scss",self)
        btn_check_scss.setChecked(self.config_json['scss'])
        btn_check_css.setFixedSize(70,35)
        btn_check_sql= QCheckBox("sql",self)
        btn_check_sql.setChecked(self.config_json['sql'])
        btn_check_sh = QCheckBox("sh",self)
        btn_check_sh.setChecked(self.config_json['sh'])
        btn_check_rb = QCheckBox("rb",self)
        btn_check_rb.setChecked(self.config_json['rb'])
        btn_check_r = QCheckBox("r",self)
        btn_check_r.setChecked(self.config_json['r'])
        btn_check_zip = QCheckBox("zip",self)
        btn_check_zip.setChecked(self.config_json['zip'])
        btn_check_rar= QCheckBox("rar",self)
        btn_check_rar.setChecked(self.config_json['rar'])
        btn_check_tar = QCheckBox("tar",self)
        btn_check_tar.setChecked(self.config_json['tar'])
        btn_check_tars = QCheckBox("tars",self)
        btn_check_tars.setChecked(self.config_json['tars'])
        btn_check_pdf = QCheckBox("pdf",self)
        btn_check_pdf.setChecked(self.config_json['pdf'])
        
        btn_check_doc.stateChanged.connect(self.checkbox_slot)
        btn_check_docx.stateChanged.connect(self.checkbox_slot)
        btn_check_xls.stateChanged.connect(self.checkbox_slot)
        btn_check_xlsx.stateChanged.connect(self.checkbox_slot)
        btn_check_ppt.stateChanged.connect(self.checkbox_slot)
        btn_check_one.stateChanged.connect(self.checkbox_slot)
        btn_check_onepkg.stateChanged.connect(self.checkbox_slot)
        btn_check_txt.stateChanged.connect(self.checkbox_slot)
        btn_check_png.stateChanged.connect(self.checkbox_slot)
        btn_check_jpeg.stateChanged.connect(self.checkbox_slot)
        btn_check_jpg.stateChanged.connect(self.checkbox_slot)
        btn_check_gif.stateChanged.connect(self.checkbox_slot)
        btn_check_mp3.stateChanged.connect(self.checkbox_slot)
        btn_check_mp4.stateChanged.connect(self.checkbox_slot)
        btn_check_wma.stateChanged.connect(self.checkbox_slot)
        btn_check_wav.stateChanged.connect(self.checkbox_slot)
        btn_check_avi.stateChanged.connect(self.checkbox_slot)
        btn_check_psd.stateChanged.connect(self.checkbox_slot)
        btn_check_psb.stateChanged.connect(self.checkbox_slot)
        btn_check_psdt.stateChanged.connect(self.checkbox_slot)
        btn_check_ai.stateChanged.connect(self.checkbox_slot)
        btn_check_eps.stateChanged.connect(self.checkbox_slot)
        
        btn_check_svg.stateChanged.connect(self.checkbox_slot)
        btn_check_ind.stateChanged.connect(self.checkbox_slot)
        btn_check_c.stateChanged.connect(self.checkbox_slot)
        btn_check_cpp.stateChanged.connect(self.checkbox_slot)
        btn_check_cs.stateChanged.connect(self.checkbox_slot)
        btn_check_css.stateChanged.connect(self.checkbox_slot)
        btn_check_java.stateChanged.connect(self.checkbox_slot)
        btn_check_js.stateChanged.connect(self.checkbox_slot)
        btn_check_py.stateChanged.connect(self.checkbox_slot)
        btn_check_php.stateChanged.connect(self.checkbox_slot)
        btn_check_go.stateChanged.connect(self.checkbox_slot)
        btn_check_ts.stateChanged.connect(self.checkbox_slot)
        btn_check_html.stateChanged.connect(self.checkbox_slot)
        btn_check_xml.stateChanged.connect(self.checkbox_slot)
        btn_check_kt.stateChanged.connect(self.checkbox_slot)
        btn_check_scss.stateChanged.connect(self.checkbox_slot)
        btn_check_sql.stateChanged.connect(self.checkbox_slot)
        btn_check_sh.stateChanged.connect(self.checkbox_slot)
        btn_check_rb.stateChanged.connect(self.checkbox_slot)
        btn_check_r.stateChanged.connect(self.checkbox_slot)
        btn_check_zip.stateChanged.connect(self.checkbox_slot)
        btn_check_rar.stateChanged.connect(self.checkbox_slot)
        btn_check_tar.stateChanged.connect(self.checkbox_slot)
        btn_check_tars.stateChanged.connect(self.checkbox_slot)
        btn_check_pdf.stateChanged.connect(self.checkbox_slot)
        
        
        check_container_layout_type.addWidget(btn_check_doc,0,0)
        check_container_layout_type.addWidget(btn_check_docx,0,1)
        check_container_layout_type.addWidget(btn_check_xls,0,2)
        check_container_layout_type.addWidget(btn_check_xlsx,0,3)
        check_container_layout_type.addWidget(btn_check_ppt,0,4)
        check_container_layout_type.addWidget(btn_check_one,0,5)
        check_container_layout_type.addWidget(btn_check_onepkg,1,0)
        check_container_layout_type.addWidget(btn_check_txt,1,1)
        check_container_layout_type.addWidget(btn_check_png,1,2)
        check_container_layout_type.addWidget(btn_check_jpeg,1,3)
        check_container_layout_type.addWidget(btn_check_jpg,1,4)
        check_container_layout_type.addWidget(btn_check_gif,1,5)
        check_container_layout_type.addWidget(btn_check_mp3,2,0)
        check_container_layout_type.addWidget(btn_check_mp4,2,1)
        check_container_layout_type.addWidget(btn_check_wma,2,2)
        check_container_layout_type.addWidget(btn_check_wav,2,3)
        check_container_layout_type.addWidget(btn_check_avi,2,4)
        check_container_layout_type.addWidget(btn_check_psd,2,5)
        check_container_layout_type.addWidget(btn_check_psb,3,0)
        check_container_layout_type.addWidget(btn_check_psdt,3,1)
        check_container_layout_type.addWidget(btn_check_ai,3,2)
        check_container_layout_type.addWidget(btn_check_eps,3,3)
        check_container_layout_type.addWidget(btn_check_svg,3,4)
        check_container_layout_type.addWidget(btn_check_ind,3,5)
        check_container_layout_type.addWidget(btn_check_c,4,0)
        check_container_layout_type.addWidget(btn_check_cpp,4,1)
        check_container_layout_type.addWidget(btn_check_cs,4,2)
        check_container_layout_type.addWidget(btn_check_java,4,3)
        check_container_layout_type.addWidget(btn_check_js,4,4)
        check_container_layout_type.addWidget(btn_check_py,4,5)
        check_container_layout_type.addWidget(btn_check_php,5,0)
        check_container_layout_type.addWidget(btn_check_go,5,1)
        check_container_layout_type.addWidget(btn_check_ts,5,2)
        check_container_layout_type.addWidget(btn_check_html,5,3)
        check_container_layout_type.addWidget(btn_check_xml,5,4)
        check_container_layout_type.addWidget(btn_check_kt,5,5)
        check_container_layout_type.addWidget(btn_check_scss,6,0)
        check_container_layout_type.addWidget(btn_check_sql,6,1)
        check_container_layout_type.addWidget(btn_check_sh,6,2)
        check_container_layout_type.addWidget(btn_check_rb,6,3)
        check_container_layout_type.addWidget(btn_check_r,6,4)
        check_container_layout_type.addWidget(btn_check_css,6,5)
        check_container_layout_type.addWidget(btn_check_rar,7,0)
        check_container_layout_type.addWidget(btn_check_tar,7,1)
        check_container_layout_type.addWidget(btn_check_tars,7,2)
        check_container_layout_type.addWidget(btn_check_zip,7,3)
        check_container_layout_type.addWidget(btn_check_pdf,7,4)

        
        

        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.addWidget(image_Settings)
        layout.addWidget(label_welcome)
        layout.addWidget(check_container)
        layout.addWidget(label_type)
        layout.addWidget(check_container_type)

        self.show()
        
    def checkbox_slot(self):
        signal = self.sender()
        key = signal.text().lower()

        print(signal.text())
        # print(f"{state}, qt {Qt.CheckState.Checked}")
        if signal.isChecked():
            print("check_container")
            self.config_json[key] = True
            print(self.config_json)
            self.config.write_file(self.config_json)
        else:
            print("uncheck_container")
            self.config_json[key] = False
            print(self.config_json)
            self.config.write_file(self.config_json)

