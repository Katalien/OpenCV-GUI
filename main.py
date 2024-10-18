import sys
from PyQt5.QtWidgets import *
from UI import MainWindow

app = QApplication(sys.argv)

window = MainWindow.MainWindow()
window.show()

app.exec()

