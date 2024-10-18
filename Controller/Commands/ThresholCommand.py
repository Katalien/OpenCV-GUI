from Controller.Commands import ICommand
import cv2

class ThresholCommand(ICommand.ICommand):
    def __init__(self, threshold_value = 125):
        self.threshold_value = threshold_value

    def execute(self, image, **params):
        return cv2.threshold(image, self.threshold_value, 255, cv2.THRESH_BINARY )[1]