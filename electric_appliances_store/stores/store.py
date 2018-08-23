class Store:

    def __init__(self, name, address, warehouse):
        self.name = name
        self.address = address
        self.warehouse = warehouse

    def get_products(self):
        print('You can buy NOW:\n')
        items_for_customers = self.warehouse.items_in_stock.keys()
        item_models = []
        for item in items_for_customers:
            item_models.append(item.description())
        for key in item_models:
            print(key)

    def send_item_to_customer(self, item):
        print self.warehouse.send_product_to_store(item)

    def get_promotional_item(self, item, customer):
        if customer.id >= 3:
            self.warehouse.send_product_to_store(item)
            print 'Your special price was {} - You got 50% off the regular price {}\n'\
                .format(item.price * 0.5, item.price)
            return item.price * 0.5
        else:
            self.warehouse.send_product_to_store(item)
            print 'Your special price was {} - You got 20% off the regular price {}\n'\
                .format(item.price * 0.8, item.price)
            return item.price * 0.8

    @staticmethod
    def get_product_connections_info(item):
        print item.get_required_connections()
