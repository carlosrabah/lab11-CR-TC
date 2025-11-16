from cow import Cow

class Dragon(Cow):
    def __init__(self, name, image):
        super().__init__(name)  # call Cow constructor
        self.set_image(image)   # set the image

    def can_breath_fire(self):
        return True
