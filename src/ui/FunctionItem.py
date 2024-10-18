from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *

class FunctionItem(QWidget):
    def __init__(self, func_name):
        super().__init__()
        self.function_name = func_name
        self.layout = QHBoxLayout()

        self.func_item = QPushButton(func_name, parent=self)
        self.func_item.setStyleSheet("background-color: rgb(155. 155, 155);"
                                     " color: rgb(0, 0, 0); "
                                     "font-size: 35px; "
                                     "text-align: left;")
        self.func_item.setFixedSize(1000, 75)

        self.func_item.clicked.connect(self.__process_btn_click)
        self.layout.addWidget(self.func_item)

        self.setLayout(self.layout)

    def __process_btn_click(self, e):
        print("Button clicked", e)