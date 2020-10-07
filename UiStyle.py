from PySide2.QtGui import QIcon, QPixmap

class UiStyle():

    # method in this class are use to set icons of buttons and other elements.
    #TODO put all icons to resources file in QT designer and use this file, then this class will not be necessary

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow


    def correctingIconsPathAndVisibleSettings(self):
        self.correctingIconsWindow()
        self.correctingIconsImageRecognize()
        self.correctingIconsPDFRecognize()

        self.mainWindow.ui.LabelCopyright.setVisible(False)
        self.mainWindow.ui.comboBoxSecondLanguageImage.setVisible(False)
        self.mainWindow.ui.comboBoxSecondLanguagePDF.setVisible(False)


    def correctingIconsWindow(self):
        self.mainWindow.ui.btnMinimize.setIcon(QIcon(u"uiForms/Icons/windowIcon/cil-window-minimize.png"))
        self.mainWindow.ui.btnMaximize.setIcon(QIcon(u"uiForms/Icons/windowIcon/cil-window-maximize.png"))
        self.mainWindow.ui.btnX.setIcon(QIcon(u"uiForms/Icons/windowIcon/cil-x.png"))
        self.mainWindow.ui.btnImageRecognize.setIcon(QIcon(u"uiForms/Icons/64x64Image.png"))
        self.mainWindow.ui.btnPDFRecognize.setIcon(QIcon(u"uiForms/Icons/64x64PDF.png"))

    def correctingIconsImageRecognize(self):
        self.mainWindow.ui.previewImage.setPixmap(QPixmap(u"uiForms/Icons/128x128 Preview.png"))
        self.mainWindow.ui.btnSaveImage.setIcon(QIcon(u"uiForms/Icons/cil-save.png"))
        self.mainWindow.ui.btnPreviewLeftImage.setIcon(QIcon(u"uiForms/Icons/bold-arrow-left.png"))
        self.mainWindow.ui.btnPreviewRightImage.setIcon(QIcon(u"uiForms/Icons/bold-arrow-right.png"))
        self.mainWindow.ui.btnChooseFIlesImage.setIcon(QIcon(u"uiForms/Icons/computer-folder-open.png"))

    def correctingIconsPDFRecognize(self):
        self.mainWindow.ui.previewPDF.setPixmap(QPixmap(u"uiForms/Icons/128x128 Preview.png"))
        self.mainWindow.ui.btnSavePDF.setIcon(QIcon(u"uiForms/Icons/cil-save.png"))
        self.mainWindow.ui.btnPreviewLeftPDF.setIcon(QIcon(u"uiForms/Icons/bold-arrow-left.png"))
        self.mainWindow.ui.btnPreviewRightPDF.setIcon(QIcon(u"uiForms/Icons/bold-arrow-right.png"))
        self.mainWindow.ui.btnChooseFIlesPDF.setIcon(QIcon(u"uiForms/Icons/computer-folder-open.png"))



