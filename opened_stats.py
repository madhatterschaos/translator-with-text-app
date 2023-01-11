from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication


class OpenedStats(QMainWindow):
    def __init__(self, count_of_new_words=0, count_of_choose_text=0, count_of_asked_words=0):
        super().__init__()
        uic.loadUi('sample_six.ui', self)
        self.conwPT.setPlainText(f'{count_of_new_words}')
        self.coctPT.setPlainText(f'{count_of_choose_text}')
        self.coawPT.setPlainText(f'{count_of_asked_words}')
        self.plainTextEdit_0.setReadOnly(True)
        self.plainTextEdit_1.setReadOnly(True)
        self.plainTextEdit_2.setReadOnly(True)
        self.conwPT.setReadOnly(True)
        self.coctPT.setReadOnly(True)
        self.coawPT.setReadOnly(True)
