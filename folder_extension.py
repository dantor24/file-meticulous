from enum import Enum


class Folder(Enum):
    DESKTOP = {'true': True,
               'false': False,
               'parent': 'Desktop',
               'name': 'Desktop_fm'}
    DOWNLOADS = {'true': True,
                 'false': False,
                 'parent': 'Downloads',
                 'name': 'Downloads_fm'}
    DOCUMENTS = {'true': True,
                 'false': False,
                 'parent': 'Documents',
                 'name': 'Documents_fm'}
    PICTURES = {'true': True,
                'false': False,
                'parent': 'Pictures',
                'name': 'Pictures_fm'}
    VIDEOS = {'true': True,
              'false': False,
              'parent': 'Videos',
              'name': 'Videos_fm'}
    MUSIC = {'true': True,
             'false': False,
             'parent': 'Music',
             'name': 'Music_fm'}


class Extension(Enum):
    PDF = "pdf"
    # microsoft 365 format
    DOC = "doc"
    DOCX = "docx"
    XLS = "xls"
    XLSX = "xlsx"
    PPT = "ppt"
    PPTX = "pptx"
    ONE = "one"
    ONEPKG = "onepkg"
    TXT = "txt"
    PNG = "png"
    JPG = "jpg"
    JPEG = "jpeg"
    GIF = "gif"
    MP3 = "mp3"
    MP4 = "mp4"
    WAV = "wav"
    WMA = "wma"
    AVI = "avi"
    # adobe format
    PSD = "psd"
    PSB = "psb"
    PSDT = "psdt"
    AI = "ai"
    EPS = "eps"
    SVG = "svg"
    IND = "ind"
    # programming language format
    C = "c"
    CPP = "cpp"
    CS = "cs"
    CSS = "css"
    JAVA = "java"
    JS = "js"
    PY = "py"
    PHP = "php"
    GO = "go"
    TS = "ts"
    HTML = "html"
    XML = "xml"
    KT = "kt"
    SCSS = "scss"
    SQL = "sql"
    SH = "sh"
    RB = "rb"
    R = "r"
    # compression format
    ZIP = "zip"
    RAR = "rar"
    TAR = "tar"
    TARS = "tars"
