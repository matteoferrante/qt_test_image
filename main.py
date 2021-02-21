import glob
import os
import sys
from random import randint

from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QScrollArea
from PyQt5.uic.properties import QtCore, QtWidgets
import cv2
import numpy as np

from dicom_data import DicomData
from ui.user_interface import Ui_MainWindow


#altro progetto
from dicom_widget import DicomWidget


#OVERALL VARIABLES


NEW_DIR=r"D:\FISICA MEDICA\MezzoDiContrasto\Immagini TEST MDC\NEW"
OLD_DIR=r"D:\FISICA MEDICA\MezzoDiContrasto\Immagini TEST MDC\OLD"

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()

        self.ui.setupUi(self)
        self.ui.img = DicomWidget(self)
        self.ui.pushButtonMax.clicked.connect(self.magic)

        #scroll_area = QtWidgets.QScrollArea()
        #scroll_area.setWidget(self.pix_label)


        #LAVORARE QUA -> METTERE FILE LIST PER CARICARE INTERE CARTELLE E TUTTA LA SERIE, CENTRARE LA VIEW, MOSTRARE ALCUNE INFO?

    def update_coordinates(self):
        self.ui.img.update_image()




    def cv2QtImg(self,path):
        cv_img=cv2.imread(path)
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w

        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)

        #p = convert_to_Qt_format.scaled(self.display_width, self.display_height, Qt.KeepAspectRatio)
        return QPixmap.fromImage(convert_to_Qt_format)

    #LAVORARE QUA AGGIUNGERE MODIFICA CONTRASTO IMMAGINI E CARICARE DICOM


    def magic(self):
        self._file_name = self.sample()
        #     #list files
        imgs=glob.glob(os.path.join( self._file_name,"*.dcm"))
        #

        try:
            self._file_name = self.sample()
            #     #list files
            imgs = glob.glob(os.path.join(self._file_name, "*.dcm"))
            data = DicomData.from_files(imgs)


            self.ui.img.data = data

            self.setWindowTitle("IEO Dicom Viewer")
            self.file_list = imgs
            self.ui.img.index = 0

        except BaseException as exc:
            print(exc)
            self.ui.img.data = None
            self.setWindowTitle("IEO Dicom Viewer: No image")


    def sample(self):
        """Pic a random number and choose newest or older images"""
        r=randint(0,1)
        if r:
            dir=NEW_DIR
        else:
            dir=OLD_DIR

        subjects= os.listdir(dir)
        rnd_sub_idx=randint(0,len(subjects)-1)
        return os.path.join(dir,subjects[rnd_sub_idx])



app = QApplication(sys.argv)

window = MainWindow()
window.show()



sys.exit(app.exec_())