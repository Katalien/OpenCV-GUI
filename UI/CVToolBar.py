from PyQt5.QtWidgets import *
from UI.FunctionSelectorWindow import FunctionSelectorWidget
from Controller.Commands.ImageProcessorInvoker import ImageProcessorInvoker
from Controller.Commands import GaussianBlurCommand, DenoisingCommand, ThresholCommand, RGB2BGRCommand
from UI.FuncListWidget import FuncListWidget

class CVToolBar(QWidget):
    def __init__(self, image_viewer):
        super().__init__()
        self.params = {"kernel_size_x": 25, "kernel_size_y": 25, "sigma_x": 0, "sigma_y": 0}
        self.image_viewer = image_viewer
        self.image_viewer.selected_image_signal.connect(self.__image_selected)
        self.invoker = ImageProcessorInvoker(self.image_viewer.image)

        self.layout = QVBoxLayout()
        self.get_orig_image_btn = QPushButton("Get original image")
        self.get_orig_image_btn.clicked.connect(self.__get_original_image)
        self.add_button = QPushButton("Add function")
        self.add_button.clicked.connect(self.__add_button_clicked)

        self.run_button = QPushButton("Run")
        self.run_button.setStyleSheet("background-color: green; color: white;")
        self.run_button.clicked.connect(self.__run_button_clicked)

        self.layout.addWidget(self.run_button)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.get_orig_image_btn)

        self.func_list_widget = FuncListWidget()
        self.layout.addWidget(self.func_list_widget)

        self.setLayout(self.layout)

    def __update_params(self, param):
        self.params.update(param)
        print(f"CV2 tools {self.params}")
        processed_image = self.invoker.execute_all(**self.params)
        self.image_viewer.update_image(processed_image)

    def __get_original_image(self):
        if self.invoker.original_image is None:
            self.__no_image_warning()
            return
        self.image_viewer.update_image(self.invoker.original_image)

    def __no_image_warning(self):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle("Warning")
        msg_box.setText("Load image before adding fuctions")
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    def __add_button_clicked(self):
        if self.invoker.original_image is None:
            self.__no_image_warning()
            return
        selector_window = FunctionSelectorWidget()
        selector_window.selected_func_signal.connect(self.function_selected)
        selector_window.exec()

    def __run_button_clicked(self):
        if self.invoker.original_image is None:
            self.__no_image_warning()
            return
        processed_image = self.invoker.execute_all()
        self.image_viewer.update_image(processed_image)

    def __image_selected(self, image):
        self.invoker.set_image(image)

    def function_selected(self, selected_func_name):
        if selected_func_name == "GaussBlur":
            command = GaussianBlurCommand.GaussianBlurCommand()
        elif selected_func_name == "Denoising":
            command = DenoisingCommand.DenoisingCommand()
        elif selected_func_name == "BGR2RGB":
            command = RGB2BGRCommand.RGB2BGRCommand()
        elif selected_func_name == "Thresholding":
            command = ThresholCommand.ThresholCommand()
        else:
            return


        self.func_list_widget.add_item(selected_func_name)
        for func_item in self.func_list_widget.get_items():
            print("cv tool bar", func_item.function_name)
            func_item.func_params_signal.connect(self.__update_params)
            print(self.params)
        self.invoker.add_command(command)
        if self.invoker.original_image is not None:
            processed_image = self.invoker.execute_all(**self.params)
            self.image_viewer.update_image(processed_image)
        else:
            print("No image")



