class Warehouse:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    items = []

    def add_product(self, item):
        self.items.append(item)

    def get_product(self, item):
        self.items.pop(item)
