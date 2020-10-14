import os

from PIL.ImageQt import ImageQt
from PySide2 import QtCore
from PySide2.QtCore import QPropertyAnimation, QSize, Qt
from PySide2.QtGui import QIcon, QPixmap
from PySide2.QtWidgets import QProgressDialog, QMessageBox

from pytesseract import pytesseract

from main import QSizeGrip
from translateWindow import TranslateWindow


class UiFunction():

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    def progressBarDialog(self, message, max):
        progressDialog = QProgressDialog(message, "Anuluj", 0, max, self.mainWindow)
        progressDialog.setStyleSheet("color:rgb(255, 255, 255); background-color:rgb(40, 40, 40);")
        progressDialog.setWindowTitle("Proszę czekać")
        progressDialog.setWindowModality(Qt.WindowModal)
        return progressDialog

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
                self.mainWindow.ui.btnImageRecognize.setIcon(QIcon(u"resources/icons/64x64Image.png"))
                self.mainWindow.ui.btnPDFRecognize.setText("  Rozpoznaj PDF")
                self.mainWindow.ui.btnPDFRecognize.setIcon(QIcon(u"resources/icons/64x64PDF.png"))
            else:
                newWidth = standard
                self.mainWindow.ui.LabelCopyright.setVisible(False)
                self.mainWindow.ui.btnImageRecognize.setText("")
                self.mainWindow.ui.btnImageRecognize.setIcon(QIcon(u"resources/icons/64x64Image.png"))
                self.mainWindow.ui.btnPDFRecognize.setText("")
                self.mainWindow.ui.btnPDFRecognize.setIcon(QIcon(u"resources/icons/64x64PDF.png"))

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
        if len(self.mainWindow.listOfElementsToRecognize) > 0:
            if self.mainWindow.ui.Pages.currentIndex() == 0:
                imgagePixmap = QPixmap(
                    str(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])).scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                 QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewImage.setPixmap(imgagePixmap)
                self.mainWindow.ui.previewImage.setScaledContents(True)
            elif self.mainWindow.ui.Pages.currentIndex() == 1:
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height(),
                                                                self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                 QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
                self.mainWindow.ui.previewPDF.setScaledContents(True)

    # TODO
    # refresh preview when resize or maximize window
    def resizeEvent(self):
        if len(self.mainWindow.listOfElementsToRecognizeStr) > 0:
            if self.mainWindow.Pages.currentIndex() == 0:
                imgagePixmap = QPixmap(
                    str(self.mainWindow.listOfElementsToRecognizeStr[self.mainWindow.whichImage])).scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                 QtCore.Qt.SmoothTransformation)
                self.mainWindow.previewImage.setPixmap(imgagePixmap)
                self.mainWindow.previewImage.setScaledContents(True)
            elif self.mainWindow.Pages.currentIndex() == 1:
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height(),
                                                                self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                 QtCore.Qt.SmoothTransformation)
                self.mainWindow.previewPDF.setPixmap(imgagePixmap)
                self.mainWindow.previewPDF.setScaledContents(True)

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

        # this solution comes from WANDERSON M.PIMENTA project from his github
        self.mainWindow.sizegrip = QSizeGrip(self.mainWindow.ui.frameSizeGrip)
        self.mainWindow.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

    def cleanPagesBeforeChangeOptions(self):
        if self.mainWindow.ui.Pages.currentIndex() == 0:
            self.mainWindow.ui.plainTextEditFilePathImage.clear()
            self.mainWindow.ui.plainTextEditOutputImage.clear()
            self.mainWindow.queueToRecognize.clear()
        elif self.mainWindow.ui.Pages.currentIndex() == 1:
            self.mainWindow.ui.plainTextEditFilePathPDF.clear()
            self.mainWindow.ui.plainTextEditOutputPDF.clear()
            self.mainWindow.queueToRecognize.clear()
        self.mainWindow.listOfElementsToRecognize.clear()
        self.mainWindow.whichImage = 0

    def changeOptions(self, numerOfOptions):
        self.cleanPagesBeforeChangeOptions()
        self.mainWindow.ui.Pages.setCurrentIndex(numerOfOptions)


    def showTranslateWindow(self, textToTranslate):
        self.mainWindow.badania = TranslateWindow(textToTranslate)

    @staticmethod
    def showErrorDialog(messege):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Warning)
        msgBox.setText(str(messege))
        msgBox.setWindowTitle("Błąd")
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.setStyleSheet("background-color: rgb(40, 40, 40); color: rgb(255, 255, 255)")
        msgBox.exec()
