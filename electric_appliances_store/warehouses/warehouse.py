class Warehouse:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    items_in_stock = {}

    def add_new_product(self, item, stock):
        self.items_in_stock[item] = stock

    def send_product_to_store(self, item):
        self.items_in_stock.pop(item)

    def get_all_items(self):
        return self.items_in_stock
