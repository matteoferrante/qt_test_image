import glob
import os
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea
from PyQt5.uic.properties import QtCore, QtWidgets
import cv2
import numpy as np
import pandas as pd
from dicom_data import DicomData
from ui.user_interface import Ui_MainWindow


#altro progetto
from dicom_widget import DicomWidget




### PALETTE PART
WHITE =     QColor(255, 255, 255)
BLACK =     QColor(0, 0, 0)
RED =       QColor(255, 0, 0)
PRIMARY =   QColor(53, 53, 53)
SECONDARY = QColor(35, 35, 35)
TERTIARY =  QColor(42, 130, 218)


def css_rgb(color, a=False):
    """Get a CSS `rgb` or `rgba` string from a `QtGui.QColor`."""
    return ("rgba({}, {}, {}, {})" if a else "rgb({}, {}, {})").format(*color.getRgb())


class QDarkPalette(QPalette):
    """Dark palette for a Qt application meant to be used with the Fusion theme."""
    def __init__(self, *__args):
        super().__init__(*__args)

        # Set all the colors based on the constants in globals
        self.setColor(QPalette.Window,          PRIMARY)
        self.setColor(QPalette.WindowText,      WHITE)
        self.setColor(QPalette.Base,            SECONDARY)
        self.setColor(QPalette.AlternateBase,   PRIMARY)
        self.setColor(QPalette.ToolTipBase,     WHITE)
        self.setColor(QPalette.ToolTipText,     WHITE)
        self.setColor(QPalette.Text,            WHITE)
        self.setColor(QPalette.Button,          PRIMARY)
        self.setColor(QPalette.ButtonText,      WHITE)
        self.setColor(QPalette.BrightText,      RED)
        self.setColor(QPalette.Link,            TERTIARY)
        self.setColor(QPalette.Highlight,       TERTIARY)
        self.setColor(QPalette.HighlightedText, BLACK)

    @staticmethod
    def set_stylesheet(app):
        """Static method to set the tooltip stylesheet to a `QtWidgets.QApplication`."""
        app.setStyleSheet("QToolTip {{"
                          "color: {white};"
                          "background-color: {tertiary};"
                          "border: 1px solid {white};"
                          "}}".format(white=css_rgb(WHITE), tertiary=css_rgb(TERTIARY)))


    def set_app(self, app):
        """Set the Fusion theme and this palette to a `QtWidgets.QApplication`."""
        app.setStyle("Fusion")
        app.setPalette(self)
        self.set_stylesheet(app)


### INIZIO CODICE


#OVERALL VARIABLES


#NEW_DIR=r"D:\FISICA MEDICA\MezzoDiContrasto\Immagini TEST MDC\NEW"
#OLD_DIR=r"D:\FISICA MEDICA\MezzoDiContrasto\Immagini TEST MDC\OLD"

NEW_DIR=rNEW_DIR=r"\\portale.ieo.it\portale\Aree_Dipartimentali\G_RAD\2- G_RAD - ALTRE CARTELLE\MDC\NEW"

OLD_DIR=r"\\portale.ieo.it\portale\Aree_Dipartimentali\G_RAD\2- G_RAD - ALTRE CARTELLE\MDC\OLD"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)

        self.info={}
        self.collected_data=[]
        self.progress=0   #actual img
        self.target= 20  #img to evaluate


        #self.ui.img = DicomWidget(self) #lavorare qua per piazzarlo
        self.ui.pushButtonStart.clicked.connect(lambda: self.load_at_start())


        ## Set the imgs
        pix_not = QPixmap(r'ui/img_not_sufficient.png').scaled(50,50)
        self.ui.labelInsufficientImg.setPixmap(pix_not)

        pix_low = QPixmap(r'ui/img_low.png').scaled(50,50)
        self.ui.labelLowImg.setPixmap(pix_low)

        pix_med = QPixmap(r'ui/img_medium.png').scaled(50, 50)
        self.ui.labelMediumImg.setPixmap(pix_med)

        pix_ok = QPixmap(r'ui/img_max.png').scaled(50, 50)
        self.ui.labelMaxImg.setPixmap(pix_ok)


        self.ui.pushButtonInsufficient.clicked.connect(lambda: self.vote(0))
        self.ui.pushButtonLow.clicked.connect(lambda: self.vote(1))
        self.ui.pushButtonMedium.clicked.connect(lambda: self.vote(2))
        self.ui.pushButtonMax.clicked.connect(lambda: self.vote(3))

        #scroll_area = QtWidgets.QScrollArea()
        #scroll_area.setWidget(self.pix_label)


    def closeEvent(self, event):
        """Save collected data on exit"""

        df=pd.DataFrame.from_dict(self.collected_data)
        phys_name = self.ui.plainTextPhysSign.toPlainText()

        df.to_csv(os.path.join(r"\\portale.ieo.it\portale\Aree_Dipartimentali\G_RAD\2- G_RAD - ALTRE CARTELLE\MDC",f"collected_data_{phys_name}.csv"))
        print(f"[INFO] Output saved to collected_data.csv")
        can_exit=True
        if can_exit:
            event.accept()  # let the window close
        else:
            event.ignore()


    def vote(self,rate):
        """This function add to info rate and physician name"""
        phys_name=self.ui.plainTextPhysSign.toPlainText()
        self.info["rate"]=rate
        self.info["Physician"]=phys_name
        self.collected_data.append(self.info)
        self.progress+=1
        self.ui.progressBar.setProperty("value", self.progress*5)
        self.magic()



    def update_coordinates(self):
        self.ui.img.update_image()
        #mostrare le info di visualizzazione
        try:
            self.ui.infoLabel.setText(f"Series: {self.header.SeriesDescription} \nWidth:\t {self.ui.img.window_width}\nCenter:\t {self.ui.img.window_center}")
        except Exception as e:
            print(e)
            self.ui.infoLabel.setText(f"Width:\t {self.ui.img.window_width}\nCenter:\t {self.ui.img.window_center}")

    def cv2QtImg(self,path):
        cv_img=cv2.imread(path)
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

        #p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(convert_to_Qt_format)

    #LAVORARE QUA AGGIUNGERE MODIFICA CONTRASTO IMMAGINI E CARICARE DICOM


    def load_at_start(self):
        #load all target images
        self.studies=[]
        self.study_headers=[]
        self.study_mean_MA=[]
        for i in range(self.target):  #three images for security
            print(f"[INFO] loading {i} of {self.target} images..")
            self.ui.progressBar.setProperty("value", i* 5)
            self._file_name = self.sample()
            #     #list files
            imgs = glob.glob(os.path.join(self._file_name, "*.dcm"))
            #
            try:
                data, header, mean_mA = DicomData.from_files(imgs)
                self.studies.append(data)
                self.study_headers.append(header)
                self.study_mean_MA.append(mean_mA)
            except:
                print("Could not load files")

        self.ui.progressBar.setProperty("value", self.progress * 5)
        self.magic()


    def magic(self):

        self.header = self.study_headers[self.progress]
        self.get_header_info(self.study_mean_MA[self.progress])
        self.ui.img.data = self.studies[self.progress]
        if self.progress == 0:  # if it's the first img set the width and the center to optimal values
            self.ui.img.window_center = 40.
            self.ui.img.window_width = 400.
        self.setWindowTitle("IEO Dicom Viewer")
        #self.file_list = imgs
        self.ui.img.index = 0
        self.ui.img.update_image()



    def magic_old(self):
        self._file_name = self.sample()
        #     #list files
        imgs=glob.glob(os.path.join( self._file_name,"*.dcm"))
        #

        try:
            self._file_name = self.sample()
            #     #list files
            imgs = glob.glob(os.path.join(self._file_name, "*.dcm"))
            data,header,mean_mA = DicomData.from_files(imgs)
            self.header=header
            self.get_header_info(mean_mA)
            self.ui.img.data = data
            if self.progress==0: #if it's the first img set the width and the center to optimal values
                self.ui.img.window_center=40.
                self.ui.img.window_width=400.
            self.setWindowTitle("IEO Dicom Viewer")
            self.file_list = imgs
            self.ui.img.index = 0
            self.ui.img.update_image()

        except BaseException as exc:
            print(exc)
            self.ui.img.data = None
            self.setWindowTitle("IEO Dicom Viewer: No image")


    def sample(self):
        """Pic a random number and choose newest or older images"""
        r=randint(0,1)
        if r:
            dir=NEW_DIR
            self.info["contrast_protocol"]="new"
        else:
            dir=OLD_DIR
            self.info["contrast_protocol"]="old"

        subjects= os.listdir(dir)
        rnd_sub_idx=randint(0,len(subjects)-1)
        return os.path.join(dir,subjects[rnd_sub_idx])


    def get_header_info(self,mean_mA):
        test=self.header
        info={
        "name": test.PatientName,
        "sex": test.PatientSex,
        "age": test.PatientAge,
        "birthday": test.PatientBirthDate,
        "patient_ID": test.PatientID,

        # study information
        "study_date": test.StudyDate,
        "study_time": test.StudyTime,
        "study_id": test.StudyID,
        "study_description": test.StudyDescription,
        "series_description": test.SeriesDescription,
        "model": test.ManufacturerModelName,
        "protocol": test.ProtocolName,

        # Other INFO
        "kVp": float(test.KVP),
     #   "mA": float(test.XRayTubeCurrent),  # QUA CAMBIA PER OGNI FETTA, FORSE ACQUISIZIONE?
        "mA": mean_mA,
        "contrast": test.ContrastBolusAgent,
        "filter_type": test.FilterType,
        "convKernel": test.ConvolutionKernel
        }

        self.info=info
        return info



app = QApplication(sys.argv)
dark_palette = QDarkPalette()
dark_palette.set_app(app)

window = MainWindow()
window.showMaximized()



sys.exit(app.exec_())

