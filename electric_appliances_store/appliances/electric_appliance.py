class ElectricAppliance:

    def __init__(self, model, color, width, height, price):
        self.model = model
        self.color = color
        self.width = width
        self.height = height
        self.price = price

    def description(self):
        desc_str = '{} in {} color (Height: {} Width: {})\n'.format(self.model, self.color, self.height, self.width)
        return desc_str

    def get_required_connections(self):
        print ('Needs only electricity!\n')
