import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox


class NewTrans(QMainWindow):
    def __init__(self, conn):
        super().__init__()
        uic.loadUi('sample_four.ui', self)

        self.inp_word = str()
        self.inp_trans = str()

        self.lineEdit_0.setReadOnly(True)
        self.lineEdit_1.setReadOnly(True)
        self.rememberNewWordbtn.clicked.connect(self.rememberNewTrans)

        self.conn = conn

    def rememberNewTrans(self):
        self.inp_word = self.WordRu.toPlainText()
        self.inp_trans = self.WordEng.toPlainText()

        def showWindowRU():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Введите слово для перевода')
            msgBox.setWindowTitle('Слово для перевода не введено')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()

        def showWindowENG():
            msgBox = QMessageBox()
            msgBox.setIcon(QMessageBox.Information)
            msgBox.setText('Введите перевод слова')
            msgBox.setWindowTitle('Перевод не введен')
            msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            msgBox.exec()

        if len(self.inp_word) == 0:
            showWindowRU()
        elif len(self.inp_trans) == 0:
            showWindowENG()
        else:
            self.inp_word = self.inp_word.lower()
            self.inp_trans = self.inp_trans.lower()
            self.SaveNewWord()

    def SaveNewWord(self):
        cur = self.conn.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS statsTable (
                    id   INTEGER PRIMARY KEY AUTOINCREMENT
                                NOT NULL
                                UNIQUE,
                    word TEXT NOT NULL,
                    word_translation TEXT NOT NULL
                );
                """)

        cur.execute(f"""INSERT INTO statsTable(word, word_translation)
                                        VALUES ('{self.inp_word}', '{self.inp_trans}')""")

        self.conn.commit()
