import unittest

from electric_appliances_store.appliances.electric_appliance import ElectricAppliance
from electric_appliances_store.appliances.refrigerator import Refrigerator
from electric_appliances_store.appliances.washing_machine import WashingMachine


class AppliancesTestCase(unittest.TestCase):

    # Set up all instances
    def setUp(self):
        self.appliance = ElectricAppliance('Beko 4353', 'blue', 35, 167, 100)
        self.refrigerator = Refrigerator('Beko 4353', 'blue', 35, 167, 100, 120)
        self.washing_machine = WashingMachine('Whirpool 8', 'pink', 35, 76, 355, 134, 'front load type')

    # Electric Appliance Tests
    def test_appliance_description(self):
        self.assertEqual('Beko 4353 in blue color (Height: 167 Width: 35)\n', self.appliance.description())

    def test_appliance_get_model(self):
        self.assertEqual('Beko 4353', self.appliance.model)

    def test_appliance_get_color(self):
        self.assertEqual('blue', self.appliance.color)

    def test_appliance_get_height(self):
        self.assertEqual(167, self.appliance.height)

    def test_appliance_get_width(self):
        self.assertEqual(35, self.appliance.width)

    def test_appliance_get_price(self):
        self.assertEqual(100, self.appliance.price)

    def test_appliance_get_required_connections(self):
        self.assertEqual('Needs only electricity!\n', self.appliance.get_required_connections())

    # Refrigerator Tests
    def test_refrigerator_get_depth(self):
        self.assertEqual(120, self.refrigerator.depth)

    # Washing Machine Tests
    def test_washing_machine_get_capacity(self):
        self.assertEqual(134, self.washing_machine.capacity)

    def test_washing_machine_get_load_type(self):
        self.assertEqual('front load type', self.washing_machine.load_type)

    def test_washing_machine_get_required_connections(self):
        self.assertEqual('Needs electricity and water!\n', self.washing_machine.get_required_connections())
