

class UiStyle():

    def __init__(self, mainWindow):
        self.mainWindow = mainWindow


    def correctingVisibleSettings(self):
        self.mainWindow.ui.LabelCopyright.setVisible(False)
        self.mainWindow.ui.comboBoxSecondLanguageImage.setVisible(False)
        self.mainWindow.ui.comboBoxSecondLanguagePDF.setVisible(False)

