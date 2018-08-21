from electric_appliances_store.warehouses.warehouse import Warehouse


class MainWarehouse(Warehouse):
    def __init__(self, name, address):
        Warehouse.__init__(self, name, address)

    def send_product_to_store(self, item):

        self.items_in_stock.pop(item)