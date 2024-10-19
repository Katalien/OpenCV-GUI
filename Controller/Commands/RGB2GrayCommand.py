from Controller.Commands import ICommand
import cv2

class RGB2GrayCommand(ICommand.ICommand):
    def execute(self, image, **params):
        return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)