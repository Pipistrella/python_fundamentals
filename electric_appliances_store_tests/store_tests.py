import unittest

from electric_appliances_store.appliances.refrigerator import Refrigerator
from electric_appliances_store.customer.customer import Customer
from electric_appliances_store.stores.store import Store
from electric_appliances_store.warehouses.warehouse import Warehouse


class StoreTestCase(unittest.TestCase):

    # Set up instances
    def setUp(self):
        self.warehouse = Warehouse('Warehouse Of Olya shop', 'Mogadishu')
        self.refrigerator = Refrigerator('Beko 4353', 'blue', 35, 167, 100, 120)
        self.refrigerator2 = Refrigerator('Beko 4353', 'pink', 35, 167, 100, 120)
        self.refrigerator3 = Refrigerator('Beko 4353', 'grey', 35, 167, 100, 120)
        self.stock_level = 10
        self.stock_level2 = 38
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.warehouse.add_new_product(self.refrigerator2, self.stock_level2)
        self.warehouse.add_new_product(self.refrigerator3, self.stock_level)
        self.store = Store('Olya shop', 'Mogadishu', self.warehouse)

    # Tests teardown to clear the In stock items
    def tearDown(self):
        self.warehouse.items_in_stock.clear()

    # Store Tests
    def test_store_get_name(self):
        self.assertEqual('Olya shop', self.store.name)

    def test_store_get_address(self):
        self.assertEqual('Mogadishu', self.store.address)

    def test_store_get_warehouse(self):
        self.assertEqual('Warehouse Of Olya shop', self.store.warehouse.name)

    def test_get_promotional_item_with_lower_promotion_customer(self):
        customer = Customer(1)
        value = self.store.get_promotional_item(self.refrigerator, customer)
        self.assertEqual(80, value)

    def test_get_promotional_item_with_higher_promotion_customer(self):
        customer = Customer(3)
        value = self.store.get_promotional_item(self.refrigerator, customer)
        self.assertEqual(50, value)
