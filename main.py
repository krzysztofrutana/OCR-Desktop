################################################################################
##
## BY: Krzysztof Rutana
## PROJECT MADE WITH: Qt Designer and PySide2
## CREDITS: WANDERSON M.PIMENTA
##
## Many elements of this design have been borrowed from the WANDERSON M.PIMENTA
## project: structure (not all), method to handle events and resize windows etc.
## The rest of the functionality was created by me. This project can be used
## freely for all uses, as long as they maintain the respective credits only in
## the Python scripts.
##
################################################################################

import sys

from app_modules import *

try:
    from PIL import Image
except ImportError:
    import Image

class MainWindow(QMainWindow):

    #image storage list
    listOfElementsToRecognize = []

    #element number which is currently previewed
    whichImage = 0

    queueToRecognize = []

    windowMaximized = False


    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.oldPos = self.pos()

        self.ui.Pages.setCurrentIndex(0)

        uiStyle = UiStyle(self)
        uiStyle.correctingVisibleSettings()

        uiFunctions = UiFunction(self)
        uiFunctions.connectionsResizeDragingWindow()

        imageRecognizeFunction = ImageRecognizeFunction(self)
        imageRecognizeFunction.buttonsConnections()

        pdfRecognizeFunction = PDFRecognizeFunction(self)
        pdfRecognizeFunction.buttonsConnections()

        # this is WANDERSON M.PIMENTA to maximize windows after duble click on top frame of window
        # and draging window
        def dobleClickMaximizeRestore(event):
                # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QtCore.QEvent.MouseButtonDblClick:
                QtCore.QTimer.singleShot(250, lambda: uiFunctions.maximize())

        self.ui.FrameTop.mouseDoubleClickEvent = dobleClickMaximizeRestore

        def moveWindow(event):
            # IF MAXIMIZED CHANGE TO NORMAL
            if self.windowMaximized == True:
                self.showNormal()
                self.windowMaximized = False

            # MOVE WINDOW
            if event.buttons() == Qt.LeftButton:
                window.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.FrameTop.mouseMoveEvent = moveWindow



if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

