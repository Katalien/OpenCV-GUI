from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI.ParameterWindow import IParameterWindow


class ThresholdParameterWindow(IParameterWindow.IParameterWindow):
    param_signal = pyqtSignal(dict)
    def __init__(self):
        super().__init__()
        self.thresholding_value = 125
        self.max_value = 255
        self.threshold_type = "THRESH_BINARY"
        self.use_otsu = False

        self.params_dict = self.get_params_dict()

        self.thresh_slider_label, self.thresh_slider = self.__create_slider_block("Thresholding", self.thresholding_value)
        self.max_val_label, self.max_val_slider = self.__create_slider_block("Max Value", self.max_value)
        self.type_label, self.type_combo_box = self.__create_thresh_type_block()
        self.otsu_label, self.otsu_checkbox = self.__create_otsu_checkbox()
        self.layout.addWidget(self.thresh_slider_label)
        self.layout.addWidget(self.thresh_slider)
        self.layout.addWidget(self.max_val_label)
        self.layout.addWidget(self.max_val_slider)
        self.layout.addWidget(self.type_label)
        self.layout.addWidget(self.type_combo_box)
        self.layout.addWidget(self.otsu_label)
        self.layout.addWidget(self.otsu_checkbox)


    def get_params_dict(self):
        return {"threshold_value": self.thresholding_value,
                "max_value": self.max_value,
                "threshold_type": self.threshold_type,
                "use_otsu": self.use_otsu}

    def __create_slider_block(self, axis_name, initial_value):
        if axis_name == "Thresholding":
            slider_label = QLabel(f"Thresholding value = {initial_value}")
        else:
            slider_label = QLabel(f"Max value = {initial_value}")
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(0)
        slider.setMaximum(255)
        slider.setValue(initial_value)
        slider.valueChanged.connect(lambda val: self.__slider_value_changed(val, axis_name))
        return slider_label, slider

    def __create_otsu_checkbox(self):
        otsu_label = QLabel("\nUse THRESH_OTSU")
        otsu_checkbox = QCheckBox()
        otsu_checkbox.setCheckable(Qt.Checked)
        otsu_checkbox.setChecked(False)
        otsu_checkbox.stateChanged.connect(self.__checkbox_otsu_changed)


        return otsu_label, otsu_checkbox

    def __checkbox_otsu_changed(self):
        self.use_otsu = not self.use_otsu
        self.params_dict["use_otsu"] = self.use_otsu
        self.param_signal.emit(self.params_dict)


    def __create_thresh_type_block(self):
        type_label = QLabel("Threshold Type")
        type_widget = QComboBox()
        type_widget.addItems(["THRESH_BINARY",
                         "THRESH_BINARY_INV",
                         "THRESH_TRUNC",
                         "THRESH_TOZERO",
                         "THRESH_TOZERO_INV"])
        type_widget.currentTextChanged.connect(self.__combo_box_value_changed)
        return type_label, type_widget

    def __combo_box_value_changed(self, new_type):
        self.threshold_type = new_type
        self.params_dict["threshold_type"] = self.threshold_type
        self.param_signal.emit(self.params_dict)

    def __slider_value_changed(self, new_value, axis_name):
        if axis_name == "Thresholding":
            self.thresh_slider_label.setText(f"Thresholding value = {new_value}")
            self.thresholding_value = new_value
            self.params_dict["threshold_value"] = self.thresholding_value
        else:
            self.max_val_label.setText(f"Max value = {new_value}")
            self.max_value = new_value
            self.params_dict["max_value"] = self.max_value

        self.param_signal.emit(self.params_dict)

