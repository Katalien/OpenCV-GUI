from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class ImageViewer(QWidget):
    def __init__(self, image_path=None, max_width=100, max_height=100):
        super().__init__()
        self.max_width = max_width
        self.max_height = max_height
        self.image_path = image_path
        self.img_label = QLabel()
        layout = QVBoxLayout()

        if image_path is not None:
            self.img_label.setPixmap(QPixmap(self.image_path))
        else:
            self.img_label.setText("No image")

        font = self.font()
        font.setPointSize(30)
        self.setFont(font)

        layout.addWidget(self.img_label)
        self.setLayout(layout)

    def load_image(self, image_path):
        self.image_path = image_path
        pixmap = QPixmap(self.image_path)

        img_width = pixmap.width()
        img_height = pixmap.height()

        if img_width > self.max_width or img_height > self.max_height:
            pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)
