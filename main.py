from InventorySystem import Inventory, Item
from Item import Item

inventory = Inventory()
while True:
    print("Welcome to the Inventory".center(100))
    print("1 --> add item\t\t2 --> Update Stock".title().center(100))
    print("3 --> display items\t\t4 --> Check Level of stock".title().center(98))
    print("Q --> Quit".title().center(98))
    choice = input(":)")
    if choice.lower() == 'q':
        print("Exiting...")
        break
    elif choice == '1':
        name = input("enter the name of item:) ".title())
        price = input("enter the price of item:) ".title())
        quantity = input("enter the quantity of item:) ".title())
        item = Item(name=name, price=price, quantity=quantity)
        inventory.add_item(item)
    elif choice == '2':
        inventory.update_stock()
    elif choice == '3':
        inventory.display_items()
    elif choice == '4':
        inventory.check_inventory_levels()
    else:
        print("Invalid Input:")
        continue
