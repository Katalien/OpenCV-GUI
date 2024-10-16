from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class FunctionSelectorWidget(QDialog):
    selected_func_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Available Functions")

        self.layout = QVBoxLayout()
        self.list_options = ["a", "b", "c", "d"]
        self.selector_window = QListWidget()
        self.selector_window.addItems(["one", "two", "three"])
        self.selector_window.currentTextChanged.connect(self.text_changed)

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.__on_ok_button_click)


        self.layout.addWidget(self.selector_window)
        self.layout.addWidget(ok_button)

        self.setLayout(self.layout)

    def text_changed(self, s):
        # Здесь ты можешь что-то делать с изменившимся текстом
        self.selected_text = s

    def __on_ok_button_click(self):
        self.selected_func_signal.emit(self.selector_window.currentItem().text())
        self.close()


class CVToolBar(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.add_button = QPushButton("Add function")
        self.add_button.clicked.connect(self.__add_button_clicked)
        self.layout.addWidget(self.add_button)

        self.func_layout = QWidget()
        self.layout.addWidget(self.func_layout)
        self.setLayout(self.layout)


    def __add_button_clicked(self):
        selector_window = FunctionSelectorWidget()
        selector_window.selected_func_signal.connect(self.function_selected)
        selector_window.exec()

    def function_selected(self, selected_text):
        print(selected_text, "in CVToolBar")