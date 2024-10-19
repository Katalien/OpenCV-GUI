from PyQt5.QtWidgets import *

class WarningWidget(QMessageBox):
    def __init__(self, text):
        super().__init__()
        self.text = text
        self.setIcon(QMessageBox.Warning)
        self.setWindowTitle("Warning")
        self.setText(str(text))
        self.setStandardButtons(QMessageBox.Ok)
        self.exec()