from electric_appliances_store.warehouses.warehouse import Warehouse


class Store:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def get_products(self):
        print("You can buy NOW:")
        items_for_customers = Warehouse.items_in_stock.keys()
        item_models = []
        for item in items_for_customers:
            item_models.append(item.description())
        for key in item_models:
            print(key)

    def send_product_to_store(self, item):
        self.items.pop(item)