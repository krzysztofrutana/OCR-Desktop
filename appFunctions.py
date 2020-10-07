import os

from PIL import Image
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QPixmap, QGuiApplication
from PySide2.QtWidgets import QFileDialog, QProgressDialog, QApplication, QDesktopWidget
from pytesseract import pytesseract
import pdf2image
from PIL.ImageQt import ImageQt
from PyPDF2 import PdfFileReader, PdfFileWriter




#this class have everything functionality using in image recognize options
from UiFunctions import UiFunction


class ImageRecognizeFunction():

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow

    #choosing files to recognize (can be more than one)
    def openFileDialog(self):
        if self.mainWindow.ui.Pages.currentIndex() == 0:
            self.mainWindow.ui.plainTextEditFilePathImage.clear()
            self.mainWindow.ui.plainTextEditOutputImage.clear()
            self.mainWindow.whichImage = 0

            filters = "Obrazy (*.bmp *.png *.jpeg *.tiff)"
            self.dialog = QFileDialog.getOpenFileNames(self.mainWindow, "/home", "", filters)

            if len(self.dialog[0]) > 0:
                self.mainWindow.listOfElementsToRecognize.clear()
                uiFunction = UiFunction(self.mainWindow)
                progressDialog = uiFunction.progressBarDialog("Ładowanie obrazów", len(self.dialog[0]))

                for i in range(0, len(self.dialog[0])):
                    self.mainWindow.ui.plainTextEditFilePathImage.appendPlainText(str(self.dialog[0][i]) + "\n")
                    self.mainWindow.listOfElementsToRecognize.append(str(self.dialog[0][i]))
                    progressDialog.setValue(i)
                    if progressDialog.wasCanceled():
                        break
                progressDialog.setValue(len(self.dialog[0]))

                
                #to preview in QLabel image before must be change to QPixmap
                pixmap = QPixmap(str(self.dialog[0][0])).scaledToWidth(self.mainWindow.ui.previewImage.width(),
                                                                       QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewImage.setPixmap(pixmap)
                self.mainWindow.ui.previewImage.setScaledContents(True)
                self.mainWindow.whichImage = 0
            else:
                return

    # save output to file
    # TODO save to PDF
    def saveOutputImage(self):
        filesTypes = "Plik tekstowy (*.txt);;Plik PDF (*.pdf)"
        name, filter = QFileDialog.getSaveFileName(self.mainWindow, 'Zapisz plik', "Bez nazwy", filesTypes)
        if not name:
            return
        file = open(name, 'w')
        output = self.mainWindow.ui.plainTextEditOutputImage.toPlainText()
        file.write(output)
        file.close()


    # next file in preview.
    # TODO when the window is maximized, when the photo is changegd the preview frame size increases
    def nextImage(self):
        if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage >= 0:
            self.mainWindow.whichImage += 1
            if self.mainWindow.whichImage == len(self.mainWindow.listOfElementsToRecognize):
                self.mainWindow.whichImage = 0
                self.mainWindow.ui.previewImage.setPixmap(
                    QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    .scaledToWidth(self.mainWindow.ui.previewImage.width(), QtCore.Qt.SmoothTransformation))
            else:
                self.mainWindow.ui.previewImage.setPixmap(
                    QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    .scaledToWidth(self.mainWindow.ui.previewImage.width(), QtCore.Qt.SmoothTransformation))

    #next file in preview
    # TODO this same bug like in nextImage method
    def previousImage(self):
        if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage < len(
                self.mainWindow.listOfElementsToRecognize):
            self.mainWindow.whichImage -= 1
            if self.mainWindow.whichImage < 0:
                self.mainWindow.whichImage = len(self.mainWindow.listOfElementsToRecognize) - 1
                self.mainWindow.ui.previewImage.setPixmap(
                    QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    .scaledToWidth(self.mainWindow.ui.previewImage.width(), QtCore.Qt.SmoothTransformation))
            else:
                self.mainWindow.ui.previewImage.setPixmap(
                    QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    .scaledToWidth(self.mainWindow.ui.previewImage.width(), QtCore.Qt.SmoothTransformation))

    # recognize text from all picture in listOfElementsToRecognize list
    def recognizeAll(self):
        uiFunction = UiFunction(self.mainWindow)
        progressDialog = uiFunction.progressBarDialog("Odczytywanie tekstu",
                                                      len(self.mainWindow.listOfElementsToRecognize))
        progressDialog.setValue(0)
        self.mainWindow.ui.plainTextEditOutputImage.clear()
        for i in range(0, len(self.mainWindow.listOfElementsToRecognize)):
            progressDialog.setValue(i)
            if progressDialog.wasCanceled():
                break
            image = Image.open(self.mainWindow.listOfElementsToRecognize[i])
            self.mainWindow.ui.plainTextEditOutputImage.appendPlainText("---------Grafika " + str(i + 1) + "---------")
            if self.mainWindow.ui.checkBoxSecondLanguageImage.isChecked():
                self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(pytesseract.image_to_string(image,
                                                                                                        lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower() +
                                                                                                             "+" + self.mainWindow.ui.comboBoxSecondLanguageImage.currentText().lower()))
            else:
                self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(
                    pytesseract.image_to_string(image,
                                                lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower()))
        progressDialog.setValue(len(self.mainWindow.listOfElementsToRecognize))

    # recognition of text from a photo that is currently on preview
    def recognizeCurrent(self):
        self.mainWindow.ui.plainTextEditOutputImage.clear()
        image = Image.open(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
        if self.mainWindow.ui.checkBoxSecondLanguageImage.isChecked():
            self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(pytesseract.image_to_string(image,
                                                                                                    lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower() +
                                                                                                         "+" + self.mainWindow.ui.comboBoxSecondLanguageImage.currentText().lower()))
        else:
            self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(
                pytesseract.image_to_string(image, lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower()))

    # method to connect everything
    def buttonsConnections(self):
        uiFunction = UiFunction(self.mainWindow)
        self.mainWindow.ui.btnChooseFIlesImage.clicked.connect(lambda: self.openFileDialog())
        self.mainWindow.ui.btnPreviewLeftImage.clicked.connect(lambda: self.previousImage())
        self.mainWindow.ui.btnPreviewRightImage.clicked.connect(lambda: self.nextImage())
        self.mainWindow.ui.btnRecognizeAllImage.clicked.connect(lambda: self.recognizeAll())
        self.mainWindow.ui.btnRecognizeCurrentImage.clicked.connect(lambda: self.recognizeCurrent())
        self.mainWindow.ui.btnSaveImage.clicked.connect(lambda: self.saveOutputImage())
        self.mainWindow.ui.btnTranslateTextImage.clicked.connect(
            lambda : uiFunction.showTranslateWindow(self.mainWindow.ui.plainTextEditOutputImage.toPlainText()))


class PDFRecognizeFunction(ImageRecognizeFunction):

    # all method is override, this class inherits from ImageRecognizeFunction and do this same

    def openFileDialog(self):
        self.mainWindow.ui.plainTextEditFilePathPDF.clear()
        self.mainWindow.ui.plainTextEditOutputPDF.clear()

        filters = "Plik PDF (*.PDF)"
        self.dialog = QFileDialog.getOpenFileName(self.mainWindow, "/home", "", filters)

        if len(self.dialog[0]) > 0:
            self.mainWindow.listOfElementsToRecognize.clear()
            self.mainWindow.ui.plainTextEditFilePathPDF.appendPlainText(str(self.dialog[0]))
            self.mainWindow.whichImage = 0

            pdfFile = PdfFileReader(open(self.dialog[0], "rb"))

            uiFunction = UiFunction(self.mainWindow)
            progressDialog = uiFunction.progressBarDialog("Ładowanie pliku PDF", pdfFile.numPages)

            for i in range(pdfFile.numPages):
                progressDialog.setValue(i)
                if progressDialog.wasCanceled():
                    break
                output = PdfFileWriter()
                output.addPage(pdfFile.getPage(i))
                with open("temp.pdf", "wb") as outputStream:
                    output.write(outputStream)
                image = pdf2image.convert_from_path("temp.pdf", poppler_path="./bin/poppler/poppler-0.68.0/bin",
                                                                 thread_count=4)
                self.mainWindow.listOfElementsToRecognize.append(image[0])
                if os.path.exists("temp.pdf"):
                    os.remove("temp.pdf")

            progressDialog.setValue(pdfFile.numPages)

            # to make QPixmap object, before from JPEG or other format necessary is make ImageQt object
            # or normal Image object
            imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
            imgagePixmap = QPixmap(imageqt).scaled(
                QSize(self.mainWindow.ui.previewPDF.width(), self.mainWindow.ui.previewPDF.height()),
                QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
            self.mainWindow.ui.previewPDF.setScaledContents(True)
            self.mainWindow.whichImage = 0
        else:
            return

    def buttonsConnections(self):
        uiFunction = UiFunction(self.mainWindow)

        self.mainWindow.ui.btnChooseFIlesPDF.clicked.connect(lambda: self.openFileDialog())
        self.mainWindow.ui.btnPreviewLeftPDF.clicked.connect(lambda: self.previousImage())
        self.mainWindow.ui.btnPreviewRightPDF.clicked.connect(lambda: self.nextImage())
        self.mainWindow.ui.btnRecognizeAllPDF.clicked.connect(lambda: self.recognizeAll())
        self.mainWindow.ui.btnRecognizeCurrentPDF.clicked.connect(lambda: self.recognizeCurrent())
        self.mainWindow.ui.btnSavePDF.clicked.connect(lambda: self.saveOutputPDF())
        self.mainWindow.ui.btnTranslateWindowPDF.clicked.connect(
            lambda: uiFunction.showTranslateWindow(self.mainWindow.ui.plainTextEditOutputPDF.toPlainText()))

    def saveOutputPDF(self):
        filesTypes = "Plik tekstowy (*.txt);;Plik PDF (*.pdf)"
        name, filter = QFileDialog.getSaveFileName(self.mainWindow, 'Zapisz plik', "Bez nazwy", filesTypes)
        if not name:
            return
        file = open(name, 'w')
        output = self.mainWindow.ui.plainTextEditOutputPDF.toPlainText()
        file.write(output)
        file.close()

    def nextImage(self):
        if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage >= 0:
            self.mainWindow.whichImage += 1
            if self.mainWindow.whichImage == len(self.mainWindow.listOfElementsToRecognize):
                self.mainWindow.whichImage = 0
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(
                    QSize(self.mainWindow.ui.previewPDF.width(), self.mainWindow.ui.previewPDF.height()),
                    QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
            else:

                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(
                    QSize(self.mainWindow.ui.previewPDF.width(), self.mainWindow.ui.previewPDF.height()),
                    QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)

    def previousImage(self):
        if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage < len(
                self.mainWindow.listOfElementsToRecognize):
            self.mainWindow.whichImage -= 1
            if self.mainWindow.whichImage < 0:
                self.mainWindow.whichImage = len(self.mainWindow.listOfElementsToRecognize) - 1
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(
                    QSize(self.mainWindow.ui.previewPDF.width(), self.mainWindow.ui.previewPDF.height()),
                    QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
            else:
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(
                    QSize(self.mainWindow.ui.previewPDF.width(), self.mainWindow.ui.previewPDF.height()),
                    QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)

    def recognizeAll(self):
        uiFunction = UiFunction(self.mainWindow)
        progressDialog = uiFunction.progressBarDialog("Odczytywanie tekstu", len(self.mainWindow.listOfElementsToRecognize))
        progressDialog.setValue(0)
        self.mainWindow.ui.plainTextEditOutputImage.clear()
        for i in range(0, len(self.mainWindow.listOfElementsToRecognize)):
            progressDialog.setValue(i)
            if progressDialog.wasCanceled():
                break
            image = self.mainWindow.listOfElementsToRecognize[i]
            self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText("---------Strona " + str(i + 1) + "---------")
            if self.mainWindow.ui.checkBoxSecondLanguagePDF.isChecked():
                self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(pytesseract.image_to_string(image,
                                                                                                      lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower() +
                                                                                                           "+" + self.mainWindow.ui.comboBoxSecondLanguagePDF.currentText().lower()))
            else:
                self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(
                    pytesseract.image_to_string(image,
                                                lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower()))
        progressDialog.setValue(len(self.mainWindow.listOfElementsToRecognize))

    def recognizeCurrent(self):
        self.mainWindow.ui.plainTextEditOutputPDF.clear()
        image = self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage]
        if self.mainWindow.ui.checkBoxSecondLanguagePDF.isChecked():
            self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(pytesseract.image_to_string(image,
                                                                                                  lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower() +
                                                                                                       "+" + self.mainWindow.ui.comboBoxSecondLanguagePDF.currentText().lower()))
        else:
            self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(
                pytesseract.image_to_string(image, lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower()))
