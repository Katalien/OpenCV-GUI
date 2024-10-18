class ICommand:
    def execute(self, image, **params):
        raise NotImplementedError("Subclasses must implement method")
