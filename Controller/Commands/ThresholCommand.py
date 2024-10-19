from Controller.Commands import ICommand
import cv2

class ThresholCommand(ICommand.ICommand):
    def __init__(self, threshold_value = 125, max_value = 255, type="THRESH_BINARY", use_otsu=False):
        self.threshold_value = threshold_value
        self.max_val = max_value
        self.type = type
        self.use_otsu = False

    def execute(self, image, **params):
        self.threshold_value = params.get("threshold_value", self.threshold_value)
        self.max_val = params.get("max_value", self.max_val)
        self.use_otsu = params.get("use_otsu", self.use_otsu)

        type_str = params.get("threshold_type", self.type)
        type_attr = getattr(cv2, type_str)
        if self.use_otsu and image.ndim == 3:
            raise ValueError("You must convert image to GRAYSCALE before applying otsu")
        elif self.use_otsu and image.ndim == 2:
            type_attr |= cv2.THRESH_OTSU
        self.type = type_str
        new_image = cv2.threshold(image, self.threshold_value, self.max_val, type_attr )[1]
        return new_image