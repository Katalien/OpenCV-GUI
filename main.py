import sys
from PyQt5.QtWidgets import *
from ui import MainWindow

app = QApplication(sys.argv)

window = MainWindow.MainWindow()
window.show()

app.exec()

