# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'translateUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_TranslateWindow(object):
    def setupUi(self, TranslateWindow):
        if not TranslateWindow.objectName():
            TranslateWindow.setObjectName(u"TranslateWindow")
        TranslateWindow.resize(855, 600)
        TranslateWindow.setMinimumSize(QSize(855, 600))
        self.gridLayout = QGridLayout(TranslateWindow)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frameTranslate = QFrame(TranslateWindow)
        self.frameTranslate.setObjectName(u"frameTranslate")
        self.frameTranslate.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.frameTranslate.setFrameShape(QFrame.StyledPanel)
        self.frameTranslate.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frameTranslate)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.frameTranslate)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMaximumSize(QSize(16777215, 50))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setSpacing(30)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(70, 16777215))
        font = QFont()
        font.setFamily(u"Impact")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.comboBoxFromLanguage = QComboBox(self.frame)
        self.comboBoxFromLanguage.setObjectName(u"comboBoxFromLanguage")
        self.comboBoxFromLanguage.setMinimumSize(QSize(50, 30))
        font1 = QFont()
        font1.setFamily(u"Impact")
        font1.setPointSize(10)
        self.comboBoxFromLanguage.setFont(font1)
        self.comboBoxFromLanguage.setStyleSheet(u"QComboBox{\n"
"	color:rgb(255, 255, 255);\n"
"	background-color: rgb(27, 27, 27);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(27, 27, 27);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(27, 27, 27);\n"
"}\n"
"QComboBox::drop-down {\n"
"color:rgb(255, 255, 255);\n"
"\n"
"	width: 25px; \n"
"\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 27, 27);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 27, 27);\n"
"}")

        self.horizontalLayout_10.addWidget(self.comboBoxFromLanguage)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 16777215))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.label_3)

        self.comboBoxToLanguage = QComboBox(self.frame)
        self.comboBoxToLanguage.setObjectName(u"comboBoxToLanguage")
        self.comboBoxToLanguage.setMinimumSize(QSize(50, 30))
        self.comboBoxToLanguage.setFont(font1)
        self.comboBoxToLanguage.setStyleSheet(u"QComboBox{\n"
"color:rgb(255, 255, 255);\n"
"	background-color: rgb(27, 27, 27);\n"
"	border-radius: 10px;\n"
"	border: 2px solid rgb(27, 27, 27);\n"
"	padding: 5px;\n"
"	padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"	border: 2px solid rgb(27, 27, 27);\n"
"}\n"
"QComboBox::drop-down {\n"
"color:rgb(255, 255, 255);\n"
"\n"
"	width: 25px; \n"
"\n"
" }\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(27, 27, 27);\n"
"	padding: 10px;\n"
"	selection-background-color: rgb(27, 27, 27);\n"
"}")

        self.horizontalLayout_11.addWidget(self.comboBoxToLanguage)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_11)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.frameTranslate)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setMaximumSize(QSize(16777215, 60))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(50)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(9, 0, 9, 0)
        self.frame_6 = QFrame(self.frame_2)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMinimumSize(QSize(100, 0))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.frame_6)
        self.label.setObjectName(u"label")
        font2 = QFont()
        font2.setFamily(u"Impact")
        font2.setPointSize(11)
        self.label.setFont(font2)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.label)

        self.labelSearchLanguage = QLabel(self.frame_6)
        self.labelSearchLanguage.setObjectName(u"labelSearchLanguage")
        self.labelSearchLanguage.setFont(font2)
        self.labelSearchLanguage.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_6.addWidget(self.labelSearchLanguage)


        self.horizontalLayout_2.addWidget(self.frame_6)

        self.btnTranslateEverything = QPushButton(self.frame_2)
        self.btnTranslateEverything.setObjectName(u"btnTranslateEverything")
        sizePolicy.setHeightForWidth(self.btnTranslateEverything.sizePolicy().hasHeightForWidth())
        self.btnTranslateEverything.setSizePolicy(sizePolicy)
        self.btnTranslateEverything.setMinimumSize(QSize(0, 0))
        self.btnTranslateEverything.setMaximumSize(QSize(200, 50))
        font3 = QFont()
        font3.setFamily(u"Impact")
        font3.setPointSize(14)
        font3.setBold(False)
        font3.setWeight(50)
        font3.setKerning(True)
        self.btnTranslateEverything.setFont(font3)
        self.btnTranslateEverything.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnTranslateEverything.setAutoFillBackground(False)
        self.btnTranslateEverything.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnTranslateEverything.setAutoRepeat(False)

        self.horizontalLayout_2.addWidget(self.btnTranslateEverything)

        self.btnTranslateSelected = QPushButton(self.frame_2)
        self.btnTranslateSelected.setObjectName(u"btnTranslateSelected")
        sizePolicy.setHeightForWidth(self.btnTranslateSelected.sizePolicy().hasHeightForWidth())
        self.btnTranslateSelected.setSizePolicy(sizePolicy)
        self.btnTranslateSelected.setMinimumSize(QSize(0, 0))
        self.btnTranslateSelected.setMaximumSize(QSize(200, 50))
        self.btnTranslateSelected.setFont(font3)
        self.btnTranslateSelected.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnTranslateSelected.setAutoFillBackground(False)
        self.btnTranslateSelected.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnTranslateSelected.setAutoRepeat(False)

        self.horizontalLayout_2.addWidget(self.btnTranslateSelected)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frameTranslate)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setSpacing(15)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.plainTextEditOriginalText = QPlainTextEdit(self.frame_3)
        self.plainTextEditOriginalText.setObjectName(u"plainTextEditOriginalText")
        self.plainTextEditOriginalText.setMinimumSize(QSize(400, 100))
        self.plainTextEditOriginalText.setMaximumSize(QSize(16777215, 16666666))
        font4 = QFont()
        font4.setPointSize(11)
        self.plainTextEditOriginalText.setFont(font4)
        self.plainTextEditOriginalText.setStyleSheet(u"QPlainTextEdit{\n"
"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
" border-bottom-left-radius:10px;\n"
" border-top-left-radius:10px;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
" background: rgb(27, 27, 27);\n"
"width: 14px;\n"
"margin: 5px 0 5px 0;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: rgb(0, 0, 0);\n"
"min-height: 25px;\n"
"border-radius: 7px\n"
" }\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"   background: rgb(27, 27, 27);\n"
"    height: 10px;\n"
"  subcontrol-position: bottom;\n"
"border-bottom-right-radius: 10px;\n"
" subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"   background:rgb(27, 27, 27);\n"
"     height: 20px;\n"
"border-top-right-radius: 10px;\n"
"    subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
" }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScr"
                        "ollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.plainTextEditOriginalText.setFrameShape(QFrame.NoFrame)
        self.plainTextEditOriginalText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout_4.addWidget(self.plainTextEditOriginalText)

        self.plainTextEditTranslateText = QPlainTextEdit(self.frame_3)
        self.plainTextEditTranslateText.setObjectName(u"plainTextEditTranslateText")
        self.plainTextEditTranslateText.setMinimumSize(QSize(400, 400))
        self.plainTextEditTranslateText.setMaximumSize(QSize(16777215, 16666666))
        self.plainTextEditTranslateText.setFont(font4)
        self.plainTextEditTranslateText.setStyleSheet(u"QPlainTextEdit{\n"
"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
" border-bottom-left-radius:10px;\n"
" border-top-left-radius:10px;\n"
"}\n"
"QScrollBar:vertical {\n"
"border: none;\n"
" background: rgb(27, 27, 27);\n"
"width: 14px;\n"
"margin: 5px 0 5px 0;\n"
"border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:vertical {\n"
"background: rgb(0, 0, 0);\n"
"min-height: 25px;\n"
"border-radius: 7px\n"
" }\n"
"QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"   background: rgb(27, 27, 27);\n"
"    height: 10px;\n"
"  subcontrol-position: bottom;\n"
"border-bottom-right-radius: 10px;\n"
" subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:vertical {\n"
"	border: none;\n"
"   background:rgb(27, 27, 27);\n"
"     height: 20px;\n"
"border-top-right-radius: 10px;\n"
"    subcontrol-position: top;\n"
"  subcontrol-origin: margin;\n"
" }\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
"}\n"
"\n"
"QScrollBar::add-page:vertical, QScr"
                        "ollBar::sub-page:vertical {\n"
"     background: none;\n"
" }")
        self.plainTextEditTranslateText.setFrameShape(QFrame.NoFrame)
        self.plainTextEditTranslateText.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.horizontalLayout_4.addWidget(self.plainTextEditTranslateText)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_5 = QFrame(self.frameTranslate)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy)
        self.frame_5.setMaximumSize(QSize(16777215, 60))
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 10)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(450, 0))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(9, 0, 9, 20)
        self.btnSaveOnlyTranslate = QPushButton(self.frame_4)
        self.btnSaveOnlyTranslate.setObjectName(u"btnSaveOnlyTranslate")
        self.btnSaveOnlyTranslate.setMinimumSize(QSize(150, 50))
        font5 = QFont()
        font5.setBold(True)
        font5.setWeight(75)
        font5.setKerning(True)
        self.btnSaveOnlyTranslate.setFont(font5)
        self.btnSaveOnlyTranslate.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnSaveOnlyTranslate.setAutoFillBackground(False)
        self.btnSaveOnlyTranslate.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/content/resources/icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSaveOnlyTranslate.setIcon(icon)
        self.btnSaveOnlyTranslate.setIconSize(QSize(35, 35))
        self.btnSaveOnlyTranslate.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.btnSaveOnlyTranslate)

        self.btnSaveEverything = QPushButton(self.frame_4)
        self.btnSaveEverything.setObjectName(u"btnSaveEverything")
        self.btnSaveEverything.setMinimumSize(QSize(50, 50))
        self.btnSaveEverything.setFont(font5)
        self.btnSaveEverything.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnSaveEverything.setAutoFillBackground(False)
        self.btnSaveEverything.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnSaveEverything.setIcon(icon)
        self.btnSaveEverything.setIconSize(QSize(35, 35))
        self.btnSaveEverything.setAutoRepeat(False)

        self.horizontalLayout.addWidget(self.btnSaveEverything)


        self.horizontalLayout_5.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frameTranslate, 0, 0, 1, 1)


        self.retranslateUi(TranslateWindow)

        QMetaObject.connectSlotsByName(TranslateWindow)
    # setupUi

    def retranslateUi(self, TranslateWindow):
        TranslateWindow.setWindowTitle(QCoreApplication.translate("TranslateWindow", u"T\u0142umaczenie", None))
        self.label_2.setText(QCoreApplication.translate("TranslateWindow", u"<html><head/><body><p>Z j\u0119zyka:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("TranslateWindow", u"<html><head/><body><p>Na:</p></body></html>", None))
        self.label.setText(QCoreApplication.translate("TranslateWindow", u"<html><head/><body><p>Wykryty j\u0119zyk:</p></body></html>", None))
        self.labelSearchLanguage.setText("")
        self.btnTranslateEverything.setText(QCoreApplication.translate("TranslateWindow", u"T\u0142umacz wszystko", None))
        self.btnTranslateSelected.setText(QCoreApplication.translate("TranslateWindow", u"T\u0142umacz zaznaczone", None))
        self.btnSaveOnlyTranslate.setText(QCoreApplication.translate("TranslateWindow", u"   Zapisz t\u0142umaczenie", None))
        self.btnSaveEverything.setText(QCoreApplication.translate("TranslateWindow", u"   Zapisz orygina\u0142 i t\u0142umaczenie", None))
    # retranslateUi

