class ElectricAppliance:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def description(self):
        desc_str = "%s is a %s color." % (self.name, self.color)
        return desc_str

    def is_connected(self):

        return False
