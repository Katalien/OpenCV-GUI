from Controller import ICommand
import cv2

class GaussianBlurCommand(ICommand.ICommand):
    def __init__(self, kernel_size=None, sigma_x = 0, sigma_y = 0):
        self.kernel_size_x = kernel_size
        self.kernel_size_y = kernel_size
        self.sigma_x = sigma_x
        self.sigma_y = sigma_y
    def execute(self, image, **params):
        self.kernel_size_x = params.get("kernel_size_x", self.kernel_size_x)
        self.kernel_size_y = params.get("kernel_size_y", self.kernel_size_y)
        self.sigma_x = params.get("sigma_x", self.sigma_x)
        self.sigma_y = params.get("sigma_y", self.sigma_y)
        return cv2.GaussianBlur(image,
                                (self.kernel_size_x, self.kernel_size_y),
                                sigmaX=self.sigma_x,
                                sigmaY=self.sigma_y)

class DenoisingCommand(ICommand.ICommand):
    def execute(self, image, **params):
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)

class RGB2BGRCommand(ICommand.ICommand):
    def execute(self, image, **params):
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

class ThresholCommand(ICommand.ICommand):

    def execute(self, image, **params):
        return cv2.threshold(image, self.threshold_value, 255, cv2.THRESH_BINARY )[1]