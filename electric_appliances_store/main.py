from electric_appliances_store.appliances.refrigerator import Refrigerator
from electric_appliances_store.appliances.washing_machine import WashingMachine
from electric_appliances_store.customer.customer import Customer
from electric_appliances_store.stores.store import Store
from electric_appliances_store.warehouses.warehouse import Warehouse


# Configuring some products
refrigerator1 = Refrigerator('Beko 4353', 'blue', 35, 167, 100, 120)
refrigerator2 = Refrigerator('Samsung Z2', 'white', 24, 1, 350, 20)
refrigerator3 = Refrigerator('Samsung WOL99', 'red', 1, 999, 238, 90)
refrigerator4 = Refrigerator('Beko 43538888887', 'blue', 235, 167, 455, 36)
washing_machine = WashingMachine('Whirpool 8', 'pink', 35, 76, 355, 134, 'front load type')

# Configuring my warehouse
my_warehouse = Warehouse('Warehouse Of Olya shop', 'Mogadishu')

# Adding product to my warehouse
my_warehouse.add_new_product(refrigerator1, 1)
my_warehouse.add_new_product(refrigerator2, 0)
my_warehouse.add_new_product(refrigerator3, 5)
my_warehouse.add_new_product(refrigerator4, 13)
my_warehouse.add_new_product(washing_machine, 7)

my_customer1 = Customer(1)
my_customer4 = Customer(4)

# Configuring my store
my_store = Store('Olya Shop','Mogadishu', my_warehouse)

# Buying products from my store
my_store.get_products()
refrigerator1.get_required_connections()
my_store.send_item_to_customer(refrigerator1)
my_store.send_item_to_customer(refrigerator2)
my_store.send_item_to_customer(refrigerator1)
my_store.get_promotional_item(washing_machine, my_customer4)
my_store.get_promotional_item(refrigerator2, my_customer4)
my_store.get_promotional_item(refrigerator4, my_customer1)
