import sys
from random import choice

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ImageViewer(QWidget):
    def __init__(self, image_path=None, max_width=100, max_height=100):
        super().__init__()
        self.max_width = max_width
        self.max_height = max_height
        self.image_path = image_path
        self.img_label = QLabel()  # Делаем self.img_label доступной в других методах
        layout = QVBoxLayout()  # Добавляем макет

        if image_path is not None:
            self.img_label.setPixmap(QPixmap(self.image_path))
        else:
            self.img_label.setText("No image")

        font = self.font()
        font.setPointSize(30)
        self.setFont(font)

        layout.addWidget(self.img_label)  # Добавляем QLabel в макет
        self.setLayout(layout)  # Устанавливаем макет

    def load_image(self, image_path):
        self.image_path = image_path
        pixmap = QPixmap(self.image_path)

        # Получаем ширину и высоту изображения
        img_width = pixmap.width()
        img_height = pixmap.height()

        # Проверяем, нужно ли изменять размер изображения
        if img_width > self.max_width or img_height > self.max_height:
            pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.KeepAspectRatio)
        # Устанавливаем масштабированное изображение в QLabel
        self.img_label.setPixmap(pixmap)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("OpenCV image processor")
        self.showFullScreen()
        screen_w, screen_h = self.__get_screen_size()

        layout = QHBoxLayout()
        self.widget_l = ImageViewer(max_width=screen_w // 2, max_height=screen_h)  # Изменили на self.widget_l, чтобы можно было обновить его позже
        widget_r = QLabel("Some other content")
        layout.addWidget(self.widget_l)
        layout.addWidget(widget_r)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        menu = self.menuBar()
        file_menu_action = QAction("Load file", self)
        file_menu_action.triggered.connect(self.file_menu_action)
        file_menu = menu.addMenu("&File")
        file_menu.addAction(file_menu_action)

    def __get_screen_size(self):
        screen = QApplication.primaryScreen()  # Получаем основной экран
        size = screen.size()  # Получаем размер экрана
        width = size.width()
        height = size.height()
        return width, height

    def file_menu_action(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "Open Image File", "",
                                                   "Image Files (*.png *.jpg *.bmp *.tiff)")

        if file_path:  # Проверяем, был ли выбран файл
            self.widget_l.load_image(file_path)  # Загружаем выбранное изображение в виджет ImageViewer

# class CustomDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
#
#         self.setWindowTitle("HELLO!")
#
#         QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
#
#         self.buttonBox = QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)
#         self.buttonBox.rejected.connect(self.reject)
#
#         layout = QVBoxLayout()
#         message = QLabel("Something happened, is that OK?")
#         layout.addWidget(message)
#         layout.addWidget(self.buttonBox)
#         self.setLayout(layout)
#
#
#
# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#
#         self.setWindowTitle("My App")
#
#         button = QPushButton("Press me for a dialog!")
#         button.clicked.connect(self.button_clicked)
#         self.setCentralWidget(button)
#
#     def button_clicked(self, s):
#         print("click", s)
#
#         dlg = CustomDialog(self)
#         if dlg.exec():
#             print("Success!")
#         else:
#             print("Cancel!")