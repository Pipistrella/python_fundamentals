import unittest
from electric_appliances_store.customer.customer import Customer


class CustomerTestCase(unittest.TestCase):

    def setUp(self):
        self.customer = Customer(100)

    def test_customer_get_id(self):
        self.assertEqual(100, self.customer.id)
