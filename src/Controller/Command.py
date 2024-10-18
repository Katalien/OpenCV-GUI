from Controller import ICommand
import cv2

class GaussianBlurCommand(ICommand.ICommand):
    def __init__(self, kernel_size):
        self.kernel_size = kernel_size

    def execute(self, image):
        return cv2.GaussianBlur(image, (self.kernel_size, self.kernel_size), 0)

class DenoisingCommand(ICommand.ICommand):
    def execute(self, image):
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

class RGB2BGRCommand(ICommand.ICommand):
    def execute(self, image):
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)