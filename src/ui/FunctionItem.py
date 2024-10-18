from PyQt5.QtWidgets import *

class FunctionItem(QWidget):
    def __init__(self, func_name):
        super().__init__()
        self.function_name = func_name
        self.layout = QHBoxLayout()

        self.label = QLabel(func_name)
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)
