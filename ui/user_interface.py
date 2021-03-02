# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\form.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

from dicom_widget import DicomWidget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 721)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem, 7, 1, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 13, 0, 1, 6)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 1, 1, 1)
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.gridLayout_2.addWidget(self.pushButtonStart, 9, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 1, 8, 1, 1)
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        self.gridLayout_2.addWidget(self.infoLabel, 11, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem3, 5, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 6, 1, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem5, 8, 1, 1, 1)
        self.plainTextPhysSign = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextPhysSign.setMaximumSize(QtCore.QSize(300, 60))
        self.plainTextPhysSign.setAcceptDrops(False)
        self.plainTextPhysSign.setAcceptRichText(False)
        self.plainTextPhysSign.setObjectName("plainTextPhysSign")
        self.gridLayout_2.addWidget(self.plainTextPhysSign, 2, 0, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem6, 1, 3, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem7, 11, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.pushButtonMax = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonMax.setFont(font)
        self.pushButtonMax.setObjectName("pushButtonMax")
        self.pushButtonMedium = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonMedium.setFont(font)
        self.pushButtonMedium.setObjectName("pushButtonMedium")
        self.pushButtonLow = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonLow.setFont(font)
        self.pushButtonLow.setObjectName("pushButtonLow")
        self.pushButtonInsufficient = QtWidgets.QPushButton(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.pushButtonInsufficient.setFont(font)
        self.pushButtonInsufficient.setObjectName("pushButtonInsufficient")
        self.gridLayout.addWidget(self.splitter, 0, 0, 4, 1)
        self.labelMaxImg = QtWidgets.QLabel(self.centralwidget)
        self.labelMaxImg.setObjectName("labelMaxImg")
        self.gridLayout.addWidget(self.labelMaxImg, 0, 1, 1, 1)
        self.labelMediumImg = QtWidgets.QLabel(self.centralwidget)
        self.labelMediumImg.setObjectName("labelMediumImg")
        self.gridLayout.addWidget(self.labelMediumImg, 1, 1, 1, 1)
        self.labelLowImg = QtWidgets.QLabel(self.centralwidget)
        self.labelLowImg.setObjectName("labelLowImg")
        self.gridLayout.addWidget(self.labelLowImg, 2, 1, 1, 1)
        self.labelInsufficientImg = QtWidgets.QLabel(self.centralwidget)
        self.labelInsufficientImg.setObjectName("labelInsufficientImg")
        self.gridLayout.addWidget(self.labelInsufficientImg, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 3, 6, 5, 3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem8, 1, 4, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem9, 12, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem10, 3, 1, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem11, 1, 6, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem12, 10, 1, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem13, 1, 7, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem14, 4, 1, 1, 1)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem15, 1, 2, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem16, 0, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 1, 5, 1, 1)
        #mia mod

        self.img=DicomWidget(MainWindow)
        self.img.setObjectName("img")
        self.gridLayout_2.addWidget(self.img, 3, 2, 6, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 990, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButtonStart.setText(_translate("MainWindow", "Avvia"))
        self.infoLabel.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonMax.setText(_translate("MainWindow", "Ottima"))
        self.pushButtonMedium.setText(_translate("MainWindow", "Media"))
        self.pushButtonLow.setText(_translate("MainWindow", "Bassa"))
        self.pushButtonInsufficient.setText(_translate("MainWindow", "Non sufficiente"))
        self.labelMaxImg.setText(_translate("MainWindow", "TextLabel"))
        self.labelMediumImg.setText(_translate("MainWindow", "TextLabel"))
        self.labelLowImg.setText(_translate("MainWindow", "TextLabel"))
        self.labelInsufficientImg.setText(_translate("MainWindow", "TextLabel"))
        #self.labelImage.setText(_translate("MainWindow", "TextLabel"))

