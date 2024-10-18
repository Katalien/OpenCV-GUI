from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI.ParameterWindow import *

class FunctionItem(QWidget):
    func_params_signal = pyqtSignal(dict)
    def __init__(self, func_name):
        super().__init__()
        self.function_name = func_name
        self.layout = QVBoxLayout()

        self.func_item = QPushButton(func_name, parent=self)
        self.func_item.setStyleSheet("background-color: rgb(155. 155, 155);"
                                     " color: rgb(0, 0, 0); "
                                     "font-size: 35px; "
                                     "text-align: left;")
        self.func_item.setFixedSize(1000, 75)

        self.func_item.clicked.connect(self.__process_btn_click)
        self.layout.addWidget(self.func_item)
        self.param_dropdown_widget = self.__set_param_drop_down_widget()
        self.layout.addWidget(self.param_dropdown_widget)
        self.setLayout(self.layout)

    def __process_btn_click(self):
        print("Button clicked", self.function_name)
        if self.param_dropdown_widget.isVisible():
            self.param_dropdown_widget.setVisible(False)
        else:
            self.param_dropdown_widget.setVisible(True)
            self.param_dropdown_widget.param_kernel_size_signal.connect(self.__get_params)

    def __get_params(self, params):
        self.func_params_signal.emit(params)
        print(f"Func item connect params {params}")

    def __set_param_drop_down_widget(self):
        if self.function_name == "GaussBlur":
            return GaussBlurParameterWindow()