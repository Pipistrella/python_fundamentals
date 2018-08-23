import unittest

from electric_appliances_store.appliances.refrigerator import Refrigerator
from electric_appliances_store.warehouses.warehouse import Warehouse


class WarehouseTestCase(unittest.TestCase):

    # Set up instances
    def setUp(self):
        self.warehouse = Warehouse('Warehouse Of Olya shop', 'Mogadishu')
        self.refrigerator = Refrigerator('Beko 4353', 'blue', 35, 167, 100, 120)
        self.refrigerator2 = Refrigerator('Beko 4353', 'pink', 35, 167, 100, 120)
        self.refrigerator3 = Refrigerator('Beko 4353', 'grey', 35, 167, 100, 120)
        self.stock_level = 10
        self.stock_level2 = 38

    # Tests teardown to clear the In stock items
    def tearDown(self):
        self.warehouse.items_in_stock.clear()

    # Warehouse Tests
    def test_warehouse_get_name(self):
        self.assertEqual('Warehouse Of Olya shop', self.warehouse.name)

    def test_warehouse_get_address(self):
        self.assertEqual('Mogadishu', self.warehouse.address)

    def test_add_new_product(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.assertIn(self.refrigerator, self.warehouse.items_in_stock)

    def test_add_new_product_stock_level(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        values = self.warehouse.items_in_stock.values()
        self.assertEqual(self.stock_level, values[0])

    def test_add_multiple_products_to_warehouse(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.warehouse.add_new_product(self.refrigerator2, self.stock_level2)
        self.assertEqual(2, len(self.warehouse.items_in_stock))

    def test_add_multiple_products_to_warehouse_stock_levels_are_correct(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.warehouse.add_new_product(self.refrigerator2, self.stock_level2)
        values = self.warehouse.items_in_stock.values()
        self.assertEqual(self.stock_level2, values[0])

    def test_send_product_to_store(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.assertEqual('Thanks for buying {} from our store!\n'.format(self.refrigerator.description()),
                         self.warehouse.send_product_to_store(self.refrigerator))

    def test_send_product_to_store_will_update_quantity(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.warehouse.send_product_to_store(self.refrigerator)
        values = self.warehouse.items_in_stock.values()
        self.assertEqual(self.stock_level - 1, values[0])

    def test_send_product_to_store_will_remove_product_when_it_goes_out_of_stock(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        for i in range(self.stock_level):
            self.warehouse.send_product_to_store(self.refrigerator)
        self.assertNotIn(self.refrigerator, self.warehouse.items_in_stock)

    def test_send_product_to_store_when_there_is_no_such_product(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.assertEqual('Sorry you just missed out {}\n'.format(self.refrigerator3.description()),
                         self.warehouse.send_product_to_store(self.refrigerator3))

    def test_get_all_items(self):
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.warehouse.add_new_product(self.refrigerator2, self.stock_level2)
        self.warehouse.add_new_product(self.refrigerator3, self.stock_level)
        self.assertEqual(3, len(self.warehouse.get_all_items()))

    def test_get_all_items_add_remove_item(self):
        only_one_in_stock = 1
        self.warehouse.add_new_product(self.refrigerator, self.stock_level)
        self.warehouse.add_new_product(self.refrigerator2, self.stock_level2)
        self.warehouse.add_new_product(self.refrigerator3, only_one_in_stock)
        self.warehouse.send_product_to_store(self.refrigerator3)
        self.assertEqual(2, len(self.warehouse.get_all_items()))
