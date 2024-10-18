from Controller.Commands import ICommand
import cv2

class DenoisingCommand(ICommand.ICommand):
    def execute(self, image, **params):
        return cv2.fastNlMeansDenoisingColored(image, None, 10, 10, 7, 21)