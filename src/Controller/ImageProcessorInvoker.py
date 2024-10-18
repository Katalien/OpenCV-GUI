class ImageProcessorInvoker:
    def __init__(self, image):
        self.commands = []
        if image is not None:
            self.original_image = image.copy()
            self.processed_image = image.copy()
        else:
            self.original_image = None
            self.processed_image = None

    def set_image(self, image):
        self.original_image = image.copy()
        self.processed_image = image.copy()

    def add_command(self, command):
        self.commands.append(command)

    def execute_all(self):
        self.processed_image = self.original_image.copy()
        for command in self.commands:
            self.processed_image = command.execute(self.processed_image)
        return self.processed_image