from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import cv2
import numpy as np

class ImageViewer(QWidget):
    selected_image_signal = pyqtSignal(np.ndarray)
    def __init__(self, image_path=None, max_width=100, max_height=100):
        super().__init__()
        self.max_width = max_width
        self.max_height = max_height
        self.image_path = image_path

        self.img_label = QLabel()
        layout = QVBoxLayout()

        if image_path is not None:
            self.image = cv2.imread(self.image_path)
            self.img_label.setPixmap(QPixmap(self.image_path))
            self.image = cv2.imread(self.image_path)
        else:
            self.img_label.setText("No image")
            self.image = None

        font = self.font()
        font.setPointSize(30)
        self.setFont(font)

        layout.addWidget(self.img_label)
        self.setLayout(layout)

    def load_image(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path)
        pixmap = QPixmap(self.image_path)

        img_width = pixmap.width()
        img_height = pixmap.height()

        if img_width > self.max_width or img_height > self.max_height:
            pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)
        self.selected_image_signal.emit(self.image)

    def update_image(self, new_image):
        new_image = cv2.cvtColor(new_image, cv2.COLOR_BGR2RGB)
        qimage = QImage(new_image.data, new_image.shape[1], new_image.shape[0], new_image.strides[0],
                        QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        if new_image.shape[1] > self.max_width or new_image.shape[0] > self.max_height:
            pixmap = pixmap.scaled(self.max_width, self.max_height, Qt.KeepAspectRatio)
        self.img_label.setPixmap(pixmap)
        self.image = new_image