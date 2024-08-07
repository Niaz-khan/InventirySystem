"""
Inventory Management System
- Develop an `Item` class with attributes for name, price, and stock quantity.
- Create an `Inventory` class that can add items, update stock, and display all items.
- Include methods for checking stock levels and generating restock alerts.
"""


class Item:
    def __init__(self, name, price, quantity):
        self.item_name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Item: {self.item_name}, Price: {self.price}, Quantity: {self.quantity}"


class Inventory:
    def __init__(self):
        self.stock = []

    def add_item(self, item):
        self.stock.append(item.item_name)
        self.stock.append(float(item.price))
        self.stock.append(int(item.quantity))

    def update_stock(self):
        if self.stock:
            print("1 --> update name of the item\n2 --> update price\n3 --> update "
                  "quantity.".title())
            choice = input(":) ")
            if choice == '1':
                name = input("what will be the name of item.")
                self.stock[0] = name
            elif choice == '2':
                price = float(input("enter the amount:) "))
                self.stock[1] = price
            elif choice == '3':
                quan = input("enter the quantity:) ")
                self.stock[2] = quan
            else:
                print("invalid input")

        else:
            print("you have nothing in the stock.".title())

    def display_items(self):
        if self.stock:
            print(self.stock)
        else:
            print("You have nothing in inventory.")

    def check_inventory_levels(self):
        if self.stock:
            if self.stock[2] <= 10:
                print("You have to add more quantity of item.")
            else:
                print("You have enough stock")
        else:
            print("Hurry you have nothing in inventory")


