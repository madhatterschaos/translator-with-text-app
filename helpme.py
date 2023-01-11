from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow


class HelpMe(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('sample_three1.ui', self)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit_0.setReadOnly(True)
        self.plainTextEdit_1.setReadOnly(True)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_3.setReadOnly(True)
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_5.setReadOnly(True)
        self.plainTextEdit_6.setReadOnly(True)
        self.plainTextEdit_7.setReadOnly(True)
        self.plainTextEdit_8.setReadOnly(True)
        self.plainTextEdit_9.setReadOnly(True)
