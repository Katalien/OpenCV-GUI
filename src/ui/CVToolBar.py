from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from ui.FunctionSelectorWindow import FunctionSelectorWidget
from ui.FunctionItem import FunctionItem
from Controller.ImageProcessorInvoker import ImageProcessorInvoker
from Controller import Command

class CVToolBar(QWidget):
    def __init__(self, image_viewer):
        super().__init__()
        self.image_viewer = image_viewer
        self.image_viewer.selected_image_signal.connect(self.image_selected)
        self.invoker = ImageProcessorInvoker(self.image_viewer.image)

        self.layout = QVBoxLayout()
        self.get_orig_image_btn = QPushButton("Get original image")
        self.get_orig_image_btn.clicked.connect(self.__get_original_image)
        self.add_button = QPushButton("Add function")
        self.add_button.clicked.connect(self.__add_button_clicked)

        self.run_button = QPushButton("Run")
        self.run_button.clicked.connect(self.__run_button_clicked)

        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.get_orig_image_btn)

        self.func_list_widget = FuncListWidget()
        self.layout.addWidget(self.func_list_widget)

        self.setLayout(self.layout)

    def __get_original_image(self):
        self.image_viewer.update_image(self.invoker.original_image)

    def __add_button_clicked(self):
        selector_window = FunctionSelectorWidget()
        selector_window.selected_func_signal.connect(self.function_selected)
        selector_window.exec()

    def __run_button_clicked(self):
        processed_image = self.invoker.execute_all()
        self.image_viewer.update_image(processed_image)

    def image_selected(self, image):
        self.invoker.set_image(image)
    def function_selected(self, selected_func_name):
        if selected_func_name == "GaussBlur":
            command = Command.GaussianBlurCommand(kernel_size=5)
        elif selected_func_name == "Denoising":
            command = Command.DenoisingCommand()
        elif selected_func_name == "BGR2RGB":
            command = Command.RGB2BGRCommand()
        else:
            return

        self.invoker.add_command(command)
        self.func_list_widget.add_item(selected_func_name)


class FuncListWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignTop)
        self.setLayout(self.layout)

    def add_item(self, func_name):
        func_item = FunctionItem(func_name)
        self.layout.addWidget(func_item)

