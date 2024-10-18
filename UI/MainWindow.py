from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from UI.ImageViewer import ImageViewer
from UI.CVToolBar import CVToolBar


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenCV image processor")
        # self.showFullScreen()
        self.screen_width, self.screen_height = self.__get_screen_size()
        self.setGeometry(0, 0, int(self.screen_width), int(self.screen_height))
        layout = QHBoxLayout()
        self.image_viewer = ImageViewer(max_width=self.screen_width // 2, max_height=self.screen_height)  # Изменили на self.widget_l, чтобы можно было обновить его позже
        self.settings_viewer = CVToolBar(self.image_viewer)
        layout.addWidget(self.image_viewer)
        layout.addWidget(self.settings_viewer)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        menu = self.menuBar()
        file_menu_action = QAction("Load file", self)
        file_menu_action.triggered.connect(self.__file_menu_action)
        file_menu = menu.addMenu("&File")
        file_menu.addAction(file_menu_action)

    def __get_screen_size(self):
        screen = QApplication.primaryScreen()
        size = screen.size()
        width = size.width()
        height = size.height()
        return width, height

    def __file_menu_action(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "",
                                                   "Image Files (*.png *.jpg *.bmp *.tiff)")

        if file_path:
            self.image_viewer.load_image(file_path)
