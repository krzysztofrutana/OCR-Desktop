import os

from PIL.ImageQt import ImageQt
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation, QSize
from PySide2.QtGui import QIcon, QPixmap

from pytesseract import pytesseract

from main import QSizeGrip


class UiFunction():

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    #add necessary Tesseract path to instalation folder, chech what languages are install and add options to combobox
    # TODO setting page in MainWindow, where will be options to choose folder with tesseract
    def addPathAndLanguageList(self):

        pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

        languages = []

        for file in os.listdir(r'C:\Program Files\Tesseract-OCR\tessdata'):
            if file.endswith(".traineddata"):
                lang = file.split('.')[0].upper()
                if lang != "EQU" and lang != "OSD":
                    languages.append(lang)

        self.mainWindow.ui.comboBoxLanguageImage.addItems(languages)
        self.mainWindow.ui.comboBoxLanguageImage.setCurrentText("POL")
        self.mainWindow.ui.comboBoxLanguagePDF.addItems(languages)
        self.mainWindow.ui.comboBoxLanguagePDF.setCurrentText("POL")
        self.mainWindow.ui.comboBoxSecondLanguagePDF.addItems(languages)
        self.mainWindow.ui.comboBoxSecondLanguagePDF.setCurrentText("POL")
        self.mainWindow.ui.comboBoxSecondLanguageImage.addItems(languages)
        self.mainWindow.ui.comboBoxSecondLanguageImage.setCurrentText("POL")

    # left side menu animation and hide or show options text (now its work good, but in future #TODO)
    def toggleMenu(self, maxWidth, enable):
        if enable:

            # get current menu width
            width = self.mainWindow.ui.FrameMenu.width()
            maxExtend = maxWidth
            standard = 70

            # set width
            if width == 70:
                newWidth = maxExtend
                self.mainWindow.ui.LabelCopyright.setVisible(True)
                self.mainWindow.ui.btnImageRecognize.setText("  Rozpoznaj zdjęcie")
                self.mainWindow.ui.btnImageRecognize.setIcon(QIcon(u"uiForms/Icons/64x64Image.png"))
                self.mainWindow.ui.btnPDFRecognize.setText("  Rozpoznaj PDF")
                self.mainWindow.ui.btnPDFRecognize.setIcon(QIcon(u"uiForms/Icons/64x64PDF.png"))
            else:
                newWidth = standard
                self.mainWindow.ui.LabelCopyright.setVisible(False)
                self.mainWindow.ui.btnImageRecognize.setText("")
                self.mainWindow.ui.btnImageRecognize.setIcon(QIcon(u"uiForms/Icons/64x64Image.png"))
                self.mainWindow.ui.btnPDFRecognize.setText("")
                self.mainWindow.ui.btnPDFRecognize.setIcon(QIcon(u"uiForms/Icons/64x64PDF.png"))

            # animation
            # this solution comes from WANDERSON M.PIMENTA project from his github
            self.mainWindow.animation = QPropertyAnimation(self.mainWindow.ui.FrameMenu, b"minimumWidth")
            self.mainWindow.animation.setDuration(400)
            self.mainWindow.animation.setStartValue(width)
            self.mainWindow.animation.setEndValue(newWidth)
            self.mainWindow.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.mainWindow.animation.start()

    # maximize or back to normal window size
    def maximize(self):
        if self.mainWindow.windowMaximized == False:
            self.mainWindow.showMaximized()
            self.mainWindow.windowMaximized = True
        else:
            self.mainWindow.showNormal()
            self.mainWindow.windowMaximized = False

    # TODO
    # refresh preview when resize or maximize window
    def resizeEvent(self):
        if len(self.mainWindow.listOfElementsToRecognizeStr) > 0:
            if self.mainWindow.Pages.currentIndex() == 0:
                imgagePixmap = QPixmap(
                    str(self.mainWindow.listOfElementsToRecognizeStr[self.mainWindow.whichImage])).scaled(
                    QSize(self.mainWindow.ui.previewImage.width(), self.mainWindow.ui.previewImage.height()),
                    QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.mainWindow.previewImage.setPixmap(imgagePixmap)
                self.mainWindow.previewImage.setScaledContents(False)
            elif self.mainWindow.Pages.currentIndex() == 1:
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(
                    QSize(self.mainWindow.ui.previewPDF.width(), self.mainWindow.ui.previewPDF.height()),
                    QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.mainWindow.previewPDF.setPixmap(imgagePixmap)
                self.mainWindow.previewPDF.setScaledContents(False)

    # hide and show combobox to choose second language
    def checkBoxLanguageStateChange(self):
        if self.mainWindow.ui.Pages.currentIndex() == 0:
            if self.mainWindow.ui.checkBoxSecondLanguageImage.isChecked():
                self.mainWindow.ui.comboBoxSecondLanguageImage.setVisible(True)
            else:
                self.mainWindow.ui.comboBoxSecondLanguageImage.setVisible(False)

        elif self.mainWindow.ui.Pages.currentIndex() == 1:
            if self.mainWindow.ui.checkBoxSecondLanguagePDF.isChecked():
                self.mainWindow.ui.comboBoxSecondLanguagePDF.setVisible(True)
            else:
                self.mainWindow.ui.comboBoxSecondLanguagePDF.setVisible(False)

    # connect click signal with method and run necessary method
    def connectionsResizeDragingWindow(self):
        self.mainWindow.ui.checkBoxSecondLanguageImage.stateChanged.connect(
            lambda: self.checkBoxLanguageStateChange())
        self.mainWindow.ui.checkBoxSecondLanguagePDF.stateChanged.connect(
            lambda: self.checkBoxLanguageStateChange())

        self.mainWindow.ui.btnToogleMenu.clicked.connect(lambda: self.toggleMenu(250, True))

        self.mainWindow.ui.btnImageRecognize.clicked.connect(lambda: self.changeOptions(0))
        self.mainWindow.ui.btnPDFRecognize.clicked.connect(lambda: self.changeOptions(1))

        self.mainWindow.ui.btnX.clicked.connect(lambda: self.mainWindow.close())
        self.mainWindow.ui.btnMaximize.clicked.connect(lambda: self.maximize())
        self.mainWindow.ui.btnMinimize.clicked.connect(lambda: self.mainWindow.showMinimized())

        # TODO
        self.resizeWindow()

        self.addPathAndLanguageList()

    def resizeWindow(self):

        # TODO
        # make frame on corner to resize window
        # now it's not working correctly
        # this solution comes from WANDERSON M.PIMENTA project from his github
        self.mainWindow.sizegrip = QSizeGrip(self.mainWindow.ui.frameSizeGrip)
        self.mainWindow.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

    def cleanPagesBeforeChangeOptions(self):
        if self.mainWindow.ui.Pages.currentIndex() == 0:
            self.mainWindow.ui.plainTextEditFilePathImage.clear()
            self.mainWindow.ui.plainTextEditOutputImage.clear()
            self.mainWindow.ui.previewImage.setPixmap(QPixmap(u"uiForms/Icons/128x128 Preview.png"))
            self.mainWindow.ui.previewImage.setScaledContents(False)
        elif self.mainWindow.ui.Pages.currentIndex() == 1:
            self.mainWindow.ui.plainTextEditFilePathPDF.clear()
            self.mainWindow.ui.plainTextEditOutputPDF.clear()
            self.mainWindow.ui.previewPDF.setPixmap(QPixmap(u"uiForms/Icons/128x128 Preview.png"))
            self.mainWindow.ui.previewPDF.setScaledContents(False)
        self.mainWindow.listOfElementsToRecognize.clear()
        self.mainWindow.whichImage = 0

    def changeOptions(self, numerOfOptions):
        self.cleanPagesBeforeChangeOptions()
        self.mainWindow.ui.Pages.setCurrentIndex(numerOfOptions)