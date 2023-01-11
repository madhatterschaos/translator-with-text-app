from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox

from googletrans import Translator


class ChoseLang(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sample_five.ui', self)

        self.SaysWhat1.setReadOnly(True)
        self.SaysWhat2.setReadOnly(True)
        self.SaysWhat3.setReadOnly(True)

        self.WordFor.setReadOnly(True)

        self.lang = 'en'
        self.word = str()

        self.Englishbtn.clicked.connect(self.en_trans)
        self.Frenchbtn.clicked.connect(self.fr_trans)
        self.Germanbtn.clicked.connect(self.de_trans)
        self.Spanishbtn.clicked.connect(self.es_trans)

    def en_trans(self):
        self.lang = 'en'
        self.diff_trans()

    def fr_trans(self):
        self.lang = 'fr'
        self.diff_trans()

    def de_trans(self):
        self.lang = 'de'
        self.diff_trans()

    def es_trans(self):
        self.lang = 'es'
        self.diff_tran()

    def diff_trans(self):
        def showWindowDumb():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Введите слово для перевода')
            msgBox.setWindowTitle('Слово для перевода не введено')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()

        self.word = self.WordRu.toPlainText()
        if len(self.word) == 0:
            showWindowDumb()
        else:
            self.word = self.word.lower()
            translator = Translator()
            trans = translator.translate(self.word, dest='ru', src=self.lang).text
            trans = trans.lower()
            self.WordFor.setPlainText(trans)
