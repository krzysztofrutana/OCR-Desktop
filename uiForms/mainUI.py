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
        MainWindow.resize(1000, 550)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1000, 550))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameTopBar = QFrame(self.centralwidget)
        self.FrameTopBar.setObjectName(u"FrameTopBar")
        sizePolicy.setHeightForWidth(self.FrameTopBar.sizePolicy().hasHeightForWidth())
        self.FrameTopBar.setSizePolicy(sizePolicy)
        self.FrameTopBar.setMaximumSize(QSize(16777215, 40))
        self.FrameTopBar.setStyleSheet(u"")
        self.FrameTopBar.setFrameShape(QFrame.NoFrame)
        self.FrameTopBar.setFrameShadow(QFrame.Raised)
        self.FrameTopBar.setLineWidth(0)
        self.horizontalLayout = QHBoxLayout(self.FrameTopBar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.FrameToogleButton = QFrame(self.FrameTopBar)
        self.FrameToogleButton.setObjectName(u"FrameToogleButton")
        sizePolicy.setHeightForWidth(self.FrameToogleButton.sizePolicy().hasHeightForWidth())
        self.FrameToogleButton.setSizePolicy(sizePolicy)
        self.FrameToogleButton.setMinimumSize(QSize(50, 0))
        self.FrameToogleButton.setMaximumSize(QSize(70, 40))
        self.FrameToogleButton.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.FrameToogleButton.setFrameShape(QFrame.NoFrame)
        self.FrameToogleButton.setFrameShadow(QFrame.Raised)
        self.FrameToogleButton.setLineWidth(0)
        self.verticalLayout_2 = QVBoxLayout(self.FrameToogleButton)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btnToogleMenu = QPushButton(self.FrameToogleButton)
        self.btnToogleMenu.setObjectName(u"btnToogleMenu")
        sizePolicy.setHeightForWidth(self.btnToogleMenu.sizePolicy().hasHeightForWidth())
        self.btnToogleMenu.setSizePolicy(sizePolicy)
        self.btnToogleMenu.setMinimumSize(QSize(50, 0))
        self.btnToogleMenu.setMaximumSize(QSize(70, 40))
        self.btnToogleMenu.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: 0px solid;\n"
"font: 75 20pt \"MS Shell Dlg 2\";")
        icon = QIcon()
        iconThemeName = u"UI"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)
        
        self.btnToogleMenu.setIcon(icon)

        self.verticalLayout_2.addWidget(self.btnToogleMenu)


        self.horizontalLayout.addWidget(self.FrameToogleButton)

        self.FrameTop = QFrame(self.FrameTopBar)
        self.FrameTop.setObjectName(u"FrameTop")
        sizePolicy.setHeightForWidth(self.FrameTop.sizePolicy().hasHeightForWidth())
        self.FrameTop.setSizePolicy(sizePolicy)
        self.FrameTop.setMaximumSize(QSize(16777215, 40))
        self.FrameTop.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.FrameTop.setFrameShape(QFrame.NoFrame)
        self.FrameTop.setFrameShadow(QFrame.Raised)
        self.FrameTop.setLineWidth(0)

        self.horizontalLayout.addWidget(self.FrameTop)

        self.FrameWindowBtn = QFrame(self.FrameTopBar)
        self.FrameWindowBtn.setObjectName(u"FrameWindowBtn")
        sizePolicy.setHeightForWidth(self.FrameWindowBtn.sizePolicy().hasHeightForWidth())
        self.FrameWindowBtn.setSizePolicy(sizePolicy)
        self.FrameWindowBtn.setMaximumSize(QSize(150, 16777215))
        self.FrameWindowBtn.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.FrameWindowBtn.setFrameShape(QFrame.StyledPanel)
        self.FrameWindowBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.FrameWindowBtn)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(2, 0, 2, 0)
        self.btnMinimize = QPushButton(self.FrameWindowBtn)
        self.btnMinimize.setObjectName(u"btnMinimize")
        self.btnMinimize.setMinimumSize(QSize(0, 30))
        self.btnMinimize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnMinimize.setIconSize(QSize(16, 16))
        self.btnMinimize.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btnMinimize)

        self.btnMaximize = QPushButton(self.FrameWindowBtn)
        self.btnMaximize.setObjectName(u"btnMaximize")
        self.btnMaximize.setMinimumSize(QSize(0, 30))
        self.btnMaximize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnMaximize.setIconSize(QSize(16, 16))
        self.btnMaximize.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btnMaximize)

        self.btnX = QPushButton(self.FrameWindowBtn)
        self.btnX.setObjectName(u"btnX")
        self.btnX.setMinimumSize(QSize(0, 30))
        self.btnX.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnX.setIconSize(QSize(16, 16))
        self.btnX.setFlat(True)

        self.horizontalLayout_9.addWidget(self.btnX)


        self.horizontalLayout.addWidget(self.FrameWindowBtn)


        self.verticalLayout.addWidget(self.FrameTopBar)

        self.FrameContent = QFrame(self.centralwidget)
        self.FrameContent.setObjectName(u"FrameContent")
        self.FrameContent.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.FrameContent.setFrameShape(QFrame.NoFrame)
        self.FrameContent.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.FrameContent)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.FrameMenu = QFrame(self.FrameContent)
        self.FrameMenu.setObjectName(u"FrameMenu")
        sizePolicy.setHeightForWidth(self.FrameMenu.sizePolicy().hasHeightForWidth())
        self.FrameMenu.setSizePolicy(sizePolicy)
        self.FrameMenu.setMinimumSize(QSize(70, 0))
        self.FrameMenu.setMaximumSize(QSize(70, 16777215))
        self.FrameMenu.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.FrameMenu.setFrameShape(QFrame.NoFrame)
        self.FrameMenu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.FrameMenu)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.FrameMenOptions = QFrame(self.FrameMenu)
        self.FrameMenOptions.setObjectName(u"FrameMenOptions")
        self.FrameMenOptions.setFrameShape(QFrame.NoFrame)
        self.FrameMenOptions.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.FrameMenOptions)
        self.verticalLayout_5.setSpacing(10)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 0)
        self.btnImageRecognize = QPushButton(self.FrameMenOptions)
        self.btnImageRecognize.setObjectName(u"btnImageRecognize")
        self.btnImageRecognize.setMinimumSize(QSize(70, 70))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(True)
        self.btnImageRecognize.setFont(font)
        self.btnImageRecognize.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnImageRecognize.setAutoFillBackground(False)
        self.btnImageRecognize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Icons/64x64Image.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnImageRecognize.setIcon(icon1)
        self.btnImageRecognize.setIconSize(QSize(60, 60))
        self.btnImageRecognize.setAutoRepeat(False)

        self.verticalLayout_5.addWidget(self.btnImageRecognize)

        self.btnPDFRecognize = QPushButton(self.FrameMenOptions)
        self.btnPDFRecognize.setObjectName(u"btnPDFRecognize")
        self.btnPDFRecognize.setMinimumSize(QSize(70, 70))
        font1 = QFont()
        font1.setBold(True)
        font1.setWeight(75)
        self.btnPDFRecognize.setFont(font1)
        self.btnPDFRecognize.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"border: 0px solid;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Icons/64x64PDF.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPDFRecognize.setIcon(icon2)
        self.btnPDFRecognize.setIconSize(QSize(60, 60))
        self.btnPDFRecognize.setAutoRepeat(True)

        self.verticalLayout_5.addWidget(self.btnPDFRecognize)


        self.verticalLayout_3.addWidget(self.FrameMenOptions, 0, Qt.AlignTop)

        self.FrameCopyright = QFrame(self.FrameMenu)
        self.FrameCopyright.setObjectName(u"FrameCopyright")
        self.FrameCopyright.setMinimumSize(QSize(0, 70))
        self.FrameCopyright.setMaximumSize(QSize(16777215, 70))
        self.FrameCopyright.setFrameShape(QFrame.NoFrame)
        self.FrameCopyright.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.FrameCopyright)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.LabelCopyright = QLabel(self.FrameCopyright)
        self.LabelCopyright.setObjectName(u"LabelCopyright")
        self.LabelCopyright.setEnabled(True)
        sizePolicy.setHeightForWidth(self.LabelCopyright.sizePolicy().hasHeightForWidth())
        self.LabelCopyright.setSizePolicy(sizePolicy)
        self.LabelCopyright.setMaximumSize(QSize(16777215, 70))
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(50)
        self.LabelCopyright.setFont(font2)
        self.LabelCopyright.setStyleSheet(u"font: 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border: 0px solid;")
        self.LabelCopyright.setTextFormat(Qt.AutoText)
        self.LabelCopyright.setAlignment(Qt.AlignCenter)
        self.LabelCopyright.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout_4.addWidget(self.LabelCopyright)


        self.verticalLayout_3.addWidget(self.FrameCopyright)


        self.horizontalLayout_2.addWidget(self.FrameMenu)

        self.FrameAppContent = QFrame(self.FrameContent)
        self.FrameAppContent.setObjectName(u"FrameAppContent")
        self.FrameAppContent.setFrameShape(QFrame.NoFrame)
        self.FrameAppContent.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.FrameAppContent)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Pages = QStackedWidget(self.FrameAppContent)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setFrameShadow(QFrame.Plain)
        self.Pages.setLineWidth(0)
        self.Image = QWidget()
        self.Image.setObjectName(u"Image")
        self.verticalLayout_10 = QVBoxLayout(self.Image)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.FrameContentUp = QFrame(self.Image)
        self.FrameContentUp.setObjectName(u"FrameContentUp")
        self.FrameContentUp.setMinimumSize(QSize(0, 300))
        self.FrameContentUp.setFrameShape(QFrame.NoFrame)
        self.FrameContentUp.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.FrameContentUp)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.FrameContentLeftSide = QFrame(self.FrameContentUp)
        self.FrameContentLeftSide.setObjectName(u"FrameContentLeftSide")
        self.FrameContentLeftSide.setMinimumSize(QSize(550, 300))
        self.FrameContentLeftSide.setFrameShape(QFrame.NoFrame)
        self.FrameContentLeftSide.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.FrameContentLeftSide)
        self.verticalLayout_9.setSpacing(20)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.FrameChooseFiles = QFrame(self.FrameContentLeftSide)
        self.FrameChooseFiles.setObjectName(u"FrameChooseFiles")
        self.FrameChooseFiles.setMinimumSize(QSize(0, 100))
        self.FrameChooseFiles.setFrameShape(QFrame.NoFrame)
        self.FrameChooseFiles.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.FrameChooseFiles)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.plainTextEditFilePathImage = QPlainTextEdit(self.FrameChooseFiles)
        self.plainTextEditFilePathImage.setObjectName(u"plainTextEditFilePathImage")
        self.plainTextEditFilePathImage.setMinimumSize(QSize(300, 80))
        self.plainTextEditFilePathImage.setMaximumSize(QSize(16777215, 80))
        font3 = QFont()
        font3.setFamily(u"Impact")
        font3.setPointSize(10)
        self.plainTextEditFilePathImage.setFont(font3)
        self.plainTextEditFilePathImage.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
" border-radius:20px;")
        self.plainTextEditFilePathImage.setFrameShape(QFrame.NoFrame)
        self.plainTextEditFilePathImage.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.plainTextEditFilePathImage)

        self.btnChooseFIlesImage = QPushButton(self.FrameChooseFiles)
        self.btnChooseFIlesImage.setObjectName(u"btnChooseFIlesImage")
        self.btnChooseFIlesImage.setMinimumSize(QSize(80, 80))
        self.btnChooseFIlesImage.setFont(font)
        self.btnChooseFIlesImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnChooseFIlesImage.setAutoFillBackground(False)
        self.btnChooseFIlesImage.setStyleSheet(u"QPushButton{\n"
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
        icon3 = QIcon()
        icon3.addFile(u"Icons/computer-folder-open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnChooseFIlesImage.setIcon(icon3)
        self.btnChooseFIlesImage.setIconSize(QSize(50, 50))
        self.btnChooseFIlesImage.setAutoRepeat(False)

        self.horizontalLayout_3.addWidget(self.btnChooseFIlesImage)


        self.verticalLayout_9.addWidget(self.FrameChooseFiles)

        self.FrameChoosingLanguage = QFrame(self.FrameContentLeftSide)
        self.FrameChoosingLanguage.setObjectName(u"FrameChoosingLanguage")
        sizePolicy.setHeightForWidth(self.FrameChoosingLanguage.sizePolicy().hasHeightForWidth())
        self.FrameChoosingLanguage.setSizePolicy(sizePolicy)
        self.FrameChoosingLanguage.setMinimumSize(QSize(0, 0))
        self.FrameChoosingLanguage.setFrameShape(QFrame.NoFrame)
        self.FrameChoosingLanguage.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.FrameChoosingLanguage)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(20, 0, 0, 0)
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.FrameChoosingLanguage)
        self.label_2.setObjectName(u"label_2")
        font4 = QFont()
        font4.setFamily(u"Impact")
        font4.setPointSize(11)
        self.label_2.setFont(font4)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_10.addWidget(self.label_2)

        self.comboBoxLanguageImage = QComboBox(self.FrameChoosingLanguage)
        self.comboBoxLanguageImage.setObjectName(u"comboBoxLanguageImage")
        self.comboBoxLanguageImage.setMinimumSize(QSize(35, 35))
        self.comboBoxLanguageImage.setFont(font3)
        self.comboBoxLanguageImage.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_10.addWidget(self.comboBoxLanguageImage)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_10)

        self.checkBoxSecondLanguageImage = QCheckBox(self.FrameChoosingLanguage)
        self.checkBoxSecondLanguageImage.setObjectName(u"checkBoxSecondLanguageImage")
        self.checkBoxSecondLanguageImage.setFont(font4)
        self.checkBoxSecondLanguageImage.setStyleSheet(u"QCheckBox {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"   border: 3px solid rgb(0, 0, 0);\n"
"width: 15px;\n"
"height: 15px;\n"
"	border-radius: 10px;\n"
" background: rgb(27, 27, 27);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(0, 0, 0);\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(85, 170, 255);\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_11.addWidget(self.checkBoxSecondLanguageImage)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBoxSecondLanguageImage = QComboBox(self.FrameChoosingLanguage)
        self.comboBoxSecondLanguageImage.setObjectName(u"comboBoxSecondLanguageImage")
        self.comboBoxSecondLanguageImage.setMinimumSize(QSize(35, 35))
        self.comboBoxSecondLanguageImage.setFont(font3)
        self.comboBoxSecondLanguageImage.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_5.addWidget(self.comboBoxSecondLanguageImage)


        self.horizontalLayout_11.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer)


        self.verticalLayout_9.addWidget(self.FrameChoosingLanguage)

        self.FrameQueue = QFrame(self.FrameContentLeftSide)
        self.FrameQueue.setObjectName(u"FrameQueue")
        sizePolicy.setHeightForWidth(self.FrameQueue.sizePolicy().hasHeightForWidth())
        self.FrameQueue.setSizePolicy(sizePolicy)
        self.FrameQueue.setMinimumSize(QSize(0, 30))
        self.FrameQueue.setMaximumSize(QSize(16777215, 1000))
        self.FrameQueue.setFont(font3)
        self.FrameQueue.setFrameShape(QFrame.StyledPanel)
        self.FrameQueue.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.FrameQueue)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.FrameQueue)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(70, 16777215))
        font5 = QFont()
        font5.setFamily(u"Impact")
        font5.setPointSize(12)
        self.label.setFont(font5)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_8.addWidget(self.label)

        self.textEditQueueImage = QTextEdit(self.FrameQueue)
        self.textEditQueueImage.setObjectName(u"textEditQueueImage")
        self.textEditQueueImage.setMinimumSize(QSize(0, 30))
        self.textEditQueueImage.setMaximumSize(QSize(16777215, 50))
        self.textEditQueueImage.setFont(font3)
        self.textEditQueueImage.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
" border-radius:10px;}\n"
"\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: n"
                        "one;\n"
" }")

        self.horizontalLayout_8.addWidget(self.textEditQueueImage)

        self.btnClearQueueImage = QPushButton(self.FrameQueue)
        self.btnClearQueueImage.setObjectName(u"btnClearQueueImage")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.btnClearQueueImage.sizePolicy().hasHeightForWidth())
        self.btnClearQueueImage.setSizePolicy(sizePolicy1)
        self.btnClearQueueImage.setMinimumSize(QSize(120, 30))
        self.btnClearQueueImage.setMaximumSize(QSize(50, 50))
        font6 = QFont()
        font6.setFamily(u"Impact")
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setWeight(50)
        font6.setKerning(True)
        self.btnClearQueueImage.setFont(font6)
        self.btnClearQueueImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnClearQueueImage.setAutoFillBackground(False)
        self.btnClearQueueImage.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnClearQueueImage.setIconSize(QSize(30, 30))
        self.btnClearQueueImage.setAutoRepeat(False)

        self.horizontalLayout_8.addWidget(self.btnClearQueueImage)


        self.verticalLayout_9.addWidget(self.FrameQueue)

        self.FrameRecognizeButtons = QFrame(self.FrameContentLeftSide)
        self.FrameRecognizeButtons.setObjectName(u"FrameRecognizeButtons")
        sizePolicy.setHeightForWidth(self.FrameRecognizeButtons.sizePolicy().hasHeightForWidth())
        self.FrameRecognizeButtons.setSizePolicy(sizePolicy)
        self.FrameRecognizeButtons.setMinimumSize(QSize(500, 0))
        self.FrameRecognizeButtons.setMaximumSize(QSize(16777215, 1000))
        self.FrameRecognizeButtons.setFrameShape(QFrame.NoFrame)
        self.FrameRecognizeButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.FrameRecognizeButtons)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 10)
        self.btnRecognizeAllImage = QPushButton(self.FrameRecognizeButtons)
        self.btnRecognizeAllImage.setObjectName(u"btnRecognizeAllImage")
        sizePolicy1.setHeightForWidth(self.btnRecognizeAllImage.sizePolicy().hasHeightForWidth())
        self.btnRecognizeAllImage.setSizePolicy(sizePolicy1)
        self.btnRecognizeAllImage.setMinimumSize(QSize(0, 0))
        self.btnRecognizeAllImage.setMaximumSize(QSize(16777215, 1000))
        self.btnRecognizeAllImage.setFont(font6)
        self.btnRecognizeAllImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnRecognizeAllImage.setAutoFillBackground(False)
        self.btnRecognizeAllImage.setStyleSheet(u"QPushButton{\n"
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
        self.btnRecognizeAllImage.setAutoRepeat(False)

        self.horizontalLayout_6.addWidget(self.btnRecognizeAllImage)

        self.btnRecognizeCurrentImage = QPushButton(self.FrameRecognizeButtons)
        self.btnRecognizeCurrentImage.setObjectName(u"btnRecognizeCurrentImage")
        sizePolicy1.setHeightForWidth(self.btnRecognizeCurrentImage.sizePolicy().hasHeightForWidth())
        self.btnRecognizeCurrentImage.setSizePolicy(sizePolicy1)
        self.btnRecognizeCurrentImage.setMinimumSize(QSize(0, 60))
        self.btnRecognizeCurrentImage.setMaximumSize(QSize(16777215, 1000))
        self.btnRecognizeCurrentImage.setFont(font4)
        self.btnRecognizeCurrentImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnRecognizeCurrentImage.setAutoFillBackground(False)
        self.btnRecognizeCurrentImage.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnRecognizeCurrentImage.setAutoRepeat(False)

        self.horizontalLayout_6.addWidget(self.btnRecognizeCurrentImage)


        self.verticalLayout_9.addWidget(self.FrameRecognizeButtons, 0, Qt.AlignHCenter)


        self.horizontalLayout_7.addWidget(self.FrameContentLeftSide)

        self.FramePreviewImage = QFrame(self.FrameContentUp)
        self.FramePreviewImage.setObjectName(u"FramePreviewImage")
        sizePolicy1.setHeightForWidth(self.FramePreviewImage.sizePolicy().hasHeightForWidth())
        self.FramePreviewImage.setSizePolicy(sizePolicy1)
        self.FramePreviewImage.setMinimumSize(QSize(100, 300))
        self.FramePreviewImage.setFrameShape(QFrame.NoFrame)
        self.FramePreviewImage.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.FramePreviewImage)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.FramePreviewImage)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setMinimumSize(QSize(0, 220))
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.previewImage = QLabel(self.frame_9)
        self.previewImage.setObjectName(u"previewImage")
        sizePolicy.setHeightForWidth(self.previewImage.sizePolicy().hasHeightForWidth())
        self.previewImage.setSizePolicy(sizePolicy)
        self.previewImage.setMinimumSize(QSize(100, 190))
        self.previewImage.setMaximumSize(QSize(800, 500))
        self.previewImage.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 5px solid;")
        self.previewImage.setPixmap(QPixmap(u"Icons/128x128 Preview.png"))
        self.previewImage.setScaledContents(False)
        self.previewImage.setAlignment(Qt.AlignCenter)
        self.previewImage.setMargin(0)

        self.horizontalLayout_4.addWidget(self.previewImage)


        self.verticalLayout_7.addWidget(self.frame_9)

        self.frame_8 = QFrame(self.FramePreviewImage)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMinimumSize(QSize(0, 34))
        self.frame_8.setMaximumSize(QSize(16777215, 15))
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_3 = QLabel(self.frame_8)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_3)

        self.labelCurrentImageNumber = QLabel(self.frame_8)
        self.labelCurrentImageNumber.setObjectName(u"labelCurrentImageNumber")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.labelCurrentImageNumber.sizePolicy().hasHeightForWidth())
        self.labelCurrentImageNumber.setSizePolicy(sizePolicy3)
        self.labelCurrentImageNumber.setFont(font3)
        self.labelCurrentImageNumber.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.labelCurrentImageNumber)

        self.label_6 = QLabel(self.frame_8)
        self.label_6.setObjectName(u"label_6")
        sizePolicy3.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy3)
        self.label_6.setFont(font5)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_6)

        self.labelAllImageCountImage = QLabel(self.frame_8)
        self.labelAllImageCountImage.setObjectName(u"labelAllImageCountImage")
        sizePolicy3.setHeightForWidth(self.labelAllImageCountImage.sizePolicy().hasHeightForWidth())
        self.labelAllImageCountImage.setSizePolicy(sizePolicy3)
        self.labelAllImageCountImage.setFont(font3)
        self.labelAllImageCountImage.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.labelAllImageCountImage)


        self.verticalLayout_7.addWidget(self.frame_8, 0, Qt.AlignHCenter)

        self.frame_7 = QFrame(self.FramePreviewImage)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy4)
        self.frame_7.setMinimumSize(QSize(0, 60))
        self.frame_7.setMaximumSize(QSize(16777215, 60))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.btnPreviewLeftImage = QPushButton(self.frame_7)
        self.btnPreviewLeftImage.setObjectName(u"btnPreviewLeftImage")
        sizePolicy.setHeightForWidth(self.btnPreviewLeftImage.sizePolicy().hasHeightForWidth())
        self.btnPreviewLeftImage.setSizePolicy(sizePolicy)
        self.btnPreviewLeftImage.setMinimumSize(QSize(0, 30))
        self.btnPreviewLeftImage.setMaximumSize(QSize(16777215, 50))
        self.btnPreviewLeftImage.setFont(font)
        self.btnPreviewLeftImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnPreviewLeftImage.setAutoFillBackground(False)
        self.btnPreviewLeftImage.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"Icons/bold-arrow-left.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPreviewLeftImage.setIcon(icon4)
        self.btnPreviewLeftImage.setIconSize(QSize(30, 30))
        self.btnPreviewLeftImage.setAutoRepeat(False)

        self.horizontalLayout_14.addWidget(self.btnPreviewLeftImage)

        self.btnAddToQueueImage = QPushButton(self.frame_7)
        self.btnAddToQueueImage.setObjectName(u"btnAddToQueueImage")
        sizePolicy.setHeightForWidth(self.btnAddToQueueImage.sizePolicy().hasHeightForWidth())
        self.btnAddToQueueImage.setSizePolicy(sizePolicy)
        self.btnAddToQueueImage.setMinimumSize(QSize(150, 30))
        self.btnAddToQueueImage.setMaximumSize(QSize(16777215, 50))
        self.btnAddToQueueImage.setFont(font6)
        self.btnAddToQueueImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnAddToQueueImage.setAutoFillBackground(False)
        self.btnAddToQueueImage.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnAddToQueueImage.setIconSize(QSize(30, 30))
        self.btnAddToQueueImage.setAutoRepeat(False)

        self.horizontalLayout_14.addWidget(self.btnAddToQueueImage)

        self.btnPreviewRightImage = QPushButton(self.frame_7)
        self.btnPreviewRightImage.setObjectName(u"btnPreviewRightImage")
        sizePolicy.setHeightForWidth(self.btnPreviewRightImage.sizePolicy().hasHeightForWidth())
        self.btnPreviewRightImage.setSizePolicy(sizePolicy)
        self.btnPreviewRightImage.setMinimumSize(QSize(0, 30))
        self.btnPreviewRightImage.setMaximumSize(QSize(16777215, 50))
        self.btnPreviewRightImage.setFont(font)
        self.btnPreviewRightImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnPreviewRightImage.setAutoFillBackground(False)
        self.btnPreviewRightImage.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"Icons/bold-arrow-right.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnPreviewRightImage.setIcon(icon5)
        self.btnPreviewRightImage.setIconSize(QSize(30, 30))
        self.btnPreviewRightImage.setAutoRepeat(False)

        self.horizontalLayout_14.addWidget(self.btnPreviewRightImage)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.frame_7.raise_()
        self.frame_9.raise_()
        self.frame_8.raise_()

        self.horizontalLayout_7.addWidget(self.FramePreviewImage)


        self.verticalLayout_10.addWidget(self.FrameContentUp)

        self.frame_6 = QFrame(self.Image)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_6)
        self.verticalLayout_8.setSpacing(10)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 15, 0, 0)
        self.plainTextEditOutputImage = QPlainTextEdit(self.frame_6)
        self.plainTextEditOutputImage.setObjectName(u"plainTextEditOutputImage")
        self.plainTextEditOutputImage.setMinimumSize(QSize(400, 90))
        self.plainTextEditOutputImage.setMaximumSize(QSize(16777215, 16666666))
        font7 = QFont()
        font7.setPointSize(11)
        self.plainTextEditOutputImage.setFont(font7)
        self.plainTextEditOutputImage.setStyleSheet(u"QPlainTextEdit{\n"
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
        self.plainTextEditOutputImage.setFrameShape(QFrame.NoFrame)
        self.plainTextEditOutputImage.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_8.addWidget(self.plainTextEditOutputImage)

        self.frame = QFrame(self.frame_6)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 60))
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 5)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(200, 0))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btnTranslateTextImage = QPushButton(self.frame_2)
        self.btnTranslateTextImage.setObjectName(u"btnTranslateTextImage")
        self.btnTranslateTextImage.setGeometry(QRect(10, 0, 111, 50))
        sizePolicy5 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.btnTranslateTextImage.sizePolicy().hasHeightForWidth())
        self.btnTranslateTextImage.setSizePolicy(sizePolicy5)
        self.btnTranslateTextImage.setMinimumSize(QSize(50, 50))
        self.btnTranslateTextImage.setMaximumSize(QSize(16777215, 50))
        self.btnTranslateTextImage.setFont(font6)
        self.btnTranslateTextImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnTranslateTextImage.setAutoFillBackground(False)
        self.btnTranslateTextImage.setStyleSheet(u"QPushButton{\n"
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
        self.btnTranslateTextImage.setIconSize(QSize(35, 35))
        self.btnTranslateTextImage.setAutoRepeat(False)

        self.horizontalLayout_12.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy6)
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.frame_5)

        self.FrameSaveBtn = QFrame(self.frame)
        self.FrameSaveBtn.setObjectName(u"FrameSaveBtn")
        self.FrameSaveBtn.setMinimumSize(QSize(100, 60))
        self.FrameSaveBtn.setMaximumSize(QSize(100, 60))
        self.FrameSaveBtn.setFrameShape(QFrame.NoFrame)
        self.FrameSaveBtn.setFrameShadow(QFrame.Raised)
        self.btnSaveImage = QPushButton(self.FrameSaveBtn)
        self.btnSaveImage.setObjectName(u"btnSaveImage")
        self.btnSaveImage.setGeometry(QRect(30, 0, 61, 61))
        self.btnSaveImage.setMinimumSize(QSize(50, 50))
        self.btnSaveImage.setFont(font)
        self.btnSaveImage.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnSaveImage.setAutoFillBackground(False)
        self.btnSaveImage.setStyleSheet(u"QPushButton{\n"
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
        icon6 = QIcon()
        icon6.addFile(u"Icons/cil-save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnSaveImage.setIcon(icon6)
        self.btnSaveImage.setIconSize(QSize(35, 35))
        self.btnSaveImage.setAutoRepeat(False)
        self.frameSizeGrip = QFrame(self.FrameSaveBtn)
        self.frameSizeGrip.setObjectName(u"frameSizeGrip")
        self.frameSizeGrip.setGeometry(QRect(94, 65, 16, 16))
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frameSizeGrip.sizePolicy().hasHeightForWidth())
        self.frameSizeGrip.setSizePolicy(sizePolicy7)
        self.frameSizeGrip.setMinimumSize(QSize(16, 16))
        self.frameSizeGrip.setMaximumSize(QSize(16, 16))
        self.frameSizeGrip.setLayoutDirection(Qt.LeftToRight)
        self.frameSizeGrip.setStyleSheet(u"")
        self.frameSizeGrip.setFrameShape(QFrame.NoFrame)
        self.frameSizeGrip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.FrameSaveBtn)


        self.verticalLayout_8.addWidget(self.frame)


        self.verticalLayout_10.addWidget(self.frame_6)

        self.Pages.addWidget(self.Image)
        self.PDF = QWidget()
        self.PDF.setObjectName(u"PDF")
        self.horizontalLayout_17 = QHBoxLayout(self.PDF)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.FrameContentLeftSidePDF = QFrame(self.PDF)
        self.FrameContentLeftSidePDF.setObjectName(u"FrameContentLeftSidePDF")
        self.FrameContentLeftSidePDF.setFrameShape(QFrame.StyledPanel)
        self.FrameContentLeftSidePDF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.FrameContentLeftSidePDF)
        self.verticalLayout_21.setSpacing(20)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.FrameCongentUPOptionsPDF = QFrame(self.FrameContentLeftSidePDF)
        self.FrameCongentUPOptionsPDF.setObjectName(u"FrameCongentUPOptionsPDF")
        sizePolicy2.setHeightForWidth(self.FrameCongentUPOptionsPDF.sizePolicy().hasHeightForWidth())
        self.FrameCongentUPOptionsPDF.setSizePolicy(sizePolicy2)
        self.FrameCongentUPOptionsPDF.setMaximumSize(QSize(16777215, 262))
        self.FrameCongentUPOptionsPDF.setFrameShape(QFrame.StyledPanel)
        self.FrameCongentUPOptionsPDF.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.FrameCongentUPOptionsPDF)
        self.verticalLayout_19.setSpacing(10)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.FrameOpenFilePDF = QFrame(self.FrameCongentUPOptionsPDF)
        self.FrameOpenFilePDF.setObjectName(u"FrameOpenFilePDF")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.FrameOpenFilePDF.sizePolicy().hasHeightForWidth())
        self.FrameOpenFilePDF.setSizePolicy(sizePolicy8)
        self.FrameOpenFilePDF.setMinimumSize(QSize(0, 40))
        self.FrameOpenFilePDF.setMaximumSize(QSize(16777215, 78))
        self.FrameOpenFilePDF.setFrameShape(QFrame.NoFrame)
        self.FrameOpenFilePDF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.FrameOpenFilePDF)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.plainTextEditFilePathPDF = QPlainTextEdit(self.FrameOpenFilePDF)
        self.plainTextEditFilePathPDF.setObjectName(u"plainTextEditFilePathPDF")
        self.plainTextEditFilePathPDF.setMinimumSize(QSize(200, 40))
        self.plainTextEditFilePathPDF.setMaximumSize(QSize(16777215, 50))
        self.plainTextEditFilePathPDF.setFont(font3)
        self.plainTextEditFilePathPDF.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
" border-radius:20px;")
        self.plainTextEditFilePathPDF.setFrameShape(QFrame.NoFrame)
        self.plainTextEditFilePathPDF.setReadOnly(True)

        self.horizontalLayout_33.addWidget(self.plainTextEditFilePathPDF)

        self.btnChooseFIlesPDF = QPushButton(self.FrameOpenFilePDF)
        self.btnChooseFIlesPDF.setObjectName(u"btnChooseFIlesPDF")
        self.btnChooseFIlesPDF.setMinimumSize(QSize(100, 40))
        self.btnChooseFIlesPDF.setFont(font)
        self.btnChooseFIlesPDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnChooseFIlesPDF.setAutoFillBackground(False)
        self.btnChooseFIlesPDF.setStyleSheet(u"QPushButton{\n"
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
        self.btnChooseFIlesPDF.setIcon(icon3)
        self.btnChooseFIlesPDF.setIconSize(QSize(50, 50))
        self.btnChooseFIlesPDF.setAutoRepeat(False)

        self.horizontalLayout_33.addWidget(self.btnChooseFIlesPDF)


        self.verticalLayout_19.addWidget(self.FrameOpenFilePDF)

        self.FrameSelectLanguagePDF = QFrame(self.FrameCongentUPOptionsPDF)
        self.FrameSelectLanguagePDF.setObjectName(u"FrameSelectLanguagePDF")
        sizePolicy2.setHeightForWidth(self.FrameSelectLanguagePDF.sizePolicy().hasHeightForWidth())
        self.FrameSelectLanguagePDF.setSizePolicy(sizePolicy2)
        self.FrameSelectLanguagePDF.setMaximumSize(QSize(16777215, 57))
        self.FrameSelectLanguagePDF.setFrameShape(QFrame.NoFrame)
        self.FrameSelectLanguagePDF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.FrameSelectLanguagePDF)
        self.horizontalLayout_28.setSpacing(20)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_5 = QLabel(self.FrameSelectLanguagePDF)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_30.addWidget(self.label_5)

        self.comboBoxLanguagePDF = QComboBox(self.FrameSelectLanguagePDF)
        self.comboBoxLanguagePDF.setObjectName(u"comboBoxLanguagePDF")
        self.comboBoxLanguagePDF.setMinimumSize(QSize(50, 35))
        self.comboBoxLanguagePDF.setFont(font3)
        self.comboBoxLanguagePDF.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_30.addWidget(self.comboBoxLanguagePDF)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_30)

        self.checkBoxSecondLanguagePDF = QCheckBox(self.FrameSelectLanguagePDF)
        self.checkBoxSecondLanguagePDF.setObjectName(u"checkBoxSecondLanguagePDF")
        self.checkBoxSecondLanguagePDF.setFont(font4)
        self.checkBoxSecondLanguagePDF.setStyleSheet(u"QCheckBox {\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"QCheckBox::indicator {\n"
"   border: 3px solid rgb(0, 0, 0);\n"
"width: 15px;\n"
"height: 15px;\n"
"	border-radius: 10px;\n"
" background: rgb(27, 27, 27);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(0, 0, 0);\n"
"color: rgb(85, 170, 255);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(85, 170, 255);\n"
"	border: 3px solid rgb(0, 0, 0);\n"
"}")

        self.horizontalLayout_28.addWidget(self.checkBoxSecondLanguagePDF)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.comboBoxSecondLanguagePDF = QComboBox(self.FrameSelectLanguagePDF)
        self.comboBoxSecondLanguagePDF.setObjectName(u"comboBoxSecondLanguagePDF")
        self.comboBoxSecondLanguagePDF.setMinimumSize(QSize(50, 35))
        self.comboBoxSecondLanguagePDF.setFont(font3)
        self.comboBoxSecondLanguagePDF.setStyleSheet(u"QComboBox{\n"
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

        self.horizontalLayout_31.addWidget(self.comboBoxSecondLanguagePDF)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_2)


        self.horizontalLayout_28.addLayout(self.horizontalLayout_31)


        self.verticalLayout_19.addWidget(self.FrameSelectLanguagePDF)

        self.FrameQueue_2 = QFrame(self.FrameCongentUPOptionsPDF)
        self.FrameQueue_2.setObjectName(u"FrameQueue_2")
        sizePolicy.setHeightForWidth(self.FrameQueue_2.sizePolicy().hasHeightForWidth())
        self.FrameQueue_2.setSizePolicy(sizePolicy)
        self.FrameQueue_2.setMinimumSize(QSize(0, 30))
        self.FrameQueue_2.setMaximumSize(QSize(16777215, 1000))
        self.FrameQueue_2.setFrameShape(QFrame.StyledPanel)
        self.FrameQueue_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.FrameQueue_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.FrameQueue_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(70, 16777215))
        self.label_8.setFont(font5)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_16.addWidget(self.label_8)

        self.textEditQueuePDF = QTextEdit(self.FrameQueue_2)
        self.textEditQueuePDF.setObjectName(u"textEditQueuePDF")
        sizePolicy4.setHeightForWidth(self.textEditQueuePDF.sizePolicy().hasHeightForWidth())
        self.textEditQueuePDF.setSizePolicy(sizePolicy4)
        self.textEditQueuePDF.setMinimumSize(QSize(0, 25))
        self.textEditQueuePDF.setMaximumSize(QSize(16777215, 50))
        self.textEditQueuePDF.setFont(font3)
        self.textEditQueuePDF.setStyleSheet(u"QTextEdit {\n"
"background-color: rgb(27, 27, 27);\n"
"color: rgb(255, 255, 255);\n"
" border-radius:10px;}\n"
"\n"
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
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: n"
                        "one;\n"
" }")
        self.textEditQueuePDF.setFrameShape(QFrame.NoFrame)
        self.textEditQueuePDF.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.textEditQueuePDF.setReadOnly(True)
        self.textEditQueuePDF.setCursorWidth(1)

        self.horizontalLayout_16.addWidget(self.textEditQueuePDF)

        self.btnClearQueuePDF = QPushButton(self.FrameQueue_2)
        self.btnClearQueuePDF.setObjectName(u"btnClearQueuePDF")
        sizePolicy1.setHeightForWidth(self.btnClearQueuePDF.sizePolicy().hasHeightForWidth())
        self.btnClearQueuePDF.setSizePolicy(sizePolicy1)
        self.btnClearQueuePDF.setMinimumSize(QSize(120, 35))
        self.btnClearQueuePDF.setMaximumSize(QSize(50, 50))
        self.btnClearQueuePDF.setFont(font6)
        self.btnClearQueuePDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnClearQueuePDF.setAutoFillBackground(False)
        self.btnClearQueuePDF.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnClearQueuePDF.setIconSize(QSize(30, 30))
        self.btnClearQueuePDF.setAutoRepeat(False)

        self.horizontalLayout_16.addWidget(self.btnClearQueuePDF)


        self.verticalLayout_19.addWidget(self.FrameQueue_2)

        self.FrameRecognizeAllBtn = QFrame(self.FrameCongentUPOptionsPDF)
        self.FrameRecognizeAllBtn.setObjectName(u"FrameRecognizeAllBtn")
        sizePolicy2.setHeightForWidth(self.FrameRecognizeAllBtn.sizePolicy().hasHeightForWidth())
        self.FrameRecognizeAllBtn.setSizePolicy(sizePolicy2)
        self.FrameRecognizeAllBtn.setMaximumSize(QSize(16777215, 123))
        self.FrameRecognizeAllBtn.setFrameShape(QFrame.StyledPanel)
        self.FrameRecognizeAllBtn.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.FrameRecognizeAllBtn)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btnRecognizeAllPDF = QPushButton(self.FrameRecognizeAllBtn)
        self.btnRecognizeAllPDF.setObjectName(u"btnRecognizeAllPDF")
        sizePolicy.setHeightForWidth(self.btnRecognizeAllPDF.sizePolicy().hasHeightForWidth())
        self.btnRecognizeAllPDF.setSizePolicy(sizePolicy)
        self.btnRecognizeAllPDF.setMinimumSize(QSize(0, 50))
        self.btnRecognizeAllPDF.setMaximumSize(QSize(16777215, 100))
        self.btnRecognizeAllPDF.setFont(font6)
        self.btnRecognizeAllPDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnRecognizeAllPDF.setAutoFillBackground(False)
        self.btnRecognizeAllPDF.setStyleSheet(u"QPushButton{\n"
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
        self.btnRecognizeAllPDF.setAutoRepeat(False)
        self.btnRecognizeAllPDF.setFlat(False)

        self.horizontalLayout_29.addWidget(self.btnRecognizeAllPDF)

        self.btnRecognizeCurrentPDF = QPushButton(self.FrameRecognizeAllBtn)
        self.btnRecognizeCurrentPDF.setObjectName(u"btnRecognizeCurrentPDF")
        sizePolicy.setHeightForWidth(self.btnRecognizeCurrentPDF.sizePolicy().hasHeightForWidth())
        self.btnRecognizeCurrentPDF.setSizePolicy(sizePolicy)
        self.btnRecognizeCurrentPDF.setMinimumSize(QSize(0, 40))
        self.btnRecognizeCurrentPDF.setMaximumSize(QSize(16777215, 100))
        self.btnRecognizeCurrentPDF.setFont(font6)
        self.btnRecognizeCurrentPDF.setContextMenuPolicy(Qt.DefaultContextMenu)
#if QT_CONFIG(tooltip)
        self.btnRecognizeCurrentPDF.setToolTip(u"")
#endif // QT_CONFIG(tooltip)
        self.btnRecognizeCurrentPDF.setAutoFillBackground(False)
        self.btnRecognizeCurrentPDF.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:20px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnRecognizeCurrentPDF.setAutoRepeat(False)

        self.horizontalLayout_29.addWidget(self.btnRecognizeCurrentPDF)


        self.verticalLayout_19.addWidget(self.FrameRecognizeAllBtn)


        self.verticalLayout_21.addWidget(self.FrameCongentUPOptionsPDF)

        self.FrameContentDownOutputSavePDF = QFrame(self.FrameContentLeftSidePDF)
        self.FrameContentDownOutputSavePDF.setObjectName(u"FrameContentDownOutputSavePDF")
        sizePolicy.setHeightForWidth(self.FrameContentDownOutputSavePDF.sizePolicy().hasHeightForWidth())
        self.FrameContentDownOutputSavePDF.setSizePolicy(sizePolicy)
        self.FrameContentDownOutputSavePDF.setFrameShape(QFrame.NoFrame)
        self.FrameContentDownOutputSavePDF.setFrameShadow(QFrame.Raised)
        self.FrameContentDownOutputSavePDF.setLineWidth(0)
        self.verticalLayout_18 = QVBoxLayout(self.FrameContentDownOutputSavePDF)
        self.verticalLayout_18.setSpacing(10)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(10, 0, 0, 0)
        self.plainTextEditOutputPDF = QPlainTextEdit(self.FrameContentDownOutputSavePDF)
        self.plainTextEditOutputPDF.setObjectName(u"plainTextEditOutputPDF")
        self.plainTextEditOutputPDF.setMinimumSize(QSize(0, 100))
        self.plainTextEditOutputPDF.setMaximumSize(QSize(16777215, 16666666))
        self.plainTextEditOutputPDF.setFont(font7)
        self.plainTextEditOutputPDF.setStyleSheet(u"QPlainTextEdit{\n"
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
        self.plainTextEditOutputPDF.setFrameShape(QFrame.NoFrame)
        self.plainTextEditOutputPDF.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_18.addWidget(self.plainTextEditOutputPDF)

        self.FrameSavePDF = QFrame(self.FrameContentDownOutputSavePDF)
        self.FrameSavePDF.setObjectName(u"FrameSavePDF")
        sizePolicy6.setHeightForWidth(self.FrameSavePDF.sizePolicy().hasHeightForWidth())
        self.FrameSavePDF.setSizePolicy(sizePolicy6)
        self.FrameSavePDF.setMinimumSize(QSize(50, 50))
        self.FrameSavePDF.setMaximumSize(QSize(16777215, 80))
        self.FrameSavePDF.setFrameShape(QFrame.NoFrame)
        self.FrameSavePDF.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.FrameSavePDF)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.FrameFilingSaveBtn = QFrame(self.FrameSavePDF)
        self.FrameFilingSaveBtn.setObjectName(u"FrameFilingSaveBtn")
        sizePolicy6.setHeightForWidth(self.FrameFilingSaveBtn.sizePolicy().hasHeightForWidth())
        self.FrameFilingSaveBtn.setSizePolicy(sizePolicy6)
        self.FrameFilingSaveBtn.setMinimumSize(QSize(0, 50))
        self.FrameFilingSaveBtn.setMaximumSize(QSize(10000000, 16777215))
        self.FrameFilingSaveBtn.setFrameShape(QFrame.StyledPanel)
        self.FrameFilingSaveBtn.setFrameShadow(QFrame.Raised)
        self.btnTranslateWindowPDF = QPushButton(self.FrameFilingSaveBtn)
        self.btnTranslateWindowPDF.setObjectName(u"btnTranslateWindowPDF")
        self.btnTranslateWindowPDF.setGeometry(QRect(0, 0, 100, 61))
        self.btnTranslateWindowPDF.setMinimumSize(QSize(100, 50))
        self.btnTranslateWindowPDF.setFont(font6)
        self.btnTranslateWindowPDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnTranslateWindowPDF.setAutoFillBackground(False)
        self.btnTranslateWindowPDF.setStyleSheet(u"QPushButton{\n"
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
        self.btnTranslateWindowPDF.setIconSize(QSize(35, 35))
        self.btnTranslateWindowPDF.setAutoRepeat(False)

        self.horizontalLayout_26.addWidget(self.FrameFilingSaveBtn)

        self.FrameSaveBtn_3 = QFrame(self.FrameSavePDF)
        self.FrameSaveBtn_3.setObjectName(u"FrameSaveBtn_3")
        self.FrameSaveBtn_3.setMinimumSize(QSize(100, 50))
        self.FrameSaveBtn_3.setMaximumSize(QSize(100, 70))
        self.FrameSaveBtn_3.setFrameShape(QFrame.StyledPanel)
        self.FrameSaveBtn_3.setFrameShadow(QFrame.Raised)
        self.btnSavePDF = QPushButton(self.FrameSaveBtn_3)
        self.btnSavePDF.setObjectName(u"btnSavePDF")
        self.btnSavePDF.setGeometry(QRect(30, 0, 61, 61))
        self.btnSavePDF.setMinimumSize(QSize(50, 50))
        self.btnSavePDF.setFont(font)
        self.btnSavePDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnSavePDF.setAutoFillBackground(False)
        self.btnSavePDF.setStyleSheet(u"QPushButton{\n"
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
        self.btnSavePDF.setIcon(icon6)
        self.btnSavePDF.setIconSize(QSize(35, 35))
        self.btnSavePDF.setAutoRepeat(False)

        self.horizontalLayout_26.addWidget(self.FrameSaveBtn_3)


        self.verticalLayout_18.addWidget(self.FrameSavePDF)


        self.verticalLayout_21.addWidget(self.FrameContentDownOutputSavePDF)


        self.horizontalLayout_17.addWidget(self.FrameContentLeftSidePDF)

        self.frame_4 = QFrame(self.PDF)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.FramePreview_3 = QFrame(self.frame_4)
        self.FramePreview_3.setObjectName(u"FramePreview_3")
        sizePolicy.setHeightForWidth(self.FramePreview_3.sizePolicy().hasHeightForWidth())
        self.FramePreview_3.setSizePolicy(sizePolicy)
        self.FramePreview_3.setMinimumSize(QSize(100, 300))
        self.FramePreview_3.setFrameShape(QFrame.NoFrame)
        self.FramePreview_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.FramePreview_3)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.previewPDF = QLabel(self.FramePreview_3)
        self.previewPDF.setObjectName(u"previewPDF")
        sizePolicy.setHeightForWidth(self.previewPDF.sizePolicy().hasHeightForWidth())
        self.previewPDF.setSizePolicy(sizePolicy)
        self.previewPDF.setMinimumSize(QSize(0, 0))
        self.previewPDF.setMaximumSize(QSize(300000, 300000))
        self.previewPDF.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"border-color: rgb(0, 0, 0);\n"
"border: 5px solid;")
        self.previewPDF.setPixmap(QPixmap(u"Icons/128x128 Preview.png"))
        self.previewPDF.setScaledContents(False)
        self.previewPDF.setAlignment(Qt.AlignCenter)
        self.previewPDF.setMargin(0)
        self.previewPDF.setIndent(0)

        self.verticalLayout_20.addWidget(self.previewPDF)


        self.verticalLayout_11.addWidget(self.FramePreview_3)

        self.frame_11 = QFrame(self.frame_4)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setMinimumSize(QSize(0, 34))
        self.frame_11.setMaximumSize(QSize(16777215, 34))
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_4 = QLabel(self.frame_11)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))
        self.label_4.setFont(font5)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_4)

        self.labelCurrentPageNumberPDF = QLabel(self.frame_11)
        self.labelCurrentPageNumberPDF.setObjectName(u"labelCurrentPageNumberPDF")
        sizePolicy3.setHeightForWidth(self.labelCurrentPageNumberPDF.sizePolicy().hasHeightForWidth())
        self.labelCurrentPageNumberPDF.setSizePolicy(sizePolicy3)
        self.labelCurrentPageNumberPDF.setFont(font5)
        self.labelCurrentPageNumberPDF.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.labelCurrentPageNumberPDF)

        self.label_7 = QLabel(self.frame_11)
        self.label_7.setObjectName(u"label_7")
        sizePolicy3.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy3)
        self.label_7.setFont(font5)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.label_7)

        self.labelAllPageNumberPDF = QLabel(self.frame_11)
        self.labelAllPageNumberPDF.setObjectName(u"labelAllPageNumberPDF")
        sizePolicy3.setHeightForWidth(self.labelAllPageNumberPDF.sizePolicy().hasHeightForWidth())
        self.labelAllPageNumberPDF.setSizePolicy(sizePolicy3)
        self.labelAllPageNumberPDF.setFont(font5)
        self.labelAllPageNumberPDF.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_15.addWidget(self.labelAllPageNumberPDF)


        self.verticalLayout_11.addWidget(self.frame_11, 0, Qt.AlignHCenter)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 60))
        self.frame_3.setMaximumSize(QSize(16777215, 60))
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_27 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_27.setSpacing(20)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.btnPreviewLeftPDF = QPushButton(self.frame_3)
        self.btnPreviewLeftPDF.setObjectName(u"btnPreviewLeftPDF")
        sizePolicy1.setHeightForWidth(self.btnPreviewLeftPDF.sizePolicy().hasHeightForWidth())
        self.btnPreviewLeftPDF.setSizePolicy(sizePolicy1)
        self.btnPreviewLeftPDF.setMinimumSize(QSize(100, 50))
        self.btnPreviewLeftPDF.setMaximumSize(QSize(100, 50))
        self.btnPreviewLeftPDF.setFont(font)
        self.btnPreviewLeftPDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnPreviewLeftPDF.setAutoFillBackground(False)
        self.btnPreviewLeftPDF.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnPreviewLeftPDF.setIcon(icon4)
        self.btnPreviewLeftPDF.setIconSize(QSize(30, 30))
        self.btnPreviewLeftPDF.setAutoRepeat(False)

        self.horizontalLayout_27.addWidget(self.btnPreviewLeftPDF)

        self.btnAddToQueuePDF = QPushButton(self.frame_3)
        self.btnAddToQueuePDF.setObjectName(u"btnAddToQueuePDF")
        sizePolicy1.setHeightForWidth(self.btnAddToQueuePDF.sizePolicy().hasHeightForWidth())
        self.btnAddToQueuePDF.setSizePolicy(sizePolicy1)
        self.btnAddToQueuePDF.setMinimumSize(QSize(200, 50))
        self.btnAddToQueuePDF.setMaximumSize(QSize(200, 50))
        self.btnAddToQueuePDF.setFont(font6)
        self.btnAddToQueuePDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnAddToQueuePDF.setAutoFillBackground(False)
        self.btnAddToQueuePDF.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnAddToQueuePDF.setIconSize(QSize(30, 30))
        self.btnAddToQueuePDF.setAutoRepeat(False)

        self.horizontalLayout_27.addWidget(self.btnAddToQueuePDF)

        self.btnPreviewRightPDF = QPushButton(self.frame_3)
        self.btnPreviewRightPDF.setObjectName(u"btnPreviewRightPDF")
        sizePolicy1.setHeightForWidth(self.btnPreviewRightPDF.sizePolicy().hasHeightForWidth())
        self.btnPreviewRightPDF.setSizePolicy(sizePolicy1)
        self.btnPreviewRightPDF.setMinimumSize(QSize(100, 50))
        self.btnPreviewRightPDF.setMaximumSize(QSize(80, 50))
        self.btnPreviewRightPDF.setFont(font)
        self.btnPreviewRightPDF.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.btnPreviewRightPDF.setAutoFillBackground(False)
        self.btnPreviewRightPDF.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"	border: 0px solid;\n"
" border-style: solid;\n"
" border-width:1px;\n"
" border-radius:15px;\n"
"\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(85, 170, 255);\n"
"}")
        self.btnPreviewRightPDF.setIcon(icon5)
        self.btnPreviewRightPDF.setIconSize(QSize(30, 30))
        self.btnPreviewRightPDF.setAutoRepeat(False)

        self.horizontalLayout_27.addWidget(self.btnPreviewRightPDF)


        self.verticalLayout_11.addWidget(self.frame_3, 0, Qt.AlignHCenter)


        self.horizontalLayout_17.addWidget(self.frame_4)

        self.Pages.addWidget(self.PDF)

        self.verticalLayout_6.addWidget(self.Pages)


        self.horizontalLayout_2.addWidget(self.FrameAppContent)


        self.verticalLayout.addWidget(self.FrameContent)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"OCR-KR", None))
        self.btnToogleMenu.setText(QCoreApplication.translate("MainWindow", u"|||", None))
        self.btnMinimize.setText("")
        self.btnMaximize.setText("")
        self.btnX.setText("")
        self.btnImageRecognize.setText("")
        self.btnPDFRecognize.setText("")
        self.LabelCopyright.setText(QCoreApplication.translate("MainWindow", u"Copyright \n"
" Krzysztof Rutana \n"
" 2020", None))
        self.btnChooseFIlesImage.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">J\u0119zyk:</span></p></body></html>", None))
        self.checkBoxSecondLanguageImage.setText(QCoreApplication.translate("MainWindow", u"Kolejny j\u0119zyk?", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Kolejka: ", None))
        self.btnClearQueueImage.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 kolejk\u0119", None))
        self.btnRecognizeAllImage.setText(QCoreApplication.translate("MainWindow", u"Rozpoznaj wszystkie pliki", None))
        self.btnRecognizeCurrentImage.setText(QCoreApplication.translate("MainWindow", u"Rozpoznaj aktualny/ \n"
"zakolejkowane pliki", None))
        self.previewImage.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Zdj\u0119cie:", None))
        self.labelCurrentImageNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.labelAllImageCountImage.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnPreviewLeftImage.setText("")
        self.btnAddToQueueImage.setText(QCoreApplication.translate("MainWindow", u"Dodaj do kolejki", None))
        self.btnPreviewRightImage.setText("")
        self.btnTranslateTextImage.setText(QCoreApplication.translate("MainWindow", u"T\u0142umacz tekst", None))
        self.btnSaveImage.setText("")
        self.btnChooseFIlesPDF.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">J\u0119zyk:</span></p></body></html>", None))
        self.checkBoxSecondLanguagePDF.setText(QCoreApplication.translate("MainWindow", u"Kolejny j\u0119zyk?", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Kolejka: ", None))
        self.btnClearQueuePDF.setText(QCoreApplication.translate("MainWindow", u"Wyczy\u015b\u0107 kolejk\u0119", None))
        self.btnRecognizeAllPDF.setText(QCoreApplication.translate("MainWindow", u"Rozpoznaj wszystkie \n"
"strony", None))
        self.btnRecognizeCurrentPDF.setText(QCoreApplication.translate("MainWindow", u"Rozpoznaj aktualn\u0105 / \n"
" zakolejkowane strony", None))
        self.btnTranslateWindowPDF.setText(QCoreApplication.translate("MainWindow", u"T\u0142umacz tekst", None))
        self.btnSavePDF.setText("")
        self.previewPDF.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Strona:", None))
        self.labelCurrentPageNumberPDF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.labelAllPageNumberPDF.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btnPreviewLeftPDF.setText("")
        self.btnAddToQueuePDF.setText(QCoreApplication.translate("MainWindow", u"Dodaj do kolejki", None))
        self.btnPreviewRightPDF.setText("")
    # retranslateUi

