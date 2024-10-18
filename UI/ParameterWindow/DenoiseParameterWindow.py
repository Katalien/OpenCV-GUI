from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from UI.ParameterWindow import IParameterWindow

class DenoiseParameterWindow(IParameterWindow.IParameterWindow):
    def __init__(self):
        super().__init__()
        self.strength_slider = QSlider(Qt.Horizontal)
        self.strength_slider.setMinimum(1)
        self.strength_slider.setMaximum(100)
        self.strength_slider.setValue(10)

        self.layout.addWidget(QLabel("Denoise Strength"))
        self.layout.addWidget(self.strength_slider)

        self.apply_button = QPushButton("Apply")
        self.apply_button.clicked.connect(self.apply_settings)
        self.layout.addWidget(self.apply_button)

    def apply_settings(self):
        self.close()

    def get_parameters(self):
        return self.strength_slider.value()