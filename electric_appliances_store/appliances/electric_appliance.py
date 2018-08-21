class ElectricAppliance:

    def __init__(self, model, color, width, height):
        self.model = model
        self.color = color
        self.width = width
        self.heigth = height

    def description(self):
        desc_str = "%s in %s color (Height: %s Width: %s)" % (self.model, self.color, self.heigth, self.width)
        return desc_str

    def connections(self):
        print ("Needs only electricity!")
