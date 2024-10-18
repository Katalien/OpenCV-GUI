from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from ui.FunctionItem import FunctionItem

class FuncListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.func_items_list = []
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    def add_item(self, func_name):
        func_item = FunctionItem(func_name)
        self.func_items_list.append(func_item)
        self.layout.addWidget(func_item)

    def get_items(self):
        return self.func_items_list
