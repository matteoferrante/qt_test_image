# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\test_qt.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1049, 782)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plainTextPhysSign = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextPhysSign.setGeometry(QtCore.QRect(20, 80, 131, 31))
        self.plainTextPhysSign.setObjectName("plainTextPhysSign")
        self.pushButtonMax = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMax.setGeometry(QtCore.QRect(780, 240, 91, 21))
        self.pushButtonMax.setObjectName("pushButtonMax")
        self.pushButtonMedium = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonMedium.setGeometry(QtCore.QRect(780, 270, 91, 21))
        self.pushButtonMedium.setObjectName("pushButtonMedium")
        self.pushButtonLow = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonLow.setGeometry(QtCore.QRect(780, 300, 91, 21))
        self.pushButtonLow.setObjectName("pushButtonLow")
        self.pushButtonInsufficient = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInsufficient.setGeometry(QtCore.QRect(780, 330, 91, 21))
        self.pushButtonInsufficient.setObjectName("pushButtonInsufficient")
        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(790, 390, 131, 81))
        self.infoLabel.setObjectName("infoLabel")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(20, 120, 93, 28))
        self.pushButtonStart.setObjectName("pushButtonStart")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1049, 26))
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
        self.pushButtonMax.setText(_translate("MainWindow", "Ottima"))
        self.pushButtonMedium.setText(_translate("MainWindow", "Media"))
        self.pushButtonLow.setText(_translate("MainWindow", "Bassa"))
        self.pushButtonInsufficient.setText(_translate("MainWindow", "Non sufficiente"))
        self.infoLabel.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonStart.setText(_translate("MainWindow", "Inizia"))

