from PyQt5.QtWidgets import *

class IParameterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.setVisible(False)

    def get_parameters(self):
        pass