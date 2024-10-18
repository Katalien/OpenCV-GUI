class ICommand:
    def execute(self, image):
        raise NotImplementedError("Subclasses must implement method")
