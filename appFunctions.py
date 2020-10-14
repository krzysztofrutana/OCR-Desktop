import os

from PIL import Image
from PySide2 import QtCore
from PySide2.QtCore import QSize
from PySide2.QtGui import QPixmap, QTextDocument
from PySide2.QtPrintSupport import QPrinter
from PySide2.QtWidgets import QFileDialog
from pytesseract import pytesseract
import pdf2image
from PIL.ImageQt import ImageQt
from PyPDF2 import PdfFileReader, PdfFileWriter
import pandas as pd



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

                try:
                    #to preview in QLabel image before must be change to QPixmap
                    pixmap = QPixmap(str(self.dialog[0][0])).scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                    self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation)
                    self.mainWindow.ui.previewImage.setPixmap(pixmap)
                    self.mainWindow.ui.previewImage.setScaledContents(True)
                    self.mainWindow.whichImage = 0

                    self.mainWindow.ui.labelCurrentImageNumber.setText(str(self.mainWindow.whichImage + 1))
                    self.mainWindow.ui.labelAllImageCountImage.setText(str(len(self.mainWindow.listOfElementsToRecognize)))
                except Exception as inst:
                    UiFunction.showErrorDialog(inst)
            else:
                return

    # save output to file
    def saveOutputImage(self):
        filesTypes = "Plik tekstowy (*.txt);;Plik PDF (*.pdf)"
        name, filter = QFileDialog.getSaveFileName(self.mainWindow, 'Zapisz plik', "Bez nazwy", filesTypes)
        if not name:
            return
        if filter == "Plik PDF (*.pdf)":
            try:
                linesOriginalText = self.mainWindow.ui.plainTextEditOutputImage.toPlainText().split("\n")
                template = pd.DataFrame(linesOriginalText, dtype=str, columns=[""])
                html = template.to_html(index=False, border=0)
                htmlFile = open("temp.html", "w", encoding="utf-8")
                htmlFile.write(html)
                htmlFile.close()

                doc = QTextDocument()
                try:
                    html = open("temp.html", "r", encoding="utf-8")
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z szablonem PDF \n" + str(inst))
                doc.setHtml(html.read())
                html.close()

                try:
                    printer = QPrinter()
                    printer.setOutputFileName(name)
                    printer.setOutputFormat(QPrinter.PdfFormat)
                    printer.setPageSize(QPrinter.A4)
                    printer.setPageMargins(4, 4, 4, 4, QPrinter.Millimeter)

                    doc.print_(printer)

                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z tworzeniem PDF \n" + str(inst))
                os.remove('temp.html')
            except Exception as inst:
                UiFunction.showErrorDialog(inst)

        elif filter == "Plik tekstowy (*.txt)":
            try:
                file = open(name, 'w')
            except Exception as inst:
                UiFunction.showErrorDialog("Wystąpił problem podczas otwierania wybranego pliku \n" + str(inst))
            output = self.mainWindow.ui.plainTextEditOutputImage.toPlainText()
            file.write(output)
            file.close()



    # next file in preview.
    # TODO when the window is maximized, when the photo is changegd the preview frame size increases
    def nextImage(self):
        try:
            if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage >= 0:
                self.mainWindow.whichImage += 1
                if self.mainWindow.whichImage == len(self.mainWindow.listOfElementsToRecognize):
                    self.mainWindow.whichImage = 0
                    self.mainWindow.ui.previewImage.setPixmap(
                        QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                        .scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                    self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation))
                    self.mainWindow.ui.previewImage.setScaledContents(True)
                else:
                    self.mainWindow.ui.previewImage.setPixmap(
                        QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                        .scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                    self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation))
                    self.mainWindow.ui.previewImage.setScaledContents(True)
        except Exception as inst:
            UiFunction.showErrorDialog("Wystąpił problem przy tworzeniu podglądu \n" + str(inst))
        self.mainWindow.ui.labelCurrentImageNumber.setText(str(self.mainWindow.whichImage + 1))

    #next file in preview
    # TODO this same bug like in nextImage method
    def previousImage(self):
        try:
            if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage < len(
                    self.mainWindow.listOfElementsToRecognize):
                self.mainWindow.whichImage -= 1
                if self.mainWindow.whichImage < 0:
                    self.mainWindow.whichImage = len(self.mainWindow.listOfElementsToRecognize) - 1
                    self.mainWindow.ui.previewImage.setPixmap(
                        QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                        .scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                    self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation))
                    self.mainWindow.ui.previewImage.setScaledContents(True)
                else:
                    self.mainWindow.ui.previewImage.setPixmap(
                        QPixmap(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                        .scaled(self.mainWindow.ui.previewImage.maximumHeight(),
                                                                    self.mainWindow.ui.previewImage.maximumWidth(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation))
                    self.mainWindow.ui.previewImage.setScaledContents(True)
        except Exception as inst:
            UiFunction.showErrorDialog("Wystąpił problem przy tworzeniu podglądu \n" + str(inst))
        self.mainWindow.ui.labelCurrentImageNumber.setText(str(self.mainWindow.whichImage + 1))

    # recognize text from all picture in listOfElementsToRecognize list
    def recognizeAll(self):
        try:
            if len(self.mainWindow.listOfElementsToRecognize) == 0:
                UiFunction.showErrorDialog("Najpierw wybierz pliki")
                return
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
                try:
                    if self.mainWindow.ui.checkBoxSecondLanguageImage.isChecked():
                        self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(pytesseract.image_to_string(image,
                                                                                                                lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower() +
                                                                                                                     "+" + self.mainWindow.ui.comboBoxSecondLanguageImage.currentText().lower()))
                    else:
                        self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(
                            pytesseract.image_to_string(image,
                                                        lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower()))
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z odczytywaniem tekstu \n" + str(inst))
            progressDialog.setValue(len(self.mainWindow.listOfElementsToRecognize))
        except Exception as inst:
            UiFunction.showErrorDialog("Wystąpił problem podczas rozpoznawania tekstu \n" + str(inst))

    # recognition of text from a photo that is currently on preview
    def recognizeCurrent(self):
        self.mainWindow.ui.plainTextEditOutputImage.clear()
        if len(self.mainWindow.queueToRecognize) == 0:
            self.mainWindow.ui.plainTextEditOutputImage.clear()
            if len(self.mainWindow.listOfElementsToRecognize) == 0:
                UiFunction.showErrorDialog("Najpierw wybierz pliki")
                return
            image = self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage]
            try:
                if self.mainWindow.ui.checkBoxSecondLanguageImage.isChecked():
                    self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(pytesseract.image_to_string(image,
                                                                                                          lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower() +
                                                                                                               "+" + self.mainWindow.ui.comboBoxSecondLanguageImage.currentText().lower()))
                else:
                    self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(
                        pytesseract.image_to_string(image,
                                                    lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower()))
            except Exception as inst:
                UiFunction.showErrorDialog("Wystąpił problem z odczytywaniem tekstu \n" + str(inst))
        else:
            number = self.mainWindow.ui.textEditQueueImage.toPlainText().split(',')
            uiFunction = UiFunction(self.mainWindow)
            progressDialog = uiFunction.progressBarDialog("Odczytywanie tekstu",
                                                          len(number))
            k = 0
            progressDialog.setValue(0)
            for i in number:
                k = k+1
                progressDialog.setValue(k)
                if progressDialog.wasCanceled():
                    break
                if len(self.mainWindow.listOfElementsToRecognize) == 0:
                    UiFunction.showErrorDialog("Najpierw wybierz pliki")
                    return
                image = self.mainWindow.listOfElementsToRecognize[int(i) - 1]
                self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(
                    "---------Grafika " + str(int(i)) + "---------")
                try:
                    if self.mainWindow.ui.checkBoxSecondLanguageImage.isChecked():
                        self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(pytesseract.image_to_string(image,
                                                                                                              lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower() +
                                                                                                                   "+" + self.mainWindow.ui.comboBoxSecondLanguageImage.currentText().lower()))
                    else:
                        self.mainWindow.ui.plainTextEditOutputImage.appendPlainText(
                            pytesseract.image_to_string(image,
                                                        lang=self.mainWindow.ui.comboBoxLanguageImage.currentText().lower()))
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z odczytywaniem tekstu \n" + str(inst))
            progressDialog.setValue(len(number))

    def addToQueue(self):
        if len(self.mainWindow.queueToRecognize) == 0:
            if len(self.mainWindow.listOfElementsToRecognize) == 0:
                UiFunction.showErrorDialog("Najpierw wybierz pliki")
                return
            self.mainWindow.ui.textEditQueueImage.setText(" " + str(self.mainWindow.whichImage + 1))
        else:
            self.mainWindow.ui.textEditQueueImage.setText(self.mainWindow.ui.textEditQueueImage.toPlainText() + ", " + str(self.mainWindow.whichImage + 1))
        self.mainWindow.queueToRecognize.append(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])

    def clearQueue(self):
        self.mainWindow.queueToRecognize.clear()
        self.mainWindow.ui.textEditQueueImage.setText("")

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
        self.mainWindow.ui.btnAddToQueueImage.clicked.connect(lambda: self.addToQueue())
        self.mainWindow.ui.btnClearQueueImage.clicked.connect(lambda: self.clearQueue())


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

            #This is not fastest solution, but work very well

            for i in range(pdfFile.numPages):
                progressDialog.setValue(i)
                if progressDialog.wasCanceled():
                    break
                try:
                    output = PdfFileWriter()
                    output.addPage(pdfFile.getPage(i))
                    with open("temp.pdf", "wb") as outputStream:
                        output.write(outputStream)
                    image = pdf2image.convert_from_path("temp.pdf", poppler_path="./bin/poppler/poppler-0.68.0/bin",
                                                                     thread_count=4)
                    self.mainWindow.listOfElementsToRecognize.append(image[0])
                except Exception as inst:
                    UiFunction.showErrorDialog("Otwieranie PDF nie powiodło się \n" + str(inst))
                if os.path.exists("temp.pdf"):
                    os.remove("temp.pdf")

            progressDialog.setValue(pdfFile.numPages)

            # to make QPixmap object, before from JPEG or other format necessary is make ImageQt object
            # or normal Image object
            try:
                imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height(),
                                                                    self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation)
                self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
                self.mainWindow.ui.previewPDF.setScaledContents(True)
                self.mainWindow.whichImage = 0
                self.mainWindow.ui.labelCurrentPageNumberPDF.setText(str(self.mainWindow.whichImage+1))
                self.mainWindow.ui.labelAllPageNumberPDF.setText(str(len(self.mainWindow.listOfElementsToRecognize)))
            except Exception as inst:
                UiFunction.showErrorDialog("Tworzenie podglądu nie powiodło się \n" + str(inst))
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
        self.mainWindow.ui.btnAddToQueuePDF.clicked.connect(lambda: self.addToQueue())
        self.mainWindow.ui.btnClearQueuePDF.clicked.connect(lambda: self.clearQueue())

    def saveOutputPDF(self):
        filesTypes = "Plik tekstowy (*.txt);;Plik PDF (*.pdf)"
        name, filter = QFileDialog.getSaveFileName(self.mainWindow, 'Zapisz plik', "Bez nazwy", filesTypes)
        if not name:
            return
        if filter == "Plik PDF (*.pdf)":
            try:
                linesOriginalText = self.mainWindow.ui.plainTextEditOutputPDF.toPlainText().split("\n")
                template = pd.DataFrame(linesOriginalText, dtype=str, columns=[""])
                html = template.to_html(index=False, border=0)
                htmlFile = open("temp.html", "w", encoding="utf-8")
                htmlFile.write(html)
                htmlFile.close()

                doc = QTextDocument()
                try:
                    html = open("temp.html", "r", encoding="utf-8")
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z szablonem PDF \n" + str(inst))
                doc.setHtml(html.read())
                html.close()

                try:
                    printer = QPrinter()
                    printer.setOutputFileName(name)
                    printer.setOutputFormat(QPrinter.PdfFormat)
                    printer.setPageSize(QPrinter.A4)
                    printer.setPageMargins(4, 4, 4, 4, QPrinter.Millimeter)

                    doc.print_(printer)
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z generowaniem pliku PDF \n" + str(inst))
                os.remove('temp.html')
            except Exception as inst:
                UiFunction.showErrorDialog("Wystąpił problem z tworzeniem pliku PDF \n" + str(inst))

        elif filter == "Plik tekstowy (*.txt)":
            try:
                try:
                    file = open(name, 'w')
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z wybranym plikiem \n" + str(inst))
                output = self.mainWindow.ui.plainTextEditOutputPDF.toPlainText()
                file.write(output)
                file.close()
            except Exception as inst:
                UiFunction.showErrorDialog("Wystąpił problem z zapisem pliku \n" + str(inst))


    def nextImage(self):
        if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage >= 0:
            self.mainWindow.whichImage += 1
            try:
                if self.mainWindow.whichImage == len(self.mainWindow.listOfElementsToRecognize):
                    self.mainWindow.whichImage = 0
                    imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height()(),
                                                                    self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation)
                    self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
                    self.mainWindow.ui.previewPDF.setScaledContents(True)
                else:

                    imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height(),
                                                                    self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation)
                    self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
                    self.mainWindow.ui.previewPDF.setScaledContents(True)
            except Exception as inst:
                UiFunction.showErrorDialog("Wystąpił problem z tworzeniem podglądu \n" + str(inst))
        self.mainWindow.ui.labelCurrentPageNumberPDF.setText(str(self.mainWindow.whichImage + 1))

    def previousImage(self):
        if len(self.mainWindow.listOfElementsToRecognize) > 1 and self.mainWindow.whichImage < len(
                self.mainWindow.listOfElementsToRecognize):
            try:
                self.mainWindow.whichImage -= 1
                if self.mainWindow.whichImage < 0:
                    self.mainWindow.whichImage = len(self.mainWindow.listOfElementsToRecognize) - 1
                    imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height(),
                                                                    self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation)
                    self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
                    self.mainWindow.ui.previewPDF.setScaledContents(True)
                else:
                    imageqt = ImageQt(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])
                    imgagePixmap = QPixmap(imageqt).scaled(self.mainWindow.ui.previewPDF.height(),
                                                                    self.mainWindow.ui.previewPDF.width(),QtCore.Qt.KeepAspectRatio,
                     QtCore.Qt.SmoothTransformation)
                    self.mainWindow.ui.previewPDF.setPixmap(imgagePixmap)
                    self.mainWindow.ui.previewPDF.setScaledContents(True)
            except Exception as inst:
                UiFunction.showErrorDialog("Wystąpił problem z tworzeniem podglądu \n" + str(inst))
        self.mainWindow.ui.labelCurrentPageNumberPDF.setText(str(self.mainWindow.whichImage + 1))

    def recognizeAll(self):
        try:
            uiFunction = UiFunction(self.mainWindow)
            if len(self.mainWindow.listOfElementsToRecognize) == 0:
                UiFunction.showErrorDialog("Najpierw wybierz plik")
                return
            progressDialog = uiFunction.progressBarDialog("Odczytywanie tekstu", len(self.mainWindow.listOfElementsToRecognize))
            progressDialog.setValue(0)

            self.mainWindow.ui.plainTextEditOutputPDF.clear()
            for i in range(0, len(self.mainWindow.listOfElementsToRecognize)):
                progressDialog.setValue(i)
                if progressDialog.wasCanceled():
                    break
                image = self.mainWindow.listOfElementsToRecognize[i]
                self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText("---------Strona " + str(i + 1) + "---------")
                try:
                    if self.mainWindow.ui.checkBoxSecondLanguagePDF.isChecked():
                        self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(pytesseract.image_to_string(image,
                                                                                                              lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower() +
                                                                                                                   "+" + self.mainWindow.ui.comboBoxSecondLanguagePDF.currentText().lower()))
                    else:
                        self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(
                            pytesseract.image_to_string(image,
                                                        lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower()))
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z odczytywaniem tekstu \n" + str(inst))
            progressDialog.setValue(len(self.mainWindow.listOfElementsToRecognize))
        except Exception as inst:
            UiFunction.showErrorDialog("Wystąpił problem podczas rozpoznawania tekstu \n" + str(inst))

    def recognizeCurrent(self):
        try:
            self.mainWindow.ui.plainTextEditOutputPDF.clear()
            if len(self.mainWindow.queueToRecognize) == 0:
                self.mainWindow.ui.plainTextEditOutputPDF.clear()
                if len(self.mainWindow.listOfElementsToRecognize) == 0:
                    UiFunction.showErrorDialog("Najpierw wybierz plik")
                    return
                image = self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage]
                try:
                    if self.mainWindow.ui.checkBoxSecondLanguagePDF.isChecked():
                        self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(pytesseract.image_to_string(image,
                                                                                                              lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower() +
                                                                                                                   "+" + self.mainWindow.ui.comboBoxSecondLanguagePDF.currentText().lower()))
                    else:
                        self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(
                            pytesseract.image_to_string(image, lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower()))
                except Exception as inst:
                    UiFunction.showErrorDialog("Wystąpił problem z odczytywaniem tekstu \n" + str(inst))
            else:
                number = self.mainWindow.ui.textEditQueuePDF.toPlainText().split(',')
                uiFunction = UiFunction(self.mainWindow)
                progressDialog = uiFunction.progressBarDialog("Odczytywanie tekstu",
                                                              len(number))
                k = 0
                progressDialog.setValue(k)
                self.mainWindow.ui.plainTextEditOutputImage.clear()
                for i in number:
                    k = k + 1
                    progressDialog.setValue(k)
                    if progressDialog.wasCanceled():
                        break
                    if len(self.mainWindow.listOfElementsToRecognize) == 0:
                        UiFunction.showErrorDialog("Najpierw wybierz plik")
                        return
                    image = self.mainWindow.listOfElementsToRecognize[int(i)-1]
                    self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText("---------Strona " + str(int(i)) + "---------")
                    try:
                        if self.mainWindow.ui.checkBoxSecondLanguagePDF.isChecked():
                            self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(pytesseract.image_to_string(image,
                                                                                                                  lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower() +
                                                                                                                       "+" + self.mainWindow.ui.comboBoxSecondLanguagePDF.currentText().lower()))
                        else:
                            self.mainWindow.ui.plainTextEditOutputPDF.appendPlainText(
                                pytesseract.image_to_string(image,
                                                            lang=self.mainWindow.ui.comboBoxLanguagePDF.currentText().lower()))
                    except Exception as inst:
                        UiFunction.showErrorDialog("Wystąpił problem z odczytywaniem tekstu \n" + str(inst))
                progressDialog.setValue(len(number))
        except Exception as inst:
            UiFunction.showErrorDialog("Wystąpił problem podczas rozpoznawania tekstu \n" + str(inst))


    def addToQueue(self):
        if len(self.mainWindow.queueToRecognize) == 0:
            if len(self.mainWindow.listOfElementsToRecognize) == 0:
                UiFunction.showErrorDialog("Najpierw wybierz plik")
                return
            self.mainWindow.ui.textEditQueuePDF.setText(" " + str(self.mainWindow.whichImage + 1))
        else:
            self.mainWindow.ui.textEditQueuePDF.setText(self.mainWindow.ui.textEditQueuePDF.toPlainText() + ", " + str(self.mainWindow.whichImage + 1))
        self.mainWindow.queueToRecognize.append(self.mainWindow.listOfElementsToRecognize[self.mainWindow.whichImage])

    def clearQueue(self):
        self.mainWindow.queueToRecognize.clear()
        self.mainWindow.ui.textEditQueuePDF.setText("")
