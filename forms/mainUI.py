# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 698)
        self.actionZamknij = QAction(MainWindow)
        self.actionZamknij.setObjectName(u"actionZamknij")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.plainTextEditFilePath = QPlainTextEdit(self.centralwidget)
        self.plainTextEditFilePath.setObjectName(u"plainTextEditFilePath")
        self.plainTextEditFilePath.setMinimumSize(QSize(380, 100))
        self.plainTextEditFilePath.setMaximumSize(QSize(16777215, 100))
        self.plainTextEditFilePath.setReadOnly(True)

        self.horizontalLayout.addWidget(self.plainTextEditFilePath)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButtonChooseFIles = QPushButton(self.centralwidget)
        self.pushButtonChooseFIles.setObjectName(u"pushButtonChooseFIles")

        self.verticalLayout.addWidget(self.pushButtonChooseFIles)

        self.pushButtonLoadFiles = QPushButton(self.centralwidget)
        self.pushButtonLoadFiles.setObjectName(u"pushButtonLoadFiles")

        self.verticalLayout.addWidget(self.pushButtonLoadFiles)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.comboBoxLanguage = QComboBox(self.centralwidget)
        self.comboBoxLanguage.setObjectName(u"comboBoxLanguage")

        self.horizontalLayout_6.addWidget(self.comboBoxLanguage)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButtonRecognizeAll = QPushButton(self.centralwidget)
        self.pushButtonRecognizeAll.setObjectName(u"pushButtonRecognizeAll")
        self.pushButtonRecognizeAll.setMinimumSize(QSize(0, 100))
        font = QFont()
        font.setPointSize(14)
        self.pushButtonRecognizeAll.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonRecognizeAll)

        self.pushButtonRecognizeCurrent = QPushButton(self.centralwidget)
        self.pushButtonRecognizeCurrent.setObjectName(u"pushButtonRecognizeCurrent")
        self.pushButtonRecognizeCurrent.setMinimumSize(QSize(0, 100))
        self.pushButtonRecognizeCurrent.setFont(font)

        self.horizontalLayout_3.addWidget(self.pushButtonRecognizeCurrent)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_4)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.preview = QLabel(self.centralwidget)
        self.preview.setObjectName(u"preview")
        self.preview.setMinimumSize(QSize(300, 250))
        self.preview.setMaximumSize(QSize(300, 250))
        self.preview.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.preview)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButtonPreviewLeft = QPushButton(self.centralwidget)
        self.pushButtonPreviewLeft.setObjectName(u"pushButtonPreviewLeft")

        self.horizontalLayout_2.addWidget(self.pushButtonPreviewLeft)

        self.pushButtonPreviewRight = QPushButton(self.centralwidget)
        self.pushButtonPreviewRight.setObjectName(u"pushButtonPreviewRight")

        self.horizontalLayout_2.addWidget(self.pushButtonPreviewRight)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_3)


        self.horizontalLayout_5.addLayout(self.verticalLayout_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_7)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.verticalLayout_2.addWidget(self.label)

        self.plainTextEditOutput = QPlainTextEdit(self.centralwidget)
        self.plainTextEditOutput.setObjectName(u"plainTextEditOutput")

        self.verticalLayout_2.addWidget(self.plainTextEditOutput)


        self.verticalLayout_5.addLayout(self.verticalLayout_2)


        self.verticalLayout_6.addLayout(self.verticalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.comboBoxOutputTarget = QComboBox(self.centralwidget)
        self.comboBoxOutputTarget.setObjectName(u"comboBoxOutputTarget")

        self.horizontalLayout_4.addWidget(self.comboBoxOutputTarget)

        self.pushButtonSave = QPushButton(self.centralwidget)
        self.pushButtonSave.setObjectName(u"pushButtonSave")

        self.horizontalLayout_4.addWidget(self.pushButtonSave)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.gridLayout.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 21))
        self.menuPlik = QMenu(self.menubar)
        self.menuPlik.setObjectName(u"menuPlik")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPlik.menuAction())
        self.menuPlik.addAction(self.actionZamknij)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OCR-KR", None))
        self.actionZamknij.setText(QCoreApplication.translate("MainWindow", u"Zamknij", None))
        self.pushButtonChooseFIles.setText(QCoreApplication.translate("MainWindow", u"Wybierz plik", None))
        self.pushButtonLoadFiles.setText(QCoreApplication.translate("MainWindow", u"Za\u0142aduj plik", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"J\u0119zyk tekstu:", None))
        self.pushButtonRecognizeAll.setText(QCoreApplication.translate("MainWindow", u"Rozpoznaj wszystkie pliki", None))
        self.pushButtonRecognizeCurrent.setText(QCoreApplication.translate("MainWindow", u"Rozpoznaj bierz\u0105cy", None))
        self.preview.setText("")
        self.pushButtonPreviewLeft.setText(QCoreApplication.translate("MainWindow", u"<<<<", None))
        self.pushButtonPreviewRight.setText(QCoreApplication.translate("MainWindow", u">>>>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:11pt; font-weight:600;\">Rozpoznany tekst</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Zapisz do:", None))
        self.pushButtonSave.setText(QCoreApplication.translate("MainWindow", u"Zapisz", None))
        self.menuPlik.setTitle(QCoreApplication.translate("MainWindow", u"Plik", None))
    # retranslateUi

