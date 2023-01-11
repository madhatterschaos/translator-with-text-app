import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QFileDialog

from googletrans import Translator

import pymorphy2

from helpme import HelpMe
from new_added_word import NewTrans
from chose_lang import ChoseLang
from opened_stats import OpenedStats


class MainWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sample_one3.ui', self)

        self.word = str()
        self.count_of_new_words = 0
        self.count_of_choose_text = 0
        self.count_of_asked_words = 0
        self.trans = str()

        self.ChoseTextbtn.clicked.connect(self.choosetext)
        self.Translatebtn.clicked.connect(self.check_is_empty)
        self.Instructionbtn.clicked.connect(self.openHowToUse)
        self.AddNewWord.clicked.connect(self.openAddNewWord)
        self.ChooseLang.clicked.connect(self.openChooseLang)
        self.Statsbtn.clicked.connect(self.openStats)

        self.WordTranslated.setReadOnly(True)

        self.conn = sqlite3.connect('files/database.sqlite')

    def check_is_empty(self):
        inp_word = self.WordToTranslate.toPlainText()

        def showWindow():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Введите слово для перевода')
            msgBox.setWindowTitle('Слово для перевода не введено')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()

        if len(inp_word) == 0:
            showWindow()
        else:
            self.count_of_asked_words += 1
            word = inp_word
            morph = pymorphy2.MorphAnalyzer()
            try:
                self.word = morph.parse(f'{word}')[0].inflect(
                    {'sing', 'nomn'}).word
            except AttributeError:
                self.word = inp_word
            self.word = self.word.lower()
            self.rememberNewTranslation()
            self.trans = self.trans.lower()
            self.WordTranslated.setPlainText(self.trans)

    def choosetext(self):
        self.count_of_choose_text += 1
        filetoopen = \
            QFileDialog.getOpenFileName(self, "Выберете файл с текстом", "", "Текстовый файл (*.txt);;Все файлы (*)")[0]
        try:
            file_text = open(filetoopen, 'r', encoding='utf-8').read()
        except FileNotFoundError:
            return None
        self.TextToTranslate.setPlainText(file_text)

    def rememberNewTranslation(self):

        cur = self.conn.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS statsTable (
            id   INTEGER PRIMARY KEY AUTOINCREMENT
                        NOT NULL
                        UNIQUE,
            word TEXT NOT NULL,
            word_translation TEXT NOT NULL
        );
        """)

        was_in_table = cur.execute(f"""SELECT * FROM statsTable 
                                    WHERE word = ?""", (self.word,)).fetchall()

        if len(was_in_table) == 0:
            self.count_of_new_words += 1
            translator = Translator()
            self.trans = translator.translate(self.word, dest='en', src='ru').text

            cur.execute(f"""INSERT INTO statsTable(word, word_translation)
                                VALUES ('{self.word}', '{self.trans}')""")
        else:
            self.trans = was_in_table[0][2]

        self.conn.commit()

    def openHowToUse(self):
        self.checkwindow = HelpMe()
        self.checkwindow.show()

    def openAddNewWord(self):
        self.addwordwindow = NewTrans(self.conn)
        self.addwordwindow.show()

    def openChooseLang(self):
        self.chooselangwindow = ChoseLang()
        self.chooselangwindow.show()

    def openStats(self):
        self.openstatswindow = OpenedStats(self.count_of_new_words, self.count_of_choose_text,
                                           self.count_of_asked_words)
        self.openstatswindow.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MainWidget()
    ex.show()
    sys.exit(app.exec_())
    ex.conn.close()
