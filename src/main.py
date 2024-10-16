import sys
from PyQt5.QtWidgets import *
from ui import MainWindow

app = QApplication(sys.argv)

window = MainWindow.MainWindow()
window.show()

# Start the event loop.
app.exec()
