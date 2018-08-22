from electric_appliances_store.appliances.electric_appliance import ElectricAppliance


class WashingMachine(ElectricAppliance):
    def __init__(self, model, color, width, height, price, capacity, load_type):
        ElectricAppliance.__init__(self, model, color, width, height, price)
        self.capacity = capacity
        self.load_type = load_type

    def get_required_connections(self):
        print ('Needs electricity and water!\n')
