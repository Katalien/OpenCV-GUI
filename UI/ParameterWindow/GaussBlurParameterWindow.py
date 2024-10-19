from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI.ParameterWindow import IParameterWindow


class GaussBlurParameterWindow(IParameterWindow.IParameterWindow):
    param_signal = pyqtSignal(dict)

    def __init__(self):
        super().__init__()

        # Начальные значения для X и Y
        self.kernel_size_value_x = 5
        self.kernel_size_value_y = 5
        self.sigma_value_x = 0
        self.sigma_value_y = 0

        self.params_dict = self.__set_params()

        # Создаем элементы для X и Y
        self.param_name_label_x, self.kernel_size_slider_x = self.__create_slider("X", self.kernel_size_value_x)
        self.param_name_label_y, self.kernel_size_slider_y = self.__create_slider("Y", self.kernel_size_value_y)
        self.param_name_label_sigma_x, self.sigma_slider_x = self.__create_slider("SigmaX", self.sigma_value_x)
        self.param_name_label_sigma_y, self.sigma_slider_y = self.__create_slider("SigmaY", self.sigma_value_y)

        # Добавляем виджеты на layout
        self.layout.addWidget(self.param_name_label_x)
        self.layout.addWidget(self.kernel_size_slider_x)
        self.layout.addWidget(self.param_name_label_y)
        self.layout.addWidget(self.kernel_size_slider_y)
        self.layout.addWidget(self.param_name_label_sigma_x)
        self.layout.addWidget(self.sigma_slider_x)
        self.layout.addWidget(self.param_name_label_sigma_y)
        self.layout.addWidget(self.sigma_slider_y)

    def __set_params(self):
        dict = {"kernel_size_x": self.kernel_size_value_x,
         "kernel_size_y": self.kernel_size_value_y,
         "sigma_x": self.sigma_value_x,
         "sigma_y": self.sigma_value_y}
        self.param_signal.emit(dict)
        return dict


    def __create_slider(self, axis_name, initial_value):
        """
        Общая функция для создания слайдера и метки для оси X или Y.
        """
        if axis_name == "X" or axis_name == "Y":
            param_name_label = QLabel(f"Kernel size {axis_name} = {initial_value}")
        else:
            param_name_label = QLabel(f"{axis_name} = {initial_value}")
        kernel_size_slider = QSlider(Qt.Horizontal)
        kernel_size_slider.setMinimum(1)
        kernel_size_slider.setMaximum(100)
        kernel_size_slider.setValue(initial_value)
        kernel_size_slider.valueChanged.connect(lambda val: self.__change_value(val, axis_name))
        return param_name_label, kernel_size_slider

    def __change_value(self, new_val, axis):
        """
        Изменение значения слайдера и обновление метки.
        """
        if (axis == "X" or axis == "Y") and new_val % 2 == 0:
            new_val += 1

        if axis == "X":
            self.kernel_size_value_x = new_val
            self.params_dict["kernel_size_x"] = self.kernel_size_value_x
            self.param_name_label_x.setText(f"Kernel size {axis} = {self.kernel_size_value_x}")
        elif axis == "Y":
            self.kernel_size_value_y = new_val
            self.params_dict["kernel_size_y"] = self.kernel_size_value_y
            self.param_name_label_y.setText(f"Kernel size {axis} = {self.kernel_size_value_y}")
        elif axis == "SigmaX":
            self.sigma_value_x = new_val
            self.params_dict["sigma_x"] = self.sigma_value_x
            self.param_name_label_sigma_x.setText(f"SigmaX = {self.sigma_value_x}")
        else:
            self.sigma_value_y = new_val
            self.params_dict["sigma_y"] = self.sigma_value_y
            self.param_name_label_sigma_y.setText(f"SigmaY = {self.sigma_value_y}")

        self.param_signal.emit(self.params_dict)

    def get_parameters(self):
        """
        Возвращает текущие значения слайдеров для X, Y, SigmaX, SigmaY в виде словаря.
        """
        return self.params_dict
