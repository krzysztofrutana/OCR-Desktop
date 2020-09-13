
import sys

from PySide2.QtGui import QPixmap
from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from forms.mainUI import Ui_MainWindow
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

class MainWindow(QMainWindow):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


    listOfElementsToRecognizeStr= []
    listOfElementsToRecognizeImage = []
    whichImage = 0

    def openFileDialog(self):

        self.ui.plainTextEditFilePath.clear()
        self.ui.plainTextEditOutput.clear()

        self.dialog = QFileDialog.getOpenFileNames(self,"/home",
                                        )
        for i in range(0, len(self.dialog[0])):
            self.ui.plainTextEditFilePath.appendPlainText(str(self.dialog[0][i]) + "\n")
            self.listOfElementsToRecognizeStr.append(str(self.dialog[0][i]))
            self.listOfElementsToRecognizeImage.append(QPixmap(str(self.dialog[0][i])))

    def loadFiles(self):
        self.ui.preview.setPixmap(self.listOfElementsToRecognizeImage[0])
        self.ui.preview.setScaledContents(True)
        self.whichImage = 0

    def nextImage(self):
        if len(self.listOfElementsToRecognizeImage) > 1 and self.whichImage >= 0:
            self.whichImage += 1
            if self.whichImage == len(self.listOfElementsToRecognizeImage):
                self.whichImage = 0
                self.ui.preview.setPixmap(self.listOfElementsToRecognizeImage[self.whichImage])
            else:
                self.ui.preview.setPixmap(self.listOfElementsToRecognizeImage[self.whichImage])

    def previousImage(self):
        if len(self.listOfElementsToRecognizeImage) > 1 and self.whichImage < len(self.listOfElementsToRecognizeImage):
            self.whichImage -= 1
            if self.whichImage < 0:
                self.whichImage = len(self.listOfElementsToRecognizeImage) -1
                self.ui.preview.setPixmap(self.listOfElementsToRecognizeImage[self.whichImage])
            else:
                self.ui.preview.setPixmap(self.listOfElementsToRecognizeImage[self.whichImage])

    def recognizeAll(self):
        self.ui.plainTextEditOutput.clear()
        for i in range(0,len(self.listOfElementsToRecognizeImage)):
            image = Image.open(self.listOfElementsToRecognizeStr[i])
            self.ui.plainTextEditOutput.appendPlainText("Grafika " + str(i+1))
            if self.ui.comboBoxLanguage.currentText() == 'PL':
                self.ui.plainTextEditOutput.appendPlainText(pytesseract.image_to_string(image, lang='pol'))
            elif self.ui.comboBoxLanguage.currentText() == 'EN':
                self.ui.plainTextEditOutput.appendPlainText(pytesseract.image_to_string(image, lang='eng'))

    def recognizeCurrent(self):
        self.ui.plainTextEditOutput.clear()
        image = Image.open(self.listOfElementsToRecognizeStr[self.whichImage])
        self.ui.plainTextEditOutput.appendPlainText("Grafika " + str(self.whichImage + 1))
        if self.ui.comboBoxLanguage.currentText() == 'PL':
            self.ui.plainTextEditOutput.appendPlainText(pytesseract.image_to_string(image, lang='pol'))
        elif self.ui.comboBoxLanguage.currentText() == 'EN':
            self.ui.plainTextEditOutput.appendPlainText(pytesseract.image_to_string(image, lang='eng'))

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        languages = ['PL', 'EN']
        self.ui.comboBoxLanguage.addItems(languages)
        self.ui.comboBoxLanguage.setCurrentIndex(0)



        self.ui.pushButtonChooseFIles.clicked.connect(lambda : self.openFileDialog())
        self.ui.pushButtonLoadFiles.clicked.connect(lambda: self.loadFiles())
        self.ui.pushButtonPreviewLeft.clicked.connect(lambda : self.previousImage())
        self.ui.pushButtonPreviewRight.clicked.connect(lambda : self.nextImage())
        self.ui.pushButtonRecognizeAll.clicked.connect(lambda : self.recognizeAll())
        self.ui.pushButtonRecognizeCurrent.clicked.connect(lambda : self.recognizeCurrent())



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

