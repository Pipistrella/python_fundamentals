from electric_appliances_store.warehouses.warehouse import Warehouse


class SupportWarehouse(Warehouse):
    def __init__(self, name, address):
        Warehouse.__init__(self, name, address)