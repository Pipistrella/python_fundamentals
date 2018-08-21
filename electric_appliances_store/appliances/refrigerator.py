from electric_appliances_store.appliances.electric_appliance import ElectricAppliance


class Refrigerator(ElectricAppliance):

    def __init__(self, model, color, depth, width, height):
        ElectricAppliance.__init__(self, model, color, width, height)
        self.depth = depth
