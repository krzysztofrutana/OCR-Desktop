import os

from PySide2.QtGui import QIcon, QTextDocument
from PySide2.QtPrintSupport import QPrinter
from PySide2.QtWidgets import QWidget, QFileDialog
from googletrans import Translator
from uiForms.translateUI import Ui_TranslateWindow

import pandas as pd

class TranslateWindow(QWidget):
    LANGUAGES = {
        'af': 'afrikaans',
        'sq': 'albański',
        'am': 'amharski',
        'ar': 'arabski',
        'az': 'azerski',
        'eu': 'beskijski',
        'be': 'białoruski',
        'bn': 'bengalski',
        'bs': 'bośniacki',
        'bg': 'bułkgaski',
        'ca': 'kataloński',
        'ceb': 'cebuański',
        'ny': 'cziczewa',
        'zh-cn': 'chiński (uproszczony)',
        'zh-tw': 'chiński (tradycyjny)',
        'co': 'korsykański',
        'hr': 'chorwacki',
        'cs': 'czeski',
        'da': 'duński',
        'nl': 'holenderski',
        'en': 'angielski',
        'eo': 'esperanto',
        'et': 'estoński',
        'tl': 'filipiński',
        'fi': 'fiński',
        'fr': 'francuski',
        'fy': 'fryzyjski',
        'gl': 'galicyjski',
        'ka': 'gruziński',
        'de': 'niemiecki',
        'el': 'grecki',
        'gu': 'gudżarati',
        'ht': 'kreolski haitański',
        'ha': 'hausa',
        'haw': 'hawajski',
        'he': 'hebrajski',
        'hi': 'hinduski',
        'hmn': 'hmong',
        'hu': 'węgierski',
        'is': 'islandzki',
        'ig': 'igbo',
        'id': 'indonezyjski',
        'ga': 'irlandzki',
        'it': 'włoski',
        'ja': 'japoński',
        'jw': 'jawajski',
        'kn': 'kannada',
        'kk': 'kazachski',
        'km': 'khmerski',
        'ko': 'koreański',
        'ku': 'kurdyjski',
        'ky': 'kirgiski',
        'lo': 'laotański',
        'la': 'łaciński',
        'lv': 'łotewski',
        'lt': 'litewski',
        'lb': 'luksemburski',
        'mk': 'macedoński',
        'mg': 'malgaski',
        'ms': 'malajski',
        'ml': 'malajski',
        'mt': 'maltański',
        'mi': 'maoryski',
        'mr': 'marathi',
        'mn': 'mongolski',
        'ne': 'nepalski',
        'no': 'norweski',
        'ps': 'pashto',
        'fa': 'perski',
        'pl': 'polski',
        'pt': 'portugalski',
        'pa': 'pendżabski',
        'ro': 'rumuński',
        'ru': 'rosyjski',
        'sm': 'samoański',
        'gd': 'szkocki gaelicki',
        'sr': 'serbski',
        'sd': 'sindhi',
        'sk': 'słowacki',
        'sl': 'słoweński',
        'so': 'somalijski',
        'es': 'hiszpański',
        'su': 'sundajski',
        'sw': 'suagili',
        'sv': 'szwedzki',
        'tg': 'tadżycki',
        'ta': 'tamilski',
        'te': 'telugu',
        'th': 'tajski',
        'tr': 'turecki',
        'uk': 'ukraiński',
        'ur': 'urdu',
        'ug': 'ujgurski',
        'uz': 'uzbecki',
        'vi': 'wietnamski',
        'cy': 'walijski',
        'xh': 'xhosa',
        'yi': 'jidysz',
        'yo': 'joruba',
        'zu': 'zulu',
    }


    def __init__(self, textToTranslate):
        super(TranslateWindow, self).__init__()
        self.ui = Ui_TranslateWindow()
        self.ui.setupUi(self)
        self.show()
        self.textToTranslate = textToTranslate

        self.ui.label.setVisible(False)
        self.ui.labelSearchLanguage.setVisible(False)
        self.ui.btnSaveEverything.setIcon(QIcon(u"uiForms/Icons/cil-save.png"))
        self.ui.btnSaveOnlyTranslate.setIcon(QIcon(u"uiForms/Icons/cil-save.png"))
        self.ui.plainTextEditOriginalText.appendPlainText(textToTranslate)
        self.ui.btnTranslateEverything.clicked.connect(lambda : self.translateText(self.ui.plainTextEditOriginalText.toPlainText()))
        self.ui.btnTranslateSelected.clicked.connect(lambda : self.translateText(self.ui.plainTextEditOriginalText.textCursor().selectedText()))
        self.ui.btnSaveEverything.clicked.connect(lambda : self.saveOriginalAndTranslate())
        self.ui.btnSaveOnlyTranslate.clicked.connect(lambda : self.saveTranslate())

        languages = self.sortuj(self.LANGUAGES)

        self.ui.comboBoxFromLanguage.addItem("Wykryj język")
        self.ui.comboBoxFromLanguage.addItems(languages.values())
        self.ui.comboBoxFromLanguage.setCurrentIndex(0)

        self.ui.comboBoxToLanguage.addItems(languages.values())
        self.ui.comboBoxToLanguage.setCurrentText("polski")

        self.comboboxChanged()

        self.ui.comboBoxFromLanguage.currentIndexChanged.connect(lambda : self.comboboxChanged())



        self.refreshStylesheet()


    def translateText(self, textToTranslate):
        self.ui.plainTextEditTranslateText.clear()
        translator = Translator()
        if self.ui.comboBoxFromLanguage.currentText() == "Wykryj język":
            dest = list(self.LANGUAGES.keys())[
                list(self.LANGUAGES.values()).index(self.ui.comboBoxToLanguage.currentText())]
            translation = translator.translate(
                textToTranslate, dest=dest)
        else:
            dest = list(self.LANGUAGES.keys())[
                list(self.LANGUAGES.values()).index(self.ui.comboBoxToLanguage.currentText())]
            src = list(self.LANGUAGES.keys())[
                list(self.LANGUAGES.values()).index(self.ui.comboBoxFromLanguage.currentText())]
            translation = translator.translate(
                textToTranslate, dest=dest, src=src)
        self.ui.plainTextEditTranslateText.appendPlainText(translation.text)


    def sortuj(self, sl, sort='asc'):
        t = {}
        wartosci = list(sl.values())
        if sort == 'asc':
            try:
                wartosci.sort(reverse=True)
            except TypeError:
                return sl
        else:
            try:
                wartosci.sort()
            except TypeError:
                return sl
        while len(wartosci) > 0:
            w = wartosci.pop()
            for k, v in sl.items():
                if v == w:
                    t[k] = v
                    continue
        return t

    def comboboxChanged(self):
        if self.ui.comboBoxFromLanguage.currentText() == "Wykryj język":
            self.ui.label.setVisible(True)
            self.ui.labelSearchLanguage.setVisible(True)

            translator = Translator()
            if self.ui.plainTextEditOriginalText.toPlainText():
                languageDetect = translator.detect(self.ui.plainTextEditOriginalText.toPlainText()).lang
                languageDetect = list(self.LANGUAGES.values())[list(self.LANGUAGES.keys()).index(languageDetect)]
                self.ui.labelSearchLanguage.setText(languageDetect)
        else:
            self.ui.label.setVisible(False)
            self.ui.labelSearchLanguage.setVisible(False)

    def refreshStylesheet(self):
        comboboxes = [self.ui.comboBoxFromLanguage, self.ui.comboBoxToLanguage]

        for i in comboboxes:
            i.setStyleSheet(u"QComboBox{\n"
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
"}"
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

        plainTextEdits = [self.ui.plainTextEditOriginalText, self.ui.plainTextEditTranslateText]

        for i in plainTextEdits:
            i.setStyleSheet(u"QPlainTextEdit{\n"
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

    def saveOriginalAndTranslate(self):

        linesOriginalText = self.ui.plainTextEditOriginalText.toPlainText().split("\n")
        linesTranslateText = self.ui.plainTextEditTranslateText.toPlainText().split("\n")


        table = [linesOriginalText, linesTranslateText]
        filesTypes = "Plik tekstowy (*.txt);;Plik PDF (*.pdf)"

        name, filter = QFileDialog.getSaveFileName(self, 'Zapisz plik', "Bez nazwy", filesTypes)

        if not name:
            return
        if filter == "Plik PDF (*.pdf)":
            template = pd.DataFrame(table,dtype=str)
            template = template.T
            template.columns = ["Oryginał", "Tłumaczenie"]
            html = template.to_html(index=False, border=0)
            htmlFile = open("temp.html", "w", encoding="utf-8")
            htmlFile.write(html)
            htmlFile.close()

            doc = QTextDocument()
            html = open("temp.html", "r", encoding="utf-8")
            doc.setHtml(html.read())
            html.close()

            printer = QPrinter()
            printer.setOutputFileName(name)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setPageSize(QPrinter.A4)
            printer.setPageMargins(4, 4, 4, 4, QPrinter.Millimeter)

            doc.print_(printer)


        elif filter == "Plik tekstowy (*.txt)":
            file = open(name, "w", encoding='utf-8')
            if len(linesOriginalText) >= len(linesTranslateText):
                longer = linesOriginalText
            else:
                longer = linesTranslateText
            for index in range(len(longer)):
                if not linesOriginalText[index]:
                    linesOriginalText.append("")
                if not linesTranslateText[index]:
                    linesTranslateText.append("")
                if len(linesOriginalText[index]) == 0 and len(linesTranslateText[index]) == 0:
                    file.write("\n")
                else:
                    file.write(str(linesOriginalText[index]) + "     -->     " + str(linesTranslateText[index]) + "\n")
            file.close()
        os.remove('temp.html')

    def saveTranslate(self):
        filesTypes = "Plik tekstowy (*.txt);;Plik PDF (*.pdf)"
        name, filter = QFileDialog.getSaveFileName(self, 'Zapisz plik', "Bez nazwy", filesTypes)
        if not name:
            return
        if filter == "Plik PDF (*.pdf)":
            linesOriginalText = self.ui.plainTextEditOriginalText.toPlainText().split("\n")
            template = pd.DataFrame(linesOriginalText, dtype=str, columns=["Tłumaczenie"])
            html = template.to_html(index=False, border=0)
            htmlFile = open("temp.html", "w", encoding="utf-8")
            htmlFile.write(html)
            htmlFile.close()

            doc = QTextDocument()
            html = open("temp.html", "r", encoding="utf-8")
            doc.setHtml(html.read())
            html.close()

            printer = QPrinter()
            printer.setOutputFileName(name)
            printer.setOutputFormat(QPrinter.PdfFormat)
            printer.setPageSize(QPrinter.A4)
            printer.setPageMargins(4, 4, 4, 4, QPrinter.Millimeter)

            doc.print_(printer)

        elif filter == "Plik tekstowy (*.txt)":
            file = open(name, 'w')
            output = self.ui.plainTextEditTranslateText.toPlainText()
            file.write(output)
            file.close()
        os.remove('temp.html')