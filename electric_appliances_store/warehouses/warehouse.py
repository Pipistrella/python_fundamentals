class Warehouse:

    def __init__(self, name, address):
        self.name = name
        self.address = address

    items_in_stock = {}

    def add_new_product(self, item, stock):
        self.items_in_stock[item] = stock

    def send_product_to_store(self, item):
        if item in self.items_in_stock and self.items_in_stock[item] > 0:
            self.items_in_stock[item] -= 1
            self.items_in_stock.pop(item)
            print 'Thanks for buying {} from our store!\n'.format(item.description())
        else:
            print 'Sorry you just missed out {}\n'.format(item.description())

    def get_all_items(self):
        return self.items_in_stock
