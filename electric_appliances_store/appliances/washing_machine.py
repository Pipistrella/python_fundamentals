from electric_appliances_store.appliances.electric_appliance import ElectricAppliance


class WashingMachine(ElectricAppliance):
    def __init__(self, model, color, capacity, load_type, width, height):
        ElectricAppliance.__init__(self, model, color, width, height)
        self.capacity = capacity
        self.load_type = load_type

    def connections(self):
        print ("Needs electricity and water!")
