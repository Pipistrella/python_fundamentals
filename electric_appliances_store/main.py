from electric_appliances_store.appliances.refrigerator import Refrigerator
from electric_appliances_store.appliances.washing_machine import WashingMachine
from electric_appliances_store.stores.store import Store
from electric_appliances_store.warehouses.main_warehouse import MainWarehouse
from electric_appliances_store.warehouses.support_warehouse import SupportWarehouse

refrigerator1 = Refrigerator("Beko 4353", "blue", 35, 167, 120)
refrigerator2 = Refrigerator("Samsung Z2", "white", 24, 1, 20)
refrigerator3 = Refrigerator("Samsung WOL99", "red", 1, 999, 90)
refrigerator4 = Refrigerator("Beko 43538888887", "blue", 235, 167, 36)
washing_machine = WashingMachine("Whirpool 8", 35, "pink", 76, "front load type", 134)

my_main_warehouse = MainWarehouse("Main Warehouse Of Olya's shop", "Mogadishu")
my_support_warehouse = SupportWarehouse("Support Warehouse Only For The Best Clients", "Hobyo")


my_main_warehouse.add_new_product(refrigerator1, 10)
my_main_warehouse.add_new_product(refrigerator2, 1)
my_main_warehouse.add_new_product(refrigerator3, 5)
my_main_warehouse.add_new_product(refrigerator4, 13)
my_main_warehouse.add_new_product(washing_machine, 7)

my_support_warehouse.add_new_product(refrigerator2, 34)

my_store = Store("Olya's Shop", "Mogadishu")
my_store.get_products()
