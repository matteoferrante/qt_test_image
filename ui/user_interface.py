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
        MainWindow.resize(1763, 897)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(250, 800, 1231, 24))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.progressBar.setFont(font)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 258, 771))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.plainTextPhysSign = QtWidgets.QPlainTextEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextPhysSign.sizePolicy().hasHeightForWidth())
        self.plainTextPhysSign.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.plainTextPhysSign.setFont(font)
        self.plainTextPhysSign.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextPhysSign.setObjectName("plainTextPhysSign")
        self.verticalLayout_2.addWidget(self.plainTextPhysSign, 0, QtCore.Qt.AlignVCenter)
        self.pushButtonStart = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonStart.sizePolicy().hasHeightForWidth())
        self.pushButtonStart.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.verticalLayout_2.addWidget(self.pushButtonStart)
        self.infoLabel = QtWidgets.QLabel(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoLabel.sizePolicy().hasHeightForWidth())
        self.infoLabel.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.infoLabel.setFont(font)
        self.infoLabel.setObjectName("infoLabel")
        self.verticalLayout_2.addWidget(self.infoLabel, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(270, 10, 1021, 771))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(1300, 70, 451, 661))
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
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
        self.labelMaxImg = QtWidgets.QLabel(self.widget)
        self.labelMaxImg.setObjectName("labelMaxImg")
        self.gridLayout.addWidget(self.labelMaxImg, 0, 1, 1, 1)
        self.labelMediumImg = QtWidgets.QLabel(self.widget)
        self.labelMediumImg.setObjectName("labelMediumImg")
        self.gridLayout.addWidget(self.labelMediumImg, 1, 1, 1, 1)
        self.labelLowImg = QtWidgets.QLabel(self.widget)
        self.labelLowImg.setObjectName("labelLowImg")
        self.gridLayout.addWidget(self.labelLowImg, 2, 1, 1, 1)
        self.labelInsufficientImg = QtWidgets.QLabel(self.widget)
        self.labelInsufficientImg.setObjectName("labelInsufficientImg")
        self.gridLayout.addWidget(self.labelInsufficientImg, 3, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1763, 26))
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
        self.label.setText(_translate("MainWindow", "Nome del medico:"))
        self.pushButtonStart.setText(_translate("MainWindow", "Inizia"))
        self.infoLabel.setText(_translate("MainWindow", "TextLabel"))
        self.pushButtonMax.setText(_translate("MainWindow", "Ottima"))
        self.pushButtonMedium.setText(_translate("MainWindow", "Media"))
        self.pushButtonLow.setText(_translate("MainWindow", "Bassa"))
        self.pushButtonInsufficient.setText(_translate("MainWindow", "Insufficiente"))
        self.labelMaxImg.setText(_translate("MainWindow", "TextLabel"))
        self.labelMediumImg.setText(_translate("MainWindow", "TextLabel"))
        self.labelLowImg.setText(_translate("MainWindow", "TextLabel"))
        self.labelInsufficientImg.setText(_translate("MainWindow", "TextLabel"))

