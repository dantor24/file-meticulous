from folder_extension import (Folder,
                              Extension)
from directory import Directory

class FileMeticulous(Directory):
    
    def __init__(self):
        super().__init__()
        self._destop_fm = self.os_path(Folder.DESKTOP.value['parent'],Folder.DESKTOP.value['name'])
        self._document_fm =  self.os_path(Folder.DOCUMENTS.value['parent'],Folder.DOCUMENTS.value['name'])
        self._download_fm =   self.os_path(Folder.DOWNLOADS.value['parent'],Folder.DOWNLOADS.value['name'])
        self._picture_fm =  self.os_path(Folder.PICTURES.value['parent'],Folder.PICTURES.value['name'])
        self._music_fm =  self.os_path(Folder.MUSIC.value['parent'],Folder.MUSIC.value['name'])
        self._video_fm =  self.os_path(Folder.VIDEOS.value['parent'],Folder.VIDEOS.value['name'])
        self._ext_pdf =  self.os_path(self.document_fm, Extension.PDF.value)
        self._ext_doc =  self.os_path(self.document_fm, Extension.DOC.value)
        self._ext_docx = self.os_path(self.document_fm, Extension.PDF.value)
        self._ext_xls =  self.os_path(self.document_fm, Extension.XLS.value)
        self._ext_xlsx = self.os_path(self.document_fm, Extension.XLSX.value)
        self._ext_ppt =  self.os_path(self.document_fm, Extension.PPT.value)
        self._ext_txt =  self.os_path(self.document_fm, Extension.TXT.value)
        self._ext_jpg =  self.os_path(self.document_fm, Extension.JPG.value)
        self._ext_png =  self.os_path(self.picture_fm, Extension.PNG.value)
        self._ext_jpeg = self.os_path(self.picture_fm, Extension.JPEG.value)
        self._ext_gif =  self.os_path(self.picture_fm, Extension.GIF.value)
        self._ext_mp3 =  self.os_path(self.music_fm, Extension.MP3.value)
        self._ext_wav =  self.os_path(self.video_fm, Extension.WAV.value)
        self._ext_mp4 =  self.os_path(self.video_fm, Extension.MP4.value)
        self._ext_avi =  self.os_path(self.video_fm, Extension.AVI.value)
        self._ext_pds =  self.os_path(self.document_fm, Extension.PSD.value)
        self._ext_psb =  self.os_path(self.document_fm, Extension.PSB.value)
        self._ext_psdt =  self.os_path(self.document_fm, Extension.PSDT.value)
        self._ext_ai =  self.os_path(self.document_fm, Extension.AI.value)
        self._ext_eps =  self.os_path(self.document_fm, Extension.EPS.value)
        self._ext_svg =  self.os_path(self.document_fm, Extension.SVG.value)
        self._ext_ind =  self.os_path(self.document_fm, Extension.IND.value)
        self._ext_c =  self.os_path(self.document_fm, Extension.C.value)
        self._ext_cpp =  self.os_path(self.document_fm, Extension.CPP.value)
        self._ext_java =  self.os_path(self.document_fm, Extension.JAVA.value)
        self._ext_js =  self.os_path(self.document_fm, Extension.JS.value)
        self._ext_html =  self.os_path(self.document_fm, Extension.HTML.value)
        self._ext_css =  self.os_path(self.document_fm, Extension.CSS.value)
        self._ext_py =  self.os_path(self.document_fm, Extension.PY.value)
        self._ext_php =  self.os_path(self.document_fm, Extension.PHP.value)
        self._ext_go =  self.os_path(self.document_fm, Extension.GO.value)
        self._ext_ts =  self.os_path(self.document_fm, Extension.TS.value)
        self._ext_xml =  self.os_path(self.document_fm, Extension.XML.value)
        self._ext_kt =  self.os_path(self.document_fm, Extension.KT.value)
        self._ext_scss =  self.os_path(self.document_fm, Extension.SCSS.value)
        self._ext_sql =  self.os_path(self.document_fm, Extension.SQL.value)
        self._ext_sh =  self.os_path(self.document_fm, Extension.SH.value)
        self._ext_rb =  self.os_path(self.document_fm, Extension.RB.value)
        self._ext_r =  self.os_path(self.document_fm, Extension.R.value)
        self._ext_zip =  self.os_path(self.document_fm, Extension.ZIP.value)
        self._ext_rar =  self.os_path(self.document_fm, Extension.RAR.value)
        self._ext_tar =  self.os_path(self.document_fm, Extension.TAR.value)
        self._ext_tars =  self.os_path(self.document_fm, Extension.TARS.value)
        
    @property
    def destop_fm(self):
        return self._destop_fm
    
    @property
    def document_fm(self):
        return self._document_fm
    
    @property
    def download_fm(self):
        return self._download_fm
    
    @property
    def picture_fm(self):
        return self._picture_fm
    
    @property
    def music_fm(self):
        return self._music_fm
    
    @property
    def video_fm(self):
        return self._video_fm
    
    @property
    def pdf_fm(self):
        return self._ext_pdf
    
    @property
    def txt_fm(self):
        return self._ext_txt
    
    @property
    def doc_fm(self):
        return self._ext_doc
    
    @property
    def docx_fm(self):
        return self._ext_docx
    
    @property
    def xls_fm(self):
        return self._ext_xls
    
    @property
    def xlsx_fm(self):
        return self._ext_xlsx
    
    @property
    def ppt_fm(self):
        return self._ext_ppt
    
    @property
    def pptx_fm(self):
        return self._ext_pptx
    
    @property
    def ai_fm(self):
        return self._ext_ai
    
    @property
    def eps_fm(self):
        return self._ext_eps
    
    @property
    def svg_fm(self):
        return self._ext_svg
    
    @property
    def ind_fm(self):
        return self._ext_ind
    
    @property
    def c_fm(self):
        return self._ext_c
    
    @property
    def cpp_fm(self):
        return self._ext_cpp
    
    @property
    def java_fm(self):
        return self._ext_java
    
    @property
    def js_fm(self):
        return self._ext_js
    
    @property
    def html_fm(self):
        return self._ext_html
    
    @property
    def css_fm(self):
        return self._ext_css
    
    @property
    def py_fm(self):
        return self._ext_py
    
    @property
    def php_fm(self):
        return self._ext_php
    
    @property
    def go_fm(self):
        return self._ext_go
    
    @property
    def ts_fm(self):
        return self._ext_ts
    
    @property
    def xml_fm(self):
        return self._ext_xml
    
    @property
    def kt_fm(self):
        return self._ext_kt
    
    @property
    def scss_fm(self):
        return self._ext_scss
    
    @property
    def sql_fm(self):
        return self._ext_sql
    
    @property
    def sh_fm(self):
        return self._ext_sh
    
    @property
    def rb_fm(self):
        return self._ext_rb
    
    @property
    def r_fm(self):
        return self._ext_r
    
    @property
    def zip_fm(self):
        return self._ext_zip
    
    @property
    def rar_fm(self):
        return self._ext_rar
    
    @property
    def tar_fm(self):
        return self._ext_tar
    
    @property
    def tars_fm(self):
        return self._ext_tars
    
    @property
    def avi_fm(self):
        return self._ext_avi
    
    @property
    def mp4_fm(self):
        return self._ext_mp4
    
    @property
    def mp3_fm(self):
        return self._ext_mp3
    
    @property
    def wav_fm(self):
        return self._ext_wav
    
    
   

        
        
        
        
    


# if __name__ == '__main__':
    
#     direc = FileMeticulous()
#     document = direc.document_fm
#     print(direc.user_path)
#     print(direc.destop_fm)
#     print(direc.document_fm)
#     print(direc.pdf_fm)
#     print(direc.ai_fm)
#     print(direc.create_folder(document))