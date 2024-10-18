from Controller.Commands import ICommand
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