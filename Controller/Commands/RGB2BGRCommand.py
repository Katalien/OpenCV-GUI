from Controller.Commands import ICommand
import cv2

class RGB2BGRCommand(ICommand.ICommand):
    def execute(self, image, **params):
        return cv2.cvtColor(image, cv2.COLOR_RGB2BGR)