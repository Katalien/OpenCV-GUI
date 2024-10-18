from PyQt5.QtCore import *
from PyQt5.QtWidgets import *



class FunctionSelectorWidget(QDialog):
    selected_func_signal = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Available Functions")

        self.layout = QVBoxLayout()
        self.selector_window = QListWidget()
        self.selector_window.addItems(["GaussBlur", "Denoising", "BGR2RGB", "Thresholding"])
        self.selector_window.currentTextChanged.connect(self.text_changed)

        ok_button = QPushButton("Ok")
        ok_button.clicked.connect(self.__on_ok_button_click)


        self.layout.addWidget(self.selector_window)
        self.layout.addWidget(ok_button)

        self.setLayout(self.layout)

    def text_changed(self, s):
        pass

    def __on_ok_button_click(self):
        self.selected_func_signal.emit(self.selector_window.currentItem().text())
        self.close()